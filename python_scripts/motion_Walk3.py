"""
Walk

Small example to make Nao walk

"""

from motion_CurrentConfig import *


####
# Create python broker

try:
  broker = ALBroker("pythonBroker","127.0.0.1",9998,IP, PORT)
except RuntimeError,e:
  print("cannot connect")
  exit(1)

####
# Create motion proxy

print "Creating motion proxy"


try:
  motionProxy = ALProxy("ALMotion")
  memoryProxy = ALProxy("ALMemory")
except Exception,e:
  print "Error when creating motion proxy:"
  print str(e)
  exit(1)
  

# ============================================================

motionProxy.setSupportMode(motion.SUPPORT_MODE_DOUBLE_LEFT)


# ShoulderMedian, ShoulderAmplitude, ElbowMedian, ElbowAmplitude 
motionProxy.setWalkArmsConfig( 100.0 * motion.TO_RAD, 10.0 * motion.TO_RAD, 30.0 * motion.TO_RAD, 10.0 * motion.TO_RAD )
motionProxy.setWalkArmsEnable(True)

#################
## Slow Walk With High Step
#################

# LHipRoll(degrees), RHipRoll(degrees), HipHeight(meters), TorsoYOrientation(degrees)
motionProxy.setWalkExtraConfig( 3.5, -3.5, 0.23, 0 )

# StepLength, StepHeight, StepSide, MaxTurn, ZmpOffsetX, ZmpOffsetY 
motionProxy.setWalkConfig( 0.04, 0.02, 0.02, 0.3, 0.02, 0.018 )

#motionProxy.addWalkStraight( 0.05*4, 80)
#motionProxy.addTurn( 0.4*4, 80 )
#motionProxy.addWalkSideways(-0.04*4, 80)
#motionProxy.walk()   #Blocking Function

#exit(0)

#################
## Speed Walk
#################

# LHipRoll(degrees), RHipRoll(degrees), HipHeight(meters), TorsoYOrientation(degrees)
motionProxy.setWalkExtraConfig( 3.5, -3.5, 0.23, 0 )

# StepLength, StepHeight, StepSide, MaxTurn, ZmpOffsetX, ZmpOffsetY 
#motionProxy.setWalkConfig( 0.04, 0.02, 0.02, 0.3, 0.015, 0.018 )
motionProxy.setWalkConfig( 0.04, 0.02, 0.02, 0.3, 0.02, 0.018 )

#motionProxy.addWalkStraight( 0.04*4, 25)
motionProxy.addWalkStraight( 0.1, 40)
motionProxy.addWalkStraight( 1.0, 30)

#motionProxy.addTurn( 0.3*5, 35 )
#motionProxy.addWalkSideways(0.02*8, 45)
#motionProxy.addWalkArc( 0.3*4, 0.3, 25 )
#motionProxy.addWalkSideways(-0.02*8, 25)
#motionProxy.addWalkStraight( -0.05*3, 25)
motionProxy.post.walk()   #Blocking Function 

#################
#Press Sensor
#################

for i in range(100):
# Get The Left Foot Force Sensor Values
  LFsrFL = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/FrontLeft/Sensor/Value",0)
  LFsrFR = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/FrontRight/Sensor/Value",0)
  LFsrBL = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/RearLeft/Sensor/Value",0)
  LFsrBR = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/RearRight/Sensor/Value",0)

  print( "Left FSR : %.2f %.2f %.2f %.2f" %  (LFsrFL, LFsrFR, LFsrBL, LFsrBR) )

# Get The Right Foot Force Sensor Values
  RFsrFL = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/FrontLeft/Sensor/Value",0)
  RFsrFR = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/FrontRight/Sensor/Value",0)
  RFsrBL = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/RearLeft/Sensor/Value",0)
  RFsrBR = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/RearRight/Sensor/Value",0)

  print( "Right FSR : %.2f %.2f %.2f %.2f\n" %  (RFsrFL, RFsrFR, RFsrBL, RFsrBR) )
  
  time.sleep(0.125)
  
#  LFsr = (LFsrFL + LFsrFR + LFsrBL + LFsrBR)/4
#  RFsr = (RFsrFL + RFsrFR + RFsrBL + RFsrBR)/4
#  sr = (LFsr + RFsr)/2

  if(LFsrFL < 700 or LFsrFR < 700 or LFsrBL < 700 or LFsrBR < 700):
     print "LFsrFL = %d, LFsrFR = %d, LFsrBL = %d, LFsrBR = %d" % (LFsrFL, LFsrFR, LFsrBL, LFsrBR)
     motionProxy.post.gotoJointStiffness('LAnklePitch',0.9, 0.0, motion.INTERPOLATION_SMOOTH)
     motionProxy.post.gotoJointStiffness('LAnkleRoll',0.9, 0.0, motion.INTERPOLATION_SMOOTH)
  else:
     motionProxy.post.gotoJointStiffness('LAnklePitch',0.7, 0.15, motion.INTERPOLATION_SMOOTH)
     motionProxy.post.gotoJointStiffness('LAnkleRoll',0.7, 0.15, motion.INTERPOLATION_SMOOTH)
  if(RFsrFL < 700 or RFsrFR < 700 or RFsrBL < 700 or RFsrBR < 700):
     motionProxy.post.gotoJointStiffness('RAnklePitch',0.9, 0.0, motion.INTERPOLATION_SMOOTH)
     motionProxy.post.gotoJointStiffness('RAnkleRoll',0.9, 0.0, motion.INTERPOLATION_SMOOTH)
  else:
     motionProxy.post.gotoJointStiffness('RAnklePitch',0.7, 0.15, motion.INTERPOLATION_SMOOTH)
     motionProxy.post.gotoJointStiffness('RAnkleRoll',0.7, 0.15, motion.INTERPOLATION_SMOOTH)

#    motionProxy.gotoJointStiffness('RAnklePitch',1.0, 0.15, motion.INTERPOLATION_SMOOTH)
#    motionProxy.gotoJointStiffness('RAnkleRoll',1.0, 0.15, motion.INTERPOLATION_SMOOTH)
#  if(LFsr >= 1600):
#    motionProxy.gotoJointStiffness('LAnklePitch',1.0, 0.15, motion.INTERPOLATION_SMOOTH)
#    motionProxy.gotoJointStiffness('LAnkleRoll',1.0, 0.15, motion.INTERPOLATION_SMOOTH)
#  else:
#    motionProxy.JointStiffness('LAnklePitch',0.75)
#    motionProxy.JointStiffness('LAnkleRoll',0.75)  
  if(not motionProxy.walkIsActive()):
  	break;

  	  
#----------------------------------------------------------

