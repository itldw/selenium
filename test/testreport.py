import unittest
from selenium import  webdriver
import time

class add(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 浏览器不提供可视化页面
        option.add_argument("--no-sandbox")
        self.driver=webdriver.Chrome(options=option)

    def test_baidu(self):
        '''
        显示名称
        '''
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys(u"python")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)
        self.assertIn(u"python",self.driver.page_source)


    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__' :
    unittest.main()