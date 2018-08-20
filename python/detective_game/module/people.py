#!/usr/bin/env python
"""
角色类模块
"""

import json
import time
import random

class Role(object):
    def __init__(self, **kwargs):
        """
        构造函数,传入参数为一个字典
        :param kwargs:用户信息字典
        :return:
        """
        self.name = kwargs["name"]
        self.alias = kwargs["alias"]
        self.sword = kwargs["sword"]
        self.blood = int(kwargs["blood"])
        self.kongfu = kwargs["kongfu"]
        self.introduce = kwargs["introduce"]
        self.talkside = "R"

    def jiezhao(self, blood, rnum):
        """
        接招函数，如果数字命中则减血,否则为命中
        :param blood: 命中后扣的生命值
        :param rnum: 随机数，如果随机数==1则命中
        :return: 是否命中
        """
        if rnum == 1:
            self.blood -= int(blood)
            print("\033[31;1m {name}躲闪不急,被刺中一刀!\033[0m".format(name=self.name))
            return True
        else:
            print("\033[33;1m {name}一个快闪,躲过了一劫。\033[0m".format(name=self.name))
            return False

    def talk(self, talkmsg, types):
        """
        对白说函数
        :param types: 显示的类型, L 左边显示 R： 右边显示
        :param talkmsg:说的内容
        :return: 返回完整对话信息
        """
        _status = ""
        blood = int(self.blood)
        if 180 < blood <= 200:
            _status = "怒吼一声"
        if 100 < blood <= 180:
            _status = "大嚷一声"
        if 50 < blood <= 100:
            _status = "气血不足"
        if 0 < blood <= 50:
            _status = "奄奄一息"

        show_msg = "{user}[{status}]: {msg} ".format(user=self.name,
                                                     status=_status,
                                                     msg=talkmsg)
        if types == "L":
            print(("\033[1;31m{0}\033[0m;".format(show_msg)).ljust(100, ' '))
        if types == "R":
            print(("\033[1;30m{0}\033[0m;".format(show_msg)).rjust(100, ' '))
        time.sleep(1)

    def choose_skill(self):
        """
        选择技能、返回技能的攻击值
        :return: 技能攻击值
        """
        skills = json.loads(self.kongfu)
        skill_list = list(skills.keys())
        # for s in skills.keys():
        #    skill_list.append(s)
        flag = False
        while not flag:
            skill = input("\033[33;1m({4})请选择招式[ 1:{0}, 2:{1},3:{2},4:{3}]:\033[0m".format(skill_list[0],
                                                                                           skill_list[1],
                                                                                           skill_list[2],
                                                                                           skill_list[3],
                                                                                           self.name)).strip()
            if skill not in ("1", "2", "3", "4"):
                continue
            else:
                flag = True
        skill_value = skills[skill_list[int(skill) - 1]]
        return skill_value

    @property
    def is_main(self):
        """
        设置角色为主角色属性，设置后主角色的对话信息显示在左边
        :return:
        """
        self.talkside = "L"

    def auto_skill(self):
        """
        设置主角色后的另一个角色将采用自动获取招式并攻击，此模块用来随机获取招式
        :return: 返回招式的攻击值
        """
        rand_int = random.randrange(4)
        # 获取对象的招式信息,返回的是一个字典（从xml中load）
        skill_dict = json.loads(self.kongfu)
        # 提取所有招式为列表
        skilllist = list(skill_dict.keys())
        # 随机取一个
        rand_skill = skilllist[rand_int]
        print(("\n\033[1;34m 看招! {0} 发起一个 【{1}】 大招!\033[0m;".format(self.name, rand_skill)).rjust(100, ' '))
        # 返回该招式对应的攻击值
        return skill_dict[rand_skill]

    @property
    def is_alive(self):
        """
        判断角色对象是否还有生命值。
        :return: 角色对象的blood值小于等于0 表示角色完蛋了,返回False，否则返回True
        """
        if self.blood <= 0:
            return False
        else:
            return True
