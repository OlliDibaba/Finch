from BirdBrain import Finch
import time

robot = Finch()

def exercise1():
    # the finch moves forward and backward 2 times
    robot.setMove('F', 30, 100)
    robot.setMove('B', 30, 100)
    robot.setMove('F', 30, 100)
    robot.setMove('B', 45, 100)

def exercise2():
    #The robot turns right
    robot.setTurn('R', 90, 100)

def exercise3():
    #The robot turns left then right
    robot.setTurn('L', 360, 50)
    robot.setTurn('R', 360, 100)

def exercise4():
    #The robot draws a square
    robot.setMove('F', 50, 100)
    robot.setTurn('R', 90, 100)
    robot.setMove('F', 50, 100)
    robot.setTurn('R', 90, 100)
    robot.setMove('F', 50, 100)
    robot.setTurn('R', 90, 100)
    robot.setMove('F', 50, 100)
    robot.setTurn('R', 90, 100)


def exercise5():
    #Finch draws a cross
    robot.setMove('F', 100, 100)
    robot.setMove('B', 300, 100)
    robot.setMove('F', 200, 100)
    robot.setTurn('L', 90, 100)
    robot.setMove('F', 100, 100)
    robot.setMove('B', 200, 100)
    robot.setMove('L', 100, 100)
    
def exercise6():
    #Finch moves through the maze
    robot.setMove('F', 270, 100)
    robot.setTurn('R', 72, 100)
    robot.setMove('F', 200, 100)

exercise6()
