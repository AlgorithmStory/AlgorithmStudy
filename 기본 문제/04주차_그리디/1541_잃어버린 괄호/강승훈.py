# 입력.
math_ex = input()

ex_len = len(math_ex)
plus_sum = 0 # 양의 수를 담을 변수.
minus_sum = 0 # 음의 수를 담을 변수.
sub_number = "" # 각각의 수에 대해서 잠깐 저장 할 변수.
turn = 1 # 컨트롤러

# 입력 받은 문자열에 대해서 순차 탐색.
for i in range(ex_len):

    # 숫자면 일단 sub_number에 문자열로 담아둠.
    if math_ex[i] != "-" and math_ex[i] != "+":
        sub_number += math_ex[i]
        # 숫자가 담겼을때, 인덱스의 마지막이면 밑에 조건문 마저 실행됨. (그게 아니면 밑에 무시.)
        if i != ex_len-1:
            continue

    # 처음 숫자가 아닌게 감지가 되면, turn에 의해서 이게 실행됨.
    if turn == 1 or (math_ex[i] == "+" and turn != 0):
        # 만약 감지 된게 "-"라면 turn을 0으로 바꿔주고 영원히 23~28줄 조건문을 실행시키지 않음.
        if math_ex[i] == "-":
            turn = 0
        plus_sum += int(sub_number) # 양의 변수에 담고,
        sub_number = "" # 잠시 저장하는 변수는 초기화.

    # 만약 "-"가 한번이라도 감지된 적이 있다면, 계속 이게 실행되면서, 음의 수를 담는 변수에 저장.
    elif i == ex_len - 1 or turn == 0:
        minus_sum += int(sub_number)
        sub_number = ""

# 출력
print(plus_sum-minus_sum)
