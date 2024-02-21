def solution(arr):
    if len(arr) == 2:
        return arr
    elif len(arr) % 4 == 0:
        return arr
    else:
        for i in range(len(arr) - (len(arr)//2)-1):  # 정수 나눗셈으로 변경합니다.
            arr.append(0)
        return arr

'''
예외처리는 하였으나 테스트케이스를 통과 못한 구간이 있다.
'''