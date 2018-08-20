#coding:utf-8
"""
公共类模块
"""
import os
import json
import time
import xml.etree.ElementTree as ET
from conf import setting

def load_info(uname):
    """
    根据输入名字获取用户的基本信息
    :param uname: 用户名，必须和xml中的key一样
    :return:
    """
    users = setting.ROLE_FILE
    _return_dict = {}

    fobj = ET.parse(users)
    root = fobj.getroot()
    for child in root:
        if child.tag == "user" and child.attrib["key"] == uname:
            for elements in child:
                _return_dict[elements.tag] = elements.text

    return _return_dict

def load_begin():
    """
    打印游戏的背景，从文件中逐行读取文件并打印
    :return:
    """
    file = os.path.join(setting.FILES, "drama")
    with open(file, "rb") as f:
        for line in f.readlines():
            print(line.decode("utf-8"))
            time.sleep(0.6)

def format_info(name_dict):
    """
    将从xml中获取的角色字典信息格式化为str类型，用于填充人物介绍模板
    :param name_dict:角色信息字典
    :return:填充完的模板数据
    """
    template = """
            角色名：{name}
            绰  号: {alias}
            生命值: {blood}
            武  器: {sword}
            技  能: {kongfu}
            介  绍: {introduct}
        """
    template = template.format(name=name_dict["name"],
                               alias=name_dict["alias"],
                               blood=name_dict["blood"],
                               sword=name_dict["sword"],
                               kongfu=",".join(list(json.loads(name_dict["kongfu"]).keys())),
                               introduct=name_dict["introduce"]
                               )
    return template