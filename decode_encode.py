#!/usr/bin/env python
#coding:utf-8
#version:3.8.5

import read_write

def de_en(path,conv_original,conv):   #编码转换
    print('正在转换：' + path)
    flie_data_original = read_write.read_file(path)
    flie_data_orig = flie_data_original.decode(conv_original)
    flie_data = flie_data_orig.encode(conv)
    read_write.write_file(path,flie_data)