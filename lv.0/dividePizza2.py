def solution(n):
    answer = 1 #피자는 일단 한개
    while ( answer * 6 ) % n != 0:
        answer += 1
    return answer

'''
while 반복문으로 풀어야겠다는 것을 직감적으로 알아야겠다.
'''