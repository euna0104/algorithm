def solution(n, k):
    sum = (n*12000)+(k*2000)
    if n % 10:
        return sum - ((n/10)*2000)
    else:
        return sum