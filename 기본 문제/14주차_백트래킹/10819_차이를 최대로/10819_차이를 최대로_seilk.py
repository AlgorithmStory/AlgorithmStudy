```python
import itertools #to use Permutation
import sys

n = int(sys.stdin.readline().rstrip())

def diff(lst, n): #argument list에서 문제의 식을 계산해주는 함수 생성
    dif = 0
    for i in range(1, n):
        maxdiff += abs(lst[i - 1] - lst[i])
    return dif

lst = list(map(int, sys.stdin.readline().split()))
p = list(itertools.permutations(lst, n)) #순서를 고려하여 lst의 원소 개수만큼 추출 최대 8!개
sol = 0 #정답 초기화
for i in p: #최대 8! loop
    sol = max(sol, diff(i, n)) #sol값은 dif중에서도 최대 dif를 return 해야 하므로 max로 갱신

print(sol)

```
