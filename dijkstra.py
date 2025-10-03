

N,M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u,v,w = map(int,input().split())
    G[u].append((v,w)); G[v].append((u,w))  # remove if directed
INF = 10**19
dist = [INF]*N; dist[0]=0
pq=[(0,0)]
while pq:
    d,u = heapq.heappop(pq)
    if d!=dist[u]: continue
    for v,w in G[u]:
        nd = d+w
        if nd < dist[v]:
            dist[v]=nd
            heapq.heappush(pq,(nd,v))
