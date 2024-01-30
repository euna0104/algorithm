def solution(date1, date2):
    #연도 비교( 연도부터 다른 경우)
    if date1[0] != date2[0]:
        if date1[0] < date2[0]:
            return 1
        else:
            return 0
    # 월 비교 (연도가 같다)
    else:
        if date1[1] < date2[1]:
            return 1
        elif date1[1] == date2[1]:
            if date1[2] < date2[2]:
                return 1
            else:
                return 0
        else:
            return 0
         