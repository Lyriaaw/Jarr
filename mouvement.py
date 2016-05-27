# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:39:42 2016

@author: julienperret
"""
import drone_relation as DroneManagment
import traitement_image as Ti
import libardrone

from numpy import tan
from numpy import pi



#drone = libardrone.ARDrone()

class Mouvement :
    # drone = libardrone.ARDrone()

    def __init__(self):
        self.drone = libardrone.ARDrone()

        bat = self.drone.navdata.get(0, dict()).get('battery', 0)
        print "Current Battery Level : %i / 100" % bat

    def takeoff(self):
        self.drone.takeoff()
        print "I'm taking off"

    def setHeight(self, height):
        self.height = height
        print "I'm going to ", height, "m"

    def rotateSelf(self):
        self.drone.turn_left()
        print "I'm rotating on myself"

    def rotateLeft(self):
        self.drone.turn_left()
        print "I'm rotating left"

    def rotateRight(self):
        print "I'm rotating right"
        self.drone.turn_right()

    def move_backward(self):
        print "I'm moving backward"

    def move_forward(self):
        self.drone.move_forward()
        print "I'm moving forward"

    def left(self):
        self.drone.move_left()
        print "I'm going left"

    def right(self):
        self.drone.move_right()
        print "I'm going right"

    def land(self):
        self.drone.land()
        print "I'm landing"
        self.setHeight(0)

    def hover(self):
        self.drone.hover()
        print "I'm hovering"

    def halt(self):
        self.drone.halt()
        print "I'm halting"

    def turn_left(self):
        self.drone.turn_left()
        print "I'm turning left"

    def turn_right(self):
        self.drone.turn_right()
        print "I'm turning right"

    def initDrone(self):
        self.drone.speed = 0.2
        self.drone.takeoff()

    def stopDrone(self):
        self.drone.land()
        self.drone.halt()

    def makeMove(self):
        self.drone.move_right()



    def getMove(self, zones):
        print "Finding the right move !"

        distanceDroneHomme = 1

        # drone = DroneManagment.Drone()
        # drone = libardrone.ARDrone()

        # if drone < 0:
        #   print "Drone Error"
        #  return -1


        (barreGauche, barreMilieu, barreDroite) = getBarsName(zones)

        (pixelHoriBGBD,
         distanceHoriBGBD,
         pixelHoriBGBM,
         distanceHoriBGBM,
         pixelHoriBMBD,
         distanceHoriBMBD,
         pixelVertiBGBD,
         distanceVertiBGBD,
         pixelVertiBGBM,
         distanceVertiBGBM,
         pixelVertiBMBD,
         distanceVertiBMBD,
         pixelHoriBMOr,
         distanceHoriBMOr) = getMeasures(barreGauche, barreMilieu, barreDroite)

        if len(zones) <= 1:
            print "turn_left"
            self.turn_left()
        elif len(zones) == 2:
            if barreMilieu == None:
                return True
            elif barreGauche == None:
                print "Turn_right"
                self.turn_right()
            else:
                print "TurnLeft"
                self.turn_left()

        else:

            if distanceHoriBGBM < 0.05 and distanceHoriBMBD < 0.05:
                print "land"
                self.land()

            elif 0.2 < distanceVertiBGBM < 0.9 or 0.2 < distanceVertiBMBD < 0.9:
                drone.setHeight(19.2857 * distanceVertiBGBM - 2.3571)
            elif distanceHoriBMOr < -0.3:
                print "left"
                self.left()

            elif distanceHoriBMOr > 0.3:
                print "Right"
                self.right()
            elif pixelHoriBGBD < 9:
                print "forward"
                self.move_forward()

            elif pixelHoriBGBD > 27:
                print "backward"
                self.move_backward()


            else:
                print "Hover"
                self.hover()

        return True




drone = DroneManagment.Drone()

def getMove(zones):
    print "Finding the right move !"
    
    distanceDroneHomme = 5

    
    (barreGauche, barreMilieu, barreDroite) = getBarsName(zones)

    (pixelHoriBGBD,
     distanceHoriBGBD,
     pixelHoriBGBM,
     distanceHoriBGBM,
     pixelHoriBMBD,
     distanceHoriBMBD,
     pixelVertiBGBD,
     distanceVertiBGBD,
     pixelVertiBGBM,
     distanceVertiBGBM,
     pixelVertiBMBD,
     distanceVertiBMBD,
     pixelHoriBMOr,
     distanceHoriBMOr) = getMeasures(barreGauche, barreMilieu, barreDroite)


  
    if len(zones) <= 1 :
        drone.rotateSelf()
    elif len(zones) == 2 :
        if barreMilieu == None :
            return True
        elif barreGauche == None :
            drone.rotateRight()
        else : 
            drone.rotateLeft()
    
    else :
        
        if distanceHoriBGBM < 0.05 and distanceHoriBMBD < 0.05 :
            drone.land()
            
        elif 0.2 < distanceVertiBGBM < 0.9 or 0.2 < distanceVertiBMBD < 0.9 :
            drone.setHeight(19.2857*distanceVertiBGBM - 2.3571)
            
        elif pixelHoriBGBD < 9 :
            drone.move_forward()
                
        elif pixelHoriBGBD > 27 :
            drone.move_backward()
        
        elif distanceHoriBMOr < -0.3 :
            drone.left()
            
        elif distanceHoriBMOr > 0.3 :
            drone.right()
        
        else :
            drone.hover()
    
    return True
    
def getBarsName(zones):

    barreDroite = None
    barreGauche = None
    barreMilieu = None

    for i in range(len(zones)):

        if zones[i].side == False or len(zones) == 1:
            barreMilieu = zones[i]
            barreMilieu.decrisToi("du milieu")

        else:
            if i > 0:

                if zones[i].x > zones[i - 1].x:
                    barreDroite = zones[i]
                    barreDroite.decrisToi("de droite")
                else:
                    barreGauche = zones[i]
                    barreGauche.decrisToi("de gauche")

            else:
                if zones[i].x > zones[i + 1].x:
                    barreDroite = zones[i]
                    barreDroite.decrisToi("de droite")
                else:
                    barreGauche = zones[i]
                    barreGauche.decrisToi("de gauche")

    return (barreGauche, barreMilieu, barreDroite)



def getMeasures(barreGauche, barreMilieu, barreDroite):

    distanceDroneHomme = 5
    pixelHoriBGBD = None
    distanceHoriBGBD = None
    pixelHoriBGBM = None
    distanceHoriBGBM = None
    pixelHoriBMBD = None
    distanceHoriBMBD = None
    pixelVertiBGBD = None
    distanceVertiBGBD = None
    pixelVertiBGBM = None
    distanceVertiBGBM = None
    pixelVertiBMBD = None
    distanceVertiBMBD = None
    pixelHoriBMOr = None
    distanceHoriBMOr = None

    if barreDroite != None and barreGauche != None:
        pixelHoriBGBD = abs(barreDroite.x - barreGauche.x)
        distanceHoriBGBD = 2 * distanceDroneHomme * tan(93 * pi / (180 * 2)) * pixelHoriBGBD / 640

    if barreMilieu != None and barreGauche != None:
        pixelHoriBGBM = abs(barreGauche.x - barreMilieu.x)
        distanceHoriBGBM = 2 * distanceDroneHomme * tan(93 * pi / (180 * 2)) * pixelHoriBGBM / 640

    if barreMilieu != None and barreDroite != None:
        pixelHoriBMBD = abs(barreMilieu.x - barreDroite.x)
        distanceHoriBMBD = 2 * distanceDroneHomme * tan(93 * pi / (180 * 2)) * pixelHoriBMBD / 640

    if barreGauche != None and barreDroite != None:
        pixelVertiBGBD = abs(barreDroite.y - barreGauche.y)
        distanceVertiBGBD = 2 * distanceDroneHomme * tan(76 * pi / (180 * 2)) * pixelVertiBGBD / 480

    if barreMilieu != None and barreGauche != None:
        pixelVertiBGBM = abs(barreGauche.y - barreMilieu.y)
        distanceVertiBGBM = 2 * distanceDroneHomme * tan(76 * pi / (180 * 2)) * pixelVertiBGBM / 480

    if barreMilieu != None and barreDroite != None:
        pixelVertiBMBD = abs(barreMilieu.y - barreDroite.y)
        distanceVertiBMBD = 2 * distanceDroneHomme * tan(76 * pi / (180 * 2)) * pixelVertiBMBD / 480

    if barreMilieu != None:
        pixelHoriBMOr = barreMilieu.x - 320
        if pixelHoriBMOr <= 0:
            distanceHoriBMOr = -2 * distanceDroneHomme * tan(93 * pi / (180 * 2)) * pixelHoriBMOr / 640
        elif pixelHoriBMOr > 0:
            distanceHoriBMOr = 2 * distanceDroneHomme * tan(93 * pi / (180 * 2)) * pixelHoriBMOr / 640

    return (pixelHoriBGBD,
            distanceHoriBGBD,
            pixelHoriBGBM,
            distanceHoriBGBM,
            pixelHoriBMBD,
            distanceHoriBMBD,
            pixelVertiBGBD,
            distanceVertiBGBD,
            pixelVertiBGBM,
            distanceVertiBGBM,
            pixelVertiBMBD,
            distanceVertiBMBD,
            pixelHoriBMOr,
            distanceHoriBMOr)




