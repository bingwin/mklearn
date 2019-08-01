# def mybin(num):
# 	if num == 0:
# 		return 0
# 	res = []
# 	while num:
# 		num, rem = divmod(num, 62)
# 		res.append(str(rem))
# 	return ''.join(reversed(res))
#
# print(mybin(38))
#
#
# CHARS = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
#
# def encode(num):
# 	if num == 0:
# 		return CHARS[0]
# 	res = []
# 	while num:
# 		num, rem = divmod(num, 62)
# 		res.append(CHARS[rem])
# 	return ''.join(reversed(res))
#
#
# print(encode(38))

from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
from flask.ext.redis import FlaskRedis

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'xxx'
app.config['MYSQL_DB'] = 'xxx'
app.config['MYSQL_CURSORCLASS'] = 'xxx'

mysql = MySQL(app)
redis_store = FlaskRedis(app)

CHARS = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(num):
	if num == 0:
		return CHARS[0]
	res = []
	while num:
		num, rem = divmod(num, 62)
		res.append(CHARS[rem])
	return ''.join(reversed(res))


@app.route('/shorten', methods=['POST'])
def shorten_url():
	long_url = request.json['url']
	index = int(redis_store.incr('SHORT_CNT'))
	token = encode(index)
	sql = "insert into short_url(token, url) VALUES (%s, %s)"
	cur = mysql.connection.cursor()
	cur.execute(sql,(token, long_url))
	mysql.connection.commit()
	shorten_url = 'https://short.com/' + token
	return jsonify(url=shorten_url)


@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(dubug=1)
