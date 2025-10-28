import turtle
xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())
pen = turtle.Turtle()
pen.up()
pen.goto(xc, yc-r)
pen.down()
pen.circle(r)
pen.up()
pen.goto(x, y)
pen.dot(5, "red")
temp = (x-xc)**2 + (y-yc)**2
if temp > r**2:
    print("точка вне окружности")
elif temp == r**2:
    print("точка на окружности")
else:
    print("точка внутри окружности")
turtle.done()



