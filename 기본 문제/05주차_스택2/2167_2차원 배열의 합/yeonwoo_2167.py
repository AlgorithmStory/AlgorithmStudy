import sys
import gc
N, M = map(int ,sys.stdin.readline().split())

origin_vec = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

del N, M
gc.collect() # 메모리 줄어드는 함수 

prt = []
for K in range(int(sys.stdin.readline())):
    result = 0
    i_input, j_input, x_input, y_input = map(int, sys.stdin.readline().split())

    # map이용해서 list만들면 메모리 줄어든다는데 이중 for문...
    # https://wikidocs.net/21057
    # https://steemit.com/kr-dev/@tmkor/for-loop-map
    for x in range(i_input-1, x_input):
        for y in range(j_input-1, y_input):
            result += origin_vec[x][y]

    prt.append(result) 
    
del origin_vec
gc.collect()

for i in prt:
    print(i)