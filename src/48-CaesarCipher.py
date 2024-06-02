def caesarCipher(s, k):
    res = ""
    k = k % 26 
    for c in s:
        if 'a' <= c <= 'z':
            res += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            res += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        else:
            res += c

    return res
