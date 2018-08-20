#coding:utf-8
"""
游戏主程序,开始游戏KO模式
start()方法开始进行游戏
print_status()方法显示生命值状态信息
"""
import random
from module import common
from module.people import Role
from files import attack_talk

def print_status(currobj, otherobj, attack_status):
    """
    根据攻击的结果输出生命值信息
    :param currobj:当前选中角色对象
    :param otherobj:对方角色
    :param attack_status:攻击的状态，True(攻击成功) False(攻击失败）
    :return:
    """
    # 显示对话
    if attack_status:
        otherobj.talk(attack_talk.attack_succ_msg[random.randrange(4)], otherobj.talkside)
    else:
        otherobj.talk(attack_talk.attack_fail_msg[random.randrange(4)], otherobj.talkside)

    #打印双方当前生命值
    print("\033[1;36m【{curr}】生命值{life1}，【{other}】 生命值：{life2}\033[0m".format(curr=currobj.name,
                                                                             life1=currobj.blood,
                                                                             other=otherobj.name,
                                                                             life2=otherobj.blood))

def start():
    # 从配置文件获取角色信息
    direnjie_info = common.load_info("direnjie")
    liyuanfang_info = common.load_info("liyuanfang")

    # 实例化两个角色对象
    direnjie =Role(**direnjie_info)
    liyuanfang =Role(**liyuanfang_info)

    print("请选择角色：")
    #根据用户选择一个主角色
    # flag = False
    # while not flag:
    choose = input("\033[1;31m 请选择游戏角色 1->狄仁杰   2->李元芳 ； \033[31m;")
    if choose == "1":
        direnjie.is_main
        currobj = direnjie
        otherobj = liyuanfang
    else:
        liyuanfang.is_main
        currobj = liyuanfang
        otherobj = direnjie
        # flag = True

    direnjie.talk("元芳，看招啊！", direnjie.talkside)
    liyuanfang.talk("大人，我不服！", liyuanfang.talkside)
    direnjie.talk("不服来战啊！", direnjie.talkside)

    exit_flag = False
    while not exit_flag:
    #主角色选择攻击招式
        skillvalue = currobj.choose_skill()
    #对手接招
        jstatus = otherobj.jiezhao(skillvalue, random.randrange(3))
        print_status(currobj, otherobj, jstatus)
    #判断对手是否被干掉
        if not otherobj.is_alive:
            print("\n\033[33;1m 终于,{0} 完胜 {1}, 不愧是{2}!!!\033[0m;".format(currobj.name, otherobj.name, currobj.alias))
            exit_flag = True

        # 对手发招(自动)
        skillvalue = otherobj.auto_skill()
        # 主角色接招
        jstatus = currobj.jiezhao(skillvalue, random.randrange(3))
        print_status(otherobj, currobj, jstatus)

        # 主角色活着吗?
        if not currobj.is_alive:
            print("\n\033[33;1m经过多个回合,{0} 不敌 {1}, 应声倒下,吐血而亡!!!\033[0m;".format(currobj.name, otherobj.name))
            exit_flag = True
    print("\nGAME OVER ")


