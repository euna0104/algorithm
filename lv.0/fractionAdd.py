from fractions import Fraction

def solution(numer1, demon1, numer2, demon2):
    answer = Fraction(numer1, demon1) + Fraction(numer2, demon2)
    return [answer.numerator, answer.denominator] # 분자, 분모
