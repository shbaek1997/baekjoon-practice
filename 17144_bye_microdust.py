import sys

input = sys.stdin.readline
R, C, T = map(int, input().split())
grid = []
for i in range(R):
    grid.append(list(map(int, input().split())))

# -1이거나 index가 밖이면 확산 x
# 확산양은 x//5 만큼 (4방향으로)
# 확산 후 양은 원래 양 - x//5*확산된 방향만큼
# 다음 grid를 empty하게 만들어 놓고, 거기에 -와 +를 추가해서 그전과 더하는 식이 맞을듯?


def diffusion_single(x, y):  # 각 미세먼지가 분산하는 것을 +,-로 계산하는 함수, 각 위치마다 해야함
    amount = grid[y][x]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    if amount > 0:
        count = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny >= 0 and ny < R and nx >= 0 and nx < C and grid[ny][nx] != -1:
                empty_grid[ny][nx] += amount // 5
                count += 1
        empty_grid[y][x] -= count * (amount // 5)


# 분산 시킨 후, 결과물을 만드는 식
def diffusion(grid):
    for i in range(R):
        for j in range(C):
            diffusion_single(j, i)
    for i in range(R):
        for j in range(C):
            grid[i][j] += empty_grid[i][j]
    return grid

# 처음 -1이 나오면 반시계로 그 줄들만 회전 (4개의 줄)
# 두번째 -1에서 시계 회전, 모든 수를 1칸씩 이동, -1은 원래 위치로 (왜냐면 청정기로 간 미세먼지는 정화됨)


def anti_clock(pos_x, grid):
    top_part = []
    test_grid = grid[:pos_x + 1]  # 윗부분까지
    for i in range(pos_x):  # 0,0,-1 부분
        top_part.append(test_grid[i][0])
    for i in range(C):
        top_part.append(test_grid[pos_x][i])
    for i in range(pos_x - 1, -1, -1):
        top_part.append(test_grid[i][-1])
    for i in range(C - 2, 0, -1):
        top_part.append(test_grid[0][i])

    test_grid[0][0] = top_part[-1]
    idx = 0
    for i in range(1, pos_x):
        test_grid[i][0] = top_part[idx]
        idx += 1
    for i in range(C):
        test_grid[pos_x][i] = top_part[idx]
        idx += 1
    for i in range(pos_x - 1, -1, -1):
        test_grid[i][-1] = top_part[idx]
        idx += 1
    for i in range(C - 2, 0, -1):
        test_grid[0][i] = top_part[idx]
        idx += 1
    test_grid[-1][0] = -1
    test_grid[-1][1] = 0
    return test_grid


def clock(pos_x, grid):
    bottom_grid = grid[pos_x + 1:]
    bottom_part = []
    for i in range(R - pos_x - 2, -1, -1):
        bottom_part.append(bottom_grid[i][0])
    for i in range(1, C):
        bottom_part.append(bottom_grid[0][i])
    for i in range(1, R - pos_x - 1):
        bottom_part.append(bottom_grid[i][-1])
    for i in range(C - 2, 0, -1):
        bottom_part.append(bottom_grid[-1][i])

    bottom_grid[-1][0] = bottom_part[-1]
    idx = 0
    for i in range(R - pos_x - 3, -1, -1):
        bottom_grid[i][0] = bottom_part[idx]
        idx += 1
    for i in range(1, C):
        bottom_grid[0][i] = bottom_part[idx]
        idx += 1
    for i in range(1, R - pos_x - 1):
        bottom_grid[i][-1] = bottom_part[idx]
        idx += 1
    for i in range(C - 2, 0, -1):
        bottom_grid[-1][i] = bottom_part[idx]
        idx += 1
    bottom_grid[0][0] = -1
    bottom_grid[0][1] = 0
    return bottom_grid


def new_grid(pos_x, grid):
    top = anti_clock(pos_x, grid)
    bottom = clock(pos_x, grid)
    total = top + bottom
    return total


for i in range(T):
    empty_grid = [[0] * C for _ in range(R)]
    new_grid = diffusion(grid)
    for i in range(R):
        if new_grid[i][0] == -1:
            pos_x = i
            break
    top = anti_clock(pos_x, grid)
    bottom = clock(pos_x, grid)
    total = top + bottom
    sum = 0
    for l in total:
        for i in l:
            sum += i
    sum += 2
    grid = total
print(sum)
