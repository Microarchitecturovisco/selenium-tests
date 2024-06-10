import time

from selenium.webdriver.common.by import By


def do_search_query(driver):
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