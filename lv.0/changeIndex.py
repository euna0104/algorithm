def solution(my_string, num1, num2):
    s = ''
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return s.join(my_string)

'''
1. num1번째, num2번째 접근을 위해 my_string을 list형태로 변경
2. num1번째와 num2번째의 순서를 변경하여 정의한다.
3. 바꾼 문자열을 join을 사용하여 s에 붙인다. 그리고 다시 string형태로 만든다.
'''