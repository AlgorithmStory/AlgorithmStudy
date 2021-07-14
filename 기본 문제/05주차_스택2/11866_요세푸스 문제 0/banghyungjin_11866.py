import sys

numbers = list(map(int, sys.stdin.readline().split()))  # 숫자 배열의 길이 N과 건너뛸 칸 숫자 K를 읽어옴
number_list = []                                        # 1부터 N까지 숫자로 이루어진 배열
index = numbers[1] - 1                                  # 제거할 배열의 인덱스 : 처음에는 K - 1 번째가 제거됨
answer = "<"                                            # 정답 스트링

for i in range(numbers[0]):                             # 1부터 N까지 숫자로 이루어진
    number_list.append(i + 1)                           # 배열 생성

while len(number_list) > 0:                             # 배열에 숫자가 남아있는 동안
    if index < len(number_list):                        # 만약 현재 인덱스가 배열의 크기보다 작아서 그냥 뺄 수 있으면
        answer += str(number_list[index])               # 정답 스트링에 해당 배열 원소를 넣음
        del number_list[index]                          # 배열에서 해당 원소 삭제
        index += numbers[1] - 1                         # 인덱스에 다음 희생자를 위해 K - 1 만큼 더해줌

    else:                                               # 만약 현재 인덱스가 배열의 크기보다 커서 그냥 뺄 수 없으면
        while index >= len(number_list):                # 인덱스가 현재 배열 길이보다 작아질 때까지
            index -= len(number_list)                   # 인덱스에서 현재 배열의 길이를 빼줌
        answer += str(number_list[index])               # 완료되면 위의 if 문과 같음
        del number_list[index]                          # -
        index += numbers[1] - 1                         # -

    if len(number_list) > 0:                            # 아직 배열에 원소가 남아있으면
        answer += ", "                                  # 정답 스트링에 원소 구별용으로 ", "를 추가

answer += ">"                                           # 정답 스트링 마지막 부분 추가
print(answer)                                           # 정답 출력
