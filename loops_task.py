import time

start_time = time.time()
curr_time = start_time
count = 0

while curr_time - start_time < 1:
    curr_time = time.time()
    count += 1

print(count)

time1 = time.time()
for iteration in range(count):
    time2 = time.time()

print(time2 - time1)

if time2 - time1 < 1:
    print('for is faster')
else:
    print('while is faster')