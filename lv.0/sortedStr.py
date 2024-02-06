def solution(my_string):
    hi = []
    for i in my_string:
        if i.isdigit():
            hi.append(int(i))
    return sorted(hi)

'''
1. hi라는 리스트 만들어주기
2. my_string 배열 for문으로 순회하기
3. 문자열이 숫자로 판별인지 아닌지 판별하기
4. 만약 숫자면, 문자열을 숫자로 하여 hi에 첨가해주기
5. 오름차순으로 정렬된 리스트 hi를 return 해주기
'''