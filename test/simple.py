

from selenium import  webdriver
from time import  sleep
import unittest
import HTMLTestRunner

option = webdriver.ChromeOptions()
#option.add_argument('headless') # 浏览器不提供可视化页面
#option.add_argument("--no-sandbox")

driver=webdriver.Chrome(options=option)
driver.implicitly_wait(10)
driver.maximize_window();
driver.get("http://192.168.101.89:8081/")
#driver.get("https://demo.yeeyoon.com/home")
current_window=driver.current_window_handle

driver.find_element_by_css_selector("input[name='username']").send_keys("test_lidawei2")
driver.find_element_by_css_selector("input[name='password']").send_keys("123456")
driver.find_element_by_class_name("login-button").click()

sleep(2)


li=driver.find_element_by_xpath("//li[@class='liClass'][10]")
li.click()

div=driver.find_element_by_link_text("采购申请")
div.click();
sleep(1)
btns=driver.find_element_by_xpath("//div[@class='ant-col-24']/button[@type='button'][1]")
btns.click()

dept=driver.find_element_by_css_selector("div[class='search_contain']")
dept.click()
sleep(2)

dt=driver.find_element_by_xpath("//div[@class='ant-modal-body']//tbody[@class='ant-table-tbody']/tr[1]")


dt.find_element_by_css_selector("input[type='radio']").click()
driver.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[@class='ant-row']//button[@type='button'][2]").click()

driver.find_element_by_id("budgetAmount").send_keys("1000")

#需求内容
xqnr=driver.find_element_by_xpath("//label[@title='需求内容']/../../div[2]")
xqnr.click()


dx=driver.find_element_by_xpath("//li[@role='menuitem'][1]");
dx.click()


jhrq=driver.find_element_by_xpath("//span[@class='ant-calendar-picker']").click();
driver.find_element_by_link_text("今天").click()

driver.find_element_by_xpath("//label[@title='一级物料分类']/../../div[2]").click()
driver.find_element_by_xpath("//li[text()='模板体系']").click();

driver.find_element_by_xpath("//label[@title='二级物料分类']/../../div[2]").click()
driver.find_element_by_xpath("//li[text()='全套']").click();

driver.find_element_by_xpath("//label[@title='物资状态']/../../div[2]").click()
driver.find_element_by_xpath("//li[text()='新板']").click();

driver.find_element_by_xpath("//label[@title='物料材质']/../../div[2]").click()
driver.find_element_by_xpath("//li[text()='铝']").click();

driver.find_element_by_id("otherRemark").click();
sleep(2)
product=driver.find_element_by_xpath("(//div[@class='ant-select-search__field__wrap'])[5]")
product.click()
product.find_element_by_xpath("input").send_keys("1")
sleep(1)
driver.find_element_by_xpath("//li[text()='有孔普通平板(W)PK(L)(1501010010026)(100PK2600)']").click()

driver.find_element_by_xpath("//input[@placeholder='数量']").send_keys("100")
driver.find_elements_by_xpath("//input[@placeholder='数量']")[1].send_keys("100")

driver.find_elements_by_xpath("//div[@class='ant-select ant-select-enabled']")[1].click()
sleep(1)
driver.find_element_by_xpath("//li[text()='件']").click();


driver.find_elements_by_xpath("//button[@class='ant-btn ant-btn-primary']")[4].click()
sleep(3)





print('title：', driver.title)
print('执行完毕：！！！')



#sleep(60)
#driver.quit()