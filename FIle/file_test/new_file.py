from multiprocessing import Pool
import time


def mycallback(x):
    with open('123.txt', 'a+') as f:
        f.writelines(str(x))


def sayHi(num):
    return num


if __name__ == '__main__':
    e1 = time.time()
    pool = Pool()

    for i in range(100):
        pool.apply_async(sayHi, (i,), callback=mycallback)

    pool.close()
    pool.join()
    e2 = time.time()
    print float(e2 - e1)