from collections import deque #덱으로 접근

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == "right":
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)

'''
rotate는 덱으로 접근하기.
덱을 사용하기 위해 from collections import deque 선언해주기.
numbers.rotate(1)은 numbers를 오른쪽으로 한칸씩 이동해준다.
numbers.rotate(-1)은 numbers를 왼쪽으로 한칸씩 이동해준다.

'''