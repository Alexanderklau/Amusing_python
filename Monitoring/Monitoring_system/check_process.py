# coding: utf-8
__author__ = 'lau.wenbo'


import psutil
import prettytable

ps_result = list()

for proc in psutil.process_iter():
    ps_result.append({'name': proc.name(), 'pid': proc.pid, 'cpu_percent': proc.cpu_percent(),
                      'memory_percent': proc.memory_percent()})

table = prettytable.PrettyTable()
table.field_names = ["No.", "Name", "pid", "Memory percent"]
for i, item in enumerate(sorted(ps_result, key=lambda x: x['memory_percent'], reverse=True)):
    table.add_row([i + 1, item['name'], item['pid'], format(item['memory_percent'] / 100, '.2%')])
    if i >= 9:
        break
print table