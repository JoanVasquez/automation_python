from .configurations import (get_driver, clean_text)
# Import the Keys class to simulate keyboard input (e.g., pressing Enter).
from selenium.webdriver.common.keys import Keys
# Import the time module to introduce delays (e.g., sleep) during automation.
import time


def main():
    # Get the configured WebDriver by calling get_driver().
    driver = get_driver("http://automated.pythonanywhere.com/login/")

    # Locate the username input element by its id and type "automated" into it.
    driver.find_element(by="id", value="id_username").send_keys("automated")

    # Wait for 2 seconds to simulate a realistic delay or to allow the page to update.
    time.sleep(2)

    # Locate the password input element by its id and type the password.
    # The Keys.RETURN at the end simulates pressing the Enter key to submit the form.
    driver.find_element(by="id",
                        value="id_password").send_keys("automatedautomated" +
                                                       Keys.RETURN)

    # Wait for 2 seconds for the login process to complete and the new page to load.
    time.sleep(2)

    # Locate a clickable element (e.g., a navigation link) using its XPath and click on it.
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()

    time.sleep(2)
    text = driver.find_element(by="xpath",
                               value="/html/body/div[1]/div/h1[2]").text
    return clean_text(text)


# Execute the main function and print its return value (which is None in this case).
print(main())
