#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Jeerrzy
# @File     : models.py
# @Time     : 2023/10/23 18:24
# @Project  : homework


import cv2
import copy
import xml.etree.ElementTree as ET


class MyImageObject(object):
    """
    MyImageObject: 自定义图像对象，用于封装常用操作
    """
    def __init__(self, image_path, annotation_path):
        self.image_data = cv2.imread(image_path)
        self.annotation_list = self.parse_xml_annotation_to_bbox_list(annotation_path)
        self.object_list = self.get_object_list()

    def show(self, annotation=False):
        """
        :argument: 在屏幕直接显示图片，并等待鼠标点击
        :param: 是否显示标注框信息，默认不显示
        """
        if not annotation:
            cv2.imshow('demo', self.image_data)
        else:
            image_data = copy.deepcopy(self.image_data)
            for (x1, y1, x2, y2) in self.annotation_list:
                cv2.rectangle(image_data, (x1, y1), (x2, y2), (0, 255, 0), 1)
            cv2.imshow('demo', image_data)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def parse_xml_annotation_to_bbox_list(xml_file_path):
        """
        :param: VOC标准的XML格式的目标检测数据标注文件路径
        :return: 包含全部标注外接矩形BBOX(x1, y1, x2, y2)的列表
        """
        bbox_list = []
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        for obj in root.iter('object'):
            xml_box = obj.find('bndbox')
            x_min = int(xml_box.find('xmin').text)
            y_min = int(xml_box.find('ymin').text)
            x_max = int(xml_box.find('xmax').text)
            y_max = int(xml_box.find('ymax').text)
            bbox_list.append([x_min, y_min, x_max, y_max])
        return bbox_list

    def get_object_list(self):
        """
        :return: 包含全部算法处理得到的目标外接矩形BBOX(x1, y1, x2, y2)的列表
        """
        object_list = []
        """
        在此补充处理代码
        ...
        ...
        ...
        """
        return object_list

    def calculate_metrics(self):
        """
        :return: 衡量算法处理结果的性能指标
        """
        """
        在此补充处理代码
        ...
        ...
        ...
        """
        pass

