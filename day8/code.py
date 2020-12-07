import copy

def processInstructions(instructions):
  procInstructions = []
  for instr in instructions:
    op, fact = instr.split()
    sign = fact[0]
    if sign == '-':
      factor = 0-int(fact[1:])
    else:
      factor = int(fact[1:])
    procInstructions.append({op: factor})
  return procInstructions

def calculateBefore(instructions, pos, sum, seenSteps):
  if pos in seenSteps:
    return sum
  seenSteps.append(pos)
  if 'acc' in instructions[pos]:
    sum += instructions[pos]['acc']
    pos+=1
  elif 'nop' in instructions[pos]:
    pos+=1
  elif 'jmp' in instructions[pos]:
    pos += instructions[pos]['jmp']
  return calculateBefore(instructions, pos, sum, seenSteps)


def checkFixedInstructions(instructions, pos, sum, seenSteps):
  if pos in seenSteps:
    return False
  end = False
  if pos == len(instructions)-1:
    end = True
  seenSteps.append(pos)
  if 'acc' in instructions[pos]:
    sum += instructions[pos]['acc']
    pos += 1
  elif 'nop' in instructions[pos]:
    pos += 1
  elif 'jmp' in instructions[pos]:
    pos += instructions[pos]['jmp']
  if end:
    return sum
  return checkFixedInstructions(instructions, pos, sum, seenSteps)

def replaceInstructions(instructions):
  for instruction in instructions:
    if 'nop' in instruction:
      fixedInstructions = copy.deepcopy(instructions)
      fixedInstructions[fixedInstructions.index(instruction)] = {'jmp' : instruction['nop']}
    elif 'jmp' in instruction:
      fixedInstructions = copy.deepcopy(instructions)
      fixedInstructions[fixedInstructions.index(instruction)] = {
          'nop': instruction['jmp']}
    else:
      continue
    sum = checkFixedInstructions(fixedInstructions, 0, 0, [])
    if sum:
      return sum

with open('testInput', 'r') as file:
  instructions = list(file)
instructions = processInstructions(instructions)
print(calculateBefore(instructions, 0, 0, []))
print(replaceInstructions(instructions))
