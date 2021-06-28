# *********************** 데이터 입력 받기 ***********************
import sys

N = int(sys.stdin.readline())
humans = []

for i in range(N):
    weight, tall = map(int,sys.stdin.readline().split())
    humans.append([weight, tall, 1])
    
# *********************** humans 등수 초기화 *******************
rank = [0]


for i in range(N):
    weight = humans[i][0]
    tall = humans[i][1]
    # print(f'\thuman{i+1} weight :{weight}, tall :{tall}')    
    for j in range(N):
        compare_weight = humans[j][0]
        compare_tall = humans[j][1]
        # print(f'\t\tcompare_human{j+1} compare_weight :{compare_weight}, compare_tall :{compare_tall}')
        if (weight < compare_weight) & (tall < compare_tall):
            humans[i][2] = humans[i][2] + 1
            
# ***************************출력************************************************
for i in range(N):
    print(humans[i][2],end=' ')