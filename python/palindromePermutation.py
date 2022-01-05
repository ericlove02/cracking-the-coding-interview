def palin_perm(s):
    """1.4: give a string, check if it is a permutation of a palindrome
    :type s: str
    :rtype: bool
    """
    # get list of letters in s, remove spaces
    # match up letters to ensure all but 0 or 1 match up
    numSoloChars = 0
    chars = list(s)
    if " " in chars:
        chars.remove(' ')  # remove spaces
    while chars:
        char = chars.pop(0)
        if char in chars:
            chars.pop(chars.index(char))
        else:
            numSoloChars += 1

    if numSoloChars <= 1:
        return True
    else:
        return False


str = str(input("String: "))
print(palin_perm(str))
