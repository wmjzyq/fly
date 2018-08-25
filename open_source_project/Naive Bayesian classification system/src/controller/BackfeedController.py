from flask import Blueprint, render_template, request, session, redirect
from model.SimpleUser import SimpleUser
from model.ReporterUser import ReporterUser
from model.UserChangeLog import UserChangeLog
from model.Admin import Admin
from model.Backfeed import Backfeed

backfeed = Blueprint("backfeed", __name__)
'''
文章反馈
'''
@backfeed.route("/backfeed")
def feedback():
    return render_template("backfeed.html")
'''
文章反馈存到数据库
'''
@backfeed.route("/backfeed.do", methods=["POST"])
def feedbackDo():
    content = request.form["content"]
    back = Backfeed(content=content)
    back.save()
    return redirect("/")
'''
反馈删除
'''
@backfeed.route("/backfeed_delete")
def feedbackDelete():
    id = request.args.get("id")
    back = Backfeed.get(Backfeed.id == id)
    back.delete_instance()
    return redirect("/")
