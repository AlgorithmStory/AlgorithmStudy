#**********단어 뒤집기**************

def get_statement():

    statement_list = input().split() # 받은값을 단어단위로 나누어 리스트 만듦
    reverse_statement = '' # 결과값을 받을 변수 선언

    # 리스트로부터 단어를 하나씩 받아오며 반복문 실행
    for word in statement_list:
        # 단어를 역순 인덱싱을 이용해 결과값 저장할 변수에 저장 - 이것이 핵심
        for i in range(1,len(word)+1):
            reverse_statement += word[-i]
        # 단어가 끝나면 띄어쓰기
        reverse_statement += ' '
    # 결과 출력
    print(reverse_statement)

if __name__ = '__mian__':
    for i in range(int(input())): # 문장 몇개 출력할지 사용자로부터 입력받음
        # 역순으로 문장 단어 출력할 함수 실행
        get_statement():