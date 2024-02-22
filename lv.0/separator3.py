import re

def solution(myStr):
  answer = re.sub("[a-c]", " ", myStr).split()
  if len(answer) >= 1:
    return answer
  else:
    return ["EMPTY"]
  
'''
"[a-c]"를 " " 공백으로 바꾼다.
그리고 공백으로 split 나눈다.
'''