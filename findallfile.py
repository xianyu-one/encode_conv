#!/usr/bin/env python
#coding:utf-8
#version:3.8.5

import os

def findAllFile(base):  #用于遍历文件夹
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname