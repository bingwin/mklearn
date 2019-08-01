# 抖音爬虫
* 1000个分享id  https://github.com/luzhisheng/crawler_learn/blob/master/douyin/douyin_hot_id.txt
* 分享页面 https://www.douyin.com/share/user/58589817703

## 抖音数字乱码破解

    {'name':[' &#xe603; ',' &#xe60d; ',' &#xe616; '],'value':0},
    {'name':[' &#xe602; ',' &#xe60e; ',' &#xe618; '],'value':1},
    {'name':[' &#xe605; ',' &#xe610; ',' &#xe617; '],'value':2},
    {'name':[' &#xe604; ',' &#xe611; ',' &#xe61a; '],'value':3},
    {'name':[' &#xe606; ',' &#xe60c; ',' &#xe619; '],'value':4},
    {'name':[' &#xe607; ',' &#xe60f; ',' &#xe61b; '],'value':5},
    {'name':[' &#xe608; ',' &#xe612; ',' &#xe61f; '],'value':6},
    {'name':[' &#xe60a; ',' &#xe613; ',' &#xe61c; '],'value':7},
    {'name':[' &#xe60b; ',' &#xe614; ',' &#xe61d; '],'value':8},
    {'name':[' &#xe609; ',' &#xe615; ',' &#xe61e; '],'value':9},

## 抖音数据抓包异常
fiddler抓包抖音时无法联网，抖音数据传出通过https加密，通常加密方式如下：
    1、根据浏览器或者说操作系统（Android）自带的证书链 （需要购买）
    2、二是使用自签名证书 （内网使用）
    3、三是自签名证书加上SSL Pinning特性 （安全性最高）

SSL Pinning，即SSL证书绑定，是验证服务器身份的一种方式，是在https协议建立通信时增加的代码逻辑，它通过自己的方式验证服务器身份，然后决定通信是否继续下去。它唯一指定了服务器的身份，所以安全性较高。

## 解决方法
安装Xposed框架 + JustTruestMe组件
Xposed是一个框架，它可以改变系统和应用程序的行为，而不接触任何APK。它支持很多模块，每个模块可以用来帮助实现不同的功能。

JustTrustMe 是一个用来禁用、绕过 SSL 证书检查的，他基于 Xposed 模块。JustTrustMe 是将 APK 中所有用于校验 SSL 证书的 API 都进行了 屏蔽，从而绕过证书检查。

手机必须获取root权限，安装xposed框架有手机变砖危险！！！手机可以直接刷带有xposed框架的系统

Xposed框架下载地址：https://repo.xposed.info/module/de.robv.android.xposed.installer

justTruestme组件下载地址：
https://github.com/Fuzion24/JustTrustMe/releases/tag/v.2

## fiddler抓包

粉丝列表接口存在3个字段nickname，unique_id，uid分别代表 “用户名”，“抖音id”，“分享页面id”

中文用户名解码方式：

![Image text](https://raw.githubusercontent.com/luzhisheng/crawler_learn/master/readme_img/jm.png)

## mitmproxy抓包拿取api数据

    import json
    try:
        from douyin.handle_mongo import save_task
    except:
        from handle_mongo import save_task

    def response(flow):
        if 'aweme/v1/user/follower/list/' in flow.request.url:
            for user in json.loads(flow.response.text)['followers']:
                douyin_info = {}
                douyin_info['share_id'] = user['uid']
                douyin_info['douyin_id'] = user['short_id']
                // 入库
                save_task(douyin_info)

## appium 进入app进行上下滑动
    相关的appium文档
    https://github.com/luzhisheng/crawler_learn/tree/master/appium_test

Desired Capability配置
```bash
{
  "platformName": "Android",
  "platformVersion": "5.1",
  "deviceName": "A1CEBNB2278J",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": True,
  "unicodeKeyboard": True, //开启输入法
  "resetKeyboard": True, //关闭输入法
}
```
https://github.com/luzhisheng/crawler_learn/blob/master/douyin/douyin_appium.py

## 多设备端并发抓取数据
    准备工作：
        1、运行多台设备（模拟器，手机设备）
        2、运行多个appium服务
        3、使用python多进程/多线程
    注意事项:
        1、模拟器连接端口（第一个模拟器端口是62001，第二个模拟器端口是62025，第三个是62025+1）

![Image text](https://raw.githubusercontent.com/luzhisheng/crawler_learn/master/readme_img/dk1.png)

        2、appium客户端设置udid
        3、appium服务端设置bootstrapPort（设备appium服务通讯的端口）
```bash
cap = {
"platformName": "Android",
"platformVersion": "7.1.2",
"deviceName": device,
"udid": device,
"appPackage": "com.ss.android.ugc.aweme",
"appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
"noReset": True,
"unicodekeyboard": True,
"resetkeyboard": True
}

driver = webdriver.Remote('http://localhost:'+str(port)+'/wd/hub', cap)
```

## 伪装appium 爬虫
```bash
mitmdump -s test.py -p 8889 --mode upstream:主机地址:端口 --upstream-auth 账户:密钥
//测试mitmdump ip代理
def request(flow):
    pass
```

## 抖音视频