def appendAndDelete(s, t, k):
    a = list(s)
    b = list(t)
    
    for i in range(k):
        if a == b[:len(a)] and k - i == len(b[len(a):]):
            a.append(b[len(a)])
        else:
            if a:
                a.pop()

    return "Yes" if a == b else "No"
