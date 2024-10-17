def solve(intervals):
    res = 0
    # st, ed = intervals.pop(0)
    st, et = 0,0
    for sT,eT in intervals:
        if sT > ed:
            ed = eT
            res += 1
    return res








N = int(input())
intervals = []
for _ in range(N):
    inter = input().split(' ')
    intervals.append((int(inter[0]), int(inter[1])))
intervals.sort(key=lambda x:x[0])
print(intervals)
print(solve(intervals))