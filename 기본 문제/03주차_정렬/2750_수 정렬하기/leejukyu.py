# 버블정렬
import sys

N = int(input())
a = [int(sys.stdin.readline()) for _ in range(N)]   # 입력 받아오기

for i in range(1, len(a)):                          
    for j in range(0,len(a)-i):                     # for문이 돌때마다 가장 뒷 자리 수가 자리를 잡으므로 연산할 필요가 없음
        if a[j] > a[j+1]:                           # 앞 번호의 수가 뒷 번호의 수보다 크다면            
            a[j], a[j+1] = a[j+1], a[j]             # 앞과 뒤 자리 바꿈

for k in range(len(a)):                             # 리스트에 넣어놓은 a를 한줄씩 출력
    print(a[k])