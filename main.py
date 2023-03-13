from selenium import webdriver
import ctypes
import re
url = 'https://www.alibaba.ir/bus/THR-IFN?departing=1401-12-26'
DRIVER_PATH = 'C:\\Users\\AmirHBakan\\PycharmProjects\\Bilit\\chromedriver.exe'
while True:
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.set_window_position(-10000, 0)
    driver.get(url)
    test = driver.page_source
    txt = test
    x = re.findall("صندلی باقی مانده", txt)
    print(x)
    if x:
        ctypes.windll.user32.MessageBoxW(0, "findddddddddd", "ticket", 1)
    driver.quit()