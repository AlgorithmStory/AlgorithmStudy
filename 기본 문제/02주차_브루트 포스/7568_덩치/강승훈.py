n = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(n)]
result = ""
for i in range(n):
    check_th = 1 # i번째 사람의 등수를 매길 변수. (매번 초기화 됨.)
    for j in range(n): # 자신을 제외한 사람 중, 자신 보다 키와 몸무게가 둘다 크면 등수 1증가시킬거임.
        if i != j:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]: # 만약 이 조건이 한번도 성립되지 않는다면, 변수의 초기 값인 1이 저장되는거.
                check_th += 1
    result += str(check_th)+" "
print(result)
