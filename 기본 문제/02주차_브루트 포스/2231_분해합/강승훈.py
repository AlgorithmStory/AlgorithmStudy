n = int(input())
result = 0
for i in range(1, n+1): # i를 매번 1씩 증가시킴. 이걸 이용해서 해결
    sum = i
    str_sub = str(i)
    for crnt in str_sub: # i의 자릿수를 다 더함.
        sum += int(crnt)
    if sum == n: # 다 더한게, 구하고자 하는 n값이랑 같으면 바로 break
        result = i
        break
print(result)