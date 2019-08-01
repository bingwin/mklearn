from flask import Flask,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask_news_mysql.forms import NewsForm
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@192.168.153.151:3306/school?charset=utf8'
app.config['SECRET_KEY'] = 'a random string'
db = SQLAlchemy(app)


class News(db.Model):
	__tablename__ = 'news'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), nullable=False)
	content = db.Column(db.String(2000), nullable=False)
	types = db.Column(db.String(10), nullable=False)
	image = db.Column(db.String(300))
	auther = db.Column(db.String(20))
	view_count = db.Column(db.Integer, default=0)
	created = db.Column(db.DateTime)
	is_valid = db.Column(db.Boolean, default=1)

	def __repr__(self):
		return '<News %r>' % self.title

# 创建表
# db.create_all()

# 新闻首页
@app.route('/')
def index():
	news_list = News.query.all()
	return render_template('index.html' ,news_list=news_list)

# 新闻类别
@app.route('/cat/<name>/')
def cat(name):
	news_list = News.query.filter(News.types == name)
	return render_template('cat.html', name=name, news_list=news_list)

# 详情页面
@app.route('/detail/<int:pk>/')
def detail(pk):
	new_obj = News.query.get(pk)
	return render_template('detail.html', new_obj=new_obj)

#############################

# 后台首页
@app.route('/admin/')
@app.route('/admin/<int:page>/')
def admin(page=None):
	if page is None:
		page = 1
	news_list = News.query.filter_by(is_valid=True).paginate(page=page,per_page=5)
	return render_template('admin/index.html', page_data=news_list)

# 修改新闻详情
@app.route('/admin/update/<int:pk>/', methods=('GET', 'POST'))
def update(pk):
	new_obj = News.query.get(pk)
	if not new_obj:
		return redirect(url_for('admin'))

	form = NewsForm(obj=new_obj)
	if form.validate_on_submit():
		# 获取数据
		new_obj.title=form.title.data,
		new_obj.content=form.content.data,
		new_obj.types=form.types.data,
		new_obj.image=form.image.data,
		new_obj.created=datetime.now()
		# 保存数据
		db.session.add(new_obj)
		db.session.commit()
		# 成功后跳转
		return redirect(url_for('admin'))

	return render_template('admin/update.html', form=form)

# 删除新闻详情
@app.route('/admin/delete/<int:pk>/', methods=('GET', 'POST'))
def delete(pk):
	new_obj = News.query.get(pk)
	if not new_obj:
		return 'no'
	new_obj.is_valid = False
	db.session.add(new_obj)
	db.session.commit()
	return 'yes'

# 增加新闻详情
@app.route('/admin/add/', methods=('GET', 'POST'))
def add():
	form = NewsForm()
	if form.validate_on_submit():
		# 获取数据
		new_obj = News(
			title = form.title.data,
			content = form.content.data,
			types = form.types.data,
			image = form.image.data,
			created = datetime.now()
		)
		# 保存数据
		db.session.add(new_obj)
		db.session.commit()
		# 成功后跳转
		return redirect(url_for('admin'))
	return render_template('admin/add.html', form=form)

if __name__ == '__main__':
	app.run(host='192.168.153.151', port=5000, debug=True)

