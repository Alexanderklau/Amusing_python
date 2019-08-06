# coding: utf-8
__author__ = 'Yemilice_lau'

import random


def redbags(money, num):
    while True:
        choice = random.sample(range(1, int(money * 100)), num - 1)
        choice.extend([0, money*100])
        choice.sort()
        for i in range(len(choice)-1):
            if (choice[i+1] - choice[i]) > (money * 100 / num * 2):   #这里控制红包最大的额度
                break
        else:
            return [(choice[i + 1] - choice[i]) / 100 for i in range(num)],choice



print(redbags(100, 10))