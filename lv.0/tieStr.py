def solution(strArr):
    answer = []
    for i in strArr:
        answer.append(len(i))
    cnt = []
    for i in set(answer):
        cnt.append(answer.count(i))
    return max(cnt)
  