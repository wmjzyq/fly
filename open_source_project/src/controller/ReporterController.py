from flask import Blueprint, render_template, request, session
from model.SimpleUser import SimpleUser
from model.ReporterUser import ReporterUser
from model.UserChangeLog import UserChangeLog
from model.Admin import Admin
from model.Article import Article

reporter = Blueprint("reporter", __name__)

@reporter.route("/reporter_article_manager")
def articleManager():
    username = session.get("username")
    arts = Article.select().where(Article.detail_source == username)
    return render_template("reporter_article_manager.html", atricles=arts)

@reporter.route("/reporter_article_manager.do", methods = ['POST'])
def article_Manager():
    username = session.get("username")
    date = request.form["date"]
    arts = Article.select().where((Article.detail_source == username) & (Article.time % (date+'%')))
    return render_template("reporter_article_manager.html", atricles=arts)

@reporter.route("/reporter_article_upload")
def articleUpload():
    return render_template("reporter_article_upload.html")