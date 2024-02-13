def solution(arr, queries):
    #answer = []
    #return answer
    queries2 = sum(queries, [])
    for i in queries2:
        arr[i] = arr[i]+1
    return arr
        

'''
queries에 있는 숫자에 1을 더한다.
sum(queries, []) -> 묶여있는 리스트들 해체하기
'''
