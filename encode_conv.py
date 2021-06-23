#!/usr/bin/env python
#coding:utf-8

import os,chardet

_check = ''

def dicide(path_original,extension_original,conv,conv_original):   #判斷文件路徑以及文件後綴
    if extension_original == _check:   #判断是否指定文件后缀
        if path_original.endswith('/'):   
            path = path_original
            extension = extension_original
            traverse(path, extension,conv,conv_original)
        else:
            path = path_original + '/'
            extension = extension_original
            traverse(path, extension,conv,conv_original)
    else:
        if path_original.endswith('/'):
            path = path_original
            if extension_original.startswith('.'):
                extension = extension_original
                traverse(path, extension,conv,conv_original)
            else:
                extension = '.' + extension_original
                traverse(path, extension,conv,conv_original)
        else:
            path = path_original + '/'
            if extension_original.startswith('.'):
                extension = extension_original
                traverse(path, extension,conv,conv_original)
            else:
                extension = '.' + extension_original
                traverse(path, extension,conv,conv_original)


def traverse(path,extension,conv,conv_original):   #自动遍历文件夹，获取指定文件，并检测是否需要自动检测
    flielist = os.listdir(path)
    for item in flielist:     
        if item.endswith(extension):   #检测文件后缀
            tra = path + item
            if conv_original == _check:  #判断是否指定原编码格式
                if conv == _check:   #判断是否指定目标编码格式
                    conv = 'UTF-8'
                    check_encode(tra,conv,conv_original)
                else:
                    check_encode(tra,conv,conv_original)
            else:
                if conv == _check:
                    conv = 'UTF-8'
                    bash_iconv(tra,conv,conv_original)
                else:
                    bash_iconv(tra,conv,conv_original)

def traverse_not_designat(path,extension,conv,conv_original):   #自动遍历文件夹，并检测是否需要自动检测
    flielist = os.listdir(path)
    for item in flielist:
        tar = path + item
        if conv_original == _check:
            if conv == _check:
                conv = 'UTF-8'
                check_encode(tra,conv,conv_original)
            else:
                check_encode(tra,conv,conv_original)
        else:
            if conv == _check:
                conv = 'UTF-8'
                bash_iconv(tra,conv,conv_original)
            else:
                bash_iconv(tra,conv,conv_original)

def check_encode(tra,conv,conv_original):
    with open(tra, 'rb') as f:    
        conv_original = chardet.detect(f.read())["encoding"]     #检测得到编码方式
    bash_iconv(tra,conv,conv_original)



def bash_iconv(tar,conv,conv_original):    #调用系统命令iconv
    sh_iconv = os.system('iconv -f ' + conv_original + ' -t ' + conv + tar + ' -o ' + tar)

path_original = input('请输入需要转换的文件夹路径：')
print('如果不需要指定文件后缀请直接回车')
extension_original = input('请输入需要转换的文件的后缀：')
print('如果使用自动编码检测请直接回车')
conv_original = input('请输入原编码：')
print('如果直接回车，将默认转换为UTF-8')
conv = input('请输入目标编码')

dicide(path_original,extension_original,conv,conv_original)