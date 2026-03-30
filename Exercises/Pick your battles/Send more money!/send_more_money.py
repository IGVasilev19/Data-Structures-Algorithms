def get_unique_letters(w1, w2, w3):
    return list(dict.fromkeys(w1 + w2 + w3))


def word_to_num(word, assignment):
    result = 0
    for letter in word:
        result = result * 10 + assignment[letter]
    return result

def backtrack(letters, index, assignment, used, w1, w2, w3, leading):
    if index == len(letters):
        n1 = word_to_num(w1, assignment)
        n2 = word_to_num(w2, assignment)
        n3 = word_to_num(w3, assignment)
        return n1 + n2 == n3

    letter = letters[index]

    for digit in range(0, 10):
        if digit in used:
            continue
        if digit == 0 and letter in leading:
            continue                         

        assignment[letter] = digit
        used.add(digit)

        if backtrack(letters, index + 1, assignment, used, w1, w2, w3, leading):
            return True                       

        del assignment[letter]
        used.remove(digit)

    return False

def solve(w1, w2, w3):
    letters  = get_unique_letters(w1, w2, w3)
    leading  = {w1[0], w2[0], w3[0]}
    assignment = {}
    used = set()

    if backtrack(letters, 0, assignment, used, w1, w2, w3, leading):
        print("Solution found:", assignment)
        print(f"{word_to_num(w1, assignment)} + {word_to_num(w2, assignment)} = {word_to_num(w3, assignment)}")
    else:
        print("No solution exists.")

solve("SEND", "MORE", "MONEY")