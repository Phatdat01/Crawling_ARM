import os
import json
import time
from pathlib import Path

from Crawl.crawling import open_web, login, access, download

DOWNLOAD_PATH = str(Path.home() / "Downloads")

def crawl(cre: json):
    if cre["path"] == "" or not os.path.exists(cre["path"]):
        cre["path"] = DOWNLOAD_PATH

    driver = open_web(cre=cre)
    driver.maximize_window()
    login(driver=driver,cre=cre)
    access(driver=driver, cre=cre)
    download(driver=driver, cre=cre)

    time.sleep(5)
    driver.quit()