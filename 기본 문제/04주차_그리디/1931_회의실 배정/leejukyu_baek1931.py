N = int(input())
a = [list(map(int,input().split())) for _ in range(N)]

a.sort(key = lambda x : (x[1],x[0]))                        # 끝나는 시간 기준으로 정렬 후 시작 시간 정렬

cnt = 1                                                     # 카운트

end = a[0][1]                                               # 첫번째 회의가 끝나는 시간

for i in range(1,len(a)):                                   # 회의 수 만큼 반복
    if end <= a[i][0]:                                      # 시작 시간이 기준 회의의 끝나는 시간보다 늦으면
        end = a[i][1]                                       # 기준 회의 업데이트
        cnt += 1                                            # 가능한 회의 +1

print(cnt)                                                  # 프린트