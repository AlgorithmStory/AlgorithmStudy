N = input().split('-')                  # - 로 나눠주기

plus = 0
minus = 0
num = len(N)

for i in range(num):                    # 나눠준 문자열 길이 만큼 반복
    if i != 0:                          # 양수에 들어가야하는 문자열이 아니면
        for j in N[i].split('+'):       # 문자열 안에서 +로 분리하고
            minus += int(j)             # 숫자 값은 전부 마이너스에 넣기
    else:
        for j in N[i].split('+'):       # 첫번째 문자열만 + 로 분리하고
            plus += int(j)              # 양수값으로 다 넣기

print(plus-minus)                       # 양수값 - 음수값