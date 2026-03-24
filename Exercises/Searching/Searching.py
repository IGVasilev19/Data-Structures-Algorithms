import re

def readFileAndSeparateWords(fileName):
    arrayOfWords = []

    with open(fileName) as f:
        for line in f:
            tempArray = re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)*", line.casefold())

            if tempArray:
                arrayOfWords.extend(tempArray)

    return sorted(arrayOfWords)


def LinearCount(word, wordArray):
    count = 0

    for i in range(len(wordArray)):
        if word == wordArray[i]:
            count+=1

    return count


class Node:
    def __init__(self,word, count):
        self.left = None
        self.right = None
        self.val = {word : count}

def buildTree(pairs):
    if not pairs:
        return None
    
    mid = len(pairs) // 2
    word, count = list(pairs[mid].items())[0]
    node = Node(word, count)

    node.left  = buildTree(pairs[:mid])
    node.right = buildTree(pairs[mid+1:])

    return node


def listOfUniqueWordsAndCounts(arrayWords):
    pairs = []
    uniqeWords = sorted(set(arrayWords))
    for word in uniqeWords:
        pairs.append({word : arrayWords.count(word)})

    return pairs


def Binarycount(word, tree):
    
    if tree is None:
        return 0
    
    wordFromThree = list(tree.val.keys())[0]
    count = list(tree.val.values())[0]

    if word == wordFromThree:
            return count
    elif word < wordFromThree:
        return Binarycount(word, tree.left)
    else:
        return Binarycount(word, tree.right)




array = readFileAndSeparateWords("story.txt")
pairs = listOfUniqueWordsAndCounts(array)
tree = buildTree(pairs)
# print(array)
# print(listOfUniqWordsAndCounts(array))
print(Binarycount("a", tree))

