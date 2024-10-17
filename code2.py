
def solve(word):
    cons = {c for c in 'aeiou'}
    res = ''
    for w in word:
        res = res + w
        if w in cons: 
            continue
        closestC = ''
        dist = 100
        for c in 'aeiou':
            distTemp = abs(ord(w)-ord(c))
            if distTemp < dist:
                dist = distTemp
                closestC = c
        res = res + closestC
        if w == 'z':
            res = res + 'z'
            continue
        for i in range(ord(w)+1, ord('z')+1):
            if chr(i) in cons:
                continue
            res = res + chr(i)
            break
    return res

st = input()
print(solve(st))
