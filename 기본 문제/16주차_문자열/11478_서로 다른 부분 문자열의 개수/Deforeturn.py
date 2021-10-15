# 입력.
s = input()

# 중복되면 안되기때문에, 가능한 모든 조합을 set에 다 담음.
result_cnt = set()
for i in range(len(s)+1):
    for j in range(len(s)-i):
        result_cnt.add(s[j:j+i+1])

# 출력.
print(len(result_cnt))
