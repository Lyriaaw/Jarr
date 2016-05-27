# -*- coding: utf-8 -*-
from numpy import tan
from numpy import pi

class Drone :
    
    def __init__(self):
        self.launch()

    def launch(self):
        self.setHeight(1.5)
    
    def setHeight(self, height):
        self.height=height
    
    def rotateSelf(self):
        return True
        
    def rotateLeft(self, distance):
        return True

    def rotateRight(self, distance):
        return True

    def leave(self):
        return True

    def comeBack(self):
        return True

    def left(self):
        return True

    def right(self):
        return True
    
    def land(self):
        print "J'atteris"

class Barre :
    
    def __init__(self, x, y, side):
        self.x=x
        self.y=y
        self.side=side
        print("Creation d'une barre !")
    
    def decrisToi(self, string):
        print("La barre {} a pour coordonnees ({},{}).\n".format(string, self.x, self.y))
        


def main():

        drone = Drone()
        b1 = Barre(100,250,True)
        b0 = Barre(360,250,False)
        b2 = Barre(500,250,True)
        
        tab = [b1,b0,b2]
        
        for i in range(len(tab)):
            
            if tab[i].side == False or len(tab) == 1 :
                barreMilieu = tab[i]
                barreMilieu.decrisToi("du milieu")
                
            else :
                if i > 0 :

                    if tab[i].x > tab[i-1].x :
                        barreDroite = tab[i]
                        barreDroite.decrisToi("de droite")
                    else :
                        barreGauche = tab[i]
                        barreGauche.decrisToi("de gauche")

                else :
                    if tab[i].x > tab[i+1].x :
                        barreDroite = tab[i]
                        barreDroite.decrisToi("de droite")
                    else :
                        barreGauche = tab[i]
                        barreGauche.decrisToi("de gauche")
        
        distanceDroneHomme = 5
        
        pixelHoriBGBD = abs(barreDroite.x-barreGauche.x)
        distanceHoriBGBD = distanceDroneHomme*tan(93*(pi/180)*pixelHoriBGBD/640)
        
        pixelHoriBGBM = abs(barreGauche.x-barreMilieu.x)
        distanceHoriBGBM = distanceDroneHomme*tan(93*(pi/180)*pixelHoriBGBM/640)
        
        pixelHoriBMBD = abs(barreMilieu.x-barreDroite.x)
        distanceHoriBMBD = distanceDroneHomme*tan(93*(pi/180)*pixelHoriBMBD/640)         
           
        pixelVertiBGBD = abs(barreDroite.y-barreGauche.y)
        distanceVertiBGBD = distanceDroneHomme*tan(93*(pi/180)*pixelVertiBGBD/640)
        
        pixelVertiBGBM = abs(barreGauche.y-barreMilieu.y)
        distanceVertiBGBM = distanceDroneHomme*tan(93*(pi/180)*pixelVertiBGBM/640)
        
        pixelVertiBMBD = abs(barreMilieu.y-barreDroite.y)
        distanceVertiBMBD = distanceDroneHomme*tan(93*(pi/180)*pixelVertiBMBD/640)
        
        pixelHoriBMOr = barreMilieu.x-320
        
        if pixelHoriBMOr < 0 :
            distanceHoriBMOr = distanceDroneHomme*tan(93*(pi/180)*pixelHoriBMOr/640)
        elif pixelHoriBMOr > 0 :
            distanceHoriBMOr = -distanceDroneHomme*tan(93*(pi/180)*pixelHoriBMOr/640)

        if len(tab) <= 1 :
            drone.rotateSelf()

        elif len(tab) == 2 :
            if barreMilieu == None :
                return True
            elif barreGauche == None :
                drone.rotateRight()
            else : 
                drone.rotateGauche()
        
        else :
            
            if distanceHoriBGBM < 0.05 and distanceHoriBMBD < 0.05 :
                drone.land()
                
            elif 0.2 < distanceVertiBGBM < 0.9 or 0.2 < distanceVertiBMBD < 0.9 :
                drone.setAltitude(19.2857*distanceVertiBGBM - 2.3571)
                
            elif pixelHoriBGBD < 40 :
                while pixelHoriBGBD < 40 :
                    drone.comeBack()
                    
            elif pixelHoriBGBD > 80 :
                while pixelHoriBGBD > 80 :
                    drone.leave()
            
            elif distanceHoriBMOr < 0.3 :
                drone.left()
            
            elif barreMilieu.x > 6 :
                drone.right()
            
            
            
            
if __name__ == '__main__' :
    main()