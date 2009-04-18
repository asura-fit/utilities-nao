"""
DCM でモーションを再生する.

DCMはけっこう危険なので、かならずRed bookのDCMの章をみること.

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

dcm.createAlias( ["ChestLeds", [
   "ChestBoard/Led/Red/Actuator/Value",
   "ChestBoard/Led/Green/Actuator/Value",
   "ChestBoard/Led/Blue/Actuator/Value"
   ]])

dcm.set(["ChestLeds", "ClearAll",  [
  [1.0, dcm.getTime(200)],
  [0.0, dcm.getTime(400)],
  [1.0, dcm.getTime(600)],
  [0.0, dcm.getTime(800)]
  ] ])

print "dcm ok"
exit(0)
