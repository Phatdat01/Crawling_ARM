import json
import time
from typing import List, Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

CONTENT_LIST = ["cn","chuyển nhượng"]

def load_edge(download_path: str):
    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True
    }
    options = webdriver.EdgeOptions()
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    return driver


def load_chrome(download_path: str):
    service = Service()
    options = webdriver.ChromeOptions()

    prefs = {
        'download.default_directory': download_path,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True
    }
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def wait_element(driver: WebDriver, timeout: int, key: str, by: str) -> WebElement:
    if by.lower() == "id":
        condition = EC.presence_of_element_located((By.ID, key))
    elif by.lower() == "class":
        condition = EC.visibility_of_element_located((By.CLASS_NAME, key))
    elif by.lower() == "name":
        condition = EC.element_to_be_clickable((By.NAME, key))
    elif by.lower() == "tag":
        condition = EC.element_to_be_clickable((By.TAG_NAME, key))
    elif by.lower() == "css":
        condition = EC.element_to_be_clickable((By.CSS_SELECTOR, key))
    else:
        return []

    try:
        element = WebDriverWait(driver, timeout).until(condition)
        return element
    except:
        return []
    

def open_web(cre: json):
    if "chrome" in cre["web"].lower():
        driver = load_chrome(download_path= cre["path"])
    else:
        driver = load_edge(download_path= cre["path"])
    driver.get(cre["url"])
    return driver


def login(driver: WebDriver, cre: json):
    name = wait_element(driver=driver, timeout=10,key="username",by="name")
    name.send_keys(cre["name"])
    pw= driver.find_element(By.NAME, "password")
    pw.send_keys(cre["pw"])
    login = wait_element(driver=driver, timeout=10,key="ui.fluid.large.submit.button",by="class")
    login.click()


def load_pages(driver: WebDriver, cre: json) -> int:
    num = 0
    while True:
        try:
            time.sleep(6.7)
            pages = wait_element(driver=driver,timeout=30,key="total",by="name")
            ward_selection = driver.find_elements(By.NAME,value="xaId")
            for ward in ward_selection:
                try:
                    need_select = Select(ward)
                    need_select.select_by_visible_text(cre["ward"])
                except:
                    pass
            time.sleep(3)
            pages = driver.find_element(By.NAME, value="total").text
            return int(pages)
        except:
            num+=1
            if num>5:
                return int(pages)


def change_to_current_page(driver: WebDriver, page: str):
    time.sleep(1.7)
    current = wait_element(driver=driver, timeout=20,key="current",by="name")
    current.click()
    time.sleep(2)
    current.clear()
    time.sleep(2)
    current.send_keys(page)
    time.sleep(2)
    current.send_keys(Keys.ENTER)
    time.sleep(2.3)


def close_file(driver: WebDriver, id: int = -1):
    try:
        driver.switch_to.window(driver.window_handles[id])
        driver.execute_script("window.close();")
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(f"Error in process_file: {e}")


def download_file(args: List[Tuple[int, WebElement]], driver: WebDriver):
    handle_index, file = args
    try:
        try:
            driver.switch_to.window(driver.window_handles[handle_index])
        except:
            driver.switch_to.window(driver.window_handles[1])
        save = wait_element(driver=driver,timeout=20,key="body",by="tag")
        save.send_keys(Keys.CONTROL + 's')
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(f"Error in process_file: {e}")


def open_file(args, driver: WebDriver):
    handle_index, file = args
    try:
        link = file.get_attribute("nodeid")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[handle_index])
        driver.get(f"https://khh.mplis.gov.vn/dc/PdfViewer?fileId={link}")
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(f"Error in process_file: {e}")

def access(driver: WebDriver, cre: json):
    # access to navigation
    arm = wait_element(driver=driver, timeout= 30, key="h-f.ng-binding.ng-scope",by="class")
    arm = driver.find_elements(By.CLASS_NAME, value="h-f.ng-binding.ng-scope")[1]
    arm.click()
    del arm

    # Wanna search
    search_option = wait_element(driver=driver, timeout= 30, key="8543",by="id")
    search_option.click()

    search_button = wait_element(driver=driver, timeout= 30, key="submit.ui.button.green.text-white.m-r-7",by="class")
    search_button.click()
    del search_button

    time.sleep(1.7)
    re_from = wait_element(driver=driver, timeout= 30, key="NgayNhanTu",by="name")
    re_from.clear()
    time.sleep(0.7)
    re_from.send_keys(cre['re_from'])
    del re_from

    re_to = wait_element(driver=driver, timeout= 30, key="NgayNhanDen",by="name")
    re_to.clear()
    time.sleep(0.7)
    re_to.send_keys(cre['re_to'])
    del re_to

    result_from = wait_element(driver=driver, timeout= 30, key="NgayHenTraTu",by="name")
    result_from.clear()
    time.sleep(0.7)
    result_from.send_keys(cre['result_from'])
    del result_from

    result_to = wait_element(driver=driver, timeout= 30, key="NgayHenTraDen",by="name")
    result_to.clear()
    time.sleep(0.7)
    result_to.send_keys(cre['result_to'])
    del result_to

    search = wait_element(driver=driver, timeout= 30, key="tkDiaChiXaThuaDat",by="id")
    ward = search.find_element(By.CLASS_NAME, value="search")
    ward.clear()
    time.sleep(0.7)
    ward.send_keys(cre['ward'])

    search = wait_element(driver=driver, timeout= 30, key="btnTimKiem",by="id")
    search.click()

def download(driver: WebDriver, cre: json):
    time.sleep(1.7)
    data = wait_element(driver=driver, timeout= 30, key="danhSachHoSo",by="id")
    row = data.find_elements(By.TAG_NAME, value="tr")

    for i in range(1,len(row)):
        txt = row[i].find_elements(By.CLASS_NAME, value= "ng-binding")[5].text
        for content in CONTENT_LIST:
            if content in txt.lower():
                print("Accept")