from flask import Blueprint, render_template, request, session, redirect
from peewee import fn
from model.SimpleUser import SimpleUser
from model.ReporterUser import ReporterUser
from model.UserChangeLog import UserChangeLog
from model.Admin import Admin
from model.Article import Article
from model.Comment import Comment

import random

index = Blueprint("index", __name__)
'''
登陆首页
'''
@index.route("/")
def indexRoute():
    articles = Article.select().order_by(fn.Rand()).limit(20)
    return render_template("index.html", articles=articles)

@index.route("/news_society")
def news_society():
    articles = select_article("news_society")
    return render_template("news_society.html", articles=articles)

@index.route("/news_entertainment")
def news_entertainment():
    articles = select_article("news_entertainment")
    return render_template("news_entertainment.html", articles=articles)

@index.route("/news_military")
def news_military():
    articles = select_article("news_military")
    return render_template("news_military.html", articles=articles)

@index.route("/news_tech")
def news_tech():
    articles = select_article("news_tech")
    return render_template("news_tech.html", articles=articles)

@index.route("/news_sports")
def news_sports():
    articles = select_article("news_sports")
    return render_template("news_sports.html", articles=articles)

@index.route("/news_finance")
def news_finance():
    articles = select_article("news_finance")
    return render_template("news_finance.html", articles=articles)

@index.route("/news_world")
def news_world():
    articles = select_article("news_world")
    return render_template("news_world.html", articles=articles)

@index.route("/news_history")
def news_history():
    articles = select_article("news_history")
    return render_template("news_history.html", articles=articles)

@index.route("/news_regimen")
def news_regimen():
    articles = select_article("news_regimen")
    return render_template("news_regimen.html", articles=articles)

def select_article(tag):
    articles =  Article.select().where(Article.tag.contains(tag)).order_by(Article.time.desc())
    return articles