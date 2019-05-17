class gate(object):
  def __init__(self,gateName,x,y):
    self.gateName = gateName
    self.x = x
    self.y = y
    self.width = 120
    self.height = 90
    self.nodesize = 20

  def checkSelected(self,givenX,givenY):
    if givenX <= self.x+self.width and givenX >= self.x:
      if givenY <= self.y+self.height and givenY >= self.y:
        return(True,givenX-self.x,givenY-self.y)
    return(False,0,0)

  def setnewPos(self,x,y):
    self.x = x
    self.y = y

  def getpos(self):
    return(self.x,self.y)

  def drawBox(self,pygame,screen,colour):
    pygame.draw.rect(screen,colour,(self.x,self.y,self.width,self.height),0)

  def drawCircleConfig1(self,pygame,screen,colour):
    pygame.draw.circle(screen,colour,(self.x,self.y+self.nodesize),self.nodesize,0)
    pygame.draw.circle(screen,colour,(self.x,self.y+self.height-self.nodesize),self.nodesize,0)
    pygame.draw.circle(screen,colour,(self.x+self.width,int(self.y+self.height/2)),self.nodesize,0)

  def drawCircleConfig2(self,pygame,screen,colour):
    pygame.draw.circle(screen,colour,(self.x,int(self.y+self.height/2)),self.nodesize,0)
    pygame.draw.circle(screen,colour,(self.x+self.width,int(self.y+self.height/2)),self.nodesize,0)

class andGate(gate):
  def __init__(self,num,in1,in2,out,x,y):
    gate.__init__(self,"and{}".format(num),x,y)
    self.in1 = in1
    self.in2 = in2
    self.out = out

  def output(self,connector):
    inp1 = connector[self.in1][2]
    inp2 = connector[self.in2][2]
    if inp1 == True and inp2 == True:
      self.out = True
    else:
      self.out = False

  def checkInOutSelected(self,math,givenX,givenY):
    z = complex(givenX,givenY)
    #for the output
    center = complex(self.x+self.width, int(self.y+self.height/2))
    if abs(z-center) < self.nodesize:
      return("Output")
    #for inputs
    center = complex(self.x,self.y+self.nodesize)
    if abs(z-center) < self.nodesize:
      return("Inp1")
    #2
    center = complex(self.x,self.y+self.height-self.nodesize)
    if abs(z-center) < self.nodesize:
      return("Inp2")

  def drawGate(self,pygame,screen):
    colour = (169,209,142)
    colour2 = (84,130,53)
    self.drawBox(pygame,screen,colour)
    self.drawCircleConfig1(pygame,screen,colour2)

class orGate(gate):

  def __init__(self,num,in1,in2,out,x,y):
    gate.__init__(self,"or{}".format(num),x,y)
    self.in1 = in1
    self.in2 = in2
    self.out = out

  def output(self,connector):
    inp1 = connector[self.in1][2]
    inp2 = connector[self.in2][2]
    if inp1 == True or inp2 == True:
      self.out = True
    else:
      self.out = False

  def checkInOutSelected(self,math,givenX,givenY):
    z = complex(givenX,givenY)
    #for the output
    center = complex(self.x+self.width, int(self.y+self.height/2))
    if abs(z-center) < self.nodesize:
      return("Output")
    #for inputs
    #1
    center = complex(self.x,self.y+self.nodesize)
    if abs(z-center) < self.nodesize:
      return("Inp1")
    #2
    center = complex(self.x,self.y+self.height-self.nodesize)
    if abs(z-center) < self.nodesize:
      return("Inp2")

  def drawGate(self,pygame,screen):
    colour = (157,195,230)
    colour2 = (46,117,182)
    self.drawBox(pygame,screen,colour)
    self.drawCircleConfig1(pygame,screen,colour2)

class notGate(gate):

  def __init__(self,num,in1,out,x,y):
    gate.__init__(self,"not{}".format(num),x,y)
    self.in1 = in1
    self.out = out

  def output(self,connector):
    inp1 = connector[self.in1][2]
    if inp1 == True:
      self.out = False
    else:
      self.out = True

  def checkInOutSelected(self,math,givenX,givenY):
    z = complex(givenX,givenY)
    #for the output
    center = complex(self.x+self.width,int(self.y+self.height/2))
    if abs(z-center) < self.nodesize:
      return("Output")
    #for inputs
    #1
    center = complex(self.x,int(self.y+self.height/2))
    if abs(z-center) < self.nodesize:
      return("Inp1")

  def drawGate(self,pygame,screen):
    colour = (255,217,102)
    colour2 = (191,144,0)
    self.drawBox(pygame,screen,colour)
    self.drawCircleConfig2(pygame,screen,colour2)
