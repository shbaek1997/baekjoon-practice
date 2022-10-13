# 0,1,2,3방향 4가지가 있고 #북동남서
# 방향이 0일때 왼쪽은 서 3
# 방향이 1일때 왼쪽은 북 0
# 방향이 2일때 왼쪽은 동 1
# 방향이 3일때 왼쪽은 남 2

# 1.현재 위치 청소
# 2.왼쪽 탐색
# 왼쪽이 비었으면 청소 후 다시 1.
# 왼쪽이 차있으면 방향 변경 후 다시 2.
# 다 되어있으면 뒤로 후진 후 다시 2.
# 다 되어있는데 뒤도 막혀있으면 종료
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())

grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))


def clean_1(r, c):
    global ans
    if grid[r][c] == 0:
        grid[r][c] = 2
        ans += 1


def search_left(r, c, mode):
    flag = False  # 왼쪽 회전 시 0이 한번이라도 있다면 true
    # 북 동 남 서
    # mode의 index에서 -1한 index로 dy,dx이동인듯
    # e.g. 동은 북 인덱스로
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    # 1-4를 index에서 빼줌
    for i in range(1, 5):
        new_mode = mode-i
        nx = c+dx[new_mode]
        ny = r+dy[new_mode]
        # 새로운 방향이 음수면 4+ 로 양수로 전환
        if new_mode < 0:
            new_mode += 4
        # 가능한 좌표면
        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            new_point = grid[ny][nx]
            # 첫번째로 0을 발견하면
            if new_point == 0:
                # 새좌표와 새 방향으로 그리고 flag를 true로 설정
                r = ny
                c = nx
                d = new_mode
                flag = True
                # loop을 멈추고
                break
    # 청소할곳을 찾았다면, 새 좌표로 이동 후 청소+ 다시 탐색
    if flag:
        clean_1(r, c)
        search_left(r, c, d)

    else:  # 아니면 뒤를 확인
        search_back(r, c, mode)


def search_back(r, c, mode):
    # 북동남서
    # 남서북동
    # 이 새 nx,ny가 뒤로 후진인것
    dy = [1, 0, -1, 0]
    dx = [0, -1, 0, 1]
    nx = c+dx[mode]
    ny = r+dy[mode]
    # 불가능한 좌표거나
    if nx < 0 or nx >= m or ny < 0 or ny >= n:
        return
    else:
        # 좌표는 가능해도 벽이라면 return
        if grid[ny][nx] == 1:
            return
        # 이동 가능이면 뒤로 후진하고 다시 왼쪽 탐색
        else:
            r = ny
            c = nx
            search_left(r, c, mode)


ans = 0
clean_1(r, c)
search_left(r, c, d)
print(ans)
