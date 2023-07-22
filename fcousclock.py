import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        time_left = end_time - time.time()
        print(f"\r{int(time_left // 60)}:{int(time_left % 60):02d}", end="")
        time.sleep(1)
    print("\nTime's up!")

focus_timer(25 * 60) # 25 minutes
