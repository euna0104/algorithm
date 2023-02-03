def solution(array, n):
    array.sort() #오름차수s
    answer = array[0] #가장 작은 수
    num = abs(n - array[0]) #주어진 수에서 array의 가장 작은수 빼기 
    for i in array:
        if num > abs(n - i): #num 보다 abs(n - i)가 더 작으면
            num = abs(n - i) #num은 abs(n - i)가 된다
            answer = i answer는 i
    return answer
