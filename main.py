from turtle import*
import math
ccolor = 0

def plot(scale):
  global exp
  if ccolor == 1:
    color(255, 0, 0)
  elif ccolor == 2:
    color(50,205,50)
  elif ccolor == 3:
    color(0,0,255)
  else:
    color(0,0,0)
  cn = -500
  penup()
  speed(0.000000000000000000000000000000000000001)
  for x in range(-600,600,30):
    #speed(999)
    goto(x,30*eval(exp))
    pendown()
    #while cn <= 500:
     # py = (m*(cn/30)+b)
      #setheading(cn,py*30)
      #goto(cn,(py*30))
      #pendown()
      #cn = cn + 1  
def mkgraph(scale):
  speed(0)
  goto(0,600)
  goto(0,-600)
  penup()
  goto(-600,0)
  pendown()
  goto(600,0)
  penup()
  xstep = 0
  ystep = 0
  while xstep <= 600:
    goto(xstep,0)
    sety(6)
    pendown()
    sety(-6)
    penup()
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
    write(drawthing)
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
    xstep = xstep - scale
  while ystep >= -600:
    speed(0)
    goto (0, ystep)
    pendown()
    setx(6)
    setx(-6)
    penup()
    setx(8)
    pendown()
    setx(13)
    penup()
    drawthing = ystep/-30
    if drawthing != -0:
      write(drawthing)
    penup()
    ystep = ystep - scale
while True:
  print ("loading...")
  mkgraph(30)
  print ('done')
  while True: 
    ccolor = ccolor + 1
    exp = input('Enter the equation in terms of x:\ny=')
    scale = 30
    print ('----------------------------------------------------------')
    #print (findequation())
    print('done, now plotting.....')
    plot(scale)
    print ('done')
    ppp = input("Add a function, exit, or start over?-----[a,e,s]")
    if ppp == 'a':
      print ('OK!')
    elif ppp == 's':
      clear()
      break
    elif ppp == 'e':
      breakx
  if ppp == 'e':
    break
print ('Bye!')