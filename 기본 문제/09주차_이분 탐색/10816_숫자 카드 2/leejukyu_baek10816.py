import sys
n = int(input())
a = [x for x in sys.stdin.readline().split()]
m = int(input())
b = [x for x in sys.stdin.readline().split()]
dic = {}

for i in a:                                         # 비교리스트
    if i in dic:                                    # 딕셔너리에 있는 값이면
        dic[i] += 1                                 # 카운트 +1
    else:                                           # 없으면
        dic[i] = 1                                  # 새로 넣어줌

for j in b:                                         # 검증리스트가
    if j not in dic:                                # 딕셔너리에 없으면
        print(0, end = " ")                         # 0
    else:                                           # 있으면
        print(dic[j], end = " ")                    # 개수 프린트