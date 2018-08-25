from flask import Blueprint, render_template, request, session, redirect
from model.SimpleUser import SimpleUser
from model.ReporterUser import ReporterUser
from model.UserChangeLog import UserChangeLog
from model.Admin import Admin

user = Blueprint("user", __name__)

@user.route("/register")
def register():
	return render_template("register.html")

@user.route("/login")
def login():
	return render_template("login.html")
'''
注册后台处理
'''
@user.route("/register.do", methods=['POST'])
def register_do():
	username = request.form["username"]
	password = request.form["password"]
	status = request.form["status"]
	Simplenames = SimpleUser.select(SimpleUser.username)
	Reporternames = ReporterUser.select(ReporterUser.username)

	if username == None or len(username.strip()) == 0 or password == None or len(password.strip()) == 0:
		return render_template("register_error.html")
	#普通用户
	if status == "simple":
		if username != None:
			for Simple_name in Simplenames:
				if Simple_name.username == username:
					return render_template("register_error.html")
		simpleUser = SimpleUser(username=username, password=password)
		id = simpleUser.save()
		log = UserChangeLog(userId=id, operate=UserChangeLog.USRE_REGISTER)
		log.save()
		return render_template("register_success.html")

	# reporter user register
	elif status == "reporter":
		if username != None:
			for Reporter_name in Reporternames:
				if Reporter_name.username == username:
					return render_template("register_error.html")
		reporterUser = ReporterUser(username=username, password=password)
		id = reporterUser.save()
		log = UserChangeLog(userId=id, operate=UserChangeLog.USRE_REGISTER)
		log.save()
		return render_template("register_success.html")

	return render_template("register_error.html")
'''
登陆后台处理
'''
@user.route("/login.do", methods=['POST'])
def login_do():
	username = request.form["username"]
	password = request.form["password"]
	status = request.form["status"]

	if username == None or len(username.strip()) == 0 or password == None or len(password.strip()) == 0:
		return render_template("login_error.html")

	if status == "simple":
		users = SimpleUser.select().where(SimpleUser.username==username, SimpleUser.password==password)
		if len(users) != 0:
			session["id"] = users[0].id
			session["username"] = users[0].username
			session["status"] = "simple"
			return redirect("/")
		else:
			return render_template("login_error.html")
	elif status == "reporter":
		users = ReporterUser.select().where(ReporterUser.username == username, ReporterUser.password == password)
		if len(users) != 0:
			session["id"] = users[0].id
			session["username"] = users[0].username
			session["status"] = "reporter"
			return redirect("/")
		else:
			return render_template("login_error.html")
	else:
		users = Admin.select().where(Admin.username == username, Admin.password == password)
		if len(users) != 0:
			session["id"] = users[0].id
			session["username"] = users[0].username
			session["status"] = "admin"
			return redirect("/")
		else:
			return render_template("login_error.html")
'''
用户信息
'''
@user.route("/info")
def info():
	id = session.get("id")
	status = session.get("status")
	if status == "simple":
		u = SimpleUser.get(SimpleUser.id == id)
		return render_template("info.html", username=u.username, password=u.password)
	elif status == "reporter":
		u = ReporterUser.get(ReporterUser.id == id)
		return render_template("info.html", username=u.username, password=u.password)
	elif status == "admin":
		u = Admin.get(Admin.id == id)
		return render_template("info.html", username=u.username, password=u.password)
	else:
		return render_template("error.html")

@user.route("/change_info")
def changeInfo():
	id = session.get("id")
	status = session.get("status")
	if status == "simple":
		u = SimpleUser.get(SimpleUser.id == id)
		return render_template("change.html", username=u.username, password=u.password)
	elif status == "reporter":
		u = ReporterUser.get(ReporterUser.id == id)
		return render_template("change.html", username=u.username, password=u.password)
	elif status == "admin":
		u = Admin.get(Admin.id == id)
		return render_template("change.html", username=u.username, password=u.password)
	else:
		return render_template("error.html")

@user.route("/change.do", methods=["POST"])
def change_do():
	id = session.get("id")
	status = session.get("status")

	username = request.form["username"]
	password = request.form["password"]

	if status == "simple":
		u = SimpleUser.get(SimpleUser.id == id)
		u.username = username
		u.password = password
		u.save()
		return render_template("change_success.html")
	elif status == "reporter":
		u = ReporterUser.get(ReporterUser.id == id)
		u.username = username
		u.password = password
		u.save()
		return render_template("change_success.html")
	elif status == "admin":
		u = Admin.get(Admin.id == id)
		u.username = username
		u.password = password
		u.save()
		return render_template("change_success.html")
	else:
		return render_template("error.html")

@user.route("/logout")
def logout():
	del session["id"]
	del session["username"]
	del session["status"]
	return redirect("/")

@user.route("/user_delete")
def user_delete():
	id = request.args.get("id")
	status = request.args.get("status")
	if status == "simple":
		u = SimpleUser.get(SimpleUser.id == id)
		u.delete_instance()
	elif status == "reporter":
		u = ReporterUser.get(ReporterUser.id == id)
		u.delete_instance()

	return redirect("/admin_user_manager")