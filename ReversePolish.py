#a piece of code to work through all items and create a reverse polish notation style thing to work out when to calculate them
# A . B + C = A B C + .
# A" . B + C = A " B C + . 
allGates = [['Light',0],['Or',0],['Or',0],['And',0],['And',0],['And',0],['Not',0],['Switch','a',False],['Switch','b',False],['Switch','c',True],['Switch','d',False]]
connector = [[0,0,1],[1,1,2],[2,1,3],[3,2,4],[4,2,5],[5,3,9],[6,3,6],[7,4,7],[8,4,9],[9,5,8],[10,5,10],[11,6,10]]

def reversePolish(allGates,connector):
  for each in connector:
    if allGates[each[1]][0] == 'Light':
      lst = recursion(allGates,connector,each[2])
  lst = flatten(lst)
  print(lst)
  equation = stackify(lst)
  print(readPolish(allGates,equation))
  
def stackify(lst):
  import stackType
  output = stackType.Stack(isMax = False)
  for each in lst:
    output.push(each)
  return(output)

def flatten(x):# James Brady - On Stack-Overflow chain --https://stackoverflow.com/questions/406121/flattening-a-shallow-list-in-python
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, str):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

def recursion(allGates,connector,allGatesLocation):
  new = []
  gate = allGates[allGatesLocation]
  if gate[0] == 'Or' or gate[0] == 'And' or gate[0] == 'Not':
    for each in connector:
      if each[1] == allGatesLocation:
        new.append(recursion(allGates,connector,each[2]))
    new.append(gate[0])
    return(new)
  if gate[0] == 'Switch':
    return gate[1]

def readPolish(allGates,lst):
  import stackType
  item = lst.pop()
  if item in ['And','Or']:
    operand = item
    opperator1 = lst.pop()
    if opperator1 in ['And','Or','Not']:
      lst.push(opperator1)
      opperator1 = readPolish(allGates,lst)
    else:
      for each in allGates:
        if each[1] == opperator1:
          opperator1 = each[2]
    opperator2 = lst.pop()
    if opperator2 in ['And','Or','Not']:
      lst.push(opperator2)
      opperator2 = readPolish(allGates,lst)
    else:
      for each in allGates:
        if each[1] == opperator2:
          opperator2 = each[2]
    if operand == 'And':
      end = True if opperator1 == True and opperator2 == True else False
    if operand == 'Or':
      end = True if opperator1 == True or opperator2 == True else False
  if item == 'Not':
    operand = item
    opperator1 = lst.pop()
    if opperator1 in ['And','Ir','Not']:
      lst.push(opperator1)
      opperator1 = readPolish(allGates,lst)
    else:
      for each in allGates:
        if each[1] == opperator1:
          opperator1 = each[2]
    end = not opperator1
  return(end)

reversePolish(allGates,connector)
