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
dcm.createAlias( ["BodyJoints", [
  "LShoulderPitch/Position/Actuator/Value"
,   "LShoulderRoll/Position/Actuator/Value"
,   "LElbowYaw/Position/Actuator/Value"
,   "LElbowRoll/Position/Actuator/Value"
,   "LHipYawPitch/Position/Actuator/Value"
,   "LHipRoll/Position/Actuator/Value"
,   "LHipPitch/Position/Actuator/Value"
,   "LKneePitch/Position/Actuator/Value"
,   "LAnklePitch/Position/Actuator/Value"
,   "LAnkleRoll/Position/Actuator/Value"
,   "RHipRoll/Position/Actuator/Value"
,   "RHipPitch/Position/Actuator/Value"
,   "RKneePitch/Position/Actuator/Value"
,   "RAnklePitch/Position/Actuator/Value"
,   "RAnkleRoll/Position/Actuator/Value"
,   "RShoulderPitch/Position/Actuator/Value"
,   "RShoulderRoll/Position/Actuator/Value"
,   "RElbowYaw/Position/Actuator/Value"
,   "RElbowRoll/Position/Actuator/Value"
]])
dcm.setAlias(
  [
    "BodyJoints",
    "ClearAll",
    "time-separate",
    0,
    [
dcm.getTime(1500)
, dcm.getTime(2500)
, dcm.getTime(3800)
, dcm.getTime(4500)
, dcm.getTime(5300)
, dcm.getTime(6300)
, dcm.getTime(7500)
, dcm.getTime(8500)
    ],
    [
 [-1.571, -0.873, -0.175, 0.000, 0.611, 1.117, 1.623, 1.833  ]
, [0.000, 0.000, 0.000, 0.000, 0.035, 0.131, 0.175, 0.192  ]
, [-1.571, -1.571, -1.571, -1.571, -0.244, -0.925, -1.571, -1.239  ]
, [0.000, -0.611, -1.658, -0.140, -0.716, -1.292, -1.396, -1.257  ]
, [0.000, 0.000, -0.873, -0.873, -0.965, -0.785, 0.000, 0.000  ]
, [0.000, 0.000, 0.000, 0.000, 0.087, 0.105, -0.010, -0.010  ]
, [0.000, -1.571, -1.571, -1.571, -1.571, -1.070, -1.047, -0.175  ]
, [2.094, 2.094, 1.047, 1.012, 2.155, 2.164, 2.094, 0.349  ]
, [-1.134, -1.134, -0.784, 0.087, -0.312, -0.716, -1.047, -0.175  ]
, [0.000, 0.000, -0.681, -0.555, -0.297, -0.105, 0.000, 0.000  ]
, [0.000, 0.000, 0.000, 0.000, -0.087, -0.105, 0.010, 0.010  ]
, [0.000, -1.571, -1.571, -1.571, -1.571, -1.070, -1.047, -0.175  ]
, [2.094, 2.094, 1.047, 1.012, 2.155, 2.164, 2.094, 0.349  ]
, [-1.134, -1.134, -0.784, 0.087, -0.312, -0.716, -1.047, -0.175  ]
, [0.000, 0.000, 0.681, 0.555, 0.297, 0.105, 0.000, 0.000  ]
, [-1.571, -0.873, -0.175, 0.000, 0.611, 1.117, 1.623, 1.833  ]
, [0.000, 0.000, 0.000, 0.000, -0.035, -0.131, -0.175, -0.192  ]
, [1.571, 1.571, 1.571, 1.571, 0.244, 0.925, 1.571, 1.239  ]
, [0.000, 0.611, 1.658, 0.140, 0.716, 1.292, 1.396, 1.257  ]
]])
