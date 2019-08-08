# 搭建仓位记录控制服务

在这次演示中，我们来搭建一个支持MongoDB数据库CRUD操作的web服务，用来进行交易仓位的管理。  

每一条仓位记录包含了以下信息：  
- 交易账号
- 股票代码
- 交易数量
- 交易价格  


## 准备工作

1. 下载安装node.js: https://nodejs.org/en/download/
2. 下载安装Postman: https://www.getpostman.com/
3. 在docker容器上运行mongod(并绑定端口到本地):  
`docker run --name mymongo -v /path/to/data:/data/db -p 27017:27017 -d mongo:4`


## 基本架构

![alt text][flowchart]

[flowchart]: docs/images/flowchart.jpg