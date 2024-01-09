# integer를 넣어야함
def solution(n, control):
    n = 0
    list(control)
    for i in control:
        if control[i] == "w":
            n += 1
        elif control[i] == "s":
            n -= 1
        elif control[i] == "n":
            n += 10
        else:
            n -= 10
        return n
            