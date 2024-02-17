def solution(strArr):
    numbers = []
    for i in strArr:
        numbers.append(len(i))
    hi = (max(set(numbers), key = numbers.count))
    return hi
        
'''
가장 큰 max값이 출력이 안되는 문제
'''
