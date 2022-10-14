import sys
from collections import deque
input = sys.stdin.readline
t = int(input())


def bfs(locations, n):
    q.append(locations[0])
    visited[0] = True
    while q:
        prev = q[0]
        for i in range(0, n+2):
            distance = abs(locations[i][0]-prev[0]) + \
                abs(locations[i][1]-prev[1])
            if not visited[i] and distance <= 1000:
                q.append(locations[i])
                visited[i] = True
        q.popleft()


ans = []
for i in range(t):
    n = int(input())
    locations = []
    q = deque([])
    for i in range(n+2):
        locations.append(list(map(int, input().split())))
    visited = [False]*(n+2)
    bfs(locations, n)
    if visited[-1]:
        ans.append('happy')
    else:
        ans.append('sad')
print(*ans)
