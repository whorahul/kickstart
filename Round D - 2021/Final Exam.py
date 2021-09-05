import sys
input = sys.stdin.readline
import bisect

for t in range(int(input())):
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    B = list(map(int, input().split()))
    ans = [0] * m
    A.sort()

    def cal(a, b, x):
        if x < a: return a
        if x > b: return b
        return x

    def split(a, b, x):
        ans = []
        if a <= x - 1: ans.append([a, x - 1])
        if x + 1 <= b: ans.append([x + 1, b])
        return ans

    for i, b in enumerate(B):
        idx = bisect.bisect_left(A, [b, float("inf")])
        tmp1, tmp2 = -1, -1
        if idx < len(A):
            tmp1 = cal(A[idx][0], A[idx][1], b)
            d1 = abs(b - tmp1)
        if idx:
            tmp2 = cal(A[idx - 1][0], A[idx - 1][1], b)
            d2 = abs(b - tmp2)
        if tmp1 == -1:
            ans[i] = tmp2
            cur = split(A[idx - 1][0], A[idx - 1][1], tmp2)
            A[idx - 1: idx] = cur
        elif tmp2 == -1:
            ans[i] = tmp1
            cur = split(A[idx][0], A[idx][1], tmp1)
            A[idx: idx + 1] = cur
        else:
            if d1 < d2:
                ans[i] = tmp1
                cur = split(A[idx][0], A[idx][1], tmp1)
                A[idx: idx + 1] = cur
            else:
                ans[i] = tmp2
                cur = split(A[idx - 1][0], A[idx - 1][1], tmp2)
                A[idx - 1: idx] = cur
    print("Case #{}:".format(t + 1), *ans)
