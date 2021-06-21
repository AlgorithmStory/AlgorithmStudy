# 설명 용
import random
N, M = map(int, input('카드의 갯수와 합 몇을 만들지 입력하시오.').split())

best_near = 0 # 가장 M과 비슷한 합을 저장할 변수
best_diff = M # M과 얼마나 차이가 나는지 저장할 변수
for i in n_list:
    print(f'i가 {i} 일때')
    for j in n_list:
        print(f'\tj가 {j} 일때')
        print(f'\tj==i : {i == j}')
        if i == j:
            print('\t중복된 카드가 있을때 continue 실행 (포문 건너뜀)')
            continue
        for k in n_list:
            print(f'\t\tk가 {k} 일때')
            print(f'\t\tk == j : {k == j}')
            print(f'\t\tk == i : {k == i}')
            if (k == j) | (k == i):
                continue
                print('\t\t중복된 카드가 있을때 continue 실행 (포문 건너뜀)')
            near = i + j + k
            diff = M - near
            print('\t\tdiff < 0 :',diff < 0)
            if diff < 0:
                print('\t\t 합이 원하는 합보다 클때 continue 실행(포문 건너뜀)')
                continue
            print('\t\tdiff < 0 :',diff < 0)
            if diff < best_diff:
                print(f'\t\t**best_diff 갱신 : {best_diff}**')
                print(f'\t\t**best_near 갱신 : {best_near}**')
                best_near = near
                best_diff = diff

print(best_near)
                    
# 백준 용         
import sys
N, M = map(int, sys.stdin.readline().split())
    
n_list = list(map(int, sys.stdin.readline().split()))
        
best_near = 0
best_diff = M
for i in n_list: 
    for j in n_list: 
        if i == j:            
            continue    
        for k in n_list:        
            if (k == j) | (k == i):
                continue        
            near = i + j + k
            diff = M - near       
            if diff < 0:                
                continue            
            if diff < best_diff:               
                best_near = near
                best_diff = diff

print(best_near)
