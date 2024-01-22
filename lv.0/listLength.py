def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1:
        for i in arr:
            if arr % 2 == 1:
                answer.append(i+n)
            
    return answer
