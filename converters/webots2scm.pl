#!/usr/bin/perl

# Webotsのモーションデータ
# C:\Program Files\Webots\projects\contests\nao_robocup\controllers\nao_soccer_player_red\*.motion
# をasura-jのschemeで再生できるようにするスクリプト.

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
  push @times, $time - $lastTime;
  $lastTime = $time;

  shift @data; # skip frameNo

  foreach my $joint (@joints){
    if(exists $head{$joint}){
#      push @{$frame}, rad2deg($data[$head{$joint}]);
      push @{$frame}, sprintf("%.3f", $data[$head{$joint}]);
    }elsif(exists $defaults{$joint}){
      push @{$frame}, $defaults{$joint};
    }else{
      push @{$frame}, 0;
    }
  }
  push @{$list}, $frame;
}

print ";XXX \n";
print '(mc-registmotion 120 "XXX" TIMED #(';
print "\n#(\n";
foreach my $frame (@{$list}){
  print '#(' . join(" ",@{$frame}) . ")\n";
}
print ") #(";
print join(" ",@times);
print ")\n)\n)\n";

