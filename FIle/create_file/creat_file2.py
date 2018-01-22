#coding: utf-8
__author__ = 'lau.wenbo'
import re

def produceBnf(infilename,outfilename):
  List=[]
  with open(infilename,'r') as inf:
    for line in inf.readlines():
      List.append(re.match("正则表达式").group())
  with open(outfilename,'w') as outf:
    i=0
    outf.write("文件头")
    for command in List:
        outf.write("写入刚刚读取的内容（也可能是某种对应关系）")
        outf.write("写入其他内容")
    outf.write("写入文件尾")