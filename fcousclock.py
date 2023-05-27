import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

# 设置专注时间（以分钟为单位）
focus_time = 25

# 开始倒计时
countdown(focus_time)
