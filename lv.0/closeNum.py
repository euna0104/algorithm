def solution(array, n):
    answer = 0
    answer2 = []
    for i in array:
        answer2.append(abs(n - i))
    num = answer2.index(min(answer2))
    return array[num]
