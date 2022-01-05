def URLify(s):
    """1.3: replace all spaces in string s with '%20'
    :type s: str
    :rtype: str
    """

    # return s.replace(" ", "%20") # simple one line answer

    out = ""
    for char in s:
        if char == " ":
            out += "%20"
        else:
            out += char
    return out


str = str(input("String: "))
print(URLify(str))