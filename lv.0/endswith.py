def solution(my_string, is_suffix):
    if my_string.endswith(is_suffix):
        return 1
    else:
        return 0    
    
# 접미사인지 확인할때는 endswith를 사용한다.