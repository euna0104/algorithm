def solution(my_string, s, e):
    a = ''
    b = ''
    c = ''
    my_str = list(my_string)
    for i in my_str[0:s:]:
        a += i
    for i in my_str[e:s-1:-1]:
        b += i
    for i in my_str[e+1::]:
        c += i
    return a+b+c
        
    
'''
세덩이로 나누겠다.
앞 a, 중간 b, 끝 c
증간은 revers 해주겠다
'''