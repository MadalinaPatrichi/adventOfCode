import re

def checkByr(data):
  if int(data) >= 1920 and int(data) <= 2002:
    return True
  return False

def checkIyr(data):
  if int(data) >= 2010 and int(data) <= 2020:
    return True
  return False

def checkEyr(data):
  if int(data) >= 2020 and int(data) <= 2030:
    return True
  return False

def checkHgt(data):
  try:
    height = int(data[:-2])
    unit = data[-2:]
    if unit == 'cm':
      if height >=150 and height <=193:
        return True
      return False
    elif unit == 'in':
      if height >= 59 and height <= 76:
        return True
      return False
  except Exception:
    return False
  return False

def checkHcl(data):
  if re.match('#[0-9a-f]{6}', data):
    return True
  return False

def checkEcl(data):
  if data in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
    return True
  return False

def checkPid(data):
  if re.match('[0-9]{9}', data) and len(data) == 9:
    return True
  return False

def checkPassportData(passport):
  print(passport)
  requiredFields = {'byr':0, 'iyr':0, 'eyr':0, 'hgt':0, 'hcl':0, 'ecl':0, 'pid':0}
  requiredFieldsChecks = {'byr': checkByr, 'iyr': checkIyr, 'eyr': checkEyr,
                    'hgt': checkHgt, 'hcl': checkHcl, 'ecl': checkEcl, 'pid': checkPid}
  for data in passport:
    field, info = data.split(':')
    if field in requiredFields:
      if requiredFieldsChecks[field](info):
        requiredFields[field] = True
      else:
        print("Failed check:", field, info)
        return False
  for key, data in requiredFields.items():
    if data != True:
      print("Missing, ", key)
      return False
  return True

def checkPassports(passports):
  passport = []
  validPassports = 0
  totalPassports = 0
  for line in passports:
    if line.rstrip() == '':
      if checkPassportData(passport):
        validPassports += 1
      passport = []
      totalPassports += 1
    else:
      passport += line.split()
  if checkPassportData(passport):
      validPassports += 1
  print(validPassports)
  print(totalPassports)


with open('input', 'r') as file:
  passports = list(file)
  checkPassports(passports)
