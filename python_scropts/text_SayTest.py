"""
StiffnessOon

Contains some examples to set stiffness on for the whole body
of Nao, or chain by chain, or joint by joint

"""

from motion_CurrentConfig import *


####
# Create python broker

try:
  broker = ALBroker("pythonBroker","127.1.0.1",9999,IP, PORT)
except RuntimeError,e:
  print("cannot connect")
  exit(1)

####
# Create motion proxy

print "Creating motion proxy"


try:
  textProxy = ALProxy("ALTextToSpeech")
except Exception,e:
  print "Error when creating motion proxy:"
  print str(e)
  exit(1)


#**************************
# BODY
#**************************

#going slowly to 1.
#textProxy.say("ich. nee. sun. she. go. rock. nana. hatch. queue. jew.");



print "auido"

try:
  aup = ALProxy("ALAudioPlayer")
except Exception,e:
  print "Error when creatin' motion proxy:"
  print str(e)
  exit(1)

aup.playFile("/home/root/mac.wav")
