"""
StiffnessOon

Contains some examples to set stiffness on for the whole body
of Nao, or chain by chain, or joint by joint

"""

from motion_CurrentConfig import *


####
# Create python broker

try:
  broker = ALBroker("pythonBroker","127.1.0.1",BPORT,IP, PORT)
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

print "Setting body stiffness to 1.0"

#going slowly to 1.
motionProxy.gotoBodyStiffness(0.1 , 0.1, motion.INTERPOLATION_SMOOTH)

#**************************
# CHAIN 
#**************************

# HEAD
#motionProxy.setChainStiffness('Head',1.0);

  
#motionProxy.setChainStiffness('LArm',1.0 );
#motionProxy.setChainStiffness('RArm',1.0 );

# LEGS
#motionProxy.setChainStiffness('LLeg',1.0 );
#motionProxy.setChainStiffness('RLeg',1.0 );

#**************************
# JOINT 
#**************************

# HEAD
#motionProxy.setJointStiffness('HeadPitch',1.0)
#motionProxy.setJointStiffness('HeadYaw',1.0)

# ARMS
#motionProxy.setJointStiffness('LShoulderPitch',1.0)
#motionProxy.setJointStiffness('LShoulderRoll',1.0)
#motionProxy.setJointStiffness('LElbowYaw',1.0)
#motionProxy.setJointStiffness('LElbowRoll',1.0)
#motionProxy.setJointStiffness('RShoulderPitch',1.0)
#motionProxy.setJointStiffness('RShoulderRoll',1.00)
#motionProxy.setJointStiffness('RElbowYaw',1.0)
#motionProxy.setJointStiffness('RElbowRoll',1.0)

# LEGS
#motionProxy.setJointStiffness('LHipYawPitch',1.0)
#motionProxy.setJointStiffness('LHipRoll',1.0)
#motionProxy.setJointStiffness('LHipPitch',1.0)
#motionProxy.setJointStiffness('LKneePitch',1.0)
#motionProxy.setJointStiffness('LAnklePitch',1.0)
#motionProxy.setJointStiffness('LAnkleRoll',1.0)
#motionProxy.setJointStiffness('RHipYawPitch',1.0)
#motionProxy.setJointStiffness('RHipRoll',1.0)
#motionProxy.setJointStiffness('RHipPitch',1.0)
#motionProxy.setJointStiffness('RKneePitch',1.0)
#motionProxy.setJointStiffness('RAnklePitch',1.0)
#motionProxy.setJointStiffness('RAnkleRoll',1.0)

print "Stiffness set to 1.0"
