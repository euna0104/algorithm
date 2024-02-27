def solution(i, j, k):
    count = 0
    for a in range(i,j+1): # i부터 j+1까지 for문을 돌릴거다. 그래서 range.
        for b in str(a): # 변수를 b로 선언. b는 a안에 있는 것들
            if b == str(k): # b가 주어진 k와 같다면
                count += 1 # count 1 증가
    return count