def solution(myString, pat):
    end = myString.rfind(pat) #'end'는 'pat'이 마지막으로 나타내는 인덱스를 나타낸다.
    
    return myString[:end + len(pat)]

'''
rfind() 함수는 문자열에서 지정된 부분 문자열을 뒤에서부터 찾아 그 위치를 반환한다.
len(pat)는 이 위치까지의 문자열을 반환함으로써 'pat'로 끝나는 가장 긴 부분 문자열을 얻을 수 있다.
'''
