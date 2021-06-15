import sys
test_case = int(input())
for _ in range(test_case):
    str,_ = sys.stdin.readline().split("\n")
    save_str = ""
    sub_str = ""
    for crnt in str:
        sub_str += crnt
        if crnt == " ":
            save_str += sub_str[::-1]
            sub_str = ""
    sub_str += " "
    save_str += sub_str[::-1]
    print(save_str[1:])
