"""
shoot.py

shoot one photo(yuv).
th_95, Shoot The Bullet!!
"""
import os
import sys
import time
import datetime

aldir_env = os.environ.get("AL_DIR")

if aldir_env is None:
	print "The environnement variable AL_DIR is not set, aborting..."
	exit(1)
aldir = os.path.abspath(aldir_env)
alpath = os.path.join(aldir,"extern/python/aldebaran")
sys.path.append(alpath)
try:
	from naoqi import ALProxy
	from naoqi import ALBroker
except ImportError, err:
	print "Unable to import naoqi module: " + str(err)
	exit(1)
	
from cameraConfig import *

IP = "192.168.1.51" #default ip
PORT = 9559 #default port

####
# command line arguments
argv = sys.argv
argc = len(argv)
if (argc != 3):
	print "usage: %s [IP Adrress] [Shoot Count]" % argv[0]
	quit()

IP = argv[1]
Count = int(argv[2])

####
# print
print "Connect to: Using IP: " + str(IP) + " and port: "  + str(PORT)

####
# Create proxy
try:
	print "Creating ALVideoDevice proxy ..."
	camProxy = ALProxy("ALVideoDevice", IP, PORT)
	print "Creating ALAudioPlayer proxy ..."
	audioProxy = ALProxy("ALAudioPlayer", IP, PORT)
except Exception,e:
	print "Error when creating proxy:"
	print str(e)
	exit(1)

#Register a Generic Video Module (G.V.M.) to the V.I.M.
camProxy.startFrameGrabber()
nameId = camProxy.subscribe("digicame3py_GVM", cResol, cColor, cFps)

#Set cameraConfs (cameraConfig.py)
print "Setting to camera configuration ..."
print "----------"
camProxy.setParam(kCameraBrightnessID, cBrightness)
camProxy.setParam(kCameraContrastID, cContrast)
camProxy.setParam(kCameraSaturationID, cSaturation)
camProxy.setParam(kCameraRedChromaID, cWhiteRed)
camProxy.setParam(kCameraBlueChromaID, cWhiteBlue)
camProxy.setParam(kCameraGainID, cGain)
camProxy.setParam(kCameraExposureID, cExposure)

camProxy.setParam(kCameraAutoGainID, cAutoGain)
camProxy.setParam(kCameraAutoExpositionID, cAutoExposition)
camProxy.setParam(kCameraAutoWhiteBalanceID, cAutoWhiteBalance)

camProxy.setParam(kCameraHFlipID, cHFlip)
camProxy.setParam(kCameraVFlipID, cVFlip)
camProxy.setParam(kCameraLensXID, cLensX)
camProxy.setParam(kCameraLensYID, cLensY)

print "CameraSelect: " + ("TOP" if cSelectCamera == cTopCam else "BOTTOM")
camProxy.setParam(kCameraSelectID, cSelectCamera)

print "----------"
print "Setting done."

time.sleep(1)

#Get a pointer to the video source image and release the image when process is finished
#rawImg = camProxy.getDirectRawImageRemote(nameId)
for x in range(Count):
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
	time.sleep(1)

#camProxy.releaseDirectRawImage(nameId)

#releaseImage
camProxy.releaseImage(nameId)
#Unregister the G.V.M.
camProxy.unsubscribe(nameId)
camProxy.stopFrameGrabber()

####
# play shot sound.
try:
	audioProxy.post.stop()
	audioProxy.post.playFile("/opt/naoqi/data/wav/bip_gentle.wav")
except Exception,e:
	print "error: sound player."

####
# output CameraConf.scm
print "writing to CameraConf.scm ..."
d = datetime.datetime.today()
fw = open('cameraConf.scm', 'w')
fw.write(';Camera Settings\n')
fw.write(';date : ' + d.strftime("%Y-%m-%d %H:%M:%S") + '\n')
fw.write('\n')
fw.write('(vc-set-param AWB %d)\n' % cAutoWhiteBalance)
fw.write('(vc-set-param AGC %d)\n' % cAutoGain)
fw.write('(vc-set-param AEC %d)\n' % cAutoExposition)
fw.write('\n')
fw.write('(vc-set-param Brightness %d)\n' % cBrightness)
fw.write('(vc-set-param Contrast %d)\n' % cContrast)
fw.write('(vc-set-param Gain %d)\n' % cGain)
fw.write('(vc-set-param Exposure %d)\n' % cExposure)
fw.write('(vc-set-param RedChroma %d)\n' % cWhiteRed)
fw.write('(vc-set-param BlueChroma %d)\n' % cWhiteBlue)
fw.close()

print "SHOOT SUCCESSFUL\n"
