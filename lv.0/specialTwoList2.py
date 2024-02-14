def solution(arr):
    answer = []
    for i in range(len(arr[0])):
        for j in range(len(arr[0])):
            if arr[i][j] == arr[j][i]:
                answer.append(1)
            else:
                answer.append(0)
    if 0 in answer:
        return 0
    else:
        return 1
    