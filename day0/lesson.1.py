from turtle import* 

#we want to paint a hause

#step 1: draw a square
speed(30)
width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)








#end of square

#drawing a door

forward(70)
color("black")
begin_fill()
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("grey")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of door

#drawing a window

penup()
goto(0, 130)
pendown()
color("brown")
begin_fill()
left(120)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

penup()
goto(180, 130)
pendown()
begin_fill()
left(90)
forward(20)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(40)
end_fill()



exitonclick()

