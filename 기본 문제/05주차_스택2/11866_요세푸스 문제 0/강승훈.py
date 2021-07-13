# 입력.
n,k = map(int, input().split(" "))
arr = [i for i in range(1, n+1)]

result_str = "<" # 여기다 담을거.
check = 0 # while문 첫번쨰 if문 맨처음은 실행 안시킬려고.
index = -1 # 가리킬 인덱스.
while len(arr) >= 1:
    if check != 0: # 처음 빼고 계속 실행 됨.
        result_str += ", "
    check = 1
    if index+k <= len(arr)-1: # index에 k를 더한 값이, 배열의 길이보다 작으면, 그대로 이동해서 바로 가져오면 됨.
        index += k
        result_str += str(arr[index])
        del arr[index]
    else: # 인덱스가 배열길이보다 크면, 나눈 나머지를 인덱스로 씀.
        index = (index + k)%len(arr)
        result_str += str(arr[index])
        del arr[index]
    index -= 1 # arr의 요소를 매번 하나씩 삭제 하니까, index도 계속 1씩 빼줌.

# 출력.
result_str += ">"
print(result_str)
