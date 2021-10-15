# 입력.
s = input()

# 반복문을 돌면서 상황에 따라 i가 유동적으로 값이 변해야 하기 때문에 for가 아니라 while을 사용.
result = 0
i = 0
while i < len(s):
    if i < len(s)-2 and s[i] == "c" and s[i+1] == "h" and s[i+2] == "u":
        i += 3
        continue
    elif (i < len(s)-1 and s[i] == "p" and s[i+1] == "i") or (i < len(s)-1 and s[i] == "k" and s[i+1] == "a"):
        i += 1
    else:
        result = 1
        break
    i += 1

# 출력.
if result == 0:
    print("YES")
else:
    print("NO")
