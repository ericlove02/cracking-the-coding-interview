def one_away(str1, str2):
    """1.5: given two strings, write a function to check if they are one or zero
    edits away
    :type str1: str
    :type str2: str
    :rtype: bool
    """
    # an edit can insert, remove, or replace a character
    # str1 and str2 will have at most 1 character different
    if(len(str1) == len(str2)):
        return oneReplace(str1, str2)
    elif(len(str1) + 1 == len(str2)):
        return oneInsert(str1, str2)
    elif(len(str1) - 1 == len(str2)):
        return oneInsert(str2, str1)
    return False


def oneReplace(str1, str2):
    foundDiff = False
    for i in range(len(str1)):
        if not str1[i] == str2[i]:
            if(foundDiff):
                return False
            foundDiff = True
    return True


def oneInsert(str1, str2):
    i1 = 0
    i2 = 0
    while(i1 < len(str1) and i2 < len(str2)):
        if not str1[i1] == str2[i2]:
            if i1 != i2:
                return False
            i2 += 1
        else:
            i1 += 1
            i2 += 1
    return True


in1 = str(input("str1: "))
in2 = str(input("str2: "))
print(one_away(in1, in2))
