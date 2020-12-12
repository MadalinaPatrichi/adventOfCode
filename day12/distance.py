dirSym = ['E', 'S', 'W', 'N']
cardinals = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

def calculateDistance(coords):
  posDir = 'E'
  pos = (0, 0)
  for dir, coord in coords:
    if dir == 'F':
      pos = (pos[0]+cardinals[posDir][0]*coord, pos[1] + cardinals[posDir][1]*coord)
    elif dir in ['R', 'L']:
      degrees = {'L': -1, 'R': 1}[dir]
      posDir = dirSym[(dirSym.index(posDir)+degrees*coord/90)%4]
    elif dir in cardinals:
      pos = (pos[0] + cardinals[dir][0]*coord, pos[1]+ cardinals[dir][1]*coord)
  return abs(pos[0]) + abs(pos[1])


def calculateWaypoint(coords):
  posDir = 'E'
  pos = (0, 0)
  posW = (10, 1)
  for dir, coord in coords:
    print(posDir, pos, posW)
    if dir == 'F':
      pos = (pos[0]+coord*posW[0], pos[1] + coord*posW[1])
    elif dir in ['R', 'L']:
      posDir = dirSym[(dirSym.index(posDir)+coord/90) % 4]
      degrees = {'L': 360 - coord, 'R': coord}[dir]
      posW = {90: (posW[1], -posW[0]), 180: (-posW[0], -posW[1]),
              270: (-posW[1], posW[0])}[degrees]
    elif dir in cardinals:
      posW = (posW[0] + cardinals[dir][0]*coord, posW[1] + cardinals[dir][1]*coord)
  return abs(pos[0]) + abs(pos[1])

with open('input', 'r') as file:
  coord = list(file)
  coordList = []
  for line in coord:
    coordList.append((line[0], int(line.rstrip()[1:])))
  print(calculateDistance(coordList))
  print(calculateWaypoint(coordList))