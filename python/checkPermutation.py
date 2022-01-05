def is_permutation(str1, str2):
    """1.2: decide if one is a permutation of the other
    :type str1: str
    :type str2: str
    :rtype: bool
    """
    # permutation need same letters but in different order
    is_perm = True
    if str1 == str2:
        is_perm = False

    chars = list(str1)
    for char in str2:
        if char not in chars:
            is_perm = False

    return is_perm


in1 = str(input("Enter str1: "))
in2 = str(input("Enter str2: "))

print(is_permutation(in1, in2))
