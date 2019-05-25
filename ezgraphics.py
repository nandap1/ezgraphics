import math
from ezgraphics import GraphicsWindow



gw_width = float(input("Enter the width: "))
gw_height = float(input("Enter the height: "))

circle_radius = float(input("Enter the radius: "))

border_color = input("Enter the circle border color: ")
inside_color = input("Enter the circle inside color: ")

win = GraphicsWindow(gw_width, gw_height)

canvas = win.canvas()

canvas.setOutline(border_color)
canvas.setFill(inside_color)

ww = circle_radius * 2
hh = circle_radius * 2
                      
xx = (gw_width / 2 ) - circle_radius
yy = (gw_width / 2 ) - circle_radius
                      
canvas.drawOval(xx, yy, ww, hh)
win.wait()
