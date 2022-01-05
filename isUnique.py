def is_unique(str1, str2):
    """1.1: determine if a string has all unique chars
    :type str1: str
    :type str2: str
    :rtype: bool
    """
    # 1.1 is unique
    chars = list(str1)
    for char in str2:
        if char in chars:
            return False
    return True


in1 = str(input("Enter str1: "))
in2 = str(input("Enter str2: "))

print(is_unique(in1, in2))
