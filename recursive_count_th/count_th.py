'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, n=None, count=None):
    if count == None:
        count = 0
    if n == None:
        n = 0
    if not len(word):
        return 0
    if n < len(word) - 1:
        if word[n] + word[n + 1] == "th":
            count += 1
        return count_th(word, n + 1, count)
    if n == len(word) - 1:
        if count == 0:
            return 0
        return count
            
