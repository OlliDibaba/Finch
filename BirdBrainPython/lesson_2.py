from BirdBrain import Finch
robot = Finch()

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
    
    leftlight = robot.getLight('L')
    rightlight = robot.getLight('R')
    difference = leftlight - rightlight
    print(leftlight, rightlight, difference)
    
    
    
exercise5l2()
