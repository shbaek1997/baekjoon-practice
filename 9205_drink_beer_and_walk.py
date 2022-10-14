import sys
from collections import deque
input = sys.stdin.readline
t = int(input())


def bfs(locations, n):
    q.append(locations[0])
    visited[0] = True
    while q:
        prev = q[0]
        for i in range(0, n+2):  # 전체 배열 확인
            distance = abs(locations[i][0]-prev[0]) + \
                abs(locations[i][1]-prev[1])
            if not visited[i] and distance <= 1000:  # 길이를 계산 후, 방문한적이 없고 길이가 가능하면
                # q에 추가
                q.append(locations[i])
                # 방문처리
                visited[i] = True
        q.popleft()


ans = []
# 입력을 받기
for i in range(t):
    n = int(input())
    # q와 location 초기화
    locations = []
    q = deque([])
    # locations 추가
    for i in range(n+2):
        locations.append(list(map(int, input().split())))
    # 방문기록 초기화
    visited = [False]*(n+2)
    # bfs 실행
    bfs(locations, n)
    # 마지막 장소가 방문처리 되었다면 happy 아니면 sad 출력
    if visited[-1]:
        print('happy')
    else:
        print('sad')
