from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()


driver.get("https://www.lambdatest.com/selenium-playground")


driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()


assert "simple-form-demo" in driver.current_url
print("URL validation passed!")


message = "Welcome to LambdaTest"


input_box = driver.find_element(By.ID, "user-message")
input_box.clear()
input_box.send_keys(message)


driver.find_element(By.ID, "showInput").click()

time.sleep(2)


output_text = driver.find_element(By.ID, "message").text

assert output_text == message, f"Expected '{message}' but got '{output_text}'"
print("Message validation passed!")

driver.quit()
