#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Jeerrzy
# @File     : demo.py
# @Time     : 2023/10/23 18:18
# @Project  : homework


from models import MyImageObject


if __name__ == "__main__":
    image = MyImageObject(
        image_path='./images/9.png',
        annotation_path='./annotations/9.xml'
    )
    image.show(annotation=True)





