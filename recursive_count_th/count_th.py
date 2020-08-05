'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# this is a O(n), input influences the count but not the runtime


def count_th(word):
    if len(word) < 2:
        return 0

    occur = word[:2]
    if occur == "th" or occur == "TH" and occur == "tH" and occur == "Th":
        return 1 + count_th(word[2:])

    return count_th(word[1:])

# prints 6

print(count_th(word="testhisthatthTHthosethemthree"))

# prints 1
print(count_th(word="leather"))

# prints 1
print(count_th(word="th"))
