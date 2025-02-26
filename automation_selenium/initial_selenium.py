from selenium import webdriver  # Import the Selenium WebDriver module for browser automation
import time  # Import time module to use sleep delays when necessary


def get_driver():
  """
    Configures and returns a Chrome WebDriver instance with custom options.
    """
  # Create an instance of ChromeOptions to customize browser settings
  options = webdriver.ChromeOptions()

  # Disable infobars that notify you that Chrome is being controlled by automated test software
  options.add_argument("disable-infobars")

  # Start the browser maximized so that it opens in full screen
  options.add_argument("start-maximized")

  # Overcome limited resource problems when running in environments like Docker
  options.add_argument("disable-dev-shm-usage")

  # Bypass the OS security model, which is required in some containerized or restricted environments
  options.add_argument("no-sandbox")

  # Exclude the "enable-automation" switch to reduce the detection of automated control
  options.add_experimental_option("excludeSwitches", ["enable-automation"])

  # Disable certain Blink (Chrome's rendering engine) features that might reveal automation usage
  options.add_argument("disable-blink-features=AutomationControl")

  # Initialize the Chrome WebDriver with the specified options
  driver = webdriver.Chrome(options=options)

  # Navigate to the target URL for the automation test
  driver.get("http://automated.pythonanywhere.com")

  # Return the configured WebDriver instance for further actions
  return driver


def clean_text(text):
  """
    Extracts and converts the temperature value from a given text.

    Assumes the text follows the format: "Some Label: <temperature>"
    where <temperature> is a numeric value.

    Args:
        text (str): The text containing the temperature.

    Returns:
        float: The extracted temperature as a float.
    """
  # Split the text by ": " and convert the second part (temperature) to a float
  output = float(text.split(": ")[1])
  return output


def main_selenium():
  """
    Main function to run the Selenium automation sequence.

    It initializes the WebDriver, locates two elements by their XPath,
    prints the text of the first element, and extracts & prints the temperature from the second.
    """
  # Obtain the WebDriver instance configured with custom options
  driver = get_driver()

  # Locate the first element on the page using its XPath
  # 'by="xpath"' specifies that we are using XPath as our locator strategy
  # 'value' provides the actual XPath string for the desired element
  element_one = driver.find_element(by="xpath",
                                    value="/html/body/div[1]/div/h1[1]")

  # Pause execution for 2 seconds to ensure the page content is fully loaded or updated
  time.sleep(2)

  # Locate the second element on the page using its XPath
  element_two = driver.find_element(by="xpath",
                                    value="/html/body/div[1]/div/h1[2]")

  # Print the text content of the first element to the console
  print(element_one.text)
  # Use the clean_text function to extract and print only the temperature from the second element's text
  print(clean_text(element_two.text))
  # Note: Optionally, you could return an element or its text if needed, but here we are just printing


# Execute the main function to run the Selenium automation script
main_selenium()
