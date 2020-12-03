def checkTree(line, pos):
  if(line[pos] == '#'):
    return True
  return False

def getTreesPerSlope(startPos, slope):
  with open('input', 'r') as file:
    numTrees = 0
    cursor = 0
    forest = list(file)
    rowLength = len(forest[0])-1
    lineCount = 0
    for line in forest[::slope]:
      if lineCount == 0:
        lineCount +=slope
        continue
      cursor += startPos
      if cursor >= rowLength:
          cursor = cursor % rowLength
      if checkTree(line, cursor):
        numTrees += 1
      lineCount += slope
  return numTrees

slope1 = getTreesPerSlope(1, 1)
slope2 = getTreesPerSlope(3, 1)
slope3 = getTreesPerSlope(5, 1)
slope4 = getTreesPerSlope(7, 1)
slope5 = getTreesPerSlope(1, 2)
print(slope1*slope2*slope3*slope4*slope5)
