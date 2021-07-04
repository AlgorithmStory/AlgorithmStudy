N, K = map(int, input().split())            
a = [int(input()) for _ in range(N)]
cnt = 0                                     # 카운트

for i in range(1, len(a)+1):                # 동전 가치를 큰 순서대로 하나씩 넣기
    if K // a[-i] > 0:                      # 몫이 0보다 크면 동전이 필요하다
        cnt += (K//a[-i])                   # 몫만큼 필요 개수 카운트
        K %= a[-i]                          # 나머지를 가치의 합으로 업데이트
        
    elif K % a[-i] == 0:                    # 나머지가 0이면 연산을 끝냄
        cnt += (K//a[-i])                   # 몫만큼 카운트
        break                               # break로 나가기
print(cnt)                                  # 필요 동전 개수 최솟값 출력