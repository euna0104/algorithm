def solution(polynomial):
    xNum = 0
    const = 0
    
    for i in polynomial.split(' + '): # 얘로 나누겠다
        if i.isdigit():
            const += int(i)
        else:
            if i == 'x':
                xNum = xNum+1
            else:
                xNum+int(c[:-1])
    if xNum == 0:
        return str(const)
    elif xNum == 1:
        return 'x'
        

'''
다항식 더하기 문제에서는 isdigit()함수를 쓰는 것이 중요한 것 같음.
isdigit는 숫자인지 아닌지 판별하는 것임.
'''
