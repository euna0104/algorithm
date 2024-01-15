def solution(array, height):
    reArray = 0
    for i in range (len(array)):
        if (height < array[i]):
            reArray += 1
    return reArray 
    