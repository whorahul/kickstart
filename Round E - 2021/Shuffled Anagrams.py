t = int(input())


"""
works by maintaining the invariant that nobody has > 1/2 the total territory
by cyclically dissipating the biggest powers.
"""
def get_answer(letters, mults,indices, total_length):
    for element in mults:
        if mults[element] > total_length/2:
            return "IMPOSSIBLE"
    # otherwise, I think a solution exists - see docstring
    answer = ["" for i in range(total_length)]
    while mults != {}:
        sizes = sorted(list(mults.keys()), key=lambda x:mults[x])
        char1 = sizes[-1]
        char2 = sizes[-2]
        if mults[char1] > mults[char2]:

            answer[ indices[char1].pop() ] = char2
            answer[ indices[char2].pop() ] = char1
            mults[char1] -= 1
            mults[char2] -= 1
            if mults[char2] == 0:
                mults.pop(char2)
                indices.pop(char2)
            # don't have to check for char1 because it's strictly greater

        else:
            maximalElements = []
            standard = mults[char1]
            for char in sizes:
                if mults[char] == standard:
                    maximalElements.append(char)
            for i in range(len(maximalElements)):
                fromChar = maximalElements[i]
                toChar = maximalElements[i-1]
                answer[ indices[toChar].pop() ] = fromChar
                mults[toChar] -= 1
        if mults[char1] == 0:
            break
    return "".join(answer)
            
    

for case in range(1, t+1):
    letters = input()
    mults = {}
    indices = {}
    total_length = len(letters)
    for i in range(total_length):
        element = letters[i]
        if element in mults:
            mults[element] += 1
            indices[element].append(i)
        else:
            mults[element] = 1
            indices[element] = [i]
    answer = get_answer(letters, mults, indices, total_length)
    print("Case #" + str(case) + ": " + answer)
