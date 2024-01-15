def solution(my_strings, parts):
    answer = ''
    for i in range (len(my_strings)):
        answer += my_strings[i][parts[i][0]:parts[i][1]+1]
    return answer
      
'''
2차원 배열로 생각해야하는 부분인가?
난 직관적인 코드가 좋음

def solution(my_strings, parts):
    answer = ""
    for i in range(len(parts)):
        answer += (my_strings[i][parts[i][0]:parts[i][1] + 1])
    return answer
    
def solution(my_strings, parts):
    result = ''
    for i in range(len(my_strings)):
        result += my_strings[i][parts[i][0] : parts[i][1] + 1]
    return result
'''