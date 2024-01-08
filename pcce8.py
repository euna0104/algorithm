def solution(storage, num):
    clean_storage=[]
    clean_num = []
    
    for i in range(len(storage)):
        if storage[i] in clean_storage: # 만약 storage에 있는 물건이 clean_storage에 있다면
            pos = clean_storage.index(storage[i]) #  clean_storage에서 그 물건이 있는 가리키는 값의 위치가 pos다.
            clean_num[pos] += num[i]
        else: # 만약 storage에 있는 물건이 clean_storage에 없다면
            clean_storage.append(storage[i]) #  clean_storage에 storage물건을 추가해준다.
            clean_num.append(num[i]) # clean_num에 num[i] 추가
    
    max = max(clean_num)
    result = clean_storage[clean_storage.index(max)]
    return result
    