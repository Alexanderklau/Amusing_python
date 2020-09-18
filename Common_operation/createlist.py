# coding: utf-8

__author__ = "lau.wenbo"


a = [1,2]
b = [3,4]
c = [5,6]

if __name__ == "__main__":
    # 方法1
    print(sum((a,b,c),[]))
    # 方法2
    print(a + b + c)
    # 方法3
    