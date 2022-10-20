from collections import deque
import sys
input = sys.stdin.readline
# input for n,l,r
n, l, r = map(int, input().split())

#


def bfs(x, y):
    if not visited[y][x]:
        coordinates = []  # 좌표를 보관
        values = []  # 좌표의 값을 보관
        # 시작점을 큐에 추가 후 방문 처리
        q.append((y, x))
        visited[y][x] = 1
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        while q:
            y, x = q.popleft()
            # 방문했던 점의 좌표 정보 저장
            coordinates.append((y, x))
            values.append(grid[y][x])
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                # 상하좌우 불가능 하면 무시하고 continue
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                # 가능한 좌표일 때 차이값 계산
                diff = abs(grid[y][x]-grid[ny][nx])
                # 차이값 조건이 성립하면
                if diff >= l and diff <= r and not visited[ny][nx]:
                    # 새좌표를 큐에 추가 이후 방문처리
                    q.append((ny, nx))
                    visited[ny][nx] = 1
        # bfs 탐색으로 여러 좌표를 탐색 종료 후, 새롭게 공유될 인구 수 계산
        value = sum(values)//len(values)
        # 인구수 계산값으로 새 Grid 생성
        for (y, x) in coordinates:
            new_grid[y][x] = value


# 처음 Grid 입력
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
# 총 인구 이동 수를 기록할 cnt
cnt = 0
while True:
    # new grid, visited, q 변수 초기화
    new_grid = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    q = deque([])
    # grid에 bfs를 실행
    for i in range(n):
        for j in range(n):
            bfs(i, j)
    # bfs 실행 후, new_grid가 grid와 같지 않다면 인구 이동이 있다는 것
    if new_grid != grid:
        # 정답에 1추가 이후, grid를 새로 만든 new_grid로 변경
        cnt += 1
        grid = new_grid
        # 같다면, 인구이동이 없었으므로 cnt를 출력 후, loop 탈출
    else:
        print(cnt)
        break
