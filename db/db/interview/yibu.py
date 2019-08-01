# import tornado.ioloop
# import tornado.web
# from tornado.httpclient import AsyncHTTPClient
#
#
# class MainHandler(tornado.web.RequestHandler):
# 	async def get(self):
# 		url = 'http://www.baidu.com/'
# 		http_client = AsyncHTTPClient()
# 		resp = await http_client.fetch(url)
# 		print(resp.body)
# 		return resp.body
#
# def make_app():
# 	return tornado.web.Application([
# 		(r"/api", MainHandler),
# 	])
#
# if __name__ == "__main__":
# 	app = make_app()
# 	app.listen(8888)
# 	tornado.ioloop.IOLoop.current().start()


# import gevent.monkey
# gevent.monkey.patch_all() # 修改内置的一些库非阻塞
#
# import gevent
# import requests
#
#
# def fetch(i):
# 	url = 'http://httpbin.org/get'
# 	resp = requests.get(url)
# 	print(len(resp.text), i)
#
#
# def asynchronous():
# 	threads = []
# 	for i in range(1, 10):
# 		threads.append(gevent.spawn(fetch, i))
# 	gevent.joinall(threads)
#
# print('asynchronous:')
# asynchronous()


import asyncio
from aiohttp import ClientSession


async def fetch(url, session):
	async with session.get(url) as response:
		return await response.read()

async def run(r=10):
	url = 'http://httpbin.org/get'
	tasks = []

	async with ClientSession() as session:
		for i in range(r):
			task = asyncio.ensure_future(fetch(url, session))
			tasks.append(task)
		responses = await asyncio.gather(*tasks)
		for resp_body in responses:
			print(len(resp_body))

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run())
loop.run_until_complete(future)

