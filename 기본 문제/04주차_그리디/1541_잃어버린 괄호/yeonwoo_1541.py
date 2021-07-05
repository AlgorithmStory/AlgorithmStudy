import sys

N = sys.stdin.readline().rstrip() # 백준 제출용

arr = N.split('-') # N으로 들고온 str값을 -로 나눠줌 55-50+40이면 '55' '50+40'
sum_min = 0

for i in arr[0].split('+'): 
    # 위에서 55+50+40이 입력되면 -로 나눌수 없기 때문에 +로나눈후
    # 전부 + 값이기 때문에 다 더해줌
    # 55 + 50 - 50 + 40로 입력됬다고 해도 arr[0]이 = 55+50 이므로
    # +로 구분 나눈후 더해주면됨
    sum_min = sum_min + int(i)

for i in arr[1:]: # 이것이 실행 되는 거 자체가 젤 처음에 -값으로 split이 됬다는 의미기 때문에
    for j in i.split('+'): # 뒤 에 배열들 +기호로 구분 나눈후 들고와서 -해줌
        sum_min = sum_min - int(j)

print(sum_min)