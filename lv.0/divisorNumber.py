def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return answer

'''
약수를 구할 때는 1부터 시작하고, n+1(끝)까지 실행해야하는
range를 정해주어야 한다는 것을 알았다.
'''
