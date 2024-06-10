import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://localhost:18453")
driver.maximize_window()
driver.implicitly_wait(5)


def do_search_query():
    # destinations
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/button[1]").click()
    # destinations options
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div/label[14]/span[1]/input").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div/label[11]/span[1]/input").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div/label[7]/span[1]/input").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div/label[4]/span[1]/input").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div/label[3]/span[1]/input").click()
    # guests
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/button[2]").click()
    # guests options
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/button[2]").click()

    # when
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/button[3]").click()
    # when from select
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div/div/button").click()
    # when from select date
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/button[1]").click()

    time.sleep(0.2)
    # when to select
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/button").click()
    # when to select date
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/button[1]").click()

    driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[1]/h1').click()

    # from
    driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div/button[4]").click()
    # from options
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/label[4]/span[1]/input").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[2]/div/label[4]/span[1]/input").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/label[6]/span[1]/input").click()
    driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div/button[5]").click()


def refresh_offers():
    driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[1]/div[1]/button[5]").click()
    time.sleep(10)


def assert_3_offers():
    listing = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]").find_elements(by=By.TAG_NAME, value="div")
    assert len(listing) == 3


def buy_offer():
    driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[3]/div[3]/a/button").click()


if __name__ == '__main__':
    do_search_query()
    time.sleep(5)

    while True:
        refresh_offers()
