#!/usr/bin/perl

# Webotsのモーションデータ
# C:\Program Files\Webots\projects\contests\nao_robocup\controllers\nao_soccer_player_red\*.motion
# をPython経由でDCMに送るスクリプトを作成するスクリプト.

# Example
# perl converters/webots2py.pl < motions/StandUpFromFront.motion > dcm_StandUpFromFront.py

use Math::Trig;
use POSIX;

my @joints = (LShoulderPitch,LShoulderRoll,LElbowYaw,LElbowRoll,LHipYawPitch,LHipRoll,LHipPitch,LKneePitch,LAnklePitch,LAnkleRoll,RHipYawPitch,RHipRoll,RHipPitch,RKneePitch,RAnklePitch,RAnkleRoll,RShoulderPitch,RShoulderRoll,RElbowYaw,RElbowRoll);

my %defaults = ();

my $c = -2;
my %head = map{ chomp; $_ => $c++; } split(",",scalar(<>));

my $list = [];
my @times;
my $lastTime = 0;
while(<>){
  my @data = split(",");
  my $frame = [];

  my $time = shift @data;
  $time =~ /(\d+):(\d+):(\d+)/;
  $time = ($1*60 + $2)*1000 + $3;
  $time *= 2;
  push @times, $time - $lastTime;
  $lastTime = $time;

  shift @data; # skip frameNo

  foreach my $joint (@joints){
    if(exists $head{$joint}){
#      push @{$frame}, rad2deg($data[$head{$joint}]);
      my $val = $data[$head{$joint}];
      chomp $val;
      push @{$frame}, sprintf("%.3f", $val);
    }elsif(exists $defaults{$joint}){
      push @{$frame}, $defaults{$joint};
    }else{
      print STDERR $joint;
      push @{$frame}, 0;
    }
  }
  push @{$list}, $frame;
}
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
my $total = 2500;

#      $#times = 10;

for(my $i = 0; $i < @times; $i ++) {
  print ", " if($i != 0);
  $total += $times[$i];
  print "dcm.getTime($total)\n";
}
print <<TEMPL2;
    ],

    [
TEMPL2
for(my $i = 0; $i < @joints; $i ++) {
  print "," if($i != 0);
  print " [";
  for(my $j = 0; $j < @times; $j ++) {
    print ", " if($j != 0);
    print $list->[$j]->[$i];
  }
  print "  ]\n";
}
print "]])\n";
