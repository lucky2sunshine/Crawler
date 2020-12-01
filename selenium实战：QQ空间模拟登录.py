# https://qzone.qq.com/

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
import time

# 无头浏览器
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 规避检测
options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable_automation'])

# 实例化浏览器对象
browser = webdriver.Chrome(executable_path='./chromedriver')

# 打开QQ空间登录页面
zone_url = 'https://qzone.qq.com/'
browser.get(zone_url)

browser.switch_to.frame('login_frame')
switch_btn = browser.find_elements_by_xpath('//*[@id="switcher_plogin"]')

# 点击 "账号密码登录"
switch_btn[0].click()

time.sleep(3)
# 输入用户名和密码
username = browser.find_element_by_id('u')
username.send_keys('xxxxxxxxx')
password = browser.find_element_by_id('p')
password.send_keys('xxxxxxxxx')

time.sleep(3)
# 点击登录按钮
login_btn = browser.find_element_by_id('login_button')
login_btn.click()

# 停留3s后关闭
time.sleep(3)
browser.quit()



