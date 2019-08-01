import socket
print(socket.socket)
print("monkey patch")
from gevent import monkey
monkey.patch_socket()
print(socket.socket)

import select
print(select.select)
monkey.patch_select()
print("monkey patch")
print(select.select)


import time
print(time.time())

def _time():
	return 12345

time.time = _time

print(time.time())