from sys import stdin

# 입력.
S = input()
n = int(input())
words = set(stdin.readline().strip() for _ in range(n))
memo = set()

# index = S 탐색용 인덱스, s_sub는 문자를 쌓기 전 초기 상태.
def recursion(index, s_sub):

    # index가 만들어야 하는 S의 길이보다 크면 만들 수 있다는거임 바로 리턴.
    if index >= len(S):
        return 1

    # 현재까지 쌓인 문자열에서, 쌓을 수 있는 경우를 next_rec에 다 담음.
    next_rec = []
    for i in range(index, len(S)):
        s_sub += S[i]
        if s_sub in words:
            next_rec.append(i+1)

    # memo에 탐색하지 않은 위치라면 재귀 돌림.
    # 그러면서 한번이라도 1이 리턴되면 바로 1 리턴.
    for i in range(len(next_rec)):
        global memo
        if next_rec[i] not in memo:
            memo.add(next_rec[i])
            answer = recursion(next_rec[i], "")
            if answer == 1:
                return 1
    return 0

# 출력.
print(recursion(0, ""))
