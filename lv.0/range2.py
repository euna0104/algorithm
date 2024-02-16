def solution(arr):
    if 2 not in arr:
        return [-1]
    else:
        answer = ""
        answer2 = []
        for i in arr:
            answer += str(i)
        first = answer.index("2")
        final = answer.rindex("2")
        return final
        for i in arr[first:final+1:1]:
            answer2.append(i)
        return answer2
        