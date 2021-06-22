import sys


def decomposed_sum(input):                              # input의 분해합을 구하는 함수
    answer = input                                      # return할 answer
    while input > 0:                                    # input의 각자리 수를 구하기위한 while문
        answer += int(input % 10)                       # answer에 각자리 수를 넣어줌
        input = int(input / 10)                         # 다음 자리 수를 구하기 위해 10으로 나눔
    return answer                                       # 구한 분해합을 반환


def find_answer():                                      # 정답을 찾기 위한 함수
    number = int(sys.stdin.readline().split()[0])       # 자연수 N을 읽어옴
    half = int(number / 2)                              # 시간을 줄일려고 N의 절반 부터 for 루프 시작
    for i in range(half, number):                       # --
        if(decomposed_sum(i) == number):                # 위의 함수로 찾아낸 분해합이 N이면
            return(i)                                   # 정답 반환 후 함수 종료
    return 0                                            # 정답이 안나오면 0 반환

print(find_answer())                                    # 정답 출력