#! /usr/bin/env python3
from flask import Flask,redirect,url_for,render_template, flash, abort, request
from flask_mongoengine import MongoEngine
from datetime import datetime
from flask_news_mongo.forms import NewsForm

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'mongo_news',
    'host': '192.168.153.151',
    'port': 27017
}
app.config['SECRET_KEY'] = 'a random string'

db = MongoEngine(app)

NEWS_TPYES = (
		('推荐', '推荐'),
		('百家', '百家'),
        ('本地', '本地'),
        ('图片', '图片'),
	)

# 新闻模型
class News(db.Document):
    title = db.StringField(max_length=50, required=True)
    img_url = db.StringField(max_length=50)
    content = db.StringField(max_length=3000, required=True)
    is_valid = db.BooleanField(default=True)
    news_type = db.StringField(choices=NEWS_TPYES, required=True)
    created_at = db.StringField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updeted_at = db.StringField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    meta = {
        'collection': 'news',
        'ordering': ['-created_at'],
    }

@app.route('/')
def index():
    news_list = News.objects.filter(is_valid=True)
    return render_template('index.html', news_list=news_list)

@app.route('/cat/<name>')
def cat(name):
    news_list = News.objects.filter(is_valid=True, news_type=name)
    return render_template('cat.html', news_list=news_list)

@app.route('/detail/<pk>')
def detail(pk):
    news_list = News.objects.filter(pk=pk).first_or_404()
    return render_template('detail.html', new_obj=news_list)



#####################



@app.route('/admin/<int:page>')
@app.route('/admin')
def admin(page=None):
    if page is None:
        page = 1
    page_data = News.objects.filter(is_valid=True).paginate(page=page, per_page=1)
    return render_template('admin/index.html', page_data=page_data)

@app.route('/add', methods=('GET', 'POST'))
def add():
    form = NewsForm()
    if form.validate_on_submit():
        # 获取数据
        new_obj = News(
            title=form.title.data,
            content=form.content.data,
            news_type=form.news_type.data,
            img_url=form.img_url.data
        )
        # 保存数据
        new_obj.save()
        # 成功后跳转
        flash('新增成功')
        return redirect(url_for('admin'))
    return render_template('admin/add.html', form=form)

@app.route('/update/<pk>/', methods=('GET', 'POST'))
def update(pk):
    new_obj = News.objects.filter(pk=pk).first()
    if not new_obj:
        abort(404)

    form = NewsForm(obj=new_obj)
    if form.validate_on_submit():
        # 获取数据
        new_obj.title = form.title.data
        new_obj.content = form.content.data
        new_obj.news_type = form.news_type.data
        new_obj.img_url = form.img_url.data
        # 保存数据
        new_obj.save()
        # 成功后跳转
        flash('修改成功')
        return redirect(url_for('admin'))

    return render_template('admin/update.html', form=form)

@app.route('/delete/<pk>', methods=['POST'])
def delete(pk):
    if request.method == 'POST':
        new_obj = News.objects.filter(pk=pk).first()
        if not new_obj:
            return 'no'
        new_obj.is_valid = False
        new_obj.save()
        # new_obj.delete() 物理删除
        return 'yes'

if __name__ == '__main__':
    app.run(host='192.168.153.151', port=5000, debug=True)