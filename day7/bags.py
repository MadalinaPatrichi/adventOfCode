import copy

def sortRules(rules):
  sortedRules = {}
  for rule in rules:
    leader, followers = rule.split(" bags contain")
    followers = followers.split(',')
    for follower in followers:
      if 'other' not in follower:
        num, bagShade, bagColor, _ = follower.split()
        if leader in sortedRules.keys():
          sortedRules[leader][bagShade + ' ' + bagColor] = num
        else:
          sortedRules[leader] = {}
          sortedRules[leader][bagShade + ' ' + bagColor] = num
      else:
        sortedRules[leader] = {}
  return(sortedRules)

def findLeaders(sortedRules, parents):
  newParents = copy.deepcopy(parents)
  for key, items in sortedRules.iteritems():
    for color in parents:
      if color in items.iterkeys():
        newParents.add(key)
  if len(newParents) == len(parents):
    return(len(parents)-1)
  return findLeaders(sortedRules, newParents)

def findFollowers(sortedRules, followers):
  totalBags = 0
  while len(followers):
    countFollower = followers.pop()
    follower = sortedRules[countFollower]
    for color, count in follower.items():
      totalBags += int(count)
      followers.extend([color] * int(count))
  return totalBags


with open('input', 'r') as file:
  rules = list(file)
  sortedRules = sortRules(rules)
  print(findLeaders(sortedRules, set({'shiny gold': 0})))
  print(findFollowers(sortedRules, ['shiny gold']))
