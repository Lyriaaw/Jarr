#!/usr/bin/env python
import time, libardrone

drone = libardrone.ARDrone()

def run():
    v = input("Choisissez moi une vitesse de deplacement : ")

    while 1==1 :
        
        saisie = raw_input("Saisissez une commande : ")
        
        if saisie == "up" :
            drone.takeoff()
            print "Je decolle\n"
        
        elif saisie == "down" :
            drone.land()
            print "J'atteris\n"
            
        elif saisie == "moveforward":
            drone.speed=v
            drone.move_forward()
            print "J avance\n"
        
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

run()

drone.land()