##############################################################################
# Name: vision_onMarkDataChange.py
# 
# Summary: Test the ALLandMarkDetection module using a callback mechanism.
#
# Usage: vision_onMarkDataChange.py [Naoqi IP address, local IP address]
#        - Naoqi IP: address Naoqi is listening to.
#        - local IP: address where you launch the script and that Naoqi can
#          use to call you back.
#
# Description:
#   - Start the LandMarkDetection extractor by subscribing to it.
#   - Create a Python broker using the provided Naoqi and local addresses.
#   - Create an ALModule object (markHandler) with its call back function.
#   - Call ALMemory's subscribeOnDataChange so that markHandler.onMarkChange()
#     is called whenever the detection results change.
#   - Wait for some time.
#   - Check that we detected some NaoMarks.
#
##############################################################################

# Used in debug logs.
testName = "python: vision_onMarkDataChange: "

import os
import sys
import time

# IP and PORT default values.
LOCAL_IP = "127.0.0.1"
LOCAL_PORT = 9999
IP = "127.0.0.1"
PORT = 9559

# Read IP address from first argument if any.
if len( sys.argv ) > 1:
  IP = sys.argv[1]

if len( sys.argv ) > 2:
  LOCAL_IP = sys.argv[2]

path = `os.environ.get("AL_DIR")`
home = `os.environ.get("HOME")`

########################################################
# import NaoQi lib
if path == "None":
  print "the environnement variable AL_DIR is not set, aborting..."
  sys.exit(1)
else:
  alPath = path + "/extern/python/aldebaran"
  alPath = alPath.replace("~", home)
  alPath = alPath.replace("'", "")
  sys.path.append(alPath)
  import naoqi
  from naoqi import ALBroker
  from naoqi import ALModule
  from naoqi import ALProxy
  from naoqi import ALBehavior
  from vision_definitions import*

##############################################################################
# Definition of our python module.
# The main point here is to declare a call back function "onMarkChange"
# which will be called by ALMemory whenever the landmark's results change.
class MarkHandlerModule(ALModule):
  def __init__(self, name):
    ALModule.__init__(self, name)
    self.BIND_PYTHON(name, "onMarkChange")
    self.mHasDetectedMarks = False

  # Call back function registered with subscribeOnDataChange that handles
  # changes in LandMarkDetection results.
  def onMarkChange(self, dataName, value, msg):
    print str(value)
    if (len(value) != 0):
      self.mHasDetectedMarks = True
  
  def hasDetectedMarks(self):
    return self.mHasDetectedMarks

##############################################################################


testFailed = 0

# Creating a proxy to ALLandMarkDetection
try:
  landMarkProxy = ALProxy("ALLandMarkDetection", IP, PORT)
except Exception,e:
  print "Error when creating ALLandMarkDetection proxy:"
  print str(e)
  exit(1)


# Subscribe to the ALLandMarkDetection module.
# This means that the module will write its results in memValue with
# the given period below.
subscriptionPeriod = 500

print "%s : Subscribe to the ALLandMarkDetection proxy..." % (testName)
try:
  landMarkProxy.subscribe("Test_LandMark", [ subscriptionPeriod ] )
  print "%s : Subscribe to the ALLandMarkDetection proxy... OK" % (testName)
except Exception, e:
  print "%s Error :"  %(testName)
  print str(e)
  testFailed = 1


# ALMemory variable where the ALLandMarkdetection module outputs its results.
memValue = "extractors/allandmarkdetection/landmarkdetected"

# Create a python broker on the local machine.
broker = ALBroker("pythonBroker", LOCAL_IP, LOCAL_PORT, IP, PORT)

try:
  markHandlerName = "markHandler"
  # Create our module object.
  markHandler = MarkHandlerModule(markHandlerName)

  # Have module.onMarkChange called back when detection results change.
  memoryProxy = ALProxy("ALMemory")
  memoryProxy.subscribeOnData(memValue, markHandler.getName(), "",
    "onMarkChange")

  # Let the NaoMark detection run for a little while.
  time.sleep(5)
  landMarkProxy.unsubscribe("Test_LandMark")
  
  # Shut the Python Broker down
  broker.shutdown()

except Exception, e:
  print "%s Error:"  %(testName)
  print str(e)
  testFailed = 1

# Check that we detected some Naomarks.
if (markHandler.hasDetectedMarks() == False):
  print "%s : Could not detect Naomarks !" % (testName) 
  testFailed = 1

if (testFailed == 1):
  print "%s : Failed" % (testName)
  exit(1)

print "%s : Success" % (testName)
