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
FILE_LIST = ["Giấy chứng nhận","Tờ khai lệ phí trước bạ nhà, đất"]

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
    elif by.lower() == "xpath":
        condition = EC.element_to_be_clickable((By.XPATH, key))
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


def check_current_page(driver: WebDriver) -> List[int]:
    """
    Check current page
    
    Args:
        driver: WebDriver
            Driver selenium
    
    Returns:
        end_range: end of range in page
        last: last row of page
    """
    current = driver.find_element(By.XPATH, value="//*[@ng-if='totalPage > 0']")
    current_range, last= current.find_elements(By.CLASS_NAME, value="ng-binding")
    _, end_range = map(int, current_range.text.split(" - "))
    return [end_range, int(last.text)]


def change_to_current_page(driver: WebDriver, page: int, limit_top: int):
    time.sleep(0.7)
    # show top x each page
    top = wait_element(driver=driver, timeout=30, key="ui.selection.floating.dropdown.w-auto", by="class")
    top.click()
    time.sleep(0.7)
    top_x = top.find_element(By.XPATH, value=f"//*[@data-value='{limit_top}']")
    top_x.click()

    time.sleep(0.7)
    # Change to current
    end_range, last = check_current_page(driver=driver)

    while page > 1:
        time.sleep(1.3)
        if end_range >= last:
            break
        page -= 1
        next = driver.find_element(By.XPATH, value="//*[@title='Trang sau']")
        next.click()
        end_range += limit_top
        

def close_file(driver: WebDriver, id: int = -1):
    try:
        driver.switch_to.window(driver.window_handles[id])
        driver.execute_script("window.close();")
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(f"Error in process_file: {e}")


def download_file(driver: WebDriver, id: int):
    try:
        try:
            driver.switch_to.window(driver.window_handles[id])
        except:
            driver.switch_to.window(driver.window_handles[1])
        save = wait_element(driver=driver,timeout=20,key="body",by="tag")
        save.send_keys(Keys.CONTROL + 's')
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


def click_to_save(driver: WebDriver, cre: json):
    time.sleep(1.7)
    info = wait_element(driver=driver, timeout=30, key="item.XTT", by="class")
    info.click()
    time.sleep(1.7)
    container_element = driver.find_elements(By.XPATH, value="//*[@ng-repeat='item in $p.objThanhPhanHoSoKemTheos']")
    file = 0

    # click to needed download
    for container in container_element:
        text = container.find_element(By.CLASS_NAME, value="text-wrap.ng-binding").text
        for file_name in FILE_LIST:
            if file_name in text:
                container.find_element(By.TAG_NAME, value="a").click()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)

    time.sleep(cre['delay'])

    for i in range(1,3):
        download_file(driver=driver, id=i)
        file += 1
    time.sleep(1.7)
    for i in range(2):
        close_file(driver=driver)

    time.sleep(1)
    # remove not need windows tag
    if  len(driver.window_handles) >1:
        for window_handle in range (1, len(driver.window_handles)):
            close_file(driver=driver, id=window_handle)

    processing = wait_element(driver=driver, timeout=30, key="//*[@ng-click='$p.quaTrinhXuLyInit()']", by="xpath")
    processing.click()

    rows = wait_element(driver=driver, timeout=30, key="//*[@ng-repeat-start='item in $data.items']", by="xpath")
    rows = driver.find_elements(By.XPATH, value="//*[@ng-repeat-start='item in $data.items']")

    for row in rows:
        text = row.find_elements(By.TAG_NAME, value="td")[2].text
        if "Bến Lức" in text:
            files = row.find_elements(By.CLASS_NAME, value="m-n.pointer.large.red.file.outline.pdf.icon")
            files[0].click()
            for fi in files:
                fi.click()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)

            for i in range(1,len(files)+1):
                download_file(driver=driver, id=i)
                file += 1
            time.sleep(1.7)
            for i in range(len(files)):
                close_file(driver=driver)

    if  len(driver.window_handles) >1:
        for window_handle in range (1, len(driver.window_handles)):
            close_file(driver=driver, id=window_handle)

    print(file)

def download(driver: WebDriver, cre: json):
    time.sleep(1.7)
    data = wait_element(driver=driver, timeout= 30, key="danhSachHoSo",by="id")
    row = data.find_elements(By.TAG_NAME, value="tr")

    ok=""
    for i in range(1,len(row)):
        txt = row[i].find_elements(By.CLASS_NAME, value= "ng-binding")[5].text
        if ok=="done":
            break
        for content in CONTENT_LIST:
            if content in txt.lower():
                row[i].click()
                click_to_save(driver=driver, cre=cre)
                ok="done"
                break