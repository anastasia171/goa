from turtle import*

#we want to paint a house

#step 1: draw a square

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

forward(70)
left(90)
color("green")

forward(120)
right(90)

forward(60)
right(90)
forward(120)
#roof
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#door knob
penup()
goto(70,60)
pendown()

color("black")

left(120)
forward(10)
#right windown
penup()
goto(25,140)
pendown()

width(4)
color("dark blue")

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
#left windown
penup()
goto(130,140)
pendown()

left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)


#window crosses
forward(20)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(40)

penup()
goto(65,160)
pendown()
left(180)
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(40)



exitonclick()