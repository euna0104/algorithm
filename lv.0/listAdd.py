def solution(arr):
    answer = []
    for i in arr:
        for j in range(i): # 수 이므로 range를 해줘야한다. i만큼 반복하겠다.
            answer.append(i)
    return answer