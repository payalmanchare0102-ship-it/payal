


INF=9999999
v=6
G=[
    [0,4,0,0,0,2],
    [4,0,6,0,0,3],
    [0,6,0,3,0,1],
    [0,0,3,0,2,0],
    [0,0,0,2,0,4],
    [2,3,1,0,4,0]
]
selected=[False]*v
no_edge=0
selected[0]=True
total_weight=0
print("Edge:Weight\n")
while no_edge<v-1:
    minimum=INF
    x=0
    y=0
    for i in range (v):
        if selected[i]:
            for j in range (v):
                if(not selected[j] and G[i][j]):
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x=i
                        y=j
    print(f"{x}-{y}:{G[x][y]}")
    total_weight += G[x][y]
    selected[y]=True
    no_edge+=1
print("\n Total weight of MST=",total_weight)