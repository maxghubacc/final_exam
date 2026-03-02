def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("7798338247658278460338648728567428338977"))