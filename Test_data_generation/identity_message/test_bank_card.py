# -*- coding: utf-8 -*-
__author__ = 'yemilice_lau'

import re
import random, functools
import collections

with open('card_code') as file:
    data = file.read()
distration = data.split('\n')
card_message = random.choice(distration)
message_list = re.split(r"\s+", card_message)
if len(message_list) == 6:
    num = message_list[4] if message_list[4] else "None"  # 取到银行卡位数(16,19)
    card_bin = message_list[5] if message_list[5] else "None"  # 取到银行卡bin,发卡行标识代码(前六位）
    card_type = message_list[3] if message_list[3] else "None"  # 取到银行卡类型(信用卡，储蓄卡)
    card_num = message_list[2] if message_list[2] else "None"  # 取到银行卡名(牡丹卡，华西通等)
    card_bank = message_list[0] if message_list[0] else "None"  # 银行卡发卡行(招商，工商)
    card_bank_custom_num = int(num) - 6
    card_bank_custom = functools.reduce(lambda x, y: 10 * x + y,
                                        [random.randint(1, card_bank_custom_num - 2)
                                         for x in range(card_bank_custom_num)])
    bank_num = str(card_bin) + str(card_bank_custom)
    a = list(bank_num)
    even_num = a[1::2]  # 计算校验码
    c = []
    for i in even_num:
        c.append(int(i) * 2)
    x = (" ".join(str(i) for i in c))
    print x
    z = []
    for i in x:
        z.append(i)
    while ' ' in z:
        z.remove(' ')
    num = len(z)
    print num


else:
    pass
