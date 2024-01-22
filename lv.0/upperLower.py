# 대문자는 소문자로, 소문자는 대문자로 하기
def solution(my_string):
    return my_string.swapcase()

'''
swapcase()로 하는게 간단하다. 근데 정석대로 풀려면,

def solution(my_string):
    answer = ''
    
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    return answer

'''