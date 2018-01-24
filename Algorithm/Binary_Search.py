#coding: utf-8

# 针对有序查找表的二分查找算法
# 时间复杂度O(log(n))

def binary_search(lis, key):
    low = 0
    high = len(lis) - 1
    time = 0
    while low < high:
        time += 1
        mid = int((low + high) / 2)
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            # 打印折半的次数
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False


if __name__ == '__main__':
    LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = binary_search(LIST, 99)
    print(result)