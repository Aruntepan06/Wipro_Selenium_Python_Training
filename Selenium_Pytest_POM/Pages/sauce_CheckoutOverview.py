from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class CheckoutOverview:

    page_title = (By.XPATH, "//span[@class='title']")
    finish_button = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_page_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.page_title)
        ).text

    def click_finish(self):
        finish = self.wait.until(
            EC.presence_of_element_located(self.finish_button)
        )

        # Scroll to button
        self.driver.execute_script("arguments[0].scrollIntoView(true);", finish)

        # Wait until clickable and click
        self.wait.until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()