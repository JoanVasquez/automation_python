from .configurations import (get_driver, clean_text)
import time  # Import time module to use sleep delays when necessary
from datetime import datetime as dt


def write_file(text):
  """Write input text to a file"""
  filename = f"{dt.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
  with open(filename, "w") as file:
    file.write(text)


def main_selenium():
  """
    Main function to run the Selenium automation sequence.

    It initializes the WebDriver, locates two elements by their XPath,
    prints the text of the first element, and extracts & prints the temperature from the second.
    """
  # Obtain the WebDriver instance configured with custom options
  driver = get_driver("http://automated.pythonanywhere.com/")

  # Locate the first element on the page using its XPath
  # 'by="xpath"' specifies that we are using XPath as our locator strategy
  # 'value' provides the actual XPath string for the desired element
  element_one = driver.find_element(by="xpath",
                                    value="/html/body/div[1]/div/h1[1]")

  # Pause execution for 2 seconds to ensure the page content is fully loaded or updated
  time.sleep(2)

  # Print the text content of the first element to the console
  print(element_one.text)

  while True:
    time.sleep(2)
    # Locate the second element on the page using its XPath
    element_two = driver.find_element(by="xpath",
                                      value="/html/body/div[1]/div/h1[2]")
    text = str(clean_text(element_two.text))
    write_file(text)


# Execute the main function to run the Selenium automation script
main_selenium()
