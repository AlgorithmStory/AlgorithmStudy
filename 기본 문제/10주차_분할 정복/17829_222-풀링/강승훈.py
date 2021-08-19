from sys import stdin

# 입력.
n = int(stdin.readline())
arr = list(list(map(int, stdin.readline().split(" "))) for _ in range(n))

# arr에 원소가 하나만 남을때까지.
while len(arr[0]) > 1:
    # 다음 arr이 될 변수.
    next_arr = []

    # 인덱스 도는데 필요한 논리 변수.(밑에 만든 bias_1에 관여)
    bias_main = 0

    # 매트릭스가 한번 돌때마다, 한 변의 길이가 반씩 줄어드는 성질을 활용.
    for i in range(len(arr)//2):
        sub_arr = [] # 한 줄에 대한 변수.
        bias_1 = bias_main # 세로 인덱스.
        bias_2 = 0 # 가로 인덱스.

        # 가로 행에 대한 탐색 포문.
        for j in range(len(arr) // 2):

            # 일단 sub_ 라는 배열에 4개의 값을 다 담음.
            sub_ = [arr[bias_1][bias_2], arr[bias_1][bias_2+1], arr[bias_1+1][bias_2+1], arr[bias_1+1][bias_2]]

            # 가장 큰 값 없앰.
            sub_.remove(max(sub_))

            # 그리고 가장 큰 값을 sub_arr에 담음.
            sub_arr.append(max(sub_))

            # 위의 3줄로, 2x2에 대한 4개의 요소 값 구하기 완료.
            bias_2 += 2 # 오른쪽으로 두칸 이동.

        # 세로 인덱스는 안쪽 포문 끝날때마다 2씩 증가.
        bias_main += 2

        # 한줄에 대한 리스트 값을 최종 리스트에 담음.
        next_arr.append(sub_arr.copy())

    # 최종 값 변경.
    arr = next_arr.copy()

# 출력.
print(arr[0][0])
