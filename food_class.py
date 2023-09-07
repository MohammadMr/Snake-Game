from turtle import Turtle

import random
class food():
    def __init__(self):
        self.temp = Turtle()
        self.creat_food()
        self.food_pos
        # self.food_pos = 


    def creat_food(self):
        '''
        creat random possition
        '''
        x = random.randrange(-280,280,10)
        y = random.randrange(-280,280,10)
        pos =(x,y)
        
        self.temp.penup()
        self.temp.pencolor("white")
        self.temp.goto(pos)
        self.temp.dot(10)
        self.temp.hideturtle()

        self.food_pos = pos
        # return pos
        
    def remove_food(self):
        self.temp.clear()

