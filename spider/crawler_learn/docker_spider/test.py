from appium import webdriver

cap = {
  "platformName": "Android",
  "platformVersion": "5.1",
  "deviceName": "192.168.1.107:5555",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": True
}

driver = webdriver.Remote("192.168.153.151:4723/wd/hub", cap)