for case in range(1,int(input())+1):
    n=int(input())
    l=list(map(int,input().split()))
    if n<4:
        print(f'Case #{case}: {n}')
        continue
    i=0
    long=3
    while i<n-1:
        d=l[i+1]-l[i]
        j=i+1
        while j<n-1 and l[j+1]-l[j]==d:j+=1
        if j<n-2 and l[j+2]-l[j]==2*d:
            k=j+2
            while k<n-1 and l[k+1]-l[k]==d:k+=1
            long=max(long,k-i+1)
            #print('A',i,j,k)
        elif i>1 and l[i]-l[i-2]==2*d:
            long=max(long,j-i+3)
            #print('B',i,j)
        else:
            long=max(long,min(n,j-i+2))
            #print('C',i,j)
        i=j
    print(f'Case #{case}: {long}')
