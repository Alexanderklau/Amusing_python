# coding: utf-8
__author__ = 'Yemilice_lau'

from threading import Thread
import time

class TimeoutException(Exception):
    pass


ThreadStop = Thread._Thread__stop


def timelimited(timeout):
    def decorator(function):
        def decorator2(*args, **kwargs):
            class TimeLimited(Thread):
                def __init__(self, _error=None, ):
                    Thread.__init__(self)
                    self._error = _error

                def run(self):
                    try:
                        self.result = function(*args, **kwargs)
                    except Exception as e:
                        self._error = str(e)

                def _stop(self):
                    if self.isAlive():
                        ThreadStop(self)

            t = TimeLimited()
            t.start()
            t.join(timeout)

            if isinstance(t._error, TimeoutException):
                t._stop()
                raise TimeoutException('timeout for %s' % (repr(function)))

            if t.isAlive():
                t._stop()
                raise TimeoutException('timeout for %s' % (repr(function)))
            if t._error is None:
                return t.result
            else:
                raise TypeError

        return decorator2

    return decorator

@timelimited(1)
def fun():
    time.sleep(3)

if __name__ == "__main__":
    try:
        fun()
    except Exception as e:
        print("timeout!")
