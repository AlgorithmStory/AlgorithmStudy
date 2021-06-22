import sys


def decomposed_sum(input):                              # input의 분해합을 구하는 함수
    answer = input                                      # return할 answer
    for i in str(input):                                # string으로 바꾼뒤 for문을 돌려 한 자리씩 읽음
        answer += int(i)                                # 읽은 string을 다시 int로 바꿔서 answer에 더함
    return answer                                       # 구한 분해합을 반환


def find_answer():                                      # 정답을 찾기 위한 함수
    number = int(sys.stdin.readline().split()[0])       # 자연수 N을 읽어옴
    for i in range(int(number / 2), number):            # 시간을 줄일려고 N의 절반 부터 for 루프 시작
        if(decomposed_sum(i) == number):                # 위의 함수로 찾아낸 분해합이 N이면
            return i                                    # 정답 반환 후 함수 종료
    return 0                                            # 정답이 안나오면 0 반환


print(find_answer())                                    # 정답 출력
