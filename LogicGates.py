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
      allGates[each][1].drawGate(pygame,screen)
    elif allGates[each][0] == 'orGate':
      allGates[each][1].drawGate(pygame,screen)
    elif allGates[each][0] == 'notGate':
      allGates[each][1].drawGate(pygame,screen)
  pygame.display.flip()
  pass

def checkqueue():
  pass


#[][][][][][][][][]End Pygame[][][][][][][][][]

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

def createAnd(allGates,Gates):
  allGates.append(['andGate',Gates.andGate(generalDic['AndNum'],False,False,False,30,40)])
  generalDic['AndNum'] += 1
  return(allGates)

def createOr(allGates,Gates):
  allGates.append(['orGate',Gates.orGate(generalDic['OrNum'],False,False,False,30,40)])
  generalDic['OrNum'] += 1
  return(allGates)

def createNot(allGates,Gates):
  allGates.append(['notGate',Gates.notGate(generalDic['NotNum'],False,False,30,40)])
  generalDic['NotNum'] += 1
  return(allGates)

def importAll():
  import pygame,math,Gates
  return pygame,math,Gates

if __name__ == '__main__':
  global generalDic
  generalDic = {}
  generalDic['AndNum'] = 0
  generalDic['OrNum'] = 0
  generalDic['NotNum'] = 0
  pygame,math,Gates = importAll()
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
          allGates = createAnd(allGates,Gates)
        if (pygame.key.get_pressed())[pygame.K_2]:
          allGates = createOr(allGates,Gates)
        if (pygame.key.get_pressed())[pygame.K_3]:
          allGates = createNot(allGates,Gates)
        if (pygame.key.get_pressed())[pygame.K_4]:
          wiring = False if wiring else True
  pygame.quit()
