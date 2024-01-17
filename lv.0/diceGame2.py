import math

def solution(a, b, c):
    answer = 0

    if a == b and b == c and a == c:
        answer = (a + b + c) * ((math.pow(a, 2)) + (math.pow(b, 2)) + (math.pow(c, 2))) * ((math.pow(a, 3)) + (math.pow(b, 3)) + (math.pow(c, 3)))
    elif a == b or b == c or a == c:
        answer = (a + b + c) * ((math.pow(a, 2)) + (math.pow(b, 2)) + (math.pow(c, 2)))
    else:
        answer = (a + b + c)

    return answer

'''
set로 푸는 신기한 방법
def solution(a, b, c):
    check=len(set([a,b,c])) // set으로 [a,b,c]하고 set의 길이 구하기
    if check == 1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check == 2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)
    
'''
