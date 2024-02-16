import heapq
def dikjshitra():
    d = {0:[(1,1),(2,4)],1:[(3,2),(2,3),(4,2)],2:[],3:[(1,1),(2,5)],4:[(3,3)]}
    shortest = {}
    start = 0
    heap = [[0,start]]
    while heap:
        w,v = heapq.heappop(heap)
        if v in shortest:
            continue
        shortest[v] = w
        for v2,w2 in d[v]:
            if v2 not in shortest:
                heapq.heappush(heap,[w+w2,v2])
    print(shortest)
dikjshitra()