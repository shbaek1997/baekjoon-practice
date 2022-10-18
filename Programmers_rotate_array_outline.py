def solution(rows, columns, queries):
    # 답을 담을 ans 배열
    ans = []
    # rows, columns로 기본 배열 생성
    grid = [[0]*columns for _ in range(rows)]
    for i in range(rows*columns):
        grid[i//columns][i % columns] = i+1

    # 문제 해결
    for q in queries:
        b = q[0]-1  # y-index low
        l = q[1]-1  # x-indx low
        t = q[2]-1  # y-index high
        r = q[3]-1  # x-index high

        # 테두리의 둘레 계산
        length = t-b+1+r-l+1
        length = length*2-4

        # 전의 값 기록
        prev = grid[b][l]
        # 처음으로 사용할 x,y 값
        x = l
        y = b
        # 움직이는 숫자 중 가장 작은 숫자를 찾기 위한 변수 설정
        min_num = 100001
        # 테두리 길이 만큼 반복
        for i in range(1, length+1):
            # 인덱스 값 변경
            # 오른쪽으로 이동
            if x < r and y == b:
                x += 1
            # 아래로 이동
            elif x == r and y < t:
                y += 1
            # 왼쪽으로 이동
            elif y == t and x > l:
                x -= 1
            # 위로 이동
            elif x == l and y > b:
                y -= 1
            # 현재값 확인
            curr = grid[y][x]
            # 최솟값 업데이트
            min_num = min(curr, min_num)
            # 직전 값과 현재 값 교환
            prev, curr = curr, prev
            grid[y][x] = curr
        ans.append(min_num)
    return ans
