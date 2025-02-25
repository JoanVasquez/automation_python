from selenium import webdriver  # Import the Selenium WebDriver module for browser automation


def get_driver():
  # Create an instance of ChromeOptions to customize browser settings
  options = webdriver.ChromeOptions()

  # Disable infobars that notify you that Chrome is being controlled by automated test software
  options.add_argument("disable-infobars")

  # Start the browser maximized to fill the screen
  options.add_argument("start-maximized")

  # Overcome limited resource problems when running in Docker or similar environments
  options.add_argument("disable-dev-shm-usage")

  # Bypass the OS security model, required for some environments like containers
  options.add_argument("no-sandbox")

  # Exclude the "enable-automation" switch to reduce detection of automation
  options.add_experimental_option("excludeSwitches", ["enable-automation"])

  # Disable certain blink features that can reveal automation control
  options.add_argument("disable-blink-features=AutomationControl")

  # Initialize the Chrome WebDriver with the specified options
  driver = webdriver.Chrome(options=options)

  # Navigate to the target URL
  driver.get("http://automated.pythonanywhere.com")

  # Return the driver instance for further actions
  return driver


def main_selenium():
  # Get the configured WebDriver instance
  driver = get_driver()

  # Locate the desired element using XPath.
  # 'by="xpath"' specifies that the locator strategy is XPath,
  # and 'value' provides the actual XPath string to locate the element.
  element = driver.find_element(by="xpath",
                                value="/html/body/div[1]/div/h1[1]")

  # Return the found element; printing it will display its string representation.
  return element


# Call the main function and print the result (the element found)
print(main_selenium())
