# N, K = map(int, )
import heapq

def solve(N,K,A,F):
    if N == 1:
        return max(0,A[0]-K)*F[0]
    elif sum(A) <= K:
        return 0
    hp = [(-A[i]*F[i], i) for i in range(N)]
    heapq.heapify(hp)
    while K>0:
        val, i = heapq.heappop(hp)
        print(val, i)
        nVal = hp[0][0]
        factor = val//nVal
        A[i] -= min(factor,K)
        K -= min(factor,K)
        newVal = -A[i]*F[i]
        heapq.heappush((newVal, i), hp)
    return -hp[0][0]



N = input().split(' ')
Nnew = []
for n in N:
    Nnew.append(int(n))
A = input().split(' ')
Anew = []
for a in A:
    Anew.append(int(a))
B = input().split(' ')
Bnew = []
for b in B:
    Bnew.append(int(b))
# for 
# print(A)
# F = list(input())


print(solve(Nnew[0], Nnew[1],Anew,Bnew ))