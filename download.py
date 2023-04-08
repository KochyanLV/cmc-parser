import requests
from os import getcwd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
class Downloader:
    def __init__(self, url, params, method = "GET"):
        self.url = url
        self.params = params
        self.method = method
        self.html = None
    
    def get_html(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        html = ''
        for i in range(10):
            driver.execute_script(f"window.scrollTo({i}, {i+1}*document.body.scrollHeight/10);")
            time.sleep(2)
        self.html = driver.page_source
        return self.html
    
    def save(self, file_path):
        if self.html == None:
            raise ValueError("No info has been gathered! Consider running get_html() method")
        with open(file_path, "w", encoding = "utf-8") as f:
            f.write(self.html)


'''URL = "https://coinmarketcap.com/view/collectibles-nfts/"

FILE_PATH = "crypto.html"'''


'''downloader = Downloader(url = URL, params = None)
html = downloader.get_html()
downloader.save(FILE_PATH, html)'''