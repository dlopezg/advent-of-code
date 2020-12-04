def parseInput(file):
    lines = [line.strip() for line in open(file).readlines()]
    passportList = list()
    lastPassport = str()
    for line in lines:
        if not line:
            passportList.append(lastPassport.split(' '))
            lastPassport = str()
            continue
        lastPassport = lastPassport + ' ' + line
    passportList.append(lastPassport.split(' '))
    return passportList

def checkRequiredFields(fields):
    validFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for requiredField in validFields:            
        if requiredField not in fields:
             return False
    return checkFieldsValidity(fields)

def checkFieldsValidity(fields):
    validEyeColor = ['amb','blu','brn','gry','grn','hzl','oth']
    validChar = ['a','b','c','d','f']
    validColorDigits = [str(digit) for digit in list(range(10))] + validChar
    
    if 1920 <= int(fields['byr']) <= 2002:
        if 2010 <= int(fields['iyr']) <= 2020:
            if 2020 <= int(fields['eyr']) <= 2030:
                if len(fields['pid']) == 9:
                    if fields['ecl'] in validEyeColor:
                        if fields['hcl'][0] == '#':
                            for digit in fields['hcl'][1:]:
                                validDigit = True
                                if digit not in validColorDigits:
                                    validDigit = False 
                            if validDigit:
                                validHeight = False
                                if fields['hgt'][-2:] == 'cm' and 150 <= int(fields['hgt'][0:-2]) <= 193:
                                    validHeight = True
                                if fields['hgt'][-2:] == 'in' and 59 <= int(fields['hgt'][0:-2]) <= 76:
                                    validHeight = True
                                if validHeight:
                                    return True
    return False

def checkPassportsValidity(passportList):
    validPassports = 0
    for passport in passportList:
        # Map each passport field in a dictionary:
        fields = {}
        for field in passport:
            if field:
                field = field.split(':')
                fields[field[0]] = field[1]
        # Check all the required fiels:   
        if checkRequiredFields(fields):
            if checkFieldsValidity(fields):
                validPassports += 1
    return validPassports

passportList = parseInput('passports.txt')
print(checkPassportsValidity(passportList))


