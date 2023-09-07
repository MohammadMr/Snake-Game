from turtle import Turtle
'''
making snake

'''

class SNAKE():
    def __init__(self):
        
        self.snake_man = []
        self.create_snake()

    def set_to_back(self, item,index):
        margin = index * 10
        item.backward(margin)

    def go_to_back_after_eat(self,item):
        last_position = self.snake_man[-2].position()
        item.goto(last_position)
        item.backward(10)

    def create_snake(self):
        for _ in range(3):
            temp = Turtle()
            temp.color("white")
            temp.shape("square")
            temp.shapesize(1)
            temp.penup()
            temp.speed(0)
            self.snake_man.append(temp)
        for index ,item in enumerate(self.snake_man):
            self.set_to_back(item,index)

    def eat_food(self):
        temp = Turtle()
        temp.color("white")
        temp.shape("square")
        temp.shapesize(1)
        temp.penup()
        temp.speed(0)
        temp.goto(self.snake_man[0].position())
        temp.setheading(self.snake_man[-1].heading())
        self.snake_man.append(temp)
        self.go_to_back_after_eat(temp)

    
            
    def move_forward(self):
        head = [] 
        for index,item in enumerate(self.snake_man):
            item.forward(10)
            head.append(item.heading())
            if head[index] != head[index-1]:
                item.setheading(head[index-1])
        
            
    def move_backward(self):
        for item in self.snake_man:
            item.backward(5)
    def turn_right(self):
        head = self.snake_man[0].heading()
        head_degree = 90
        if head == 270:
            head_degree *= -1
        right_head = head - head_degree
        self.snake_man[0].setheading(right_head)
        
    def turn_left(self):
        head = self.snake_man[0].heading()
        head_degree = 90
        if head == 270:
            head_degree *= -1
        left_head = head + head_degree
        self.snake_man[0].setheading(left_head)
        
    def on_w_click(self):
        if self.snake_man[0].heading() == 0 or self.snake_man[0].heading() == 180:
            self.snake_man[0].setheading(90)
    def on_s_click(self):
        if self.snake_man[0].heading() == 0 or self.snake_man[0].heading() == 180:
            self.snake_man[0].setheading(270)

        


