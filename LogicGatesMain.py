#[][][][][][][][][]Pygame[][][][][][][][][]

def createWindow(pygame):
  pygame.init()
  width,height = 400,400
  caption = "Logic Gate Sim"
  pygame.display.set_caption(caption)
  pygame.display.init
  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((width,height),pygame.VIDEORESIZE)
  generalDic['bg'] = (127, 138, 155)
  generalDic['notIMG'] = pygame.image.load('NotGate.png')
  generalDic['orIMG'] = pygame.image.load('OrGate.png')
  generalDic['andIMG'] = pygame.image.load('AndGate.png')
  return (screen,clock)


def updateWindow(pygame,screen,allGates):
  screen.fill(generalDic['bg'])
  for each in range(len(allGates)-1,-1,-1):
    if allGates[each][0] == 'andGate':
      screen.blit(generalDic['andIMG'],(allGates[each][1].x,allGates[each][1].y))
    elif allGates[each][0] == 'orGate':
      screen.blit(generalDic['orIMG'],(allGates[each][1].x,allGates[each][1].y))
    elif allGates[each][0] == 'notGate':
      screen.blit(generalDic['notIMG'],(allGates[each][1].x,allGates[each][1].y))
  pygame.display.flip()
  pass

def checkqueue():
  pass


#[][][][][][][][][]End Pygame[][][][][][][][][]

class gate(object):
  def __init__(self,gateName,x,y):
    self.gateName = gateName
    self.x = x
    self.y = y
    self.width = 149
    self.height = 91

  def checkSelected(self,givenX,givenY):
    if givenX <= self.x+self.width and givenX >= self.x:
      if givenY <= self.y+self.height and givenY >= self.y:
        return(True,givenX-self.x,givenY-self.y)
    return(False,0,0)

  def setnewPos(self,x,y):
    self.x = x
    self.y = y

class andGate(gate):
  def __init__(self,num,in1,in2,out,x,y):
    gate.__init__(self,"and{}".format(num),x,y)
    self.in1 = in1
    self.in2 = in2
    self.out = out

  def test(self):
    print("Yoo hoo")
          
  def output(self):
    if self.in1 == True and self.in2 == True:
      self.out = True
    else:
      self.out = False

  def getpos(self):
    return(self.x,self.y)


  def checkInOutSelected(self,math,givenX,givenY):
    z = complex(givenX,givenY)
    #for the output
    center = complex(self.x+133, self.y+44)
    if abs(z-center) < 16:
      return('Output')
    #for inputs
    #1
    center = complex(self.x+15,self.y+15)
    if abs(z-center) < 16:
      return("Inp1")
    #2
    center = complex(self.x+15,self.y+75)
    if abs(z-center) < 16:
      return("Inp2")
    return("")

def testfunc(complex,screen):
  import pygame, time
  pygame.draw.circle(screen,(0,0,0),[int(complex.real),int(complex.imag)],16)
  pygame.display.flip()
  time.sleep(1)
  pass

class orGate(gate):

  def __init__(self,num,in1,in2,out,x,y):
    gate.__init__(self,"or{}".format(num),x,y)
    self.in1 = in1
    self.in2 = in2
    self.out = out

  def output(self):
    if self.in1 == True or self.in2 == True:
      self.out = True
    else:
      self.out = False

  def getpos(self):
    return(self.x,self.y)

  def checkInOutSelected(self,math,givenX,givenY):
    z = complex(givenX,givenY)
    #for the output
    center = complex(self.x+133, self.y+44)
    if abs(z-center) < 16:
      return('Output')
    #for inputs
    #1
    center = complex(self.x+15,self.y+15)
    if abs(z-center) < 16:
      return("Inp1")
    #2
    center = complex(self.x+15,self.y+75)
    if abs(z-center) < 16:
      return("Inp2")
    return("")

class notGate(gate):

  def __init__(self,num,in1,out,x,y):
    gate.__init__(self,"not{}".format(num),x,y)
    self.in1 = in1
    self.out = out

  def output(self):
    if self.in1 == True:
      self.out = False
    else:
      self.out = True

  def getpos(self):
    return(self.x,self.y)

  def checkInOutSelected(self,math,givenX,givenY):
    z = complex(givenX,givenY)
    #for the output
    center = complex(self.x+133, self.y+44)
    if abs(z-center) < 16:
      return('Output')
    #for inputs
    #1
    center = complex(self.x+15,self.y+44)
    if abs(z-center) < 16:
      return("Inp1")
    return("")

def checkAllSelected(pygame,screen,allGates,pos):
  for each in allGates:
    selected,x,y = each[1].checkSelected(pos[0],pos[1])
    if selected:
      moveobject(pygame,screen,each[1],allGates,x,y)
      break
##
##def checkAllWiring(pygame,math,allGates,pos,screen):
##  for each in allGates:
##    first = each[1].checkInOutSelected(math,pos[0],pos[1])
##    start = True if first != '' else False
##    startPos = pos
##  while start == True:
##    pos = pygame.mouse.get_pos()
##    updateWindow(pygame,screen,allGates)
####  for each in allGates:
##    if "inp" in each[1].checkInOutSelected(math,pos[0],pos[1]) and "out" in first:
##      pass
##      #do thang
##    elif "out" in each[1].checkInOutSelected(math,pos[0],pos[1]) and "inp" in first:
##      pass
##      #do thanh
      
    
      


def moveobject(pygame,screen,Gate,allGates,extraX,extraY):
  finished = False
  while not finished:
    for event in pygame.event.get():
      finished = True if event.type == pygame.MOUSEBUTTONDOWN else False
    [x,y] = pygame.mouse.get_pos()
    Gate.setnewPos(x-extraX,y-extraY)
    updateWindow(pygame,screen,allGates)

def createAnd(allGates):
  allGates.append(['andGate',andGate(generalDic['AndNum'],False,False,False,30,40)])
  generalDic['AndNum'] += 1
  return(allGates)

def createOr(allGates):
  allGates.append(['orGate',orGate(generalDic['OrNum'],False,False,False,30,40)])
  generalDic['OrNum'] += 1
  return(allGates)

def createNot(allGates):
  allGates.append(['notGate',notGate(generalDic['NotNum'],False,False,30,40)])
  generalDic['NotNum'] += 1
  return(allGates)

def importAll():
  import pygame,math
  return pygame,math
  
if __name__ == '__main__':
  global generalDic
  generalDic = {}
  generalDic['AndNum'] = 0
  generalDic['OrNum'] = 0
  generalDic['NotNum'] = 0
  pygame,math = importAll()
  connector = []
  wiring = False
  allGates = []
  finished = False
  screen,clock = createWindow(pygame)
  while finished == False:
    updateWindow(pygame,screen,allGates)
    clock.tick(10)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        finished = True
      if event.type == pygame.VIDEORESIZE:
        screen = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
      if event.type == pygame.MOUSEBUTTONDOWN and not wiring:
        checkAllSelected(pygame,screen,allGates,pygame.mouse.get_pos())
      if event.type == pygame.MOUSEBUTTONDOWN and wiring:
        checkAllWiring(pygame,math,allGates,pygame.mouse.get_pos(),screen)
      if event.type == pygame.KEYDOWN:
        if (pygame.key.get_pressed())[pygame.K_1]:
          allGates = createAnd(allGates)
        if (pygame.key.get_pressed())[pygame.K_2]:
          allGates = createOr(allGates)
        if (pygame.key.get_pressed())[pygame.K_3]:
          allGates = createNot(allGates)
        if (pygame.key.get_pressed())[pygame.K_4]:
          wiring = False if wiring else True
