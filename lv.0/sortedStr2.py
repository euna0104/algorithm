def solution(my_string):
    hi = my_string.lower()
    return ''.join(sorted(hi))

#하나로 이어진 문자열을 만들기 위해서 ''.join을 사용한다.
