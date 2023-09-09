from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


class CrawlBySelenium:
    options: Options
    driver: any

    def __init__(self, options, driver) -> None:
        self.options = options
        self.driver = driver

    def getApp(self, url):
        self.driver.get(url)

    def getElementByClassName(self, className):
        return self.driver.find_elements(By.CLASS_NAME, className)

    def getElementById(self, id):
        return self.driver.find_element(By.ID, id)


url = 'https://shopee.vn'
f = open('./data/' + url.replace('/', '').replace('.', '').replace(':', '') +
         'shopeeSource.html', 'w', encoding="utf-8")

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True) #keep browser open
options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])

driver = webdriver.Edge(options=options)

CrawlWorker = CrawlBySelenium(options, driver)
CrawlWorker.getApp(url)

# f.write(CrawlWorker.driver.page_source)
f.write(CrawlWorker.getElementById('main').get_attribute("outerHTML"))
