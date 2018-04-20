# -*- coding: utf-8 -*-
from app.views.common import *
from sqlalchemy import desc , extract,and_

# 定义蓝图
index_url = Blueprint('index', __name__)


@index_url.route('/')
@login_required  # 登录保护
def index():
    return render_template('index/index.html')


@index_url.route('/index_data', methods=["GET", "POST"])
@login_required  # 登录保护
def index_data():
    if request.method == 'POST':

            hostzc = Hosts.query.filter_by(status=1).count()
            hostlc = Hosts.query.filter_by(status=0).count()

            projectac = Project.query.count()
            deployc = Deploy_logs.query.filter(Deploy_logs.deploy_time.like(time.strftime("%Y-%m-%d", time.localtime()) + "%")).count()

            saltmc = Operation_logs.query.filter(and_(Operation_logs.type == "salt_file"),Operation_logs.time.like(time.strftime("%Y-%m-%d", time.localtime()) + "%")).count()
            cmdc = Operation_logs.query.filter(and_(Operation_logs.type == "cmd_execute"),Operation_logs.time.like(time.strftime("%Y-%m-%d", time.localtime()) + "%")).count()

            userac = Users.query.count()
            useryc = Users.query.filter_by(active=0).count()
            return json.dumps({"code": 1, "msg": u"请求数据成功!", "hostzc": hostzc,"hostlc":hostlc,"projectac":projectac,"deployc":deployc,"saltmc":saltmc,"cmdc":cmdc,"userac":userac,"useryc":useryc})

