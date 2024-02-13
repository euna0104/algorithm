def solution(arr, queries):
    for l,r in queries:
        for i in range(l, r+1):
            arr[i] += 1
    return arr
        
'''
queries에 있는 숫자에 1을 더한다.
sum(queries, []) -> 묶여있는 리스트들 해체하기

 순서대로 s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.
 -> 생각해보니 해체가 중요한게 아니였다.
 이 수열 구간 안에 있는 애들에게 1을 더하는 것
'''
