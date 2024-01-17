def solution(n, k):
    sum = (n*12000)+(k*2000)
    if n >= 10 :
        return sum - (int(n/10)*2000)
    else:
        return sum

'''
int로 바꿔주는 것 꼭 생각하기.
소수점자리 날려주는 거것 생각하기 
'''
