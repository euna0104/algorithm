def solution(n):
    def count_divisors(n):
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        return count
    
    answer = 0
    for i in range(4, n + 1):
        if count_divisors(i) >= 3:
            answer += 1
    return answer
