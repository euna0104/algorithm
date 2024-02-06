def solution(n):
    answer = []
    for i in n:
        if n % i == 0:
            answer.append(i)
    return answer
