# eval 은 True 또는 False로 반환
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!','')+str(m)))

'''
eval은 상태를 True 또는 False로 반환해준다.
그리고 int를 사용해서 1 또는 0으로 반환해준다.
'''