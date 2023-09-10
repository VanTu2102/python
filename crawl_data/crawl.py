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

    def getRoot(self, dom: any, visited=[]):
        if (visited == None):
            visited = []
        if (dom not in visited):
            childs = {dom: {}}
            visited.append(dom)
            lst_child = self.getAllChild(dom)
            childs[dom].update({'count': len(lst_child)})
            for elem in lst_child:
                childs[dom].update(self.getRoot(elem, visited))
            return childs
        else:
            return {}

    def getAllChild(self, dom: WebElement):
        return dom.find_elements(By.XPATH, "./*")


url = 'https://vi.wikipedia.org/wiki/T%E1%BA%A3o_l%E1%BB%A5c'
f = open('./data/' + url.replace('/', '').replace('.', '').replace(':', '') +
         'Source.html', 'w', encoding="utf-8")

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)  # keep browser open
options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])

driver = webdriver.Edge(options=options)

# CrawlWorker = CrawlBySelenium(options, driver)
# driver.implicitly_wait(2)
driver.get(url)
# f.write(driver.page_source)
for cate in driver.find_elements(By.ID, 'mw-panel-toc-list'):
    root = WebAnalyst(cate)
    dict = root.getRoot(root.dom)
    print(dict)
    for a in dict:
        if(type(a) == WebElement):
            print(a.get_attribute('outerHTML'), dict[a]['count'])
        for b in dict[a]:
            if(type(b) == WebElement):
                print(b.get_attribute('outerHTML'), dict[a][b]['count'])
#     for htmlElem in cate.find_elements(By.XPATH, ".//*"):
#         print(htmlElem.get_attribute("outerHTML"))
# f.write(driver.find_element(By.ID, 'main').get_attribute("outerHTML"))
