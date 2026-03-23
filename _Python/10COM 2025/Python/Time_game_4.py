import time

print("This is a test of your time estimation. You need")
temp = input("Timer starts when you hit enter")
start_time = time.time()
print(start_time)

temp = input("Timer will stop when you hit enter. Try for ")
stop_time = time.time()
print(stop_time)

total_time = stop_time - start_time
print("You took this many seconds:", total_time)

total_time = abs(total_time - 10)

if total_time < 0.1:
    print("Incredible!")