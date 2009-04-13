"""
 This file will be read by shoot.py.

 Please descript camera configurations.
 
 Parameter is shown vision_definitions.py
"""

from vision_definitions import *


###################################
# Basic Camera Configrations

#Auto Gain (off, on)
cAutoGain = OFF
#Auto Exposition
cAutoExposition = ON
#Auto WhiteBalance
cAutoWhiteBalance = OFF

# Whitebalance
# Red Chroma [0, 255]
cWhiteRed = 76

# Blue Chroma [0, 255]
cWhiteBlue = 160

# Gain [0, 255]
cGain = 4

#Exposure [?, ?]
cExposure = 42


###################################
# Advanced Camera Configrations

#resolution
cResol = kQVGA

#colourspace
cColor = kYUV422InterlacedColorSpace

#frame rate (5, 10, 15, 30)
cFps = 30

#Brightness [0, 255]
cBrightness = 128

#Contrast [0, 127]
cContrast = 64

#Saturation [0, 255]
cSaturation = 128

#Hue [-180, 180]
cHue = 0

#Horizontal Flip
cHFlip = 1
#Vertical Flip
cVFlip = 1

#LensX
cLensX = 0
#LensY
cLensY = 0

