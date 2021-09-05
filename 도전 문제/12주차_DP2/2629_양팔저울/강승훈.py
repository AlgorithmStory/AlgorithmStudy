# 입력.
n = int(input())
weights = list(map(int, input().split(" ")))
m = int(input())
beads = list(map(int, input().split(" ")))

# 가능한 경우
possible_cases = set([0])

# 현재까지 구한 가능한 경우에 대해서,
# 모든 추를 탐색하여 (더하기, 빼기, 현재 추)가 가능한 목록에 존재 하지 않는다면 넣어줌.
for weight in weights:
    for case in possible_cases.intersection():
        plus = weight + case
        minus = abs(weight - case)
        if plus not in possible_cases:
            possible_cases.add(plus)
        if minus not in possible_cases:
            possible_cases.add(minus)
        if weight not in possible_cases:
            possible_cases.add(weight)

# 출력.
for bead in beads:
    if bead in possible_cases:
        print("Y", end=" ")
    else:
        print("N", end=" ")
