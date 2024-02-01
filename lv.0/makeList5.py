def solution(intStrs, k, s, l):
    answer = []
    answer2 = []
    #먼저 부분 배열 만들기
    for i in range(len(intStrs)):
        answer.append(intStrs[i][s:s+l])
    return answer