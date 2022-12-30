#NO.11053 가장 긴 증가하는 부분 수열
n = int(input())
array = list(map(int,input().split()))
dp = [1]*n

for i in range(n) :
    for j in range(i) :
        if array[i] > array[j] :
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

# 첫번째 인덱스부터 수열의 길이의 최댓값을 저장해 나간다.
# 수열 a = {10, 20, 10, 30, 20, 50}이 있을때, 4번째 숫자(30)까지의 
# 수열의 길이의 최댓값을 구해보자.
# 첫번째 숫자부터 검사를 해 나간다.
# 자기 자신(30)보다 작은 숫자들 중 가장 큰 길이를 구하고 그 길이에 +1을 하면 된다.