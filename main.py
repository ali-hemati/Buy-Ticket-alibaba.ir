from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import ctypes
import re
y=[]
url = 'https://www.alibaba.ir/bus/THR-IFN?departing=1401-12-26'
DRIVER_PATH = 'C:\\Users\\AmirHBakan\\PycharmProjects\\Bilit\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.set_window_position(-10000, 0)
driver.get(url)
while True:
    try:
        y=[]
        while len(y) < 2:
            test = driver.page_source
            txt = test
            y = re.findall("تکمیل ظرفیت", txt)
            print(y)
        x = re.findall("صندلی باقی مانده", txt)
        if x:
            print('x is', x)
            ctypes.windll.user32.MessageBoxW(0, "findddddddddd", "ticket", 1)
        driver.refresh()
    except TimeoutException:
        print("Loading took too much time!")
        driver.refresh()


    # driver.quit()