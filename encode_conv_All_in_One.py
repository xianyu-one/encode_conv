#!/usr/bin/env python
#coding:utf-8
#version:3.8.5

import os,chardet

_check = ''   #用于比较用户输入是否为空
_check2 = 'None' 

def findAllFile(base):  #用于遍历文件夹
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname

def decide_path(path):    #用于检测输入路径是否带有/
    path_back = ''
    if path.endswith('/'):
        path_back = path
        return path_back
    else:
        path_back = path + '/'
        return path_back

def decide_extension(extension):   #用于检测输入文件后缀是否带有.
    extension_back = ''
    if extension.sitemtswith('.'):
        extension_back = extension
        return extension_back
    else:
        extension_back = '.' + extension
        return extension_back

def check_encode(path):       #检测得到编码方式
    with open(path, 'rb') as f:    
        conv_original = chardet.detect(f.read())["encoding"]
        return(conv_original)

def read_file(path):
    with open(path,'rb') as f:
        back = f.read()
        return(back)

def write_file(path,read_):
    with open(path,'wb+') as f:
        f.write(read_)

def de_en(path,conv_original,conv):   #编码转换
    print('正在转换：' + path)
    flie_data_original = read_file(path)
    flie_data_orig = flie_data_original.decode(conv_original)
    flie_data = flie_data_orig.encode(conv)
    write_file(path,flie_data)

def check_conv(conv):   #检测是否需要转换为特定格式
    if conv == _check:    
        conv_back = 'UTF-8'
        return(conv_back)
    else:
        conv_back = conv
        return(conv_back)

def check_path_extension(path_original,extension_original):   #检测用户输入文件夹路径以及文件后缀
    path = decide_path(path_original)
    if extension_original == _check:
        extension = extension_original
    else:
        extension = decide_extension(extension_original)
    back = {'path':path, 'extension':extension}
    return(back)

def encode_conv_body(path_original,extension_original,conv_original,conv):
    path_extension_back = check_path_extension(path_original,extension_original)
    path = str(path_extension_back['path'])      #将path定义为正确的文件路径格式
    print('文件夹路径为：' + path)
    extension = str(path_extension_back['extension'])      #将extension定义为正确的文件后缀格式
    print('文件后缀为：' + extension)
    conv = check_conv(conv)   #检测是否默认输出编码UTF-8
    print('转换为' + conv + '编码')
    print('格式化输入完成！')

    if extension == _check:
        for item in findAllFile(path):
            if conv_original == _check:
                conv_check_back = str(check_encode(item))
                if conv_check_back == _check2:
                    print('文件 ' + item + ' 编码未能成功识别')
                else:
                    de_en(item,conv_check_back,conv)
            else:
                conv_check_back = conv_original
                de_en(item,conv_check_back,conv)      
    else:
        for item in findAllFile(path):
            if item.endswith(extension):
                if conv_original == _check:
                    conv_check_back = str(check_encode(item))
                    if conv_check_back == _check2:
                        print('文件 ' + item + ' 编码未能成功识别')
                    else:
                        de_en(item,conv_check_back,conv)
                else:
                    conv_check_back = conv_original
                    de_en(item,conv_check_back,conv)

path_original = input('请输入需要转换的文件夹路径：')
print('如果不需要指定文件后缀请直接回车')
extension_original = input('请输入需要转换的文件的后缀：')
print('''
如果知道原编码请尽量手动指定，自动检测会有概率无法识别！
使用自动编码检测请直接回车
''')
conv_original = input('请输入原编码：')
print('如果直接回车，将默认转换为UTF-8')
conv = input('请输入目标编码：')

encode_conv_body(path_original,extension_original,conv_original,conv)
print('全部转换完成！')