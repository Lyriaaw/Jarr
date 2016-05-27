# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:49:54 2016

@author: julienperret
"""


class Drone :
    
    def __init__(self):
        self.takeoff()

    def takeoff(self):
        self.setHeight(1.5)
    
    def setHeight(self, height):
        self.height=height
    
    def rotateSelf(self):
        return True
        
    def rotateLeft(self, distance):
        return True

    def rotateRight(self, distance):
        return True

    def move_backward(self):
        return True

    def move_forward(self):
        print 

    def left(self):
        return True

    def right(self):
        return True
    
    def land(self):
        self.setHeight(0)
    
    def hover(self):
        return True
    
    def halt(self):
        return True
    
    def turn_left(self):
        return True
    
    def turn_right(self):
        return True
        
def main():
    
    drone = Drone()
    
    v = input("Choisissez moi une vitesse de deplacement : ")

    while 1==1 :
        
        saisie = raw_input("Saisissez une commande : ")
        
        if saisie == "up" :
            drone.takeoff()
            print "Je décolle\n"
        
        elif saisie == "down" :
            drone.land()
            print "J'atteris\n"
            
        elif saisie == "moveforward":
            drone.speed=v
            drone.move_forward()
            print "J'avance\n"
        
        elif saisie == "movebackward":
            drone.speed=v
            drone.move_backward()
            print "Je recule\n"
            
        elif saisie == "moveright" :
            drone.move_right()
            print "Je me deplace a droite\n"
        
        elif saisie == "moveleft" :
            drone.move_left()
            print "Je me deplace a gauche\n"
        
        elif saisie == "turnleft" :
            drone.turn_left()
            print "Je tourne sur ma gauche"

        elif saisie == "turnright" :
            drone.turn_right()
            print "Je tourne sur ma droite"
            
        elif saisie == "hover" :
            drone.hover()
            print "Je stagne\n"
            
        else :
            break

    drone.land()
    print "J'atteris"
    drone.halt()

if __name__ == '__main__' :
    main()