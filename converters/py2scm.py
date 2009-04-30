#!/usr/bin/python
# -*- coding: utf-8 -*-
# dcmのtime-separateコマンドをschemeに変換するスクリプト
# usage

# from py2scm import *
#
# dcm = DCM2SCM()
#
# dcm.createAlias( ["BodyJoints", [
# ...
# dcm.setAlias(
# ...
# 

class DCM2SCM:
    def __init__(self):
        self.aliases = {}

    def createAlias(self, args):
        self.aliases[args[0]] = args[1]

    def setAlias(self, args):
        alias = self.aliases[args[0]]
        durations = args[4]
        data = args[5]

        print """
;XXX
(mc-registmotion %d "%s" TIMED #(
#(""" % (0, "Motion0")
        for i, v in enumerate(durations):
            print '#(',
            for j, d in enumerate(data):
                if len(data) == 19 and j == 10:
                    print "%.3ff" % d[4],
                print "%.3ff" % d[i],
            print ')'
        print ') #(',
        for i in range(len(durations)):
            if i == 0:
                print "%d" % durations[i],
            else:
                print "%d" % (durations[i] - durations[i-1]),
        print ')'
        print ')'
        print ')'

    def getTime(self, time):
        return time

