from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
x = 400
y = 90
moveP = 1
while(1):
    if (moveP == 1):
        x = 400
        y = 90
        while (x < 800):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x + 4
            delay(0.01)

        while (y < 550):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y + 4
            delay(0.01)

        while (x > 0):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x - 4
            delay(0.01)

        while (y > 90):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y - 4
            delay(0.01)

        while (x < 400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x + 4
            delay(0.01)

        moveP = 2
    if (moveP == 2):
        rad = 270
        while (rad < 360):
            clear_canvas_now()
            grass.draw_now(400, 30)
            x = 210* math.cos(rad /360*2*math.pi)
            y = 210* math.sin(rad /360*2*math.pi)
            character.draw_now(x + 400, y + 300)
            rad = rad + 1
            delay(0.01)
        rad = 0
        while (rad < 270):
            clear_canvas_now()
            grass.draw_now(400, 30)
            x = 210* math.cos(rad /360*2*math.pi)
            y = 210* math.sin(rad /360*2*math.pi)
            character.draw_now(x + 400, y + 300)
            rad = rad + 1
            delay(0.01)

        moveP = 1

close_canvas()
