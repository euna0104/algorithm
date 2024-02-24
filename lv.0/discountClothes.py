def solution(price):
  if price>=500000:
    price = price*0.8
  elif price>=300000:
    price = price*0.9
  elif price>=100000:
    price=price*0.8
  return int(price)
  
'''
가격을 내림차순으로 해야한다.
'''
