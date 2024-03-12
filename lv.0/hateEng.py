def solution(numbers):
    nums = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]
    
    for i, v in enumerate(nums):
        numbers = numbers.replace(v, str(i))
    return int(numbers)
  
'''
튜플로 접근해야함을 깨닳았다.
'''
