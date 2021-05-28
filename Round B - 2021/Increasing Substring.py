for case in range(1,int(input())+1):
    n=int(input())
    s=input()
    l=[1]
    for i in range(1,n):
        if s[i]>s[i-1]:l.append(l[-1]+1)
        else:l.append(1)
    print(f'Case #{case}: {" ".join(str(i) for i in l)}')
