#! /usr/bin/env python3
from flask import Flask, redirect, url_for, render_template, flash, abort, request
from datetime import datetime
from flask_news_redis.redis_news import RedisNews
from flask_news_mongo.forms import NewsForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a random string'

@app.route('/')
def index():
	news_list = RedisNews().get_all_news()
	return render_template('index.html', news_list=news_list)


@app.route('/cat/<name>')
def cat(name):
	news_list = RedisNews().get_news_from_cat(name)
	return render_template('cat.html', news_list=news_list)


@app.route('/detail/<pk>')
def detail(pk):
	news_list = RedisNews().get_nes_from_id(pk)
	return render_template('detail.html', new_obj=news_list)


@app.route('/admin/<int:page>')
@app.route('/admin')
def admin(page=None):
	if page is None:
		page = 1
	page_data = RedisNews().paginage(page,5)
	return render_template('admin/index.html', page_data=page_data)


@app.route('/add', methods=('GET', 'POST'))
def add():
	return render_template('admin/add.html', form=form)


@app.route('/update/<pk>/', methods=('GET', 'POST'))
def update(pk):
	new_obj = RedisNews().get_nes_from_id(pk)
	if not new_obj:
		abort(404)

	form = NewsForm(data=new_obj)
	if form.validate_on_submit():
		# 获取数据
		new_obj['title'] = form.title.data
		new_obj['content'] = form.content.data
		new_obj['news_type'] = form.news_type.data
		new_obj['img_url'] = form.img_url.data
		new_obj['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		# 保存数据
		RedisNews().update_news(pk, new_obj)
		# 成功后跳转
		flash('修改成功')
		return redirect(url_for('admin'))

	return render_template('admin/update.html', form=form)


@app.route('/delete/<pk>', methods=['POST'])
def delete(pk):
	news_obj = RedisNews().get_nes_from_id(pk)
	if not news_obj:
		abort(404)
	RedisNews().delete_news(int_id=pk, news_obj=news_obj)
	return 'yes'


if __name__ == '__main__':
	app.run(host='192.168.153.151', port=5000, debug=True)
