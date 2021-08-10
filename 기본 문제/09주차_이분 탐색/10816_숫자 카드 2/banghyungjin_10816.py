import sys

_ = int(sys.stdin.readline().split()[0])                    # 안쓰는거 읽어옴
input_list = list(map(int, sys.stdin.readline().split()))   # 첫 리스트 읽어옴
_ = int(sys.stdin.readline().split()[0])                    # 안쓰는거 읽어옴
find_list = list(map(int, sys.stdin.readline().split()))    # 다음 리스트 읽어옴
dictionary = {}                                             # 각 값의 갯수를 같이 저장할 딕셔너리
answer = []                                                 # 답을 저장할 리스트

for i in input_list:                                        # 첫 리스트 순회
    if i not in dictionary:                                 # 딕셔너리에 없는 값이면
        dictionary[i] = 1                                   # 1로 value를 넣어줌
    else:                                                   # 딕셔너리에 있는 값이면
        dictionary[i] += 1                                  # value에 1 더해줌

for i in find_list:                                         # 다음 리스트 순회
    if i in dictionary:                                     # 딕셔너리에 없는 값이면
        answer.append(dictionary[i])                        # 답 리스트에 값 추가
    else:                                                   # 딕셔너리에 없는 값이면
        answer.append(0)                                    # 답 리스트에 0 추가

print(*answer)                                              # 정답 출력
