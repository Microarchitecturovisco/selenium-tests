import random
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
        time.sleep(random.randint(5, 10))


if __name__ == '__main__':
    num_workers = 4

    initial_delay = [x for x in range(2, num_workers * 2 + 2, 2)]

    Parallel(n_jobs=num_workers)(delayed(worker_task)(delay) for delay in initial_delay)
