"""
StiffnessOff

Contains some examples to set stiffness off for the whole body
of Nao, or chain by chain, or joint by joint

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
# Create motion proxy

print "Creating motion proxy"


try:
  motionProxy = ALProxy("ALMotion")
except Exception,e:
  print "Error when creating motion proxy:"
  print str(e)
  exit(1)


#**************************
# BODY
#**************************
  
numBodyJoints = len(motionProxy.getBodyJointNames())

print "Setting body stiffness to 0.0"
motionProxy.setBodyStiffness( 0.0 )

#**************************
# CHAIN 
#**************************

# HEAD
#motionProxy.setChainStiffness('Head',0.0);

  
#motionProxy.setChainStiffness('LArm',0.0 );
#motionProxy.setChainStiffness('RArm',0.0 );

# LEGS
#motionProxy.setChainStiffness('LLeg',0.0 );
#motionProxy.setChainStiffness('RLeg',0.0 );

#**************************
# JOINT 
#**************************

# HEAD
#motionProxy.setJointStiffness('HeadPitch',0.0)
#motionProxy.setJointStiffness('HeadYaw',0.0)

# ARMS
#motionProxy.setJointStiffness('LShoulderPitch',0.0)
#motionProxy.setJointStiffness('LShoulderRoll',0.0)
#motionProxy.setJointStiffness('LElbowYaw',0.0)
#motionProxy.setJointStiffness('LElbowRoll',0.0)
#motionProxy.setJointStiffness('RShoulderPitch',0.0)
#motionProxy.setJointStiffness('RShoulderRoll',0.00)
#motionProxy.setJointStiffness('RElbowYaw',0.0)
#motionProxy.setJointStiffness('RElbowRoll',0.0)

# LEGS
#motionProxy.setJointStiffness('LHipYawPitch',0.0)
#motionProxy.setJointStiffness('LHipRoll',0.0)
#motionProxy.setJointStiffness('LHipPitch',0.0)
#motionProxy.setJointStiffness('LKneePitch',0.0)
#motionProxy.setJointStiffness('LAnklePitch',0.0)
#motionProxy.setJointStiffness('LAnkleRoll',0.0)
#motionProxy.setJointStiffness('RHipYawPitch',0.0)
#motionProxy.setJointStiffness('RHipRoll',0.0)
#motionProxy.setJointStiffness('RHipPitch',0.0)
#motionProxy.setJointStiffness('RKneePitch',0.0)
#motionProxy.setJointStiffness('RAnklePitch',0.0)
#motionProxy.setJointStiffness('RAnkleRoll',0.0)

print "Stiffness set to 0.0"
