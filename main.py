import time
def countdowntime(sec):
    while sec>0:
        minutes=int(sec/60)
        second=int(sec%60)
        timer=f'{minutes}:{second}'
        print(timer)
        sec -= 1
    print('time up')
sec=int(input("Enter The Time In No. Or Seconds"))
countdowntime(sec)