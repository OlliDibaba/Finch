from BirdBrain import Finch
import time

robot = Finch()



def exercise1():
    def drawSquare():
        for i in range(6):
            bird.setMove('F', 15, 50)
            bird.setTurn('R', 90, 50)
        bird.setTurn('L', 60, 50)
    drawSquare()
