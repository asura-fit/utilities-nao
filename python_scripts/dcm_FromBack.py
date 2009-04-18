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
dcm.getTime(1000)
, dcm.getTime(2000)
, dcm.getTime(2800)
, dcm.getTime(3500)
, dcm.getTime(4000)
, dcm.getTime(5000)
, dcm.getTime(5900)
, dcm.getTime(6900)
, dcm.getTime(7400)
, dcm.getTime(8500)
, dcm.getTime(9500)
    ],
    [
 [0.000, 2.094, 2.094, 2.094, 2.094, 0.698, 0.741, 0.733, 0.733, 1.710, 1.833  ]
, [1.571, 0.803, 0.471, 0.367, 0.000, 1.047, 0.499, 0.499, 0.499, 0.035, 0.192  ]
, [0.000, 0.157, 0.087, 0.087, 0.087, 0.083, 0.094, 0.083, 0.083, -1.257, -1.239  ]
, [0.000, 0.000, -1.658, -0.698, 0.000, -0.489, -0.824, -0.805, -0.805, -1.134, -1.257  ]
, [0.000, 0.000, -0.000, -0.663, 00.000, -0.499, -0.859, -0.402, -0.402, -0.402, 0.000  ]
, [0.000, 0.000, 0.000, 0.000, 0.541, 0.155, -0.291, 0.192, 0.367, 0.000, -0.010  ]
, [0.000, -0.175, -0.175, -1.571, -1.571, -0.857, 0.386, -0.855, -0.836, -0.873, -0.175  ]
, [0.000, 1.676, 1.676, 1.676, 1.676, 2.201, 1.775, 2.206, 2.206, 2.094, 0.349  ]
, [0.000, 0.244, 0.244, 0.244, 0.785, -0.571, -1.222, -1.222, -1.222, -1.222, -0.175  ]
, [0.000, 0.000, 0.000, 0.000, 0.000, -0.396, -0.104, 0.118, 0.087, 0.000, 0.000  ]
, [0.000, 0.000, 0.000, 0.000, -0.541, -0.558, -0.566, -0.297, -0.017, 0.000, 0.010  ]
, [0.000, -0.175, -0.175, -1.571, -1.571, -1.525, -1.560, -0.906, -0.906, -0.873, -0.175  ]
, [0.000, 1.676, 1.676, 1.676, 1.676, 1.222, 1.080, 0.876, 1.763, 2.094, 0.349  ]
, [0.000, 0.244, 0.244, 0.244, 0.785, 0.785, 0.691, 0.403, -0.579, -1.222, -0.175  ]
, [0.000, 0.000, 0.000, 0.000, 0.000, 0.009, -0.129, 0.680, 0.278, 0.000, 0.000  ]
, [0.000, 2.094, 2.094, 2.094, 2.094, 2.094, 1.774, 0.891, 0.891, 1.710, 1.833  ]
, [-1.571, -0.803, -0.471, -0.367, 0.000, -0.576, -0.278, -0.873, -0.681, -0.035, -0.192  ]
, [0.000, -0.157, -0.087, -0.087, -0.087, -0.081, -0.082, 0.001, 0.001, 1.257, 1.239  ]
, [0.000, 0.000, 1.658, 0.698, 0.000, 0.072, 0.058, 0.454, 0.560, 1.134, 1.257  ]
]])
