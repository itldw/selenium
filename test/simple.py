

from selenium import  webdriver
from time import  sleep
import unittest
import HTMLTestRunner

option = webdriver.ChromeOptions()
option.add_argument('headless') # 浏览器不提供可视化页面
option.add_argument("--no-sandbox")

driver=webdriver.Chrome(options=option)
driver.implicitly_wait(10)
driver.maximize_window();
driver.get("http://192.168.101.89:8081/")
current_window=driver.current_window_handle

driver.find_element_by_css_selector("input[name='username']").send_keys("test_lidawei2")
driver.find_element_by_css_selector("input[name='password']").send_keys("123456")
driver.find_element_by_class_name("login-button").click()

sleep(2)


li=driver.find_element_by_xpath("//li[@class='liClass'][11]")
li.click()
print('title：', driver.title)
print('执行完毕：！！！')
 
driver.quit()