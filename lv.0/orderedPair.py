def solution(n):
    answer = 0
    for i in range(1, n+1):
        j = n % i
        if j == 0:
            answer += 1
    return answer

# for문을 한번만 작성해주기. 시간복잡도 해결 성공.