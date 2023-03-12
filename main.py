# import requests
url = 'https://www.alibaba.ir/bus/THR-IFN?departing=1401-12-26'
# data = requests.get(url)
# print(data.text)
##################################
# from requests_html import HTMLSession
#
# session = HTMLSession()
# r = session.get(url)
# r.html.render()
from selenium import webdriver

DRIVER_PATH = 'C:\\Users\\AmirHBakan\\PycharmProjects\\Bilit\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(url)
test = driver.page_source
print(test)