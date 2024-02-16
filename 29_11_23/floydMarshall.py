n=4
def floyds(G):
    distance = G
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j],distance[i][k]+distance[k][j])
    
    print(distance)
g = [[0,9,-4,999],[6,0,999,2],[999,5,0,999],[999,999,1,0]]
floyds(g)