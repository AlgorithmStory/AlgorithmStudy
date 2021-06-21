import sys


def find_answer():                                                                              # 원하는 카드들을 찾는 함수
    count = sys.stdin.readline().split()                                                        # 카드 갯수와 원하는 수 배열
    numbers = sys.stdin.readline().split()                                                      # 카드 숫자 배열
    answer = 0                                                                                  # 예비용 답
    for i in range(int(count[0])):                                                              # 카드 숫자 배열을
        numbers[i] = int(numbers[i])                                                            # int 자료형으로 변환
    for i in range(len(numbers) - 2):                                                           # 3중 for문 사용
        for j in range(i + 1, len(numbers) - 1):                                                # --
            for k in range(j + 1, len(numbers)):                                                # --
                now = numbers[i] + numbers[j] + numbers[k]                                      # 3개 뽑은걸 계산
                if now == int(count[1]):                                                        # 원하는 수와 같으면
                    return (now)                                                                # 그거 반환하고 바로 종료
                elif int(count[1]) - (now) < int(count[1]) - answer and now < int(count[1]):    # 같은 건 아닌데 이전 예비 답보다 좀 더 가까운 수 일때
                    answer = now                                                                # 예비 답에 저장 후 다음 번 뽑은 수들과 비교
    return (answer)                                                                             # 원하는 수가 안나왔으면 예비 답을 반환


print(find_answer())                                                                            # 위의 함수 실행
