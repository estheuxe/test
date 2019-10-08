from multiprocessing import Process
import time
import random

def worker(num):
	sleep = random.randrange(1,10)
	time.sleep(sleep)
	print('worker #{}, slept for {}'.format(num,sleep))

for i in range(5):
	t = Process(target=worker, args=(i,))
	t.start()

print('lesgo')