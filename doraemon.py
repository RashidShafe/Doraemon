from turtle import *

#go to point x, y
def run(x,y):
    up()
    goto(x,y)
    down()
 

#head just the outside with blue fill   
def matha():
    up()
    circle(150,40)
    down()
    fillcolor("#00a0de")
    begin_fill()
    circle(150,280)
    end_fill()

#the red belt on his neck
def belt():
    fillcolor("#fc0313")
    begin_fill()
    seth(0)
    forward(200)
    circle(-5,90)
    forward(10)
    circle(-5,90)
    forward(205)
    circle(-5,90)
    forward(10)
    circle(-5,90)
    end_fill()

#whole face
def chehara():
    forward(180)
    left(45)
    fillcolor("#ffffff")
    begin_fill()
    circle(120,100)
    seth(180)
    forward(122)
    seth(215)
    circle(120,100)
    end_fill()
    run(63, 218)
    seth(90)
    
    #drawing both face
    chukh()
    seth(180)
    up()
    forward(62)
    down()
    seth(90)
    
    chukh()

#Eyes
def chukh():
    fillcolor("#ffffff")
    begin_fill()
    tracer(False)#reducing the drawing time
    a = 2.5
    
    for i in range(120):
        if 0<= i <30 or 60 <=i <90:
            a -= 0.05
            left(3)
            forward(a)
            
        else:
            a+=0.05
            left(3)
            forward(a)
            
    tracer(True)
    end_fill()


#black cornia :P
def kala_chukh():
    seth(0)
    run(-22, 195)
    fillcolor("#000000")
    begin_fill()
    circle(13)
    end_fill()
    pensize(6)
    run(18, 205)
    seth(75)
    circle(-10,150)
    pensize(3)
    run(-17, 200)
    seth(0)
    fillcolor("#ffffff")
    begin_fill()
    circle(5)
    end_fill()

#nose
def nak():
    run(-12, 158)
    seth(315)
    fillcolor("#fc0313")
    begin_fill()
    circle(20)
    end_fill()

#Mouth
def mukh():
    run(3,148)
    seth(270)
    forward(100)
    seth(0)
    circle(120,50)
    seth(230)
    circle(-120,100)
    
#mustache
def dhari():
    #Doreamon's right side
    run(-32, 135)
    seth(165)
    forward(60)
    
    run(-32, 125)
    seth(180)
    forward(60)
    
    run(-32, 115)
    seth(180+13)
    forward(60)
    
    #Doraemon's left side
    run(37, 135)
    seth(15)
    forward(60) 
    
    run(37, 125)
    seth(0)
    forward(60)
    
    run(37, 115)
    seth(-13)
    forward(60)
        
#The yellow bell on the neck
def gonta():
    run(-103.42, 15.09)
    up()
    forward(90)
    down()
    seth(70)
    fillcolor("#ffd200")
    begin_fill()
    circle(-20)
    end_fill()
    seth(170)
    fillcolor("#ffd200")
    begin_fill()
    circle(-2,180)
    seth(10)
    circle(-100,22)
    circle(-2,180)
    seth(180-10)
    circle(100,22)
    end_fill()
    
    goto(-13.42,15.09)
    seth(250)
    circle(20,110)
    seth(90)
    forward(15)
    dot(10)
    run(0,150)

#White part of belly
def pet():
    run(-103.42, 15.09)
    seth(0)
    forward(38)
    seth(230)
    begin_fill()
    circle(90,260)
    end_fill()
    
def pocket():
    run(5, -40)
    seth(0)
    forward(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    forward(70)
    
#DRAWING
def Doraemon():
    matha()
    belt()
    chehara()
    kala_chukh()
    nak()
    mukh()
    dhari()
    
    
    #Left hand
    seth(0)
    run(0, 0)
    up()
    circle(150,50)
    down()
    seth(30)
    forward(40)
    seth(70)
    circle(-30,270)
    
    #body start
    fillcolor("#00a0de")
    begin_fill()
    seth(230)
    forward(80)
    seth(90)
    circle(1000,1)
    seth(-89)
    circle(-1000,10)
    seth(180)
    forward(70)
    seth(90)
    circle(30,180)
    seth(180)
    forward(70)
    #body end
    
    #Right hand
    seth(100)
    circle(-1000,9)
    seth(-86)
    circle(1000,2)
    seth(230)
    forward(40)
    
    circle(-30,230)
    seth(45)
    forward(81)
    seth(0)
    forward(203)
    circle(5,90)
    forward(10)
    circle(5,90)
    forward(7)
    seth(40)
    circle(150,10)
    seth(30)
    forward(40)
    end_fill()
    seth(70)
    fillcolor("#ffffff")
    begin_fill()
    circle(-30)
    end_fill()
    
    run(103.74, -182.59)
    seth(0)
    fillcolor("#ffffff")
    begin_fill()
    forward(15)
    circle(-15,180)
    forward(90)
    circle(-15,180)
    forward(10)
    end_fill()
    
    run(-96.26, -182.59)
    seth(180)
    fillcolor("#ffffff")
    begin_fill()
    forward(15)
    circle(15,180)
    forward(90)
    circle(15,180)
    forward(10)
    end_fill()
    
    #belly
    pet()
    
    pocket()
    #Bell
    gonta()
    
    

if __name__ == '__main__':
    screensize(600,400, "#f0f0f0")
    pensize(3)
    speed(20)
    Doraemon()
    run(100, -250)
    color('blue')
    write('By Rashid Shafe',move='True', font=('Arial',20))
    hideturtle()
    #run(0, 0)
    mainloop()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    