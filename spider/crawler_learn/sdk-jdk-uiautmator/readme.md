Android sdk 指的是android专属的软件开发工具包
# 安装sdk准备工作
配置jdk环境,下载地址：https://www.oracle.com/technetwork/cn/java/javase/downloads/jdk8-downloads-2133151-zhs.html

设置JAVA环境变量--》windows控制面板-》高级系统设置--》环境变量

![Image text](https://raw.githubusercontent.com/luzhisheng/crawler_learn/master/readme_img/hjblzz.png)
```bash
变量名：Path
变量值：C:\ProgramData\Oracle\Java\javapath;%java_home%\bin;%java_home%\jre\bin
新建
变量名：JAVA_HOME
变量值：C:\java\jdk
新建
变量名：ClassPath
变量值：.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;
```
cmd--》输入java 检查是否安装成功

cmd--》输入javac 检查是否安装成功

## SDK
SDK下载，http://tools.android-studio.org/index.php/sdk

## 设置安卓环境变量
```bash
ANDROID_HOME	C:\SDK
PATH	%ANDROID_HOME%\platform-tools;%ANDROID_HOME%\tools;
```
## 安装sdk工具包 --》SDK Manager.exe
* android sdk tools 基础工具包
* android sdk platform-tools 
* android sdk build-tools
* extras 扩展包

# adb工具
platform-tools ---》adb

adb ( Android Debug Bridge)是一个通用命令行工具，其允许您与模拟器实例或连接的 Android 设备进行通信。它可为各种设备操作提供便利，如安装和调试应用。

cmd--》adb--》检查是否安装成功

## adb工具连接安卓设备
* 启动adb服务器 ```adb start-server```
* 手机开发者模式--》usb调试 （模拟器版本不一致需要覆盖adb）
* 查看当前连接的安卓设备 adb devices
* 进入手机文件 adb -s 设备名称 shell

![Image text](https://raw.githubusercontent.com/luzhisheng/crawler_learn/master/readme_img/adb-t.png)

操作符$代表没有root权限，#代表有root权限

## adb命令工具安装app
```bash
adb devices
adb -s 设备名称 install apk文件名
```

## adb命令工具卸载app
```bash
adb -s 设备名称 shell
进入包名列表 cd /data/app--》ls--》记住包名，退出
adb -s 设备名称 uninstall apk包名
```

## adb查看系统的所有应用包名
```bash
adb shell pm list package
//如果想知道应用对应的apk文件在手机上的安装位置则可以在上面的命令后加-f参数
adb shell pm list packages -f
```
## adb其他命令
```bash
//将pc文件写入手机
adb push pc文件路径名称 手机路径
//将手机文件导出pc
adb pull 手机路径名称 pc文件路径
//进行截图
adb shell screencap 存放的路径名称
```

# uiautomator
Android 4.3发布的时候发布的测试工具
uiautomator是用来做UI测试的。也就是普通的手工测试，点击每个控件元素 看看输出的结果是否符合预期。比如 登陆界面 分别输入正确和错误的用户名密码然后点击登陆按钮看看是否能否登陆以及是否有错误提示等
uiautomatorviewer – 一个图形界面工具来扫描和分析应用的UI控件。存放在tools目录
uiautomator – 一个测试的Java库，包含了创建UI测试的各种API和执行自动化测试的引擎。

## 开启uiautomator
存放在 sdk工具包--》tools--》uiautomatorviewer.bat

## 升级uiautomator 增加xpath功能
链接：https://pan.baidu.com/s/1ZGSM8U8oyX723SuFc4aV4A 
提取码：frvc 

* uiautomator和appium存在端口冲突
* uiautomator主要用作快照拿取xpath