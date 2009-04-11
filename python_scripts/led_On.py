"""
MotionStop

Stops any ALMotion task.
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
  leds = ALProxy("ALLeds")
except Exception,e:
  print "Error when creating led proxy:"
  print str(e)
  exit(1)


 # leds.on("AllLeds")
#  leds.off("AllLeds")
  leds.on("AllLeds")

  # Turn the red LED of the left foot half on
  leds.set("LFoot/Led/Red/Actuator/Value",0.5)

  # Turn the green face LEDs half on
  leds.set("FaceLedsGreen",0.5)
  leds.rasta(10)

print "LEDs switched on"


