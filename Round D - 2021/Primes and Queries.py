import sys
input = sys.stdin.readline
from collections import Counter


class Fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)
        self.n = n

    def update(self, x, val):
        while x <= self.n:
            self.tree[x] += val
            x += x & -x

    def query(self, x):
        ans = 0
        while x:
            ans += self.tree[x]
            x -= x & -x
        return ans


for t in range(int(input())):
    n, Q, P = map(int, input().split())
    A = list(map(int, input().split()))

    def cal(x):
        if x == 0: return 0, 0
        cnt = 0
        while not x % P:
            cnt += 1
            x //= P
        return cnt, x

    bit = [Fenwick(n) for _ in range(4)]
    ans = []
    for i, a in enumerate(A, 1):
        cnt, x = cal(a)
        for s in range(4):
            if cnt:
                bit[s].update(i, cnt * (s + 1))
            else:
                cnt2, y = cal(x ** (s + 1) - (x % P) ** (s + 1))
                bit[s].update(i, cnt2)

    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            idx = q[1]
            val = q[2]
            cnt, x = cal(val)
            for s in range(4):
                tmp = bit[s].query(idx) - bit[s].query(idx - 1)
                if cnt:
                    bit[s].update(idx, cnt * (s + 1) - tmp)
                else:
                    cnt2, y = cal(x ** (s + 1) - (x % P) ** (s + 1))
                    bit[s].update(idx, cnt2 - tmp)
        else:
            s, l, r = q[1:]
            cur = bit[s - 1].query(r) - bit[s - 1].query(l - 1)
            ans.append(cur)

    print("Case #{}:".format(t + 1), *ans)
