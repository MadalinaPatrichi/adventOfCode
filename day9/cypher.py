import copy

def checkPreambul(subset, num):
  for term1 in subset:
    for term2 in subset:
      if (term1+term2) == num:
        return True

def findWeakness(cypher, preLength):
  for num in cypher:
    idx = cypher.index(num)
    if preLength < idx:
      if not checkPreambul(cypher[idx-preLength:idx], num):
        return num

def findWeaknessSum(cypher, weaknessSum):
  cypherSums = copy.deepcopy(cypher)
  for sumLength in range(2, len(cypher)/2):
    try:
      for idx in range(len(cypherSums)):
          cypherSums[idx] += cypher[idx+sumLength-1]
          if cypherSums[idx] == weaknessSum:
            sequence = cypher[idx: idx+sumLength]
            print("Found sequence", sequence)
            return min(sequence) + max(sequence)
    except IndexError:
      print("Ran out of bounds, just continue to the next sumLength")

with open("input", 'r') as file:
  cypher = [int(elem.rstrip()) for elem in list(file)]
  preLength = 25
  print(findWeakness(cypher, preLength))
  print(findWeaknessSum(cypher, findWeakness(cypher, preLength)))
