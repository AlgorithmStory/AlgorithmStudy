while True:
    
    try:
        N, M = map(int ,input("N과 M값 입력").split())    
    except:
        # except로 제어문 설정 N,M 에 숫자 아닌 값 넣으면
        # 다시 N, M값 입력하라고 만드는 것
        print("N, M은 숫자")
        continue

    if (N < 3 or N > 100) or (M < 10 or M > 300000):
        # 숫자로 받아온 N, M 범위 확인
        print(" N(3 ≤ N ≤ 100), M(10 ≤ M ≤ 300,000)")
        continue

    inp = list(map(int, input().split())) # 리스트 형식으로 받아와줌
# print(inp)
    result = 0
    prt = 0
    for i in range(N): # 0,1,2,3 4
        for j in range(i+1, N): # 1, 2, 3, 4
            for k in range(j+1, N): # 2, 3, 4
                # N = 5, M = 21
                # list = [5 6 7 8 9]일때 
                # result = 5 + 6 + 7
                # result = 5 + 6 + 8
                # result = 5 + 6 + 9
                # result = 5 + 7 + 8
                # result = 5 + 7 + 9
                # ...
                # result = 7 + 8 + 9
                result = inp[i] + inp[j] + inp[k]
                if result > M:
                    continue
                else:
                    prt = max(prt, result) # 작은 값이 리셋되면 안되서 max값만 들어가게 해줌

    print(prt)
    break




# N, M = map(int ,input().split())
# inp = list(map(int, input().split()))

# result = 0
# prt = 0
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             result = inp[i] + inp[j] + inp[k]
#             if result > M:
#                 continue
#             else:
#                 prt = max(prt, result)

# print(prt) # 백준 제출용
