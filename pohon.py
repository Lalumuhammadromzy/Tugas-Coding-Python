import turtle
import colorsys

def draw_stick(x, y, length, pensize, color, angel):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(angel)
    turtle.pensize(pensize)
    turtle.down()
    turtle.color(color)
    turtle.fd(length)
    
def draw_tree(x, y, length, pensize, hue, angel, fat_angel, n):
    if n == 0:
        return
    (r,g,b) = colorsys.hsv_to_rgb(hue, 1, 1)
    draw_stick(x, y, length, pensize, (r,g,b), angel)
    tx = turtle.xcor()
    ty = turtle.ycor()
    
    draw_tree(tx, ty, length * 0.7, pensize * 0.7, hue - 1/13, angel + fat_angel, fat_angel, n - 1)
    draw_tree(tx, ty, length * 0.7, pensize * 0.7, hue - 1/13, angel - fat_angel, fat_angel, n - 1)
    
turtle.setup(800,700)
turtle.title("Pohon Pelangi - Kelompok 1")
turtle.speed(0)
turtle.tracer(n=1, delay=0)
turtle.bgcolor("White")
turtle.shape("turtle")

draw_tree(0, -300, 200, 10, 9 / 8, 90, 25, 12)
turtle.done()