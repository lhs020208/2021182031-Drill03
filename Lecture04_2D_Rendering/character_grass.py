from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    character.draw_now(x, y)
    delay(0.01)

def run_circle():
    print('circle')

    r, cx, cy = 300, 800//2, 600//2
    for degree in range(0,360,3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        draw_boy(x,y)
        
def run_top():
    print('top')
    for x in range(0,800,10):
        draw_boy(x,550)
    pass
    
def run_right():
    print('right')
    for y in range(550,0,-10):
        draw_boy(790,y)
    pass
    
def run_bottom():
    print('bottom')
    for x in range(800,0,-10):
        draw_boy(x,0)
    pass
    
def run_left():
    print('left')
    pass
    
def run_rectangle():
    print('rect')
    #run_top()
    run_right()
    run_bottom()
    run_left()
    pass

while(True):
    #run_circle()
    run_rectangle()
    break

close_canvas()
