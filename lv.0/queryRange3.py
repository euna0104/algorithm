def solution(arr, queries):
    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]  
        
    return arr

'''
replace로 푸는 것이 아니었다.
대입으로 풀기 였다.
'''
