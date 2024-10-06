from time import sleep

from src.abstracts.browser import Browser
from selenium.webdriver.common.by import By


class Google(Browser):
    url = "https://www.google.com"

    def run(self):
        super().run()
        self.__input_search_text()
        self.__click_the_search_button()
        sleep(5)

    def __input_search_text(self):
        search_input = self.web_driver.find_element(By.CLASS_NAME, "gLFyf")
        search_input.send_keys("python_boilerplate")

    def __click_the_search_button(self):
        search_button = self.web_driver.find_element(
            By.CSS_SELECTOR, 'input[type="submit"]'
        )
        self.web_driver_wait((By.CSS_SELECTOR, 'input[type="submit"]'))

        search_button.click()


if __name__ == "__main__":
    Google().run()
