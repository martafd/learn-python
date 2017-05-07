import threading
import multiprocessing
import time
import random
from multiprocessing import Pool

def worker(number):
    sl = random.randrange(1, 10)
    time.sleep(sl)
    print "Worker {0} sleep {1} seconds".format(number, sl)

print "All threads are running, let's wait until they end!"

for i in range(5):
    t = multiprocessing.Process(target=worker, args=(i,))
    t.start()

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(3)
    print p.map(f, [1, 2, 3])
