def solution(a, b, c):
    answer = 0
    if (a != b != c):
        answer = (a+b+c)
    elif (a == b == c):
        answer = (a+b+c)*(pow(a,2)+pow(b,2)+pow(c,2))*(pow(a,3)+pow(b,3)+pow(c,3)) 
    else:
        answer = (a+b+c)*(pow(a,2)+pow(b,2)+pow(c,2))
    return answer
