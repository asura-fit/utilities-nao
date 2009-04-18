#!/usr/bin/perl

# Choregraphe default.xal中のモーションデータを変換するスクリプト.
# 一部のデータのみ対応.

# Example
# perl converters/xal2py.pl < motions/default.xal

# http://search.cpan.org/~grantm/XML-SAX-0.96/SAX.pm

my @joints = (LShoulderPitch,LShoulderRoll,LElbowYaw,LElbowRoll,LHipYawPitch,LHipRoll,LHipPitch,LKneePitch,LAnklePitch,LAnkleRoll,RHipRoll,RHipPitch,RKneePitch,RAnklePitch,RAnkleRoll,RShoulderPitch,RShoulderRoll,RElbowYaw,RElbowRoll);

use strict;
use warnings;

use Math::Trig;
use POSIX;

package XALSAXHandler;

use base qw( XML::SAX::Base );

sub start_document {
  my ($self) = @_;
  $self->{state} = 0;
  $self->{vstate} = 0;
  $self->{motions} = [];
}

sub end_document {
  my ($self) = @_;
  foreach my $m (@{$self->{motions}}){
    print "Prccess $m->{name}\n";
    &main::topy($m);
  }
}

sub start_element {
  my ($self, $el) = @_;
  my $name = $el->{Name};

  if($name eq "Box"){
    $self->{cur} = {};
    $self->{state} = 1;
    return;
  }
  if($self->{state} == 1){
    if($name eq "name"){
      $self->{vstate} = 6;
    }
    if($name eq "Timeline"){
      $self->{cur}->{timeline} = {};
      $self->{cur}->{timeline}->{layers} = [];
      $self->{state} = 2;
    }
    if($name eq "Input" || $name eq "Output"){
    	$self->{state} = -1;
    }
    return;
  }
  if($self->{state} == 2){
    if($name eq "fps"){
      $self->{vstate} = 1;
      return;
    }
    if($name eq "MotionLayer"){
      push @{$self->{cur}->{timeline}->{layers}}, [];
      $self->{state} = 3;
      return;
    }
  }
  if($self->{state} == 3 && $name eq "MotionKeyframe"){
    push @{$self->{cur}->{timeline}->{layers}->[-1]}, {};
    $self->{state} = 4;
    return;
  }
  if($self->{state} == 4){
    if($name eq "index"){
      $self->{vstate} = 2;
    }
    if($name eq "interpolation"){
      $self->{vstate} = 3;
    }
    if($name eq "Motors"){
      $self->{cur}->{timeline}->{layers}->[-1]->[-1]->{"data"} = {};
      $self->{state} = 5;
    }
    return;
  }
  if($self->{state} == 5){
    if($name eq "Motor"){
      $self->{tmp} = {};
    }
    if($name eq "name"){
      $self->{vstate} = 4;
    }
    if($name eq "value"){
      $self->{vstate} = 5;
    }
  }
}

sub characters{
  my ($self, $el) = @_;
  return if($el->{Data} eq '');

  $self->{cur}->{timeline}->{fps} = $el->{Data} if($self->{vstate} == 1);
  $self->{cur}->{timeline}->{layers}->[-1]->[-1]->{"index"} =  $el->{Data} if($self->{vstate} == 2);
  $self->{cur}->{timeline}->{layers}->[-1]->[-1]->{"interpolation"} = $el->{Data} if($self->{vstate} == 3);
  $self->{tmp}->{name} = $el->{Data} if($self->{vstate} == 4);
  $self->{cur}->{timeline}->{layers}->[-1]->[-1]->{"data"}->{$self->{tmp}->{name}} = $el->{Data} if($self->{vstate} == 5);
  $self->{cur}->{name} = $el->{Data} if($self->{vstate} == 6);

  $self->{vstate} = 0;
}

sub end_element{
  my ($self, $el) = @_;
  my $name = $el->{Name};

  if($self->{state} == -1){
    if($name eq "Input" || $name eq "Output"){
      $self->{state} = 1;
    }
  }
  if($self->{state} == 1){
    if($name eq "Box"){
      if(defined $self->{cur}->{timeline}){
        push @{$self->{motions}}, $self->{cur};
      }
      $self->{state} = 0;
    }
    return;
  }
  if($self->{state} == 2){
    if($name eq "Timeline"){
      $self->{state} = 1;
    }
    return;
  }
  if($self->{state} == 3 && $name eq "MotionLayer"){
    $self->{state} = 2;
    return;
  }
  if($self->{state} == 4){
    if($name eq "MotionKeyframe"){
      $self->{state} = 3;
    }
    return;
  }
  if($self->{state} == 5){
    if($name eq "Motors"){
      $self->{state} = 4;
    }
    return;
  }
}

package main;

my $parser
= do {
  use XML::SAX::ParserFactory;

  XML::SAX::ParserFactory->parser();
};

my $source = do { local $/; <> };   # slurp!

$parser->parse_string($source, Handler => XALSAXHandler->new());

sub topy{
  my $motion = shift;

  open(OUT, "> dcm_" . $motion->{name} . ".py");
  select(OUT);
  print <<TEMPL0;
"""
DCM


"""

from motion_CurrentConfig import *

####
# Create python broker

try:
  broker = ALBroker("pythonBroker","127.0.0.1",BPORT,IP, PORT)
except RuntimeError,e:
  print("cannot connect")
  exit(1)

####
# Create led proxy

print "Creating led proxy"


try:
  dcm = ALProxy("DCM")
except Exception,e:
  print "Error when creating DCM proxy:"
  print str(e)
  exit(1)
TEMPL0

          #  my @joints = keys %{${$self->{cur}->{timeline}->{layers}}[-1]->{"data"}}:

  print 'dcm.createAlias( ["BodyJoints", [';
  print "\n";
  for(my $i = 0; $i < @joints; $i++) {
    print ", " if($i != 0);
    print '  "' . $joints[$i] . '/Position/Actuator/Value"';
    print "\n";
  }
  print ']])';
  print "\n";

  print <<TEMPL1;
dcm.setAlias(
  [
    "BodyJoints",
    "ClearAll",
    "time-separate",
    0,
    [
TEMPL1

  my $step = 1000 / ($motion->{timeline}->{"fps"});

  for(my $i = 0; $i < @{$motion->{timeline}->{"layers"}->[-1]}; $i++) {
    print ", " if($i != 0);
    my $time = $step*$motion->{timeline}->{"layers"}->[-1]->[$i]->{"index"};
    print "dcm.getTime($time)\n";
  }
  print <<TEMPL2;
    ],
    [
TEMPL2

  for(my $i = 0; $i < @joints; $i ++) {
    print "," if($i != 0);
    print " [";
    for(my $j = 0; $j < @{$motion->{timeline}->{"layers"}->[-1]}; $j ++) {
      print ", " if($j != 0);
      my $value = $motion->{timeline}->{"layers"}->[-1]->[$j]->{data}->{$joints[$i]};
      if(!defined $value){
        print STDERR "Nothing $joints[$i]\n";
        print 0;
      }
      print sprintf("%.3f", deg2rad($value));
    }
    print "  ]\n";
  }
  print "]])\n";
  close(OUT);
  select(STDOUT);
}
