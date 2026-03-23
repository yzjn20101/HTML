import time
print(time.time())
print("You need to time exactly 10 seconds")
temp = input("Hit enter to start the 10 seconds")
start_time = time.time()
temp = input("Hit enter again when you think 10 seconds has passed")
finish_time = time.time

print(f"Start time: {start_time}")
print(f"Finish time: {finish_time}")