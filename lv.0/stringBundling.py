def solution(strArr):
    answer = [len(i) for i in strArr]
    tmp = []
    for i in set(answer):
        tmp.append(answer.count(i))
    return max(tmp)
  
  '''
  set으로 answer 리스트에서 중복된 요소 삭제하기.
  '''
  