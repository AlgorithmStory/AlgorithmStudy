from sys import stdin
def main():
    co, lo  = map(int, stdin.readline().split(' '))# 문서 갯수, 위치 입력
    li = list(map(int,stdin.readline().split(' ')))# 문서들의 중요도값 입력

    c_d = {}                                    # 문서들의 중요도값과 해당 중요도값의 갯수를 저장하기 위한 딕셔너리 선언 

                                                # 딕셔너리 값 넣기
    for i in range(1,9+1):
        if li.count(i) == 0:
            continue
        c_d[i] = li.count(i)                    # (키 : 중요도, value : 중요도가 같은 문서들의 갯수) 로 딕셔너리 item 추가

    seq = 0                                     # 출력 순서를 저장할 변수 선언

                                                # 입력받은 리스트가 다 출력될때 까지 수행하자(물론 중간에 궁금한 리스트 출력될때 중단할 것이다.)
    while 0 != len(li):
            
                                                # 만약 현재 인덱스의 리스트 값이 최대값일때
        if li[0] == max(c_d.keys()) :
            
            seq += 1                            # 순번을 갱신하자
            
                                                # 만약 알고자 하던 문서가 출력될 차례라면
            if lo == 0:
                return seq                      # 순서를 반환하고 함수를 종료하자
            

            c_d[li[0]] = c_d[li[0]] - 1         # 해당 중요도 문서 하나가 출력되어서 리스트에 더이상 없으므로 딕셔너리 갱신

                
                                                # 해당 문서의 중요도 의 갯수가 0 이면 키에 해당하는 item 삭제
            if c_d[li[0]] == 0: 
                del c_d[li[0]]
                
                                                # 리스트 갱신
            del li[0]
            lo -= 1                             # 궁금한 문서의 위치 갱신
            
            
                                                # 만약 현재 인덱스의 리스트 값이 최대값이 아닐때
        else:
                                                # 큐를 수행하자
            li.append(li[0])                        # 첫번쨰 리스트의 요소를 리스트 맨뒤인덱스에 추가
            li.remove(li[0])                        # 첫번쨰 리스트의 요소를 삭제

                                                # 만약 알고자 하던 문서가 큐 수행 당했을 땐
            if lo == 0: 
                    
                lo = len(li)                    # 위치를 문서 맨 뒷자리 + 1 로 설정해주자 (이유는 if 문 끝나면 -1 이 수행되기 때문)
                
            lo -= 1                             # 궁금한 문서 위치 1 감소시키자

if __name__ == '__main__':
    for _ in range(int(stdin.readline())):# 테스트 케이스 만큼 실행
        print(main()) # 순서를 출력하자
