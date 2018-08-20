#coding:utf-8

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 角色的基础配置文件
ROLE_FILE = os.path.join(BASE_DIR, "conf/users.xml")

# 剧情文件
FILES = os.path.join(BASE_DIR, "files")
