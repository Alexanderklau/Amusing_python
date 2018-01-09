import multiprocessing
import sys


def worker_with(lock, f):
    with lock:
        fs = open(f, 'a+')
        n = 20
        while n > 1:
            fs.write("Lockd acquired via with\n")
            n -= 1
        fs.close()


def worker_no_with(lock, f):
    lock.acquire()
    try:
        fs = open(f, 'a+')
        n = 20
        while n > 1:
            fs.write("Lock acquired directly\n")
            n -= 1
        fs.close()
    finally:
        lock.release()


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    f = "file.txt"
    w = multiprocessing.Process(target=worker_with, args=(lock, f))
    nw = multiprocessing.Process(target=worker_no_with, args=(lock, f))
    w.start()
    nw.start()
    print "end"