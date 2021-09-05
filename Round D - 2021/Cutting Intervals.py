import sys
input = sys.stdin.readline
from collections import Counter

for t in range(int(input())):
    n, c = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    cand = []
    for a, b in A:
        if a + 1 < b:
            cand.append((a + 1, 1))
            cand.append((b, -1))
    cand.sort()
    cnt = Counter()
    cur = 0
    stack = []
    tot = [0]
    for x, z in cand:
        if z == 1:
            cur += 1
            stack.append(x)
            tot.append(0)
        else:
            y = stack.pop()
            cnt[cur] += x - y - tot.pop()
            tot[-1] += x - y
            cur -= 1
    ans = n
    for k in sorted(cnt, reverse=True):
        v = cnt[k]
        x = min(c, v)
        ans += k * x
        c -= x
        if not c: break
    print("Case #{}: {}".format(t + 1, ans))
