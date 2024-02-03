def solution(my_string, s, e):    
    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]
    
'''
for문 보다 slice로 해주는 것이 더 좋다.
'''