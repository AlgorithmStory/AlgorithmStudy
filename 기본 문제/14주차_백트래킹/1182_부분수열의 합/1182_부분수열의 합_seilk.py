```python
from sys import stdin
n, s = map(int, stdin.readline().split())
series = list(map(int, stdin.readline().split())) #전체 수열 list 생성
dp = [[] for i in range(n)] #series와 index가 서로 대응하는 dp 생성 (dp[i] == series[i]에서 가능한 부분수열들)
count = 0 #S와 같은 값 count initialization

if series[0] == s: #series의 시작 값이 s일 수 있음
    count += 1
dp[0].append(series[0])

for i in range(1, n):
    if series[i] == s: #series의 시작 값이 s일 수 있음
        count += 1
    dp[i].append(series[i])

    for j in dp[i - 1]: 
        dp[i].append(j) #i보다 한칸 뒤에 있는 수열 합을 모두 dp[i]에 넣어줌
                        #j에 있는 값들은 s와 같은지 아닌지 이미 한 단계 전에 파악했으므로 조건문 불필요

    for j in dp[i - 1]: #i보다 한칸 뒤에 있는 수열 합과 i번째 숫자를 더한 값을 dp[i]에 넣어줌
        if j + series[i] == s: #i보다 한칸 뒤에 있는 수열합과 i번째 숫자를 더한 합이 s가 되는지 확인
            count += 1 
        dp[i].append(j + series[i]) #마찬가지로 dp에 전부 넣어줌

print(count)
```
