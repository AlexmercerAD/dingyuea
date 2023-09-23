# 导入time和datetime模块
import time
import datetime

# 定义一个函数，用来获取当前的时间和日期
def get_current_time_and_date():
    # 获取当前的时间戳
    timestamp = time.time()
    # 将时间戳转换为本地时间
    local_time = time.localtime(timestamp)
    # 格式化时间和日期
    time_str = time.strftime("%H:%M:%S", local_time)
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    # 返回时间和日期的字符串
    return time_str, date_str

# 定义一个循环，用来不断地显示时钟
while True:
    # 调用函数，获取当前的时间和日期
    current_time, current_date = get_current_time_and_date()
    # 清空屏幕
    print("\033c", end="")
    # 打印时钟
    print(f"当前时间：{current_time}")
    print(f"当前日期：{current_date}")
    # 暂停一秒
    time.sleep(1)
