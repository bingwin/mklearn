from message.api import MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class MessageServiceHandler:

	def sendMobileMessage(self, mobile, message):
		print("sendMobileMessage")
		return True


	def sendEmailMessage(self, email, message):
		print("sendEmailMessage")
		return True


if __name__ == '__main__':
	handler = MessageServiceHandler()
	processor = MessageService.Processor(handler)
	transport = TSocket.TServerSocker("localhost", "9090") # 监听9090端口
	tfactory = TTransport.TFramedTransportFactory() # 定义传输的方式
	pfactory = TBinaryProtocol.TBinaryProtocolFactory() # 传输协议

	# 创建一个server
	server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
	print("python thrift server start")
	server.serve()
	print("python thrift server exit")