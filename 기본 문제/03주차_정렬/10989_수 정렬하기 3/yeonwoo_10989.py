import sys
N = int(sys.stdin.readline())
count_N = [0] * 10001 
# count_N 은 둘째줄부터 주어지는 숫자가 N보다 작은수가 아닌 10000보다 작거나 같아
# 0~10000까지 값을 넣어주기 위해 길이가 10001인 0배열 만듦


for i in range(N):
    count_index = int(sys.stdin.readline())
    count_N[count_index] = count_N[count_index] + 1 
    # count_index로 count_N에 해당하는 인덱스 값에 +1 해줌
    # 만약에 1 1 3 5로 받아오면
    # count_N[1] = 1 count_N[1] = 2 count_N[3] = 1 count_N[5] = 1
    # 즉 count_N[count_index]에 해당하는 값이 각 count_index값의 받아온 횟수가 됨

for count_index in range(10001):
    # 자연수가 10000보다 작거나 같은수라 10001지정
    # len(count_N)해도 상관 X
    for j in range(count_N[count_index]):
        # 위에서 설명햐였듯이 count_N[count_index]는 count_index를 받아온 횟수
        print(count_index)

# print(count_N)