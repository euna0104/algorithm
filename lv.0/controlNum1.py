# integer를 넣어야함
def solution(n, control):
    for i in range (len(control)):
        if control[i] == "w":
            n += 1
        elif control[i] == "s":
            n -= 1
        elif control[i] == "d":
            n += 10
        elif control[i] == "a":
            n -= 10
    return n
            
'''
control의 길이만큼 해줄 것.
그리고 들여쓰기로 인해 제대로된 n이 출력 안됨.
문자열로 해결 법

def solution(n, control):
    for i in control: # 문자열로 해결
        if i == "w":
            n += 1
        elif i == "s":
            n -= 1
        elif i == "d":
            n += 10
        else:
            n -= 10
    return n
        
'''
