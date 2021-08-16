import sys


def do_something(input_paper):              # 종이를 사분할 할지 말지 정하는 메소드
    prev = input_paper[0][0]                # 확인용 첫지점의 색

    for i in input_paper:                   # 종이 순회
        for j in i:                         # -
            if prev != j:                   # 만약 각 점의 색이 다른게 있으면
                first_quarter = []          # 사분할 할 종이들
                second_quarter = []         # -
                third_quarter = []          # -
                fourth_quarter = []         # -
                # 종이를 사분할
                for i in range(len(input_paper) // 2):
                    first_quarter.append(input_paper[i][:len(input_paper[i]) // 2])
                    second_quarter.append(input_paper[i][len(input_paper[i]) // 2:])
                for i in range(len(input_paper) // 2, len(input_paper)):
                    third_quarter.append(input_paper[i][:len(input_paper[i]) // 2])
                    fourth_quarter.append(input_paper[i][len(input_paper[i]) // 2:])
                # 사분할 된 종이에 대해 다시 메소드 실행
                do_something(first_quarter)
                do_something(second_quarter)
                do_something(third_quarter)
                do_something(fourth_quarter)
                return                      # 실행 했으므로 메소드 종료

    answer[input_paper[0][0]] += 1      # for 문을 빠져나왔으면 종이 색이 하나라는 뜻이므로 해당 색에 해당하는 정답 하나 추가
    return                              # 메소드 종료


M = int(sys.stdin.readline().split()[0])    # 종이 크기 읽어옴
paper = []                                  # 종이
answer = [0, 0]                             # 정답 [파란색, 하얀색]

for _ in range(M):                          # 종이 색깔 읽어옴
    input_lines = list(map(int, sys.stdin.readline().split()))
    paper.append(input_lines)

do_something(paper)                         # 메소드 실행

for i in answer:                            # 정답 출력
    print(i)
