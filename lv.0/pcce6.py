def solution(numbers, our_score, score_list):
    result= []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:
            result.append("Same")
        else:
            result.append("Different")
           
    return result