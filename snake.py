from turtle import Turtle
import time
from snake_class import SNAKE
from screen_class import snake_screen
from food_class import food
import os.path

def creat_score_board():
    
    score_board = Turtle()
    score_board.color("white")
    score_board.penup()
    score_board.goto((0,280))
    score_board.hideturtle()
    return score_board

def game_over_logo(point,high_score):
    gameover = Turtle()
    gameover.color("white")
    gameover.penup()
    gameover.goto((0,0))
    gameover.hideturtle()
    gameover.color("red")
    gameover.write(f"GAME OVER\npoint: {point}\nHigh score : {high_score}", False,"center",font=('Arial', 12, 'normal'))


def round_pos(position):
    x = position[0]
    y = position[1]
    rounded_x = round(x/10)*10
    rounded_y = round(y/10)*10
    return (rounded_x,rounded_y)


def update_score_board(score_board , point,high_score):
    score_board.clear()
    score_board.write(f"points : {point}               High score : {high_score}", False,"center",font=('Arial', 12, 'normal'))
    
def food_range(position):
    x = position[0]
    y = position[1]
    position_list = [position]
    for i in range(x,x-11,-1):
        position_list.append((i,y))
    for i in range(x,x+11):
        position_list.append((i,y))    
    
    for i in range(y,y-11,-1):
        position_list.append((x,i))
    for i in range(y,y+11):
        position_list.append((x,i))
        
    return position_list

def is_duplicate(anylist):
    # if type(anylist) != 'list':
    #     return("Error. Passed parameter is Not a list")
    if len(anylist) != len(set(anylist)):
        return True
    else:
        return False
    
# def makehighscorefile():
#     file = open("high_score.txt","w")
#     file.write("0")

def get_high_score():
    if os.path.isfile("high_score.txt") != True:
        file = open('high_score.txt', 'w')
        file.write("0")
        high_score = 0
        file.close
    else:
        file = open('high_score.txt', 'r')
        # Read & print the entire file
        high_score = file.read()   
        file.close()
    return int(high_score)

screen = snake_screen()
snake = SNAKE()
snake_food = food()

# snake.snake.snake_man
 
'''
getting last high score
'''
high_score = get_high_score()
last_high_score = high_score


'''
turning sanke
'''

screen.screen.listen()
screen.screen.onkeypress(fun= snake.on_w_click , key= "w")
screen.screen.onkeypress(fun= snake.on_s_click , key= "s")
screen.screen.onkeypress(fun= snake.turn_left , key= "a")
screen.screen.onkeypress(fun= snake.turn_right , key= "d")



'''
moving snake with time
'''

end_of_game = False
point = 0
obj = creat_score_board()
update_score_board(obj , point,high_score)
screen.screen.update()
# snake.snake_man[0].color("green")
while end_of_game != True:    
    
    
    snake.move_forward()
    screen.screen.update()
    # if it hit's himself
    all_pos = [round_pos(item.pos()) for item in snake.snake_man]
    if is_duplicate(all_pos) :
        end_of_game = True
        game_over_logo(point,high_score)
        high_score = point


    current_pos = round_pos(all_pos[0])
    #if it hit's the wall
    abs_current_pos = (abs(current_pos[0]),abs(current_pos[1]))
    if abs_current_pos[0] >= 290 or abs_current_pos[1] >= 290:
        end_of_game = True
        game_over_logo(point,high_score)
        high_score = point

    # spon food and eat the food
    food_pos_range = food_range(snake_food.food_pos)

    if current_pos in food_pos_range:
        point+=1
        update_score_board(obj,point,high_score)
        snake_food.remove_food()
        snake_food.creat_food()
        snake.eat_food()
    
    time.sleep(0.1)

# int(get_high_score())
if high_score > last_high_score:
    f = open("high_score.txt", "w+")
    f.write(str(high_score))
    f.close()
    













screen.screen.exitonclick()

