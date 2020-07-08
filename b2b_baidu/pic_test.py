#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 13:38
# @Author  : Zhang Fei
# @Site    : 
# @File    : pic_test.py
# @Software: PyCharm

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor

# 本模块的功能:<更改图片尺寸>

import os
import os.path
from PIL import Image
'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''
def ResizeImage(filein, fileout, width, height, type):
  img = Image.open(filein)
  out = img.resize((width, height),Image.ANTIALIAS)
  #resize image with high-quality
  out.save(fileout, type)



if __name__ == "__main__":
  filein = r'./6928872808309_0.jpg'
  fileout = r'./6928872808309_01.jpg'
  width = 210
  height = 210
  # type = 'jpg'
  type = 'png'
  ResizeImage(filein, fileout, width, height, type)
