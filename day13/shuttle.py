import math

def findEarliest(bus, timetable):
  earliest = min(timetable, key=lambda b: -bus % b)
  return (earliest * (-bus % earliest))

def lcm(x, y):
    return x * y // math.gcd(x, y)

def findConsecutive(timetable):
  # Applying Chinese Remainder theorem
  N = [1] * len(timetable)
  for _, bus in timetable.items():
    N = [lcm(n, bus) for n in N]
  M = N[0]
  i = 0
  for _, bus in timetable.items():
    N[i] //= bus
    i += 1
  X = [pow(n, -1, m) for n, m in zip(N, timetable.values())]
  sum = 0
  for b, n, x in zip(timetable.keys(), N, X):
    sum += b*n*x
  return sum % M

with open('input', 'r') as file:
  bus, timetable = list(file)
  bus = int(bus)
  table = [int(b) for b in timetable.split(',') if b!='x']
  # This resumes to the Chinese Remainder Theorem. The detail I had initially missed
  # is that the remainder must not have a modulo applied to it and that a minus needs to be
  # applied to it, as we need to find the t0, not the tn for the bus times
  timetableDict = {-i: int(b) for i, b in enumerate(timetable.split(',')) if b != "x"}
  print(timetableDict)
  print(findEarliest(bus, table))
  print(findConsecutive(timetableDict))
