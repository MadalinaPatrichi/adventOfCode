from collections import Counter, defaultdict

def calculateAdaptor(input):
  counter = Counter()
  prev = 0
  for adaptor in input:
    counter[adaptor-prev] += 1
    prev = adaptor
  return counter[1] * counter[3]

def calculateArrangements(input):
  inputDif={key:0 for key in input}
  inputDif[0] = 1
  for adaptor in input:
    # For every adaptor and accepted difference (1,2,3), add to the next accumulator
    # we can get to.
    for diff in range(1,4):
      next_adaptor = adaptor + diff
      if next_adaptor in input:
        inputDif[next_adaptor] += inputDif[adaptor]
      print(inputDif)
  return inputDif[input[len(input)-1]]

with open('simpleInput', 'r') as file:
  input = [int(line.strip()) for line in list(file)]
  input.sort()
  input.append(input[-1]+3)
  input.insert(0,0)
  print(calculateAdaptor(input))
  print(calculateArrangements(input))
