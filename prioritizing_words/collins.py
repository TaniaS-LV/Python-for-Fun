from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

COLLINS_URL = "https://www.collinsdictionary.com/dictionary/"

class Collins:

    def check_frequency(self, word,language):
        chrome_driver_path = "C:\Development\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        driver.get(f"{COLLINS_URL}{language}-english")
        time.sleep(2)
        cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        input_field = driver.find_element(By.NAME, 'q')
        button = driver.find_element(By.CLASS_NAME, 'search-submit')
        cookies.click()
        input_field.send_keys(word)
        button.click()

        try:
            frequency_element = driver.find_element(By.CLASS_NAME, 'word-frequency-img').get_attribute('data-band')
        except NoSuchElementException:
            print('Sorry, Collins has no data for this word')
        else:
            translation = driver.find_element(By.CLASS_NAME, 'type-translation').text
            print(f'\nThe word {word} has a frequency of {frequency_element}')


        driver.quit()