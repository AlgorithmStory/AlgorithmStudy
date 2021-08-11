# 입력.
n,m = map(int, input().split(" "))
trees_arr = list(map(int, input().split(" ")))

# 내림차순 정렬.
trees_arr.sort(reverse=True)

# 가장 높은 나무의 높이.
max_height = trees_arr[0]

# 초기 전기톱 위치.
saw_height = 0

# 첫번쨰 while 이후로 한번더 연산이 필요한지 확인 하기 위한 변수.
check = 0
while True:
    # 자를 수 있는 나무중, 잘린 값을 합을 구함.
    cut_lenght = 0
    for tree in trees_arr:
        if tree > saw_height:
            cut_lenght += tree - saw_height
        else:
            break
            
    # 잘린 나무의 합이, 가져가야하는 나무의 합보다 크다면,
    if cut_lenght > m:
        # 가장 높은 나무의 1/3 높이만큼 전기톱 위치에서 더해주면서 반복.
        saw_height += int(max_height / 3)
    # 그게 아니라, 잘린 나무의 합이 가져가야하는 나무의 합보다 작아지면 break.
    elif cut_lenght <= m:
        if cut_lenght == m: # 딱 맞아 떨어지면 check는 1로 바꾸고 break.
            check = 1
        break

# 딱 맞아떨어진게 아니라면, 전기톺의 높이를 조금씩 줄여주면서, 가져갈수있는 최소 값을 구함.
if check != 1:
    while True:
        cut_lenght = 0
        for tree in trees_arr:
            if tree > saw_height:
                cut_lenght += tree - saw_height
            else:
                break
        if cut_lenght >= m:
            break
        else:
            saw_height -= 1

# 출력.
print(saw_height)
