import sys

numbers_of_tests = int(sys.stdin.readline().split()[0])                 # 테스트의 개수

for i in range(numbers_of_tests):                                       # 테스트의 개수 만큼
    test = list(map(int, sys.stdin.readline().split()))                 # 해당 테스트의 문서 개수 N, 알고싶은 문서 숫자 M
    importance = list(map(int, sys.stdin.readline().split()))           # 각 문서들의 중요도
    wanted_print = [test[1], importance[test[1]]]                       # 원하는 문서 [M, 중요도]
    test_cases = []                                                     # 각 문서 리스트 [인덱스, 중요도]

    for j in range(test[0]):                                            # N 만큼
        test_cases.append([j, importance[j]])                           # 문서 리스트에 문서 추가

    # 현재 문서 리스트의 첫번째 프린트가 원하는 프린트이면서 그걸 인쇄해야하는 상황이 아닐때
    while test_cases[0] != wanted_print or wanted_print[1] != max(test_cases, key=lambda x: x[1])[1]:
        if test_cases[0][1] == max(test_cases, key=lambda x: x[1])[1]:  # 만약 리스트의 첫 프린트를 인쇄해야하면
            test_cases.pop(0)                                           # 리스트에서 그냥 제거
        else:                                                           # 만약 리스트의 첫 프린트를 인쇄하는게 아니면
            test_cases.append(test_cases[0])                            # 첫 프린트를 마지막으로 이동
            test_cases.pop(0)                                           # -
    
    # while 문을 빠져나오면 원하는 문서가 출력된다는 의미 
    print(test[0] - len(test_cases) + 1)                                # N - 현재 남은 프린트 개수 + 1 출력                     
