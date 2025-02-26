# Import the Selenium WebDriver module for browser automation.
from selenium import webdriver
# Import the Keys class to simulate keyboard input (e.g., pressing Enter).
from selenium.webdriver.common.keys import Keys
# Import the time module to introduce delays (e.g., sleep) during automation.
import time


def get_driver():
  """
    Configures and returns a Chrome WebDriver instance with custom options.
    This function sets up various Chrome options to improve compatibility and hide automation flags.
    """
  # Create an instance of ChromeOptions to customize browser settings.
  options = webdriver.ChromeOptions()

  # Disable infobars that notify you that Chrome is being controlled by automated test software.
  options.add_argument("disable-infobars")

  # Start the browser maximized so that it opens in full screen.
  options.add_argument("start-maximized")

  # Overcome limited resource problems when running in environments like Docker.
  options.add_argument("disable-dev-shm-usage")

  # Bypass the OS security model, which is required in some containerized or restricted environments.
  options.add_argument("no-sandbox")

  # Exclude the "enable-automation" switch to reduce the detection of automated control.
  options.add_experimental_option("excludeSwitches", ["enable-automation"])

  # Disable certain Blink (Chrome's rendering engine) features that might reveal automation usage.
  options.add_argument("disable-blink-features=AutomationControl")

  # Initialize the Chrome WebDriver with the specified options.
  driver = webdriver.Chrome(options=options)

  # Navigate to the target URL for the automation test (login page).
  driver.get("http://automated.pythonanywhere.com/login/")

  # Return the configured WebDriver instance for further actions.
  return driver


def main():
  # Get the configured WebDriver by calling get_driver().
  driver = get_driver()

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

  # Print the current URL of the browser to confirm navigation.
  print(driver.current_url)


# Execute the main function and print its return value (which is None in this case).
print(main())
