def solution(arr, flag):
    X = []
    for i, v in enumerate(flag):
        if v:
            X += [arr[i]] * (arr[i]*2)
        else:
            for j in range(arr[i]):
                X.pop()
    return X
    
  
'''
flag 리스트를 순회하려고 enumerate 사용
if문에서 만약 순회할 때 v가 True이면 밑에 조건문
실행
'''
