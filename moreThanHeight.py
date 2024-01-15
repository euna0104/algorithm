def solution(array, height):
    sum = 0
    for i in array: # array 배열 안에서
        if i > height: # i의 수가 주어진 height 보다 크다면
            sum += 1 # sum에 1을 더한다.
    return sum
    