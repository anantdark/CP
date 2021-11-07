#CoDeD By AnAnT
import datetime
def timeconvert(v):
    ktime = datetime.datetime.strptime(v, "%I:%M %p")
    ltime = datetime.datetime.strftime(ktime, "%H:%M")
    return(ltime)
def checker():
    count = ''
    mytime = input()
    ontime = timeconvert(mytime)
    for i in range(int(input())):
        time = input()
        starttime = timeconvert(time[:8])
        endtime = timeconvert(time[9:])
        if ontime >= starttime and ontime <= endtime:
            count += '1'
        else:
            count += '0'
    return count
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print(checker())