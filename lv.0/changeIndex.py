def solution(my_string, num1, num2):
    answer = ''
    for i in my_string:
        if i == num1:
            answer += my_string.replace(my_string[num2], my_string[num1])
        elif i == num2:
            answer += my_string.replace(my_string[num1], my_string[num2])
        else:
            answer += i
    return answer
