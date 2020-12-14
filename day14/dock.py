
import re
import itertools

def sumInstructions(program):
  mask = 'X'*36
  mem = {}
  for line in program:
    line.rstrip()
    if line.startswith('mask'):
      mask = re.findall('mask = ([X01]{36})', line)[0]
    elif line.startswith('mem'):
      addr, value = re.findall('mem\[(\d+)\] = (\d+)', line)[0]
      binaryValue = format(int(value), '036b')
      mem[addr] = ''.join([n if m == 'X' else m for m, n in zip(mask, binaryValue)])
  sum = 0
  for _, value in mem.items():
    sum += int(value, 2)
  return sum

def floatInstructions(program):
  mask = 'X'*36
  mem = {}
  memComp = {}
  for line in program:
    line.rstrip()
    if line.startswith('mask'):
      mask = re.findall('mask = ([X01]{36})', line)[0]
    elif line.startswith('mem'):
      addr, value = re.findall('mem\[(\d+)\] = (\d+)', line)[0]
      binaryValue = format(int(addr), '036b')
      mem[addr] = ''.join(
          [m if m == 'X' else n if m == '0' else '1'  for m, n in zip(mask, binaryValue)])
      floatCount = mem[addr].count('X')
      res = []
      for t in itertools.product('01', repeat=floatCount):
        it = iter(t)
        elem = ''.join(next(it) if c == 'X' else c for c in mem[addr])
        res.append(int(elem, 2))
      for r in res:
        memComp[r] = int(value)
  return sum(memComp.values())

with open('input', 'r') as file:
  program = list(file)
  print(sumInstructions(program))
  print(floatInstructions(program))