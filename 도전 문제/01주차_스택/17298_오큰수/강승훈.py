# 이렇게 풀면, 단순 for문으로 풀었을때보다 공간복잡도가(stact에 이전 값을 저장하니까) "약간" 증가하는 대신,
# 시간복잡도가 "획기적"으로 줄어듬.
# ---------------------------------------------------------------------------------
n = int(input())
arr = list(map(int, input().split(" ")))
stact = []
result = []

# 뒤에서부터 탐색함.
for i in range(1, n+1):
    while True:
        if len(stact) == 0: # 첨엔 이게 실행 됨.
            result.append("-1")
            stact.append(arr[-i]) # 여기에 값을 넣으면서, 추후에 있을 탐색 원소들에 대해서 비교할거임.
            break
        else:
            if arr[-i] < stact[-1]: # 첨에 실행되는 if문이랑 논리적으로 똑같음.
                result.append(str(stact[-1]))
                stact.append(arr[-i])
                break
            elif arr[-i] >= stact[-1]: # 탐색하는 요소가 stact.top 값보다 크거나 같으면, 버리고, while loop 계속 돔.
                stact.pop()


# result에저장하면서, 기댓값과 반대로 저장되기 때문에, 단순히 뒤집어 주는거.
result2 = ""
for i in range(1, n+1):
    result2 += result[-i]
    if i != n:
        result2 += " "
print(result2)




