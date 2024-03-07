def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1:
        for i in range(0,len(arr)+1,1):
            if i % 2 == 1:
                answer.append(arr[i])
            else:
                answer.append(arr[i]+n)
    else:
        return 0
        