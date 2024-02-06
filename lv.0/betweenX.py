def solution(myString):
    result = []
    answer = myString.split("x")
    for i in answer:
        result.append(len(i))
    return result

'''
1. result 라는 배열 미리 생성하기
2. answer라는 배열 생성. 
3. 근데 이  answer배열은 x로 문자열을 분리했다.
4. for문으로 answer 배열을 순회한다.
5. 그리고 answer배열 안에 있는 i의 길이를 result배열에 첨가한다.
6. result 배열을 return 한다.
'''