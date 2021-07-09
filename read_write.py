#!/usr/bin/env python
#coding:utf-8
#version:3.8.5

import os

def read_file(path):     #读文件
    with open(path,'rb') as f:
        back = f.read()
        return(back)

def write_file(path,read_):     #写文件
    with open(path,'wb+') as f:
        f.write(read_)