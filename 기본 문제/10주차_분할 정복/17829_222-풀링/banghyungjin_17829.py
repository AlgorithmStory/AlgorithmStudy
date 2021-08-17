import sys


def do_something(input_image):                                      # 2 * 2 로 분할하는 메소드
    if len(input_image) == 1:                                       # 이미지가 1칸 짜리면
        return input_image[0][0]                                    # 내용 반환

    else:                                                           # 이미지가 1칸 보다 크면
        next_image = []                                             # 메소드 적용 후 이미지

        for x in range(len(input_image) // 2):                      # 이미지를 2 * 2 씩으로 나눔
            temp_line = []                                          # 다음 이미지에 들어갈 리스트
            for y in range(len(input_image) // 2):                  # -
                temp_list = [input_image[2 * x][2 * y],             # 2 * 2 각 칸의 내용
                             input_image[2 * x][2 * y + 1],         # -
                             input_image[2 * x + 1][2 * y],         # -
                             input_image[2 * x + 1][2 * y + 1]]     # -
                temp_list.sort()                                    # 오름차순 정렬
                temp_line.append(temp_list[2])                      # 2 번째로 큰 수 찾음
            next_image.append(temp_line)                            # 해당 수를 다음 이미지에 넣어줌
        return do_something(next_image)                             # 다음 이미지에 대해 메소드 다시 실행


M = int(sys.stdin.readline().split()[0])                            # 이미지 크기 읽어옴
image = []                                                          # 이미지 리스트

for _ in range(M):                                                  # 이미지 내용 읽어옴
    input_lines = list(map(int, sys.stdin.readline().split()))      # -
    image.append(input_lines)                                       # -

print(do_something(image))                                          # 메소드 실행 후 정답 출력
