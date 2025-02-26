# Import the Selenium WebDriver module for browser automation.
from selenium import webdriver


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


def get_driver(url: str):
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
  driver.get(url)

  # Return the configured WebDriver instance for further actions.
  return driver
