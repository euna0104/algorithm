def solution(arr, queries):
    answer = []
    arr = str(arr)
    for i in range(len(queries)):
        arr.replace(arr[queries[i][0]], arr[queries[i][1]])            
        
    return list(arr)
