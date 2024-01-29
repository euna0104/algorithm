def solution(n):
    answer = [[0]*n for i in range(n)] # 0x0 형식의 배열 만들기
    for i in range(n):
        answer[i][i]=1 # n이 i에서 i번째의 수를 1로 바꿔주기
    return answer