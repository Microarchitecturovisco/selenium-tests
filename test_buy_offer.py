import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import random


def open_main_page():
    driver = webdriver.Firefox()
    port = 3000
    driver.get("http://localhost:" + str(port))
    driver.maximize_window()
    return driver


def do_search_query(driver):
    # destinations
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/button[1]").click()
    # destinations options
    for i in range(5):
        random_index = random.randint(1, 14)  # Assuming the range of indices is from 1 to 14
        xpath = f"/html/body/div[2]/div/div/div/div/div/label[{random_index}]/span[1]/input"
        driver.find_element(by=By.XPATH, value=xpath).click()

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

    time.sleep(0.5)
    # when to select
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/button").click()
    # when to select date
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/button[1]").click()

    driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[1]/h1').click()

    # from
    driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div/button[4]").click()
    # from options - by plane
    for i in range(3):
        random_index = random.randint(1, 6)
        xpath = f"/html/body/div[2]/div/div/div[1]/div[2]/label[{random_index}]/span[1]/input"
        driver.find_element(by=By.XPATH, value=xpath).click()

    # from options - by bus
    for i in range(3):
        random_index = random.randint(1, 6)
        xpath = f"/html/body/div[2]/div/div/div[2]/div[2]/div/label[{random_index}]/span[1]/input"
        driver.find_element(by=By.XPATH, value=xpath).click()
    # confirm from options choice
    driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div/button[5]").click()


def select_first_offer(driver):
    driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[3]/div[3]/a/button").click()


def book_offer(driver):
    # book offer - show booking details
    driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/div[2]/div/a/button").click()
    time.sleep(2)
    # book offer confirmation
    driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/button").click()


def buy_offer(driver, pay_correctly_or_not):
    pay_correct_button_xpath = "/html/body/div/div[2]/div[2]/div/button[1]"
    pay_incorrect_button_xpath = "/html/body/div/div[2]/div[2]/div/button[2]"

    if pay_correctly_or_not:
        driver.find_element(by=By.XPATH, value=pay_correct_button_xpath).click()
    else:
        driver.find_element(by=By.XPATH, value=pay_incorrect_button_xpath).click()


def assert_more_than_one_offer_found(driver):
    listing = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]").find_elements(by=By.TAG_NAME, value="div")
    return len(listing)


def book_and_buy_offer(driver, pay_correctly_or_not):
    time.sleep(5)
    listing_len = 0
    while listing_len == 0:
        do_search_query(driver)
        listing_len = assert_more_than_one_offer_found(driver)

    time.sleep(5)
    select_first_offer(driver)
    time.sleep(4)
    book_offer(driver)
    time.sleep(4)
    buy_offer(driver, pay_correctly_or_not)
    time.sleep(2)


if __name__ == '__main__':
    print("Beginning test - book_and_buy_offer, pay successfully")
    driver = open_main_page()
    book_and_buy_offer(driver, True)
    time.sleep(3)
    driver.quit()
    print("Finished test - book_and_buy_offer, pay successfully")

    print("Beginning test - book_and_buy_offer, pay unsuccessfully")
    driver = open_main_page()
    book_and_buy_offer(driver, False)
    time.sleep(3)
    driver.quit()
    print("Finished test - book_and_buy_offer, pay unsuccessfully")
