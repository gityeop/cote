import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a = int(input())
    dp = [0]*(a+1)
    try:
        dp[1]=1
        dp[2]=1
        dp[3]=1
        dp[4]=2
    except:
        pass
    if a < 5:
        print(dp[a])
    else:
        for i in range(5, a+1):
            dp[i] = dp[i-1] + dp[i-5]
        print(dp[a])