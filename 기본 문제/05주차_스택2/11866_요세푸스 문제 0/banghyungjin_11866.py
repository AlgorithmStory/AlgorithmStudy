import sys

numbers = list(map(int, sys.stdin.readline().split()))  # 숫자 배열의 길이 N과 건너뛸 칸 숫자 K를 읽어옴
number_list = [i for i in range(1, numbers[0] + 1)]     # 1부터 N까지 숫자로 이루어진 배열
index = numbers[1] - 1                                  # 제거할 배열의 인덱스 : 처음에는 K - 1 번째가 제거됨
answer = "<"                                            # 정답 스트링

while len(number_list) > 1:                             # 배열에 숫자가 남아있는 동안
    answer += str(number_list[index]) + ", "            # 정답 스트링에 해당 배열 원소를 넣음
    del number_list[index]                              # 배열에서 해당 원소 삭제
    index += numbers[1] - 1                             # 인덱스에 다음 희생자를 위해 K - 1 만큼 더해줌
    index %= len(number_list)                           # 인덱스가 배열보다 커지는 것을 막기위해 다시 나눠줌

answer += f'{number_list[0]}>'                          # 정답 스트링 마지막 부분 추가
print(answer)                                           # 정답 출력
