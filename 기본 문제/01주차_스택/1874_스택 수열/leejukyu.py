import sys

n = int(sys.stdin.readline().split(' ')[0])
num = [0]
count = 1
a = [int(sys.stdin.readline().split(' ')[0]) for i in range(n)]
result = []
i = 0

while  True:
    # 수열보다 크면 append
    if a[i] > num[-1]:
        num.append(count)
        count += 1
        result += "+"

    # 같은 값이면 pop
    elif a[i] == num[-1]:
        num.pop()
        result += "-"
        # i값 업데이트
        i += 1
        # i값이 n값보다 커지기 전에 멈춤, 첫번째 if문에서 인덱스 넘어감
        if i == n:
            break
    else:
        result = "NO"
        break

if result == "NO":
    print(result)
else:
    for i in result:
        print(i)