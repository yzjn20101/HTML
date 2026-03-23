import time
temp = input("Hit enter to start")
start_time=time.time()
temp = input("Hit enter to stop - exactly 10 seconds later!")
stop_time=time.time()

time_difference = stop_time - start_time
time_difference = abs(time_difference - 10)
print(time_difference)