import math
for case in range(1,int(input())+1):
    n,q=map(int,input().split())
    adj={i:[] for i in range(1,n+1)}
    for i in range(n-1):
        x,y,li,ai=map(int,input().split())
        adj[x].append([x,y,li,ai])
        adj[y].append([y,x,li,ai])
    heads={}
    toexplore=adj[1]
    while toexplore:
        x,y,li,ai=toexplore.pop()
        heads[y]=[x,li,ai]
        for x0,y0,li0,ai0 in adj[y]:
            if y0!=x:
                toexplore.append([x0,y0,li0,ai0])
    ans=[]
    for i in range(q):
        cj,wj=map(int,input().split())
        cost=0
        while cj!=1:
            cj,li,ai=heads[cj]
            if wj>=li:cost=math.gcd(ai,cost)
        ans.append(cost)
    print(f'Case #{case}:',' '.join(str(i) for i in ans))
