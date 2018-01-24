#coding: utf-8

# 插入排序

def insert_sort(lists):
    count = len(lists)  #统计总数
    for i in range(1, count):   #遍历
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

list = [23,33,123,456,123]
print insert_sort(list)