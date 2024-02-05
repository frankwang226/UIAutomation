from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


desire_caps = {
    "platformName": "Android",
    "platformVersion": "6.0",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.ezr.assistant.sellerassistant",
    "appActivity": "com.assistant.kotlin.activity.LoginActivity",
    "automationName": "UiAutomator2",
    "unicodeKeyboard": True,
    "resetKeyboard": True
    }

# 设置以下两个参数来控制启动app和关闭掉app
#caps["appium:forceAppLaunch"] = True
#caps["appium:shouldTerminateApp"] = True
# appium服务器地址
appium_server_url = 'http://127.0.0.1:4723'
driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(caps=desire_caps))

#driver.quit()