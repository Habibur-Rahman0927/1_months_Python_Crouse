
import time

t = time.gmtime()
print(t)
print(t.tm_year)
print(t.tm_hour)
print(t[0])
print(t[3])

t = time.localtime()
print(t)


start = time.time()
print(start)
count = 0
while count <= 1000:
    count += 1

stop = time.time()
print('Total time: ', stop-start)


start = time.time()
time.sleep(3)
stop = time.time()
print('Paused Time: ', stop-start)