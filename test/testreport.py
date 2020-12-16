import unittest
from selenium import  webdriver
import time

class add(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 浏览器不提供可视化页面
        option.add_argument("--no-sandbox")
        self.driver=webdriver.Chrome(options=option)

    def testBaidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys(u"python")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)
        assert  u"python" in self.driver.page_source,"页面不存在关键字"

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__' :
    unittest.main()