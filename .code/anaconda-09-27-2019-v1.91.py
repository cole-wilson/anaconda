#(c) September 27, 2019
# by Cole Wilson
#for Python 3+

# Please Note: this program can only be ran in a graphical session.

#----------------------------------------------Start Code-----------------------------------------------------------------#


#import modules
from turtle import*
import time
import math

#set data
ver = str(1.91)
platform = 'repl.it Web Server'
print('Anaconda: v' +ver+ ' for '+platform)

#Defining keys for segmaented numbers
# '8', top, topleft, bottomleft, bottom, bottomright, topright, middle
numberk = {' ':80000000,'=':81000001,'-':80000001,'l':80001110,'i':80110000,'a':81110111,'m':800101010010101,'0':81111110,'1':80110000,'2':81101101,'3':81111001,'4':80110011,'5':81011011,'6':81011111,'7':81110000,'8':81111111,'9':81111011}

#Define main variables
ccolor = 0
shape('classic')
speed(0)
table = {}
penplot = Turtle()
penplot.speed(0)
penplot.penup()
penplot.goto(10000,10000)
penplot.shape('none')

#function defenitions
def plot(scale):
  if ccolor == 1:
    penplot.color(255, 0, 0)
  elif ccolor == 2:
    penplot.color(50,205,50)
  elif ccolor == 3:
    penplot.color(0,0,255)
  else:
    color(ccolor/30,ccolor/20,ccolor/1579)
  cn = -500
  penup()
  speed(0)
  if table[end]/table[end-1] == table[end-1]/table[end-2]:
    penplot.penup()
    for x in range(-600,600,5):
      penplot.goto(float(x),30*(float(b)*(float(r)**(float(x)/30))))
      penplot.pendown()
  elif dod != 0:
    penup()
    for x in range(-600,600,5):
      penplot.goto(float(x),30.0*((float(dod)/2.0)*((float(x)/30.0)**2.0))+(float(b)*(float(x)/30.0))+(30*(table[0])))
      penplot.pendown()
  elif dod == 0:
    penplot.penup()
    for x in range(-600,600,30):
      penplot.goto(x,30*(m*(x/30)+b))
      penplot.pendown()
def drawn(num,size,step):
  length = len(str(num))
  for ccc in range(length):
    if num == 0:
      ccc = length+1
      break
    snum = str(num)
    cnum = (snum[ccc])
    penup()
    key = str(numberk[cnum])
    x = xcor()
    y = ycor()
    goto(x+size,y+size)
    counter = 1
    for x in range(0,1):
      while counter <= 7:
        if key[counter] == '0':
          penup()
        else:
          pendown()
        forward(size)
        if counter == 1:
          right(90)
        elif counter == 3:
          right(90)
        elif counter == 4:
          right(90)
        elif counter == 6:
          x = xcor()
          y = ycor() - size
          goto(x,y)
          right(90)
        counter = counter +1
    penup()
    forward(step)
def findequation():
  dd2=table[end]-table[end-1]
  dd1=table[end-1]-table[end-2]
  global dod
  global r
  global b
  dod=(dd2-dd1)
  if table[end]/table[end-1] == table[end-1]/table[end-2]:
    b = table[0]
    r = table[end]/table[end-1]
    y = 'y='
    equation = y + str(b) + '(' + str(r) + ')^x'
    return equation
  elif dod != 0:
    b=(table[1]-table[-1])/2
    bx=str(b) + "x" + "+"
    global c
    c = table[0]
    xsqrd = 'x^2)+'
    y = 'y='
    equation = y + "(" + str(dod/2) + xsqrd + bx + str(c)
    return equation
  elif dod == 0:
    global m
    m = table[end]-table[end-1]
   
    b = table[0]
    eq = "y=" + str(m) + "x" + "+" + str(b)
    return eq
def gttab(start,end):
  count = start
  while count <= end:
    n = float(input('What is Y if X is ' + str(count) + '?'))
    table[count]=n
    count = count + 1
  print (table)
def mkgraph(scale):
  speed(0)
  goto(0,600)
  setheading(90)
  stamp()
  goto(0,-600)
  setheading(270)
  stamp()
  penup()
  goto(-600,0)
  setheading(180)
  stamp()
  pendown()
  goto(600,0)
  setheading(0)
  stamp()
  penup()
  xstep = 0
  ystep = 0
  shape('turtle')
  while xstep <= 600:
    goto(xstep,0)
    sety(6)
    pendown()
    sety(-6)
    penup()
    x = xcor()-10
    setx(x)
    sety(-14)
    drawthing = xstep/30
    drawn(drawthing,5,0.5)
    xstep = xstep + scale
  while ystep <= 600:
    speed(0)
    goto (0, ystep)
    pendown()
    setx(6)
    setx(-6)
    penup()
    setx(6)
    drawthing = ystep/30
    drawn(drawthing,5,0.5)
    penup()
    ystep = ystep + scale
  xstep = 0
  ystep = 0
  while xstep >= -600:
    goto(xstep,0)
    sety(6)
    pendown()
    sety(-6)
    penup()
    sety(6)
    x = xcor()-14
    setx(x)
    sety(-14)
    setheading(0)
    if xstep !=0:
      pendown()
      forward(4)
    drawthing = xstep/-30
    drawn(drawthing,5,0.5)
    xstep = xstep - scale
  while ystep >= -600:
    
    speed(0)
    goto (0, ystep)
    pendown()
    setx(6)
    setx(-6)
    penup()
    setx(11)
    pendown()
    setx(16)
    penup()
    drawthing = ystep/-30
    drawn(drawthing,5,0.5)
    penup()
    ystep = ystep - scale

#loading
print ("loading...")
print ("This might take a while, all of the graphing is done with Turtle graphics. This should be fixed in later versions.")
#mainloop
while True:
  mkgraph(30)
  print ('done')
  while True: 
    ccolor = ccolor + 1
    print ('Please enter values in table form')
    start = int(input('Start Value for Table?'))
    end = int(input('End Value for Table?'))
    while end-start <=3:
      print ('Error:  Must have at least 4 X values')
      start = int(input('Start Value for Table?'))
      end = int(input('End Value for Table?'))
  
    gttab(start, end)
    scale = 30
    print ('----------------------------------------------------------')
    print (findequation())
    print('done, now plotting.....')
    plot(scale)
    print ('done')
    ppp = input("Add a function, exit, or start over?-----[a,e,s]")
    if ppp == 'a':
      print ('OK!')
    elif ppp == 's':
      penplot.clear()
      break
    elif ppp == 'e':
      breakx
  if ppp == 'e':
    break
print ('Bye!')
#----------------------------------------------End Code-----------------------------------------------------------------#

#Thank you!
