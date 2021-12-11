t = int(input())

for case in range(1, t+1):
    n = int(input())
    Sum = 0
    for i in range(1,n+1):
        newElement = 1 + Sum/i
        Sum += newElement
    ans = newElement
    print("Case #%s: %s" % (case, ans))
