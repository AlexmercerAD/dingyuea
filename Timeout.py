import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('倒计时结束!')

# 输入倒计时时间（以秒为单位）
t = input("输入倒计时时间（以秒为单位）: ")

countdown(int(t))
