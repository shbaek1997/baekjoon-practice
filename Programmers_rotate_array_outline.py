def solution(rows, columns, queries):
    ans = []
    grid = [[0]*columns for _ in range(rows)]
    for i in range(rows*columns):
        grid[i//columns][i % columns] = i+1
    for q in queries:
        b = q[0]-1  # index
        l = q[1]-1
        t = q[2]-1
        r = q[3]-1
        length = t-b+1+r-l+1
        length = length*2-4
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        last_item = grid[b+1][l]
        prev = grid[b][l]
        x = l
        y = b
        min_num = 100001
        for i in range(1, length+1):
            if x < r and y == b:
                x += 1
            elif x == r and y < t:
                y += 1
            elif y == t and x > l:
                x -= 1
            elif x == l and y > b:
                y -= 1
            curr = grid[y][x]
            min_num = min(curr, min_num)
            prev, curr = curr, prev
            grid[y][x] = curr
        ans.append(min_num)
    return ans
