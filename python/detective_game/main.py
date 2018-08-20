# coding:utf-8
"""
主程序文件,选择菜单
"""
from conf import setting
from conf import templates
from module import games
from module import common
import sys

if __name__ == '__main__':
    #开始菜单
    print (templates.GAME_MENU)
    exit_flags = False  #退出标志
    while not exit_flags:
        func = input("请选择功能编号：[1-4]")
        if func not in ("1", "2", "3", "4"):
            print('重新选择')
            continue

        #退出吗
        if func == "4":
            exit_flags = True
            continue

        #游戏背景
        if func == "1":
            print(templates.GAME_TITLE.format(currole="", appoment=""))
            common.load_begin()

        #查看人物信息
        if func == "2":
            dir_di = common.format_info(common.load_info("direnjie"))
            dir_li = common.format_info(common.load_info("liyuanfang"))
            print(templates.ROLE_INFO.format(di=dir_di, li=dir_li))

        if func == "3":
            games.start()




