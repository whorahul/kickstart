import sys
input = sys.stdin.readline
from collections import Counter

for t in range(int(input())):
    A = [[0] * 3 for _ in range(3)]
    for i in range(3):
        if i == 1:
            A[i][0], A[i][2] = map(int, input().split())
        else:
            A[i][0], A[i][1], A[i][2] = map(int, input().split())
    ans = 0
    if A[0][1] - A[0][0] == A[0][2] - A[0][1]: ans += 1
    if A[2][1] - A[2][0] == A[2][2] - A[2][1]: ans += 1
    if A[1][0] - A[0][0] == A[2][0] - A[1][0]: ans += 1
    if A[1][2] - A[0][2] == A[2][2] - A[1][2]: ans += 1
    cnt = Counter()
    for a, b in [(A[0][0], A[2][2]), (A[2][0], A[0][2]), (A[1][0], A[1][2]), (A[0][1], A[2][1])]:
        x = (a + b) // 2
        if x - a == b - x: cnt[x] += 1
    ans += max(cnt.values() or [0])
    print("Case #{}: {}".format(t + 1, ans))
