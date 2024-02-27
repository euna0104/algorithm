def solution(n):
    answer = 0
    for i in range(4, n+1):
        if (i % 2 == 0) or (i % 3 == 0) or ( i == 25) or ( i == 49):
            answer += 1
    return answer
