
import turtle
import tilt

while True:
    mgx, mgy, _ = tilt.get_tilt_data()
    x, y = turtle.pos()
    turtle.goto(x + mgx/100, y - mgy/100)