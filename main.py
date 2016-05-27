#Python script

import traitement_image as Ti
import drone_relation as DroneSimulated
import libardrone
import mouvement as Move

from PIL import Image as Image



def main():
    # drone = Drone.Drone()
    # drone = libardrone.ARDrone()



    """
    move = Move.Mouvement()
    move.initDrone()



    counter = 1

    while counter < 3 :
        print ""
        print ""
        print ""
        print "Starting new thing"
        image = DroneSimulated.getImage(counter)
        zones = Ti.manageImage(image)
        move.getMove(zones)

        #if move == -1:
         #   break

        counter += 1
        print "Counter = " + str(counter)


    move.makeMove()

    while (raw_input("Type anything")):
        print "test"




    Ti.stopDrone()

    """



    zones = Ti.manageImage(Image.open("Images/ImageBigTest2.png"))

    for zone in zones:
        outputString = ""

        outputString += str(zone.x) + " "
        outputString  += str(zone.y) + " "
        outputString += str(zone.side)

        print outputString

    drone = Drone.Drone()
    drone.speed = 0.1
    while True : 
        image = Drone.getImage()
        zones = Ti.manageImage(image)
        move = Move.getMove(zones)


main()







