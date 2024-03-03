def solution(arr):
    answer = []
    for i in arr:
        if (i >= 50 and i % 2 == 0) :
            answer.append(i / 2)
        elif (i < 50 and i % 2 == 1):
            answer.append(i * 2)
        else:
            answer.append(i)
    return answer
  
'''
&이 쓰는 것이 아니다. 
and를 써야한다.
'''
