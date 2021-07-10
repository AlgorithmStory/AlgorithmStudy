import sys


def i_cant_built_there():                                           # 함수 선언
    num_of_sensors = int(sys.stdin.readline().split()[0])           # 센서의 총 개수 : 사용하지 않음
    num_of_relay = int(sys.stdin.readline().split()[0])             # 집중국의 총 개수
    sensors = list(set(map(int, sys.stdin.readline().split())))     # 센서의 위치 좌표 : 읽어올 때 set를 사용해 중복 값 제거
    sensors.sort()                                                  # 센서의 위치를 차례대로 정렬
    distances = []                                                  # 센서 간 거리

    for i in range(1, len(sensors)):                                # 센서 간 거리 리스트에
        distances.append(sensors[i] - sensors[i - 1])               # 이웃한 센서 간의 거리를 계산에서 넣어줌

    distances.sort(reverse=True)                                    # 센서 간 거리 리스트를 내림차순으로 정렬
    return sum(distances[num_of_relay - 1:])                        # 센서 간 거리 리스트에서 집중국 개수 - 1 만큼 앞의 원소를 빼고 총합을 반환
    # 집중국이 하나 늘어날 때마다 거리 리스트에서 가장 긴 거리를 잘라서 센서들을 나누면 수신 가능영역의 합이 제일 작아짐


print(i_cant_built_there())                                         # 정답 출력
