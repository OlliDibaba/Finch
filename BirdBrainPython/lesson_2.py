from BirdBrain import Finch
robot = Finch()

def exercise1():
    #This will get the distance of anything in front of the finch.
    print('distance: ', robot.getDistance())

def exercise2():
    
    print('distance: ', robot.getLight('R'))# gets the value for the right light sensor
    print('distance: ', robot.getLight('L'))#gets the value for the left light sensor
    print('distance: ', robot.getButton('A'))#gets the value of button a on the micro:bit
    print('distance: ', robot.getOrientation())#gets the orientation of the finch
    print('distance: ', robot.getEncoder('R'))#gets the amount of spins made with the right wheel


def exercise3():
    #finding all of the data types from exercise 2
    print(type(robot.getDistance(int))
    print(type(robot.getDistance(float))
    print(type(robot.getDistance(bool))
    print(type(robot.getDistance(str))

def exercise4():
    #This code will get the distance of the wall in front of it and multiply it by 2 then by 4
    currentDistance = robot.getDistance()
    print(currentDistance)
    print(2*currentDistance)
    print(4*currentDistance)

def exercise5():
    #Turn both sensors into variables and then find the difference between both sensors
    leftlight = robot.getLight('L')
    rightlight = robot.getLight('R')
    difference = leftlight - rightlight
    print(leftlight, rightlight, difference)

def exercise6():
    #This code will find both sensors and add them up and divide them by 2 to find the mean of the sensors
    leftlight = robot.getLight('L')
    rightlight = robot.getLight('R')
    mean = (leftlight + rightlight)/2
    print(leftlight, rightlight, mean)
    
    
    
    
exercise6()
