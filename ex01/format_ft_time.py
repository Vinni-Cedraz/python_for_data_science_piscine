import time as time
import datetime as datetime

seconds_since_epoch = time.time()
print(f"Seconds since January 1, 1970:\
 {seconds_since_epoch:.4f} or {seconds_since_epoch:.2e}\
 in scientific notation")
current_time = datetime.datetime.now()
print(f"{current_time:%b %d %Y}")
