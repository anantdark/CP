#CoDeD By AnAnT
import sys
def printer(boxes, mike, maxlim):
    while boxes:
        mike += boxes.pop()
        if mike >= maxlim:
            return(tval-len(boxes))
    else: 
        return ("-1")
def final(boxes, mike, tracy, maxlim):
    for i in range(len(boxes)):
        if tracy+boxes[i] >= maxlim:
            tracy += boxes.pop(i)
            return(printer(boxes, mike, maxlim))
if __name__ == "__main__":
    for i in range(int(sys.stdin.readline())):
        noval, maxlim = map(int, sys.stdin.readline().split())
        boxes = list(map(int, sys.stdin.readline().split()))
        if sum(boxes)//2<maxlim:
            print("-1")
            continue
        boxes.sort()
        tracy, mike, tval = 0, 0, len(boxes)
        while noval>0:
            tracy += boxes[-1]
            if tracy<maxlim:
                boxes.pop()
                mike += boxes.pop()
                noval -= 2
                continue
            elif tracy==maxlim:
                boxes.pop()
                print(printer(boxes, mike, maxlim))
                break
            elif tracy>maxlim:
                tracy -= boxes[-1]
                print(final(boxes, mike, tracy, maxlim))
                break
        else:
            print("-1")