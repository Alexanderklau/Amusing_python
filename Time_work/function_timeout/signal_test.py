# coding: utf-8
__author__ = 'Yemilice_lau'

import signal


def time_limit(interval):
    def wraps(func):
        def handler():
            raise RuntimeError()

        def deco(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(interval)
            res = func(*args, **kwargs)
            signal.alarm(0)
            return res

        return deco

    return wraps
