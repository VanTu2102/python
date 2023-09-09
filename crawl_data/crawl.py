from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


class WebAnalyst:
    dom: WebElement

    def __init__(self, dom: WebElement) -> None:
        self.dom = dom

    def getRoot(self):
        childs = {self.dom: {}}
        node_vistied = [self.dom]
        child = childs[self.dom]
        lst_key_child = [self.dom]
        while len(self.getAllChild(lst_key_child[0])) > 0:
            child.update({self.getAllChild(lst_key_child[0])[0]: {}})
            lst_key_child = list(child.keys())
            child = child[lst_key_child[0]]
        return childs

    def getAllChild(self, dom: WebElement):
        return dom.find_elements(By.XPATH, ".//*")


url = 'https://shopee.vn'
f = open('./data/' + url.replace('/', '').replace('.', '').replace(':', '') +
         'shopeeSource.html', 'w', encoding="utf-8")

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)  # keep browser open
options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])

driver = webdriver.Edge(options=options)

# CrawlWorker = CrawlBySelenium(options, driver)
# driver.implicitly_wait(1)
driver.get(url)

# f.write(driver.page_source)
for cate in driver.find_elements(By.CLASS_NAME, 'image-carousel__item'):
    root = WebAnalyst(cate)
    print(root.getRoot(), '\n')
#     for htmlElem in cate.find_elements(By.XPATH, ".//*"):
#         print(htmlElem.get_attribute("outerHTML"))
# f.write(driver.find_element(By.ID, 'main').get_attribute("outerHTML"))
