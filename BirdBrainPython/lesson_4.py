from BirdBrain import Finch
import time
robot = Finch()

def exercise1():
    robot.setTurn(50, 50)
    sleep(1)
    bird.stop()
    
def exercise2():
    userResponse = input("What should be the speed of the left and right wheel(1-100, 1-100)?")
    number = int(userResponse)
    robot.setTurn(number)
    sleep(1)
    bird.stopAll()

def exercise3():
    
    for i in range(360):
        robot.setMove('F', 1, 100)
        robot.setTurn('R', 1, 100)

def exercise4():
    #this function will make it so that when g is clicked, the lights will shine green but if not it will say "sorry not my favorite color"
    color = input("Please enter a letter: ")
    if(color == 'g'):
        robot.setBeak(0,100,0)
    else:
        print('Sorry not my favorite letter!')
    sleep(1)
    robot.stopAll()


def exercise5():
    rightorleft = input("Please enter 'r' or 'l': ")
    if(rightorleft == 'r'):
        robot.setTurn('R', 90, 100)

    else:
        robot.setTurn('L', 90, 100)

    robot.stopAll()

def exercise6():
    userResponse = input("Please enter a speed (-10 to 10): ")
    speed = int(userResponse)
    if (speed >= -10) and (speed<= 10):
        robot.setMotors(speed,speed)
        time.sleep(1)
        robot.stop()
    else:
        print("That speed is not valid!")

def exercise7():
    userResponse = input("Please enter a speed (0 to 50): ")
    speed = int(userResponse)
    if(speed >= 0) and (speed <= 50):
        robot.setMotors(speed, speed)
        time.sleep(5)
        robot.stop()
    else:
        print("Error!")

def exercise8():
    userResponse = input("It's Party Time! What would you like the finch to dance?: ")
    if(userResponse == 'yes'):
        for i in range(3):
            robot.setTurn('L', 360, 50)
            robot.setBeak(100, 0, 0)
            robot.setBeak(100, 64.7, 0)
            robot.setBeak(100, 100, 0)
            robot.setBeak(0, 100, 0)
            robot.setBeak(0, 0, 100)
            robot.setBeak(100, 0, 100)
            time.sleep(1)
            robot.stopAll()
    else:
        robot.setBeak(100, 0, 0)
        print("The finch is mad now!")
        time.sleep(3)
        robot.stopAll()


exercise8()
