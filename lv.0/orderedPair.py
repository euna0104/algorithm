def solution(n):
    answer = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j == n:
                answer += 1
    return answer

# 이렇게 해결하면 시간이 오래걸리는 문제가 존재한다.
