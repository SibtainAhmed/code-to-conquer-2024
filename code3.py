def solve(s):
    enter = ext = 0
    for i in s:
        if i == '+':
            enter += 1
        else:
            ext += 1
    return abs(enter-ext)



def solveC(s):
    enter = ext = cnt = 0
    for i in s:
        if i == '+':
            cnt += 1
        else:
            cnt  -= 1
        enter = max(enter, cnt)
        ext = min(ext, cnt)
    return enter-ext




st = input()
print(solve(st))
print(solveC(st))