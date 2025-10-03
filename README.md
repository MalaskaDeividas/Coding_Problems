# Coding_Problems

# get all built in functions
import builtins
[name for name in dir(builtins) if callable(getattr(builtins, name))]

# String methods
print(dir(str))

# List methods
print(dir(list))

# Dictionary methods
print(dir(dict))

# Set methods
print(dir(set))

# Fast I/O & basics
import sys, math, heapq, bisect
from collections import deque, defaultdict, Counter
input = sys.stdin.readline
# sys.setrecursionlimit(1_000_000)


"""
NCPC PYTHON CHEATSHEET (COPY-PASTE)
Fast I/O & basics, BFS grid (4-dir), Dijkstra (weighted), DSU/Union-Find, Binary Search on answer

=====================
FAST I/O & BASICS
=====================
- Use sys.stdin.readline for faster input. Collect outputs and print once.
- Common imports you’ll likely need in NCPC.

    import sys, math, heapq, bisect
    from collections import deque, defaultdict, Counter
    input = sys.stdin.readline
    # sys.setrecursionlimit(1_000_000)   # Uncomment if you use deep recursion

- Fast output pattern:
    out = []
    # out.append(str(value))
    # print("\n".join(out))

=====================
BFS (GRID, 4-DIR)
=====================
- Typical shortest steps on unweighted grid with walls '#'.
- dist[r][c] == -1 means unvisited.

    H, W = map(int, input().split())
    grid = [input().rstrip("\n") for _ in range(H)]
    dist = [[-1]*W for _ in range(H)]
    sr, sc = 0, 0       # set start
    dq = deque([(sr, sc)])
    dist[sr][sc] = 0
    DIRS = [(1,0),(-1,0),(0,1),(0,-1)]
    while dq:
        r, c = dq.popleft()
        for dr, dc in DIRS:
            nr, nc = r+dr, c+dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#' and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                dq.append((nr, nc))
    # dist[r][c] gives shortest steps, -1 if unreachable.

=====================
DIJKSTRA (WEIGHTED GRAPH)
=====================
- For nonnegative edge weights. If edges are 0/1, consider 0-1 BFS.
- G[u] = list of (v, w). If directed, only push one direction.

    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        # If input is 1-indexed: u -= 1; v -= 1
        G[u].append((v, w))
        G[v].append((u, w))  # remove this if graph is directed

    INF = 10**18
    dist = [INF]*N
    start = 0
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in G[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    # dist[i] is shortest distance from start to i.

=====================
DSU / UNION-FIND
=====================
- Supports merging sets and checking connectivity in near O(α(N)).
- Path compression + union by size/rank.

    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
            self.sz = [1]*n
            self.cc = n  # number of connected components (optional)

        def find(self, x):
            while x != self.p[x]:
                self.p[x] = self.p[self.p[x]]
                x = self.p[x]
            return x
            # Alternatively (recursive):
            # if self.p[x] != x:
            #     self.p[x] = self.find(self.p[x])
            # return self.p[x]

        def union(self, a, b):
            a = self.find(a); b = self.find(b)
            if a == b:
                return False
            if self.sz[a] < self.sz[b]:
                a, b = b, a
            self.p[b] = a
            self.sz[a] += self.sz[b]
            self.cc -= 1
            return True

        def same(self, a, b):
            return self.find(a) == self.find(b)

    # Usage:
    # dsu = DSU(n)
    # dsu.union(u, v)
    # dsu.same(u, v)

=====================
BINARY SEARCH ON ANSWER
=====================
- Use when the predicate is monotone over an integer range.
- Convention below finds the MINIMUM x such that ok(x) is True.

    def ok(x):
        # Return True if x is feasible under problem constraints
        return True

    lo, hi = 0, 10**18    # set bounds to problem range
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid          # feasible -> try smaller
        else:
            lo = mid + 1      # infeasible -> try larger
    ans = lo
    # For MAXIMUM x such that ok(x) is True: switch to:
    # while lo < hi:
    #     mid = (lo + hi + 1) // 2
    #     if ok(mid): lo = mid
    #     else: hi = mid - 1

=====================
TIPS & PITFALLS
=====================
- Carefully handle 0/1 indexing from input.
- For big input: avoid per-line prints; batch output.
- Edge cases: empty sets, N=0/1, all equal, already sorted, negatives.
- If T test cases: wrap logic in a loop and re-init per test.
- For grids: beware newline/whitespace; use rstrip().
"""

