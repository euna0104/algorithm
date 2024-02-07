def solution(myString):
    answer = myString.split("x")
    answer = list(filter(None, answer))
    return sorted(answer)

'''
split("x")를 사용하여 x를 기준으로 나눈 배열을 만든다.
filter함수 사용. answer배열에서 None인 것 제거한다.
정렬된 answer를 리턴.
'''