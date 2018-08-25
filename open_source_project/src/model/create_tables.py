# coding=utf-8
from BaseModel import db
from Admin import Admin
from Article import Article
from Backfeed import Backfeed
from Comment import Comment
from ReporterUser import ReporterUser
from SimpleUser import SimpleUser
from UserChangeLog import UserChangeLog

# 创建表
if __name__ == '__main__':
    db.create_tables([Admin, Article, Backfeed, Comment, ReporterUser, SimpleUser, UserChangeLog])