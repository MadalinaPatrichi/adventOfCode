def isValidPartOne(atLeast, atMost, letter, password):
  count = password.count(letter)
  if count >= atLeast and count <= atMost:
    return True
  return False

def isValidPartTwo(firstPos, secondPos, letter, password):
  print(password[firstPos], password[secondPos])
  if (password[firstPos] == letter) ^ (password[secondPos] == letter):
    return True
  return False

with open('input', 'r') as file:
  validPartOneCount = 0
  validPartTwoCount = 0
  for line in file:
    times, letter, password = line.split()
    atLeast, atMost = times.split("-")
    letter = letter[0]
    if isValidPartOne(int(atLeast), int(atMost), letter, password):
      validPartOneCount+=1
    if isValidPartTwo(int(atLeast)-1, int(atMost)-1, letter, password):
      validPartTwoCount += 1
  print(validPartOneCount, validPartTwoCount)
