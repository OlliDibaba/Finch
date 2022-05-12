from BirdBrain import Finch
from time import sleep

robot = Finch()

def exercise1():
    #This turns the beak a red color
    robot.setBeak(100, 0, 0)
    sleep(1)
    robot.setBeak(0, 0, 0)

def exercise2():
    #This turns the beak purple, cyan, and white
    robot.setBeak(100, 0, 100)
    sleep(1)
    robot.setBeak(0, 100, 100)
    sleep(1)
    robot.setBeak(100, 100, 0)
    sleep(1)
    robot.setBeak(0, 0, 0)


#This code makes the 1st and 4th light of the tail blue for 2 seconds then turns them off
def exercise3():
    robot.setTail(1, 0, 0, 100) 
    robot.setTail(4, 0, 0, 100)
    sleep(2)
    robot.stopAll()


#This code makes it so that the robot shines colors in a rainbow type way
def exercise4():
    robot.setTail(1, 100, 0, 0)
    robot.setTail(2, 255, 165, 0)
    robot.setTail(3, 100, 100, 0)
    robot.setTail(4, 0, 100, 0)
    robot.setBeak(0, 0, 100)
    sleep(1)
    robot.setTail(1, 100, 0, 0)
    robot.setTail(2, 255, 165, 0)
    robot.setTail(3, 100, 100, 0)
    robot.setTail(4, 0, 100, 0)
    robot.setBeak(75, 0, 130)
    sleep(1)
    robot.setTail(1, 100, 0, 0)
    robot.setTail(2, 255, 165, 0)
    robot.setTail(3, 100, 100, 0)
    robot.setTail(4, 0, 100, 0)
    robot.setBeak(127, 0, 255)
    sleep(1)
    robot.stopAll()

    
def exercise5():
    userResponse = input("Which tail light (1-4) should be red? ") # Get user input
    number = int(userResponse)                                     #Convert to int
    robot.setTail(number, 100, 0, 0)
    sleep(1)
    robot.stopAll()

#asks the user what the color of the light should be
def exercise6():
    userResponse = input("How much RGB (1-100, 1-100, 1-100) should the light be?")
    number = int(userResponse)
    robot.setBeak(number)
    sleep(1)
    robot.stopAll()

#makes a square with different lights at each end
def exercise7():
    robot.setMove("F", 100, 100)
    robot.setBeak(100, 0, 0)
    sleep(1)
    robot.stopAll()
    robot.setMove("F", 100, 100)
    robot.setBeak(0, 100, 0)
    sleep(1)
    robot.stopAll()
    robot.setMove("F", 100, 100)
    robot.setBeak(0, 0, 100)
    sleep(1)
    robot.stopAll()
    robot.setMove("F", 100, 100)
    robot.setBeak(100, 0, 100)
    sleep(1)
    robot.stopAll()

    
exercise7()
