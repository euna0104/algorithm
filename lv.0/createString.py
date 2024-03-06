def solution(my_string, index_list):
    answer = ''
    for i in range(len(index_list)):
        answer += my_string[index_list[i]]
    return answer
  
'''
list뿐만 아니라 string에서도 []를 쓸 수 있다.
'''
