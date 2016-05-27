# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:39:25 2016

@author: julienperret
"""

from scipy import *
from PIL import Image as Image


## a pixel is a image basic element. Can determinate if he is red and
## know its PixelGroup
class Pixel:
    # We are searching for red
    minRedValue = 190
    maxOtherValues = 50

    test = 0;



    def __init__(self, x, y, r, g, b):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.pixelGroup = False

    def displayThisPixel(self):  # I hate it, but it's useful sometimes
        print "This pixel position is x = " + str(self.x) + " y = " + str(self.y) + " and its color is " + str(
            self.r) + "." + str(self.g) + "." + str(self.b)

    def quickDisplay(self):

        outputString = "(" + str(self.x) + "," + str(self.y) + " [" + str(self.r) + "," + str(self.g) + "," + str(
            self.b) + "]"
        if self.pixelGroup != False:
            outputString += str(self.pixelGroup.id) + ","
        else:
            outputString += "N,"

        if self.isRed():
            outputString += "R)"
        else:
            outputString += "O)"

        for it in range(len(outputString), 23):
            outputString += " "
        return outputString

    def isRed(self):
        if self.r > Pixel.minRedValue and self.g < Pixel.maxOtherValues and self.b < Pixel.maxOtherValues:
            return True
            # print "I'm Red"
        else:
            return False
            # print "I'm not red"

    def setPixelGroup(self, pixelGroup):
        self.pixelGroup = pixelGroup

    def belongToPixelGroup(self):  # if the pixel belong to a pixel group
        if self.pixelGroup != False:
            return True
        else:
            return False




## A PixelGroup is a neighborhood of pixel on the image
## Has average X and Y coordinates, the amount of pixel he owns and his ID number
class PixelGroup:
    actualAmount = 0

    def __init__(self):
        self.id = PixelGroup.actualAmount + 1
        PixelGroup.actualAmount += 1
        self.pixelsList = []
        self.side = False
        self.x = 0
        self.y = 0

    def addPixel(self, pixel):
        self.pixelsList.append(pixel)

    def calculateAverageCoordinates(self):
        # print "id = " + str(self.id) + " pixelsList size = " + str(len(self.pixelsList))

        self.x = 0
        self.y = 0
        for pixel in self.pixelsList:
            self.x = self.x + pixel.x
            self.y = self.y + pixel.y
        if len(self.pixelsList) > 0:
            self.x /= len(self.pixelsList)
            self.y /= len(self.pixelsList)

        return self.x, self.y

    def displayAllPixels(self):
        for currentPixel in self.pixelsList:
            currentPixel.displayThisPixel()

    def getAllPixels(self):
        return self.pixelsList

    def decrisToi(self, string):
        print("La barre {} a pour coordonnees ({},{}).\n".format(string, self.x, self.y))


## Creating the pixel matrix
def geratePixelMatrix(height):
    generatedPixelMatrix = []
    for it in range(height):
        generatedPixelMatrix.append([])

    return generatedPixelMatrix


## Filling matrix width pixels
def fillPixelMatrix(emptyMatrix, pointMatrix, width, height):
    for jt in range(height):
        for it in range(width):
            # print "Coordinates in the map : it : " + str(it) + " , jt : " + str(jt)

            # creating new pixel with all datas (x, y, (r, g, b))
            tempPixel = Pixel(it, jt, pointMatrix[it, jt][0], pointMatrix[it, jt][1], pointMatrix[it, jt][2])
            emptyMatrix[jt].append(tempPixel)  # adding pixel to pixel matrix
    return emptyMatrix


def displayPixelMatrix(pixelMatrix, width, height):
    for bt in range(height):  # displaying the matrix with grave
        lineString = ""
        for at in range(width):
            lineString += str(pixelMatrix[bt][at].quickDisplay()) + " "
        print lineString


def createPixelsZone(pixelMatrix, width, height):
    # all the pixels zones
    pixelsGroupsList = []

    for jt in range(height):
        for it in range(width):
            # print "Working on  it = " + str(it) + " jt = " + str(jt) + " pixel = " + str(pixelMatrix[jt][it].quickDisplay())
            # pixelMatrix[jt][it].displayThisPixel()

            if pixelMatrix[jt][it].isRed() and not pixelMatrix[jt][it].belongToPixelGroup():
                # print "This pixel is red !"

                pixelMatrix, pixelsGroupsList = infectRedZone(pixelMatrix, width, height, it, jt, pixelsGroupsList)

    return pixelMatrix, pixelsGroupsList


def infectRedZone(pixelMatrix, width, height, initialPixelX, initialPixelY, pixelsGroupsList):
    # print "Launching a red Pixel Infection from " + pixelMatrix[initialPixelY][initialPixelX].quickDisplay()

    # List with all already infected pixel
    infectedPixels = []

    pixelGroup = PixelGroup()  # Creating the pixelGroup
    pixelsGroupsList.append(pixelGroup)
    pixelMatrix[initialPixelY][initialPixelX].pixelGroup = pixelGroup

    infectedPixels.append(pixelMatrix[initialPixelY][initialPixelX])

    # print "Group " + str(pixelGroup.id) + " is created"

    # Running to every pixels to prepare infection
    for currentPixel in infectedPixels:
        # The max function avoid IndexOutOfBoundException
        for jt in range(max([currentPixel.y - 1, 0]), min([currentPixel.y + 2, height])):
            for it in range(max([currentPixel.x - 1, 0]), min([currentPixel.x + 2, width])):
                # print "Running throw pixels : " + pixelMatrix[jt][it].quickDisplay()
                if pixelMatrix[jt][it].isRed() and not pixelMatrix[jt][it].belongToPixelGroup():
                    pixelMatrix[jt][it].pixelGroup = pixelGroup
                    pixelGroup.addPixel(pixelMatrix[jt][it])

                    infectedPixels.append(pixelMatrix[jt][it])

    return pixelMatrix, pixelsGroupsList


def displayPixelsGroups(pixelsGroupsList):
    for pixelGroup in pixelsGroupsList:
        x, y = pixelGroup.calculateAverageCoordinates()
        print "x = " + str(x) + " y = " + str(y)


def getPixelsGroupsSideValue(pixelsGroups, width):

    for it in range(len(pixelsGroups)):
        pixelsGroups[it].calculateAverageCoordinates()


    if len(pixelsGroups) == 3:
        for it in range(len(pixelsGroups)):
            if pixelsGroups[it].x == max(pixelsGroups[0].x, pixelsGroups[1].x, pixelsGroups[2].x) or pixelsGroups[it].x == min(pixelsGroups[0].x, pixelsGroups[1].x, pixelsGroups[2].x):
                pixelsGroups[it].side = True
            else:
                pixelsGroups[it].side = False

    # for this search we determine the absolute value between the group and the center of the image
    # The middle group is the one that as the smallest absolute value
    if len(pixelsGroups) == 2:
        print "There is two pixels groups"
        absoluteDistance0 = getAbsoluteDistance(pixelsGroups[0].x, width);
        absoluteDistance1 = getAbsoluteDistance(pixelsGroups[1].x, width);

        pixelsGroups[0].side = True if absoluteDistance0 < absoluteDistance1 else False
        pixelsGroups[1].side = not pixelsGroups[0].side





def getAbsoluteDistance(x, imageWidth):
    return abs( x - imageWidth / 2 )











    return pixelsGroups


def manageImage(image):
    print "Managing image"

    basePixelMatrix = image.load()  # getting image as an array
    width, height = image.size  # Getting the future matrix size

    # print "This image's size is " + str(width) + " x " + str(height)

    emptyPixelMatrix = geratePixelMatrix(height)

    pixelMatrix = fillPixelMatrix(emptyPixelMatrix, basePixelMatrix, width, height)

    # displayPixelMatrix(pixelMatrix, width, height)

    pixelMatrix, pixelsGroups = createPixelsZone(pixelMatrix, width, height)



    pixelsGroups = getPixelsGroupsSideValue(pixelsGroups, width)

    return pixelsGroups

    # displayPixelMatrix(pixelMatrix, width, height)
    # displayPixelsGroups(pixelsGroups)
