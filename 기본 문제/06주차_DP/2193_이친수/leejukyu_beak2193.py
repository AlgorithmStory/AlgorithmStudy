n = int(input())
a = [0,1]
for i in range(2, n+1):
    a.append(a[i-1]+a[i-2]) # 앞선 두개의 합이 다음번 개수
print(a[-1])