from BirdBrain import Finch
import time
robot = Finch()





def exercise1():
    userName = input("What's your name? ")
    robot.print("Hi")         
    time.sleep(1.5)
    robot.print(userName)
    time.sleep(3)


exercise1()
