import sys

N,L = map(int, input().split())
a = [int(x) for x in sys.stdin.readline().split()]
a.sort()                                                # 오름차순 정렬

len = 0                                                 # 원소 저장소
cnt = 1                                                 # 카운트

for i in a:                                             
    if len == 0:                                        # 처음 돌때
        len = i                                         # 첫번째 값을 저장
    elif (i-len) >= L:                                  # 현재 위치와 이전 위치를 뺀 값이 테이프 길이보다 크거나 같으면
        cnt += 1                                        # 테이프 한 개 더 필요
        len = i                                         # 테이프 시작점 업데이트

print(cnt)