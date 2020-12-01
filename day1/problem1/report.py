with open('input', 'r') as file:
  report = [int(i) for i in file]
  print(report)

sum = 2020
# Two terms
for term1 in report:
  term2 = sum - term1
  if term2 in report:
    print(term1 * term2)

# Three terms
for term1 in report:
  term23 = sum - term1
  for term2 in report:
    term3 = term23 - term2
    if term3 in report:
      print(term1 * term2 * term3)
