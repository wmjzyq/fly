# coding=utf-8
import os
import random
import datetime
from controller.UserController import user
from controller.AdminController import admin
from controller.ReporterController import reporter
from controller.ArticleController import article
from controller.BackfeedController import backfeed
from controller.IndexController import index
from flask import Flask, render_template, request, redirect,url_for,make_response


app = Flask(__name__)
app.secret_key = "wafgawre25qasdf"
'''
注册上传图片路由
'''
def gen_rnd_filename():
    filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))

@app.route('/ckupload/', methods=['POST', 'OPTIONS'])
def ckupload():
    error = ''
    url = ''
    callback = request.args.get("CKEditorFuncNum")

    if request.method == 'POST' and 'upload' in request.files:
        fileobj = request.files['upload']
        fname, fext = os.path.splitext(fileobj.filename)
        rnd_name = '%s%s' % (gen_rnd_filename(), fext)
        filepath = os.path.join(app.static_folder, 'upload', rnd_name)
        # 检查路径是否存在，不存在则创建
        dirname = os.path.dirname(filepath)
        if not os.path.exists(dirname):
            try:
                os.makedirs(dirname)
            except:
                error = 'ERROR_CREATE_DIR'
        elif not os.access(dirname, os.W_OK):
            error = 'ERROR_DIR_NOT_WRITEABLE'

        if not error:
            fileobj.save(filepath)
            url = url_for('static', filename='%s/%s' % ('upload', rnd_name))
    else:
        error = 'post error'

    res = """<script type="text/javascript">
  window.parent.CKEDITOR.tools.callFunction(%s, '%s', '%s');
</script>""" % (callback, url, error)

    response = make_response(res)
    response.headers["Content-Type"] = "text/html"
    return response

'''
注册蓝图
'''
app.register_blueprint(index)
app.register_blueprint(user)
app.register_blueprint(admin)
app.register_blueprint(reporter)
app.register_blueprint(article)
app.register_blueprint(backfeed)


if __name__ == '__main__':
    app.run(port=8080, debug=True)