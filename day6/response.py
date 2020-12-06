

def countGroupUnion(group):
  groupUnion=[]
  for answer in group:
    groupUnion = list(set(groupUnion) | set(answer))
  return len(groupUnion)

def countGroupIntersection(group):
  i=1
  sets = list(dict.fromkeys(group[0]))
  while i<len(group):
    sets = list(set((group[i])) & set(sets))
    i+=1
  return(len(sets))


def countAnswers(answers):
  group = []
  totalCountUnion = totalCountIntersection = 0
  for line in answers:
    if line.rstrip() == '':
      totalCountUnion += countGroupUnion(group)
      totalCountIntersection += countGroupIntersection(group)
      group = []
    else:
      group += line.split()
  totalCountUnion += countGroupUnion(group)
  totalCountIntersection += countGroupIntersection(group)
  return totalCountUnion, totalCountIntersection

with open('input', 'r') as file:
  answers = list(file)
  print(countAnswers(answers))
