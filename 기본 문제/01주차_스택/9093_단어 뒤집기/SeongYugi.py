N = int(input())

for i in range(N) :
    text = input()
    # print(text)
    text_list = text.split(" ")
    for k in text_list :
        k = k[::-1]
        print(k,end=" ")