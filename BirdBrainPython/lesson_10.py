from BirdBrain import Finch
import time

robot = Finch()



def exercise1():
    #This makes a function that can draw a square and impliments it
    def drawSquare():
        for i in range(6):
            bird.setMove('F', 15, 50)
            bird.setTurn('R', 90, 50)
        bird.setTurn('L', 60, 50)
    for i in range(6):
        drawSquare()

def exercise2():
    #This makes a function that can draw a circle
    def drawCircle():
        for i in range(365)
        robot.setMove('F', 1, 100)
        robot.setTurn('R', 1, 100)

    drawCircle()
    

def exercise3():
    #Track the line until you find an obstacle
    def lineTrack():
        while (robot.getDistance() > 20):
            robot.setMove('F', 10, 100)
            
    while (robot.getDistance() > 20):
        lineTrack()

def exercise4():
    #This function makes it so that the robot can maneuver through the maze
    def wallFollowing():
        while robot.getDistance() > 20:
            robot.setMove('F', 20, 50)
        robot.setTurn('R', 90, 50)
        while robot.getDistance > 10:
            robot.setMove('F', 10, 50)
        robot.setTurn('L', 90, 50)
        while robot.getDistance > 16:
            robot.setMove('F', 12, 50)
        robot.setTurn('L', 90, 50)
        while robot.getDistance > 10:
            robot.setMove('F', 5, 50)
        robot.setTurn('R', 90, 50)
    wallfollowing()

def exercise5():
    #This function makes the finch draw a square. It requires
    #an integer parameter that is the side length of the square
    #in centimeters.
    def drawSquare2(size):
        for i in range(4)
        robot.setMove('F', size, 50)
        robot.setTurn('R', 90, 50)

    drawSquare2(10)


def exercise6():
    #This code makes it so that it blinks the colors chosen.
    def blinkAll(red, green, blue):
        robot.setTail('all', red, green, blue)
        robot.setBeak(red, green, blue)
        time.sleep(3)
        robot.setBeak(red, green, blue)
        robot.setTail('all', red, green, blue)
        time.sleep(3)
        robot.stopAll()
    while not getButton('A'):
        blinkAll(13, 40, 100)
