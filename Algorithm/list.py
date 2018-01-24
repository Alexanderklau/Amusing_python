#coding: utf-8
# 最基础的遍历无序列表的查找算法
# 时间复杂度O(n)

def sequential_search(lis, key):
    length = len(lis)
    for i in range(length):
        if lis[i] == key:
            return i
        else:
            return False


if __name__ == '__main__':
    LIST = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    result = sequential_search(LIST, 123)
    print(result)
