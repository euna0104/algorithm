'''
1. 파이썬 함수를 사용할 예정
2. 문자열에서 중복된 것이 있다면 
3. 삭제하도록 하기
'''
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer
