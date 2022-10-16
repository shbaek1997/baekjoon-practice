n = int(input())
dp = [0]*1000001
big_no = 1000000000
# n이 양수인 경우 피보나치는 걍 구하고
# n이 음수인 경우 피보나치는 f(i)=f(i-2)+f(i-1) => f(i-2)=f(i)-f(i-1)
# f(i)=f(i+2)-f(i+1)
# 그니까 음수이면 f(-1)+f(-2)=f(0)
# f(-2)=f(0)-f(-1)
# dp[n]=dp[n-2]-dp[n-1]
dp[0] = 0
dp[1] = 1
if n >= 0:
    for i in range(2, n+1):
        dp[i] = (dp[i-1] % big_no+dp[i-2] % big_no) % big_no
else:
    n = abs(n)
    for i in range(2, n+1):
        next_no = dp[i-2]-dp[i-1]
        if next_no > 0:
            dp[i] = next_no % big_no
        else:
            pos_no = abs(next_no) % big_no
            dp[i] = -pos_no
ans = dp[n]
if ans > 0:
    print(1)
elif ans == 0:
    print(0)
else:
    print(-1)
print(abs(ans))
