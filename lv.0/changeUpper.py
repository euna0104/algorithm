def solution(my_string, alp):
    if alp in my_string:
        point = my_string.index(alp)
        return (my_string[point].upper() + my_string[point+1:])
    else:
        return my_string
