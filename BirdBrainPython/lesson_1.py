from BirdBrain import Finch
import time

robot = Finch()

def exercise1():
    robot.setMove('F', 30, 100)
    robot.setMove('B', 30, 100)
    robot.setMove('F', 30, 100)
    robot.setMove('B', 45, 100)

def exercise2():
    robot.setTurn('R', 90, 100)

def exercise3():
    robot.setTurn('L', 360, 50)
    robot.setTurn('R', 360, 100)

def exercise4():
    robot.setMove('F', 50, 100)
    robot.setTurn('R', 90, 100)
    robot.setMove('F', 50, 100)
    robot.setTurn('R', 90, 100)
    robot.setMove('F', 50, 100)
    robot.setTurn('R', 90, 100)
    robot.setMove('F', 50, 100)
    robot.setTurn('R', 90, 100)



def exercise6():
    robot.setMove('F', 270, 100)
    robot.setTurn('R', 72, 100)
    robot.setMove('F', 200, 100)

def practice1():
    robot.setMove('F', 240, 100)
    robot.setTurn('L', 114, 100)
    robot.setMove('F', 275, 100)
    robot.setTurn('R', 65, 100)
    robot.setMove('F', 40, 100)


practice1()
