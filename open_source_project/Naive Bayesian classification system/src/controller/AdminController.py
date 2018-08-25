from flask import Blueprint, render_template, request, session, redirect
from model.SimpleUser import SimpleUser
from model.ReporterUser import ReporterUser
from model.UserChangeLog import UserChangeLog
from model.Admin import Admin
from model.Backfeed import Backfeed
from model.Article import Article

admin = Blueprint("admin", __name__)
'''
管理员文章管理路由
'''
@admin.route("/admin_article_manager")
def articleManager():
	articles = Article.select()
	return render_template("admin_article_manager.html", articles=articles)
'''
文章查询路由
'''
@admin.route("/admin_article_manager.do", methods=["POST"])
def article_Manager():
	date = request.form["date"]
	name = request.form["name"].strip()
	if name == '':
		articles = Article.select().where(Article.time % (date + '%'))
		return render_template("admin_article_manager.html", articles=articles)
	if name != '':
		articles = Article.select().where((Article.time % (date+'%')) & (Article.detail_source == name))
		return render_template("admin_article_manager.html", articles=articles)
'''
管理员确认用户身份
'''
@admin.route("/admin_user_manager")
def userManager():
	simpleUser = SimpleUser.select()
	reporterUser = ReporterUser.select()
	return render_template("admin_user_manager.html", simpleUser=simpleUser, reporterUser=reporterUser)
'''
管理员查看用户反馈
'''
@admin.route("/admin_backfeed_manager")
def backfeedManager():
	backfeeds = Backfeed.select()
	return render_template("admin_backfeed_manager.html", backfeeds=backfeeds)
'''
管理员删除新闻
'''
@admin.route("/admin_article_delete")
def articleDelete():
	id = request.args.get("id")
	art = Article.get(Article.id == id)
	art.delete_instance()
	return redirect("/admin_article_manager")