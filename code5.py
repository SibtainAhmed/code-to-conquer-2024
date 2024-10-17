from collections import defaultdict



N = int(input())
intervals = defaultdict()
for _ in range(N):
    inter = str(input())
    if inter not in intervals:
        intervals[inter] = 0
    intervals[inter] += 1

# print(intervals)
if not(len(intervals)):
    print(0)
else:
    print(max(intervals.values()))