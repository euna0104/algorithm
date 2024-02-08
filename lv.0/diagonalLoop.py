def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n):
        answer.append(num_list[n*i : n*(i+1)])
    return answer
    
'''
겉을 돌고 그다음 안을 돈다.
'''