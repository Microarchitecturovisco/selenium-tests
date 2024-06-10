import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from core import do_search_query
from joblib import Parallel, delayed


def worker_task(initial_delay):
    driver = webdriver.Firefox()
    driver.get("http://localhost:18453")
    driver.maximize_window()
    time.sleep(initial_delay)

    do_search_query(driver)

    while True:
        driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[1]/div[1]/button[5]").click()
        time.sleep(6)


if __name__ == '__main__':
    initial_delay = [2, 4, 6, 8]
    Parallel(n_jobs=4)(delayed(worker_task)(delay) for delay in initial_delay)
