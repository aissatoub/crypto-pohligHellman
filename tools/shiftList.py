#shift the given polynomial n times to the right 
#example: shiftListToTheRight([1,2],3) gives [0, 0, 0, 1, 2]
def shiftListToTheRight(x,n):
    if len(x) > 1 or len(x) == 1 and x[0] != 0:
        return [0 for i in range(n)] + x
    else: 
        return x
