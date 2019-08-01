# 打造多任务端app应用数据抓取系统架构图
![Image text](https://raw.githubusercontent.com/luzhisheng/crawler_learn/master/readme_img/dkd.png)

# docker
    docker search ubuntu 搜索镜像
    docker images 查看镜像
    docker pull ubuntu 下载镜像
    docker run --name ubuntu-test -it ubuntu /bin/bash 创建容器并进入容器
    docker run --name ubuntu-test -d ubuntu /bin/sh -c "while true;do sleep 2;done" 创建容器守护进程启动
    docker ps -a 查看所有容器
    docker start 容器id 启动容器
    docker stop 容器id 结束容器
    docker kill 容器id 结束容器
    docker exec -t 容器id /bin/bash 进入容器终端
    docker pause 容器id 暂停容器
    docker unpause 容器id 暂停容器
    docker rm 容器id 删除容器
    docker rm -v $(docker ps -aq -f status=exited) 批量删除所有已经退出的容器
    docker rmi 删除镜像

##docker run -it centos /bin/bash

按照顺序，Docker做了这些事情：
    1）拉取centos镜像: Docker检查centos镜像是否存在，如果在本地没有该镜像，Docker会从Docker Hub下载。如果镜像已经存在，Docker会使用它来创建新的容器。
    2）创建新的容器: 当Docker有了这个镜像之后，Docker会用它来创建一个新的容器。
    3）分配文件系统并且挂载一个可读写的层: 容器会在这个文件系统中创建，并且一个可读写的层被添加到镜像中。
    4）分配网络/桥接接口: 创建一个允许容器与本地主机通信的网络接口。
    5）设置一个IP地址: 从池中寻找一个可用的IP地址并且服加到容器上。
    6）运行你指定的程序: 运行指定的程序。
    7）捕获并且提供应用输出: 连接并且记录标准输出、输入和错误让你可以看到你的程序是如何运行的。

更多：http://www.yujzw.com/docker/docker-help.html

# docker部署
    docker search httpd 
    docker run -d -p 80 httpd (-d：后台运行容器，并返回容器id，也即启动守护式容器：)
    docker run -d -p 8080:80 httpd (8080是宿主机端口，80是容器的端口)

## 在linux系统中安装appium:
纯手动安装appium

https://oxygenengine.github.io/%E6%8A%80%E6%9C%AF/2017/10/18/install-auto-test-environment-on-centos-7/

docker安装appium
    
    docker pull appium

# appium容器连接安卓模拟器
https://github.com/appium/appium-docker-android

## 创建 appium 容器
    docker run --privileged -d -p 4723:4723  -v /dev/bus/usb:/dev/bus/usb --name container-appium appium/appium
    docker run --privileged -d -p 4723:4723 --name container-appium appium/appium （不添加容器数据卷）

## 验证adb设备是否可以检测连接的Android设备
    docker exec -it container-appium adb devices

## appium容器连接手机
    先本地设置usb连接改变ip地址连接 adb -s deviceName设备名称 tcpip 5555
    
    appium容器连接手机 docker exec -it container-appium adb connect 手机ip地址:端口
    
    查看是否连接 docker exec -it container-appium adb devices
    
    测试脚本：
    from appium import webdriver

    cap = {
    "platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "手机ip地址:端口",
    "appPackage": "com.tal.kaoyan",
    "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
    "noReset": True
    }

    driver = webdriver.Remote("docker的ip地址:端口/wd/hub", cap)
    
    查看appium容器日志：
    docker exec -it 容器名称 /bin/bash
    cd /var/log
    tail -f appium.log
    
