def is_palindrom1(word):
    return word == word[::-1] # s[start:end:step]

def is_palindrom2(word):
    list_word = list(word)
    for i in range(len(list_word)//2):
        if list_word[i] != list_word[-i-1]:
            return False
    return True

def is_palindrom3(word):
    if len(word) < 2 :
        return True
    if word[0] !=word[-1]:
        return False
    return is_palindrom3(word[1:-1])
