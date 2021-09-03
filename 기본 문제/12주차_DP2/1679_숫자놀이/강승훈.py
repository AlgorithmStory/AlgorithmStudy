# 짝순, 홀순 두 선수 모두 매 경기마다 최선(최소를 구함)의 선택을 한다고 가정.
from sys import stdin

# 입력.
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split(" ")))

# 사용된 숫자의 수가 이걸 넘기면 진거임.
limite_n = int(stdin.readline())

# 경기 기록을 저장할 배열
dp_arr = [[0 for _ in range(n+1)]]

# 몇번째 경기인지.
round = 0

while True:
    round += 1
    index_save = 0
    min_check = limite_n + 1

    # 주어진 사용 가능한 숫자들을 이용해서,
    # 주어진 숫자 만큼의 이전의 횟수에 1을 더하면 현재의 사용 가능 횟수가 구해짐.
    # 근데 사용 횟수최소를 찾아야 하므로, 범위를 벗어나기 전까진 주어진 모든 카드를 다 써봐야됨.
    for i in range(n):

        # 오름차순으로 주어진다고 했으니, 과거 라운드의 범위 벗어나면 바로 나감.
        if round - arr[i] >= 0:

            # 그게 아니면, 과거의 경기에서 1을 더한 값이 현재 라운드의 최소보다 작으면 갱신해줌.
            if limite_n >= dp_arr[round - arr[i]][-1] + 1:
                if min_check > dp_arr[round - arr[i]][-1] + 1:
                    min_check = dp_arr[round - arr[i]][-1] + 1
                    index_save = i
        else:
            break

    # 주어진 숫자 중 어떤걸 써야 최소의 결과가 되는지,
    # 위의 포문으로 확인을 했으니, dp_arr에 현재 경기 결과를 append 해주면 됨.
    next_arr = dp_arr[round - arr[index_save]].copy()
    next_arr[index_save] += 1
    next_arr[-1] += 1
    dp_arr.append(next_arr.copy())

    # 만약 현재 경기 숫자 사용횟수가 오버됫으면 바로 나감.
    if min_check > limite_n:
        break

# 출력.
if round%2 == 0:
    print(f"holsoon win at {round}")
else:
    print(f"jjaksoon win at {round}")
