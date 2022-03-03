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

def exercise1l2():
    print('distance: ', robot.getDistance())

def exercise2l2():
    print('distance: ', robot.getLight('R'))
    print('distance: ', robot.getLight('L'))
    print('distance: ', robot.getButton('A'))
    print('distance: ', robot.getOrientation())
    print('distance: ', robot.getEncoder('R'))


def exercise3l2():
    print(type(robot.getLight('R')))
    print(type(robot.getLight('L')))
    print(type(robot.getButton('A')))
    print(type(robot.getOrientation()))
    print(type(robot.getEncoder('R')))

def exercise4l2():
    currentDistance = robot.getDistance()
    print(currentDistance)
    print(2*currentDistance)
    print(4*currentDistance)

def exercise5l2():
    print('difference: ', (robot.getLight('R')))
    
exercise5l2()
