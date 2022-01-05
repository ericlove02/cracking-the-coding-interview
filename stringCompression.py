def string_compression(s):
    """perform basic string compression using the count of repeated characters
    for ex: aabcccccaaa -> a2b1c5a3
    :type s: str
    :rtype: str
    """
    onChar = None
    count = 0
    out = ""
    for i in range(len(s)):
        if s[i] != onChar:
            if onChar is not None:
                out += str(onChar) + str(count)
            onChar = s[i]
            count = 1
        elif s[i] == onChar:
            count += 1
    out += str(onChar) + str(count)
    if len(out) >= len(s):  # if the compressed string is not smaller, return original string
        return s
    else:
        return out


inp = str(input("String: "))
print(string_compression(inp))
