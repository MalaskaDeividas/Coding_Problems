


H,W = map(int,input().split())
g = [input().rstrip() for _ in range(H)]
dq = deque(); dist = [[-1]*W for _ in range(H)]
# dq.append((sr,sc)); dist[sr][sc]=0
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
while dq:
    r,c = dq.popleft()
    for dr,dc in dirs:
        nr,nc = r+dr, c+dc
        if 0<=nr<H and 0<=nc<W and g[nr][nc] != '#' and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            dq.append((nr,nc))
