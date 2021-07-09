#!/usr/bin/env python
#coding:utf-8
#version:3.8.5

import os,chardet,check_all,decode_encode,decide_

_check = ''
_check2 = 'None' 

def encode_conv_body(path_original,extension_original,conv_original,conv):
    path_extension_back = check_all.check_path_extension(path_original,extension_original)
    path = str(path_extension_back['path'])      #将path定义为正确的文件路径格式
    print('文件夹路径为：' + path)
    extension = str(path_extension_back['extension'])      #将extension定义为正确的文件后缀格式
    print('文件后缀为：' + extension)
    conv = check_all.check_conv(conv)   #检测是否默认输出编码UTF-8
    print('转换为' + conv + '编码')
    print('格式化输入完成！')

    flielist = os.listdir(path)
    if extension == _check:
        for item in flielist:
            tar = path + item
            if conv_original == _check:
                conv_check_back = str(check_all.check_encode(tar))
                if conv_check_back == _check2:
                    print('文件 ' + tar + ' 编码未能成功识别')
                else:
                    decode_encode.de_en(tar,conv_check_back,conv)
            else:
                conv_check_back = conv_original
                decode_encode.de_en(tar,conv_check_back,conv)      
    else:
        for item in flielist:
            if item.endswith(extension):
                tar = path + item
                if conv_original == _check:
                    conv_check_back = str(check_all.check_encode(tar))
                    if conv_check_back == _check2:
                        print('文件 ' + tar + ' 编码未能成功识别')
                    else:
                        decode_encode.de_en(tar,conv_check_back,conv)
                else:
                    conv_check_back = conv_original
                    decode_encode.de_en(tar,conv_check_back,conv)

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