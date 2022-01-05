# NOT COMPLETE

def one_away(str1, str2):
    """1.5: given two strings, write a function to check if they are one or zero
    edits away
    :type str1: str
    :type str2: str
    :rtype: bool
    """
    # an edit can insert, remove, or replace a character
    # str1 and str2 will have at most 1 character different
    if len(str1) < len(str2):
        temp = str1
        str1 = str2
        str2 = temp

    edits = 0
    for i in range(len(str1)):
        if i >= len(str2):
            edits += 1
        elif not str1[i] == str2[i] or str1[i+1] == str2[i]:
            edits += 1

    print(edits)
    if edits > 1:
        return False
    else:
        return True

in1 = str(input("str1: "))
in2 = str(input("str2: "))
print(one_away(in1, in2))
