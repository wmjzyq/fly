import re
import datetime
from flask import Blueprint, render_template, request, session, redirect
from model.SimpleUser import SimpleUser
from model.ReporterUser import ReporterUser
from model.UserChangeLog import UserChangeLog
from model.Admin import Admin
from model.Article import Article
from model.Comment import Comment
from classify.bayes_classify import classify

pattn = 'src="([\s\S]*?)"'

article = Blueprint("article", __name__)
'''
文章修改
'''
@article.route("/article_update")
def articleUpdate():
	id = request.args.get("id")
	art = Article.get(Article.id  == id)
	return render_template("reporter_article_update.html", article=art)
'''
文章修改后提交
'''
@article.route("/article_update.do", methods=["POST"])
def articleUpdateDo():
	title = request.form["title"]
	content = request.form["content"]

	id = request.args.get("id")
	art = Article.get(Article.id == id)
	art.title = title
	art.content = content
	art.save()
	return render_template("article_update_success.html")
'''
文章上传
'''
@article.route("/article_upload")
def articleUpload():
	return render_template("reporter_article_upload.html")
'''
上传文章存到数据库
'''
@article.route("/article_upload.do", methods=["POST"])
def articleUploadDo():
	id = session.get("id")
	title = request.form["title"]
	content = request.form["content"]
	img = re.compile(pattn).search(content)
	if img != None:
		img = img.group(1)
	if img != None:
		img_url = img
	else:
		img_url = '/static/upload/new.jpg'
	tag = classify(content)
	detail_source = session.get('username')
	time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	art = Article(title=title, content=content, detail_source=detail_source, img_url=img_url, tag=tag, time=time)
	art.save()
	return render_template("article_upload_success.html")
'''
文章删除
'''
@article.route("/article_delete")
def articleDelete():
	id = request.args.get("id")
	art = Article.get(Article.id == id)
	art.delete_instance()
	return render_template("article_delete_success.html")
'''
文章详情
'''
@article.route("/article_detail")
def articleDetail():
	id = request.args.get("id")
	art = Article.get(Article.id == id)
	comments = Comment.select().where(Comment.articleId == id)
	return render_template("article_detail.html", article=art, comments=comments)
'''
文章评论
'''
@article.route("/article_comment.do", methods=["POST"])
def articleComment():
	articleId = request.args.get("articleId")
	# name = request.form["name"]
	username = session.get('username')
	if username != None:
		name = username
	else:
		name = '匿名用户'
	content = request.form["content"]
	time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	comment = Comment(articleId=articleId, name=name, content=content, time=time)
	comment.save()
	return redirect("/article_detail?id=" + articleId)