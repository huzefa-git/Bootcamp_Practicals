def belmanford():
    d = {0:[(1,-1),(2,4)],1:[(2,3),(3,2),(4,2)],2:[],3:[(2,5),(1,1)],4:[(3,-3)]}
    n =5
    dist = [999]*n
    start = 0
    dist[start]=0
    for v in d:
        for v2,w2 in d[v]:
            if dist[v]!=999 and dist[v]+w2<dist[v2]:                                             
                dist[v2] = dist[v]+w2
    print(dist)
belmanford()