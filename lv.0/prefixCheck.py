def solution(my_string, is_prefix):
    str = my_string[0:len(is_prefix)]
    if str == is_prefix:
        return 1
    else:
        return 0
