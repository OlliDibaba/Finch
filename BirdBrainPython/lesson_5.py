from BirdBrain import Finch
import time
robot = Finch()


def exercise1():
    #If you click button a or b the finch's beak will light up green otherwise the finch will glow red
    if robot.getButton('A' or 'B'):
        robot.setBeak(0, 100, 0)
        
    else:
        robot.setBeak(100, 0, 0)
    time.time.sleep(1)
    bird.stopAll()


def exercise2():
    #When the button b is pressed it moves backwards otherwise it moves forward
    if robot.getButton('B'):
        robot.setMove('B', 20, 100)
        
    else:
        robot.setMove('F', 20, 100)
    time.time.sleep(1)
    bird.stopAll()

def exercise3():
    #It will print a distance and if it is less than 30, then the tail will flash
    #all green, but if it is more than 30 the tail will flash all red.
    print(robot.getDistance())
    if robot.getDistance() < 30:
        robot.setTail("all", 0, 0, 100)
    else:
        robot.setTail("all", 100, 0, 0)
    time.sleep(2)
    robot.stopAll()

def exercise4():
    #The robot will get the amount of it's surroundings, if its more than 50 cm ahead of him he will move forward
    #If the wall is closer than 50 cm then the finch will move backward
    print(robot.getDistance())
    if robot.getDistance() > 50:
        robot.setMove('F', 50, 100)
    else:
        robot.setMove('B', 50, 100)

def exercise5():
    while robot.getDistance() < 30:     #As long as distance is less than 30
        robot.setBeak(100, 0, 0)        #It turns red if less than 30
    robot.setBeak(0, 100, 0)            #It turns green if not less than 30
    time.sleep(1)
    robot.stopAll()

def exercise6():
    #the finch will move forward until it is in front of an obstacle and then turn red
    while robot.getDistance() > 1:
        robot.setMove('F', 10, 100)
    robot.setBeak(100, 0, 0)
    time.sleep(2)
    robot.stopAll()

def exercise7():
    #If something is in front of it, it will start blinking red and blue
    while robot.getDistance() > 20:
        robot.setTail("all", 100, 0, 0)
        time.sleep(3)
        robot.setTail("all", 0, 0, 100)
        time.sleep(3)
    robot.stopAll()

def exercise8():
    #This makes it so that if the door is closed it will blink red
    #If the door is open it will spin in circles and blink red and blue
    while robot.getLight('L') < 10:
        robot.setBeak(100, 0, 0)
        robot.setTail("all", 100, 0, 0)
        time.sleep(3)
        robot.setBeak(100, 0, 0)
        robot.setTail("all", 100, 0, 0)
        time.sleep(3)
    for i in range(4):
        robot.setTurn('R', 360, 100)
        robot.setBeak(100, 0, 0)
        robot.setTail(1, 3, 100, 0, 0)
        time.sleep(3)
        robot.setTurn('R', 360, 100)
        robot.setBeak(0, 0, 100)
        robot.setTail(2, 4, 0, 0, 100)
        time.sleep(3)
    robot.stopAll()

def exercise9():
    #While the button isn't being pressed the finch will blink until pressed
    while not robot.getButton('A'):
        robot.setTail(1, 0, 100, 0)
        time.sleep(0.1)
        robot.setTail(3, 0, 100, 0)
        time.sleep(0.1)
        robot.stopAll()

def exercise10():
    #while the button B isn't pressed the finch moves back and forth
    while not robot.getButton('B'):
        robot.setMove('F', 50, 100)
        robot.setMove('B', 50, 100)
    robot.stopAll()

def exercise11():
    #
    robot.setBeak(100, 0, 0)
    while robot.getDistance() < 30:
        pass
    robot.setBeak(0, 100, 0)
    time.sleep(1)
    robot.stopAll

def exercise12():
    while not robot.getButton('A'):         #Repeat until button A is pressed
        if (robot.getDistance() > 30):      #No obstacles
            bird.setTail("all", 0, 100, 0)
        else:
            robot.setTail("all", 0, 100, 0)
        bird.stopAll()

exercise11()
