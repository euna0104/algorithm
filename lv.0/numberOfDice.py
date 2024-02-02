def solution(box, n):
    return (int(box[0] // n) * int(box[1] // n) * int(box[2] // n))
    
'''
box엔 리스트가 들어있음
구하는법은 가로.세로.높이 몫을 곱하는 것이다.

파이썬 함수 중 math.prod() 를 사용하는 방법도 있다.
math.prod()는 ()안에 있는 모든 iterable 요소들의 곱을 구한다.


import math

def solution(box, n):
    return math.prod(map(lambda v: v//n, box))
    
box안에 있는 모든 값 v들을 n으로 나눈 값의 몫을 모두 곱하는 것이다.

'''