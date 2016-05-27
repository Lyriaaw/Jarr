# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:38:16 2016

@author: julienperret
"""

from PIL import Image as Image



def getImage(testProcedureImageValue):
    print "Getting the image"
    # drone = Drone()

    fileName = "Images/ImageBigTest" + str(testProcedureImageValue) + ".png"

    # fileName = "Images/ImageBigTest5.png"
    img = Image.open(fileName)


    img = Image.open("ImageBigTest.png")
    return img

class Drone :


    def __init__(self):
        self.takeoff()

    def takeoff(self):
        print "I'm taking off"
        self.setHeight(1.5)

    def setHeight(self, height):
        self.height=height
        print "I'm going to ",height,"m"

    def rotateSelf(self):
        print "I'm rotating on myself"
        return True

    def rotateLeft(self):
        print "I'm rotating left"
        self.turn_left()
        return True

    def rotateRight(self):
        print "I'm rotating right"
        self.turn_right()
        return True

    def move_backward(self):
        print "I'm moving backward"
        return True

    def move_forward(self):
        print "I'm moving forward"
        print

    def left(self):
        print "I'm going left"
        return True

    def right(self):
        print "I'm going right"
        return True

    def land(self):
        print "I'm landing"
        self.setHeight(0)

    def hover(self):
        print "I'm hovering"
        return True

    def halt(self):
        print "I'm halting"
        return True

    def turn_left(self):
        print "I'm turning left"
        return True

    def turn_right(self):
        print "I'm turning right"
        return True
