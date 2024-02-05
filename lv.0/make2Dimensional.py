def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n):
        answer.append(num_list[n*i : n*(i+1)])
    return answer
    
'''
for문에서 len을 사용할 때는 range를 사용하는 것을 잊지말자
'''