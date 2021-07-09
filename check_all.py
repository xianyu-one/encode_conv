#!/usr/bin/env python
#coding:utf-8
#version:3.8.5

import os,chardet,decide_

_check = ''

def check_encode(path):       #检测得到编码方式
    with open(path, 'rb') as f:    
        conv_original = chardet.detect(f.read())["encoding"]
        return(conv_original)

def check_conv(conv):   #检测是否需要转换为特定格式
    if conv == _check:    
        conv_back = 'UTF-8'
        return(conv_back)
    else:
        conv_back = conv
        return(conv_back)

def check_path_extension(path_original,extension_original):   #检测用户输入文件夹路径以及文件后缀
    path = decide_.decide_path(path_original)
    if extension_original == _check:
        extension = extension_original
    else:
        extension = decide_.decide_extension(extension_original)
    back = {'path':path, 'extension':extension}
    return(back)

