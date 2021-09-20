N, S = map(int, input().split())
nums = list(map(int, input().split()))

def dfs(idx, cur):
    if idx == N:
        if cur == S:
            global answer
            answer += 1
    else:
        dfs(idx + 1, cur)
        dfs(idx + 1, cur + nums[idx])

if S != 0: answer = 0
else: answer = -1
dfs(0, 0)
print(answer)
