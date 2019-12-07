# Are any two adjacent numbers identical?
def twinAdjDigits(digits):
    answer = False
    for i in range(0,5):
        if digits[i] == digits[i+1]:
            answer = True
    return answer

# Do the numbers never decrease?
def neverDecrease(digits):
    answer = True
    for i in range(0,5):
        if digits[i] > digits[i+1]:
            answer = False
    return answer

# For the given range, return all numbers that satisfy above conditions
def crack():
    possiblePass = []
    for i in range(125730, 579382):
        spread = map(int, str(i))
        if twinAdjDigits(spread) & neverDecrease(spread):
            possiblePass.append(i)
    return possiblePass

# Given a digit and the set of numbers in that digit are there only doubles for
# adjacent numbers?
def onlyDouble(digit, numSet):
    answer = False
    for i in numSet:
        if digit.count(i) == 2:
            answer = True
    return answer

def doubleCrack(digits):
    possiblePass = []
    for num in digits:
        spread = map(int, str(num))
        unique = set(spread)
        if onlyDouble(spread, unique):
            possiblePass.append(num)
    return possiblePass

possiblePasswords = crack()
print(len(possiblePasswords))
print(len(doubleCrack(possiblePasswords)))
