"""
shoot.py

shoot one photo(yuv).
th_95, Shoot The Bullet!!
"""

import sys

from motion_CurrentConfig import *
from cameraConfig import *


####
# command line arguments
argv = sys.argv
argc = len(argv)

if (argc != 2):
	print "usage: %s [IP Adrress]"
	quit()


IP = argv[1]


####
# Create python broker

try:
	broker = ALBroker("pythonBroker", "127.0.0.1", BPORT, IP, PORT)
except RuntimeError,e:
	print("cannot connect")
	exit(1)

####
# Create motion proxy

print "Creating NaoCam proxy"


try:
	camProxy = ALProxy("NaoCam")
except Exception,e:
	print "Error when creating NaoCam proxy:"
	print str(e)
	exit(1)



#Register a Generic Video Module (G.V.M.) to the V.I.M.
camProxy.startFrameGrabber()
nameId = camProxy.register("digicame3py_GVM", cResol, cColor, cFps)

#Set cameraConfs (cameraConfig.py)
camProxy.setParam(kCameraBrightnessID, cBrightness)
camProxy.setParam(kCameraContrastID, cContrast)
camProxy.setParam(kCameraSaturationID, cSaturation)
camProxy.setParam(kCameraRedChromaID, cWhiteRed)
camProxy.setParam(kCameraBlueChromaID, cWhiteBlue)
camProxy.setParam(kCameraGainID, cGain)
#setParam(kCameraExposureID, cExposure)

camProxy.setParam(kCameraAutoGainID, cAutoGain)
camProxy.setParam(kCameraAutoExpositionID, cAutoExposition)
camProxy.setParam(kCameraAutoWhiteBalanceID, cAutoWhiteBalance)

camProxy.setParam(kCameraHFlipID, cHFlip)
camProxy.setParam(kCameraVFlipID, cVFlip)
camProxy.setParam(kCameraLensXID, cLensX)
camProxy.setParam(kCameraLensYID, cLensY)


#Get a pointer to the video source image and release the image when process is finished
#rawImg = camProxy.getDirectRawImageRemote(nameId)

rawImg = camProxy.getImageRemote(nameId)
  
#  tstamp = rawImg[4] << 64 + rawImg[5];
tstamp = ((rawImg[4] << 32) + rawImg[5]);
  
if rawImg[2] == 1:
	print "write image to digicame%d.pgm" % (tstamp)
	conv = os.popen("rawtopgm %d %d > digicame%d.pgm" % (rawImg[0], rawImg[1], tstamp), 'wb')
elif rawImg[2] == 3:
	print "write image to digicame%d.ppm" % (tstamp)
	conv = os.popen("rawtoppm %d %d > digicame%d.ppm" % (rawImg[0], rawImg[1], tstamp), 'wb')
#	yuvu to yuv
elif rawImg[2] == 2:
	print "write image to digicame%d.ppm" % (tstamp)
	conv = os.popen("./yuyv2yuv | rawtoppm %d %d > ./ppm/digicame%d.ppm" % (rawImg[0], rawImg[1], tstamp), 'wb')

else:
	print "Error unsupported."
	print "rawImg[2]: %d" % (rawImg[2])
	exit(1)
conv.write(rawImg[6]);
conv.close();
#time.sleep(1)

#camProxy.releaseDirectRawImage(nameId)

#Unregister the G.V.M.
#camProxy.unRegister(nameId)
camProxy.stopFrameGrabber()
#More explications in the documentation..

print "Test terminated successfully" 
