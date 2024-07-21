def bsort(g):
    n = len(g)
    for i in range(n-1 , 0, -1):
        for j in range(i):
            if g[j]>g[j+1]:
                t = g[j]
                g[j] = g[j+1]
                g[j+1] = t
    for i in g:print(i,sep="")
s = int(input())
g = list(map(int, input().split()))
bsort(g)
