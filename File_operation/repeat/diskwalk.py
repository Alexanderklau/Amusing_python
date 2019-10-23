# coding: utf-8

__author__ = "lau.wenbo"


import os,sys


class diskwalk(object):
    def __init__(self, path):
        self.path = path
    def paths(self):
        path = self.path
        path_collection = (os.path.join(root,fn) for root,dirs,files in os.walk(path) for fn in files)
        return path_collection

