import sys


def i_mino(input_width_height, input_paper, x, y):  # 그냥 각 블록 형태의 좌표를 싹 다 저장해서 비교
    sums = [0]
    if y < input_width_height[1] - 3:
        sums.append(input_paper[x][y] + input_paper[x][y + 1] + input_paper[x][y + 2] + input_paper[x][y + 3])
    if x < input_width_height[0] - 3:
        sums.append(input_paper[x][y] + input_paper[x + 1][y] + input_paper[x + 2][y] + input_paper[x + 3][y])
    return max(sums)


def o_mino(input_width_height, input_paper, x, y):
    if x < input_width_height[0] - 1 and y < input_width_height[1] - 1:
        return input_paper[x][y] + input_paper[x][y + 1] + input_paper[x + 1][y] + input_paper[x + 1][y + 1]
    return 0


def t_mino(input_width_height, input_paper, x, y):
    sums = [0]
    if x < input_width_height[0] - 1 and y < input_width_height[1] - 2:
        sums.append(input_paper[x][y] + input_paper[x][y + 1] + input_paper[x][y + 2] + input_paper[x + 1][y + 1])
        sums.append(input_paper[x + 1][y] + input_paper[x + 1][y + 1] + input_paper[x + 1][y + 2] + input_paper[x][y + 1])
    if x < input_width_height[0] - 2 and y < input_width_height[1] - 1:
        sums.append(input_paper[x][y] + input_paper[x + 1][y] + input_paper[x + 2][y] + input_paper[x + 1][y + 1])
        sums.append(input_paper[x][y + 1] + input_paper[x + 1][y + 1] + input_paper[x + 2][y + 1] + input_paper[x + 1][y])
    return max(sums)


def s_mino(input_width_height, input_paper, x, y):
    sums = [0]
    if x < input_width_height[0] - 1 and y < input_width_height[1] - 2:
        sums.append(input_paper[x + 1][y] + input_paper[x + 1][y + 1] + input_paper[x][y + 1] + input_paper[x][y + 2])
        sums.append(input_paper[x][y] + input_paper[x][y + 1] + input_paper[x + 1][y + 1] + input_paper[x + 1][y + 2])
    if x < input_width_height[0] - 2 and y < input_width_height[1] - 1:
        sums.append(input_paper[x][y] + input_paper[x + 1][y] + input_paper[x + 1][y + 1] + input_paper[x + 2][y + 1])
        sums.append(input_paper[x][y + 1] + input_paper[x + 1][y + 1] + input_paper[x + 1][y] + input_paper[x + 2][y])
    return max(sums)


def j_mino(input_width_height, input_paper, x, y):
    sums = [0]
    if x < input_width_height[0] - 1 and y < input_width_height[1] - 2:
        sums.append(input_paper[x][y] + input_paper[x][y + 1] + input_paper[x][y + 2] + input_paper[x + 1][y + 2])
        sums.append(input_paper[x][y] + input_paper[x + 1][y] + input_paper[x + 1][y + 1] + input_paper[x + 1][y + 2])
        sums.append(input_paper[x][y] + input_paper[x][y + 1] + input_paper[x][y + 2] + input_paper[x + 1][y])
        sums.append(input_paper[x + 1][y] + input_paper[x + 1][y + 1] + input_paper[x + 1][y + 2] + input_paper[x][y + 2])
    if x < input_width_height[0] - 2 and y < input_width_height[1] - 1:
        sums.append(input_paper[x][y] + input_paper[x][y + 1] + input_paper[x + 1][y] + input_paper[x + 2][y])
        sums.append(input_paper[x][y + 1] + input_paper[x + 1][y + 1] + input_paper[x + 2][y + 1] + input_paper[x + 2][y])
        sums.append(input_paper[x][y] + input_paper[x][y + 1] + input_paper[x + 1][y + 1] + input_paper[x + 2][y + 1])
        sums.append(input_paper[x][y] + input_paper[x + 1][y] + input_paper[x + 2][y] + input_paper[x + 2][y + 1])
    return max(sums)


def solve(input_paper, input_width_height):
    answer = []
    for x in range(input_width_height[0]):
        for y in range(input_width_height[1]):
            answer.append(max(i_mino(input_width_height, input_paper, x, y),
                              o_mino(input_width_height, input_paper, x, y),
                              t_mino(input_width_height, input_paper, x, y),
                              s_mino(input_width_height, input_paper, x, y),
                              j_mino(input_width_height, input_paper, x, y)))
    return max(answer)


width_height = list(map(int, sys.stdin.readline().split()))

paper = []
for i in range(width_height[0]):
    paper.append(list(map(int, sys.stdin.readline().split())))

print(solve(paper, width_height))
