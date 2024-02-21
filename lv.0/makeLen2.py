def solution(arr):
    count = 0
    length = len(arr)
    while length > 1:
        length = length / 2 #3
        count += 1 #3
    return arr + [0] * (2 ** count - len(arr))  #8-6=2 0을 2벚 추가
