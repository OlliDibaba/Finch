from BirdBrain import Finch
import time
robot = Finch()


def exercise1():
    if robot.getButton('A'):
        robot.setBeak(0, 100, 0)
        
    else:
        robot.setBeak(100, 0, 0)
    time.sleep(1)
    bird.stopAll()


def exercise2():
    if robot.getButton('B'):
        robot.setMove('B', 20, 100)
        
    else:
        robot.setMove('F', 20, 100)
    time.sleep(1)
    bird.stopAll()

def exercise3():
    #It will print a distance and if it is less than 30, then the tail will flash
    #all green, but if it is more than 30 the tail will flash all red.
    print(bird.getDistance())
    if robot.getDistance() < 30:
        robot.setTail("all", 0, 0, 100)
    else:
        robot.setTail("all", 100, 0, 0)
    sleep(2)
    robot.stopAll()

def exercise4():
    
