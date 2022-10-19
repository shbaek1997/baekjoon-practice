# 그니까 대각선이 가로/세로 보다 짧으면 짝수 이동은 전부 대각선 두개로 해야함
# 홀수라면 무조건 가로 세로 이동이 강제됨
# 만약에 가로+세로가 대각선보다 작다면 다 가로 세로 하는것이 맞음 => 항상 가능
# 만약에 가로+세로가 대각선보다 크면
# 예로 대각:1 가로 세로 10 이면
# 무조건 최대한 대각 후, 짝수 개수는 대각선 두개로 이동 후, 1개를 그냥 감
x, y, w, s = map(int, input().split())
if s >= 2*w:  # 만약 대각선이 두 번 가로 세로 보다 크다면 전부 가로 세로
    ans = x*w+y*w
else:  # 대각선이 걍 항상 w보다도 작으면 전부 대각선, 아니면 가로 세로
    ans = 0
    big_no = max(x, y)
    small_no = min(x, y)
    ans += small_no*s
    remainder = big_no-small_no
    if w < s:
        ans += remainder*w
    elif remainder % 2 == 0:
        ans += remainder*s
    else:
        ans += (remainder-1)*s
        ans += w

print(ans)
