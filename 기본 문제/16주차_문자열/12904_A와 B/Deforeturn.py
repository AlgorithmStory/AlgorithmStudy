# 입력.
s = [crnt for crnt in input()]
t = [crnt for crnt in input()]

# 끝이 A거나 B인 경우를 파악 하여 접근 하면 됨.
while len(t) > len(s):
    if t[-1] == "A":
        t.pop()
    else:
        next_s = [t[-i] for i in range(2, len(t)+1)]
        t = next_s

# 출력.
if s == t:
    print(1)
else:
    print(0)
