from BirdBrain import Finch
import time
robot = Finch()

def exercise1():
    #This just turns both wheels speed
    robot.setMotors(50, 50)
    sleep(1)
    bird.stop()
    
def exercise2():
    #It asks the user what the speed of both wheels should be and what ever 2 numbers are inputed are the numbers that are used as the finch's motor speed
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
    #It asks the user if they would like right or 'l' and if 'r' is chosen then it turns right, but if r isn't chosen then it turns left
    rightorleft = input("Please enter 'r' or 'l': ")
    if(rightorleft == 'r'):
        robot.setTurn('R', 90, 100)

    else:
        robot.setTurn('L', 90, 100)

    robot.stopAll()

def exercise6():
    #It asks for a speed in between -10 and 10 and if its any higher or lower than that it gives an error message
    userResponse = input("Please enter a speed (-10 to 10): ")
    speed = int(userResponse)
    if (speed >= -10) and (speed<= 10):
        robot.setMotors(speed,speed)
        time.sleep(1)
        robot.stop()
    else:
        print("That speed is not valid!")

def exercise7():
    #The user will give a valid speed and the left wheel will go as the user asked and the right wheel will go twice as fast
    userResponse = input("Please enter a speed (0 to 50): ")
    speed = int(userResponse)
    if(speed >= 0) and (speed <= 50):
        robot.setMotors(speed, speed*2)
        time.sleep(5)
        robot.stop()
    else:
        print("Error!")

def exercise8():
    #The user is asked if he wants to dance and if he does want to dance then the finch will spin in circles and light up
    #If the user doesn't want to dance the finch turns red and it prints 'the finch is mad now!'
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
