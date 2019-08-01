from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "hello world"

if __name__ == '__main__':
	app.run(host='192.168.153.151', port=5001)