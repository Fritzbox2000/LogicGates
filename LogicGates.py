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
  return (screen,clock)


def updateWindow(pygame,screen,allGates,connector,initialPos = '', pos = ''):
  screen.fill(generalDic['bg'])
  for each in allGates:
    each[1].drawGate(pygame,screen)
  for each in connector:
    if each[2] == False:
      pygame.draw.line(screen,(255,255,255),each[4],each[5],10)
    if each[2] == True:
      pygame.draw.line(screen,(255,0,0),each[4],each[5],10)
    if initialPos != '' or pos != '':
      pygame.draw.line(screen,(255,255,255),initialPos,pos,10)
  pygame.display.flip()
  pass

def checkqueue(connector,allGates):
  for index,each in enumerate(connector,start =0):
    connector[index][2] = allGates[3].output()
  pass

#[][][][][][][][][]End Pygame[][][][][][][][][]

def checkAllSelected(pygame,screen,allGates,pos):
  for each in allGates:
    selected,x,y = each[1].checkSelected(pos[0],pos[1])
    if selected:
      moveobject(pygame,screen,each[1],allGates,x,y)
      break

def checkAllWiring(pygame,math,screen,allGates,pos,connector):
  initialPos = pos
  for index,each in enumerate(allGates,start=0):
    inOut = each[1].checkInOutSelected(math,pos[0],pos[1])
    if inOut is not None:
      found = True
      break
  finished = True if found == False else False
  while not finished:
    pos = pygame.mouse.get_pos()
    updateWindow(pygame,screen,allGates,connector,initialPos,pos)
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        for index2,each in enumerate(allGates,start=0):
          newInOut = each[1].checkInOutSelected(math,pos[0],pos[1])
          if newInOut is not None:
            if 'Inp' in newInOut and 'Out' in inOut:
              connector.append([generalDic['ConnectorIndex'],False,index,index2,initialPos,pos])
              if newInOut == 'Inp1':
                allGates[index2].in1 = generalDic['ConnectorIndex']
              if newInOut == 'Inp2':
                allGates[index2].in2 = generalDic['ConnectorIndex']
              generalDic['ConnectorIndex']+=1
              finished = True
            if 'Out' in newInOut and 'Inp' in inOut:
              connector.append([generalDic['ConnectorIndex'],False,index2,index,initialPos,pos])
              if inOut == 'Inp1':
                allGates[index].in1 = generalDic['ConnectorIndex']
              if inOut == 'Inp2':
                allGates[index].in2 = generalDic['ConnectorIndex']
              generalDic['ConnectorIndex']+=1
              finished = True
  return(connector)

def deleteSelected(pygame,screen,allGates,pos):
  for each,index in enumerate(allGates,start = 0):
    selected,x,y = each[1].checkSelected(pos[0],pos[1])
    if selected:
      allGates.pop(index)
      break


def moveobject(pygame,screen,Gate,allGates,extraX,extraY):
  finished = False
  connector = []
  while not finished:
    for event in pygame.event.get():
      finished = True if event.type == pygame.MOUSEBUTTONDOWN else False
    [x,y] = pygame.mouse.get_pos()
    Gate.setnewPos(x-extraX,y-extraY)
    updateWindow(pygame,screen,allGates,connector)

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
  generalDic['AndNum'],generalDic['OrNum'],generalDic['NotNum'],generalDic['ConnectorIndex'] = 0,0,0,0
  pygame,math,Gates = importAll()
  wiring,deleting,finished = False,False,False
  allGates,connector = [],[]
  screen,clock = createWindow(pygame)
  while finished == False:
    updateWindow(pygame,screen,allGates,connector)
    clock.tick(10)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        finished = True
      if event.type == pygame.VIDEORESIZE:
        screen = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
      if event.type == pygame.MOUSEBUTTONDOWN and not wiring and not deleting:
        checkAllSelected(pygame,screen,allGates,pygame.mouse.get_pos())
      if event.type == pygame.MOUSEBUTTONDOWN and wiring and not deleting:
        checkAllWiring(pygame,math,screen,allGates,pygame.mouse.get_pos(),connector)
      if event.type == pygame.MOUSEBUTTONDOWN and not wiring and deleting:
        deleteSelected(pygame,math,allGates,pygame.mouse.get_pos())
      if event.type == pygame.KEYDOWN:
        if (pygame.key.get_pressed())[pygame.K_1]:
          allGates = createAnd(allGates,Gates)
        if (pygame.key.get_pressed())[pygame.K_2]:
          allGates = createOr(allGates,Gates)
        if (pygame.key.get_pressed())[pygame.K_3]:
          allGates = createNot(allGates,Gates)
        if (pygame.key.get_pressed())[pygame.K_4]:
          wiring = False if wiring else True
        if (pygame.key.get_pressed())[pygame.K_5]:
          deleting = False if deleting else True
