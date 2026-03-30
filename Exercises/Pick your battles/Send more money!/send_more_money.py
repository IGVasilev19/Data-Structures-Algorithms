def getUniqueLetters(words):
    combinedWords = []
    for i in range(len(words)):
        combinedWords += words[i]

    return list(dict.fromkeys(combinedWords))

def getFirstLetters(words):
    firstLetters = []

    for i in range(len(words)):
        firstLetters.append(words[i][0])

    return firstLetters

def assignCoversionToWord(word, mappings):
    num = 0
    for i in range(len(word)):
        num = num * 10 + mappings[word[i]]

    return num

def checkSuffice(words, mappings):
    count = 0

    for i in range(0, len(words)-1):
        count += assignCoversionToWord(words[i], mappings)

    return count == assignCoversionToWord(words[len(words)-1], mappings)

def printSolution(words, mappings):
    for i in range(len(words)-1):
        print(str(assignCoversionToWord(words[i], mappings)) + " +")
    print(" = " + str(assignCoversionToWord(words[len(words)-1], mappings)))
    

def solveCryptarithmetic(letterIndex, words, mappings, firstLetters, uniqueLetters):

    if len(words) == 0:
        return False

    if letterIndex == len(uniqueLetters):
        return checkSuffice(words, mappings)

    
    for i in range(10):
        if (firstLetters.count(uniqueLetters[letterIndex]) != 0 and i == 0) or i in mappings.values():
            continue
        
        mappings[uniqueLetters[letterIndex]] = i

        result = solveCryptarithmetic(letterIndex + 1, words, mappings, firstLetters, uniqueLetters)

        if result == True:
            return True
        
        mappings.pop(uniqueLetters[letterIndex])

    return False    

words = ["SEND", "MORE", "MONEY"]

firstLetters = getFirstLetters(words)
uniqueLetters = getUniqueLetters(words)
mappings = {}

if solveCryptarithmetic(0, words, mappings, firstLetters, uniqueLetters):
    printSolution(words, mappings)
else:
    print("No solution")