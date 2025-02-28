from .configurations import get_driver
from selenium.webdriver.common.keys import Keys
import time


def main():
    driver = get_driver(
        "https://titan22.com/account/login?return_url=%2Faccount")
    driver.find_element(by="id",
                        value="CustomerEmail").send_keys("app7flask@gmail.com")
    time.sleep(2)
    driver.find_element(by="id",
                        value="CustomerPassword").send_keys("??!65EhGMg8.WwY" +
                                                            Keys.RETURN)
    time.sleep(2)
    driver.find_element(
        by="xpath",
        value='//*[@id="shopify-section-footer"]/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a'
    ).click()
    print(driver.current_url)


print(main())
