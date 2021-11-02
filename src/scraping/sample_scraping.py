from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SampleScraping:
    def __init__(self) -> None:
        self.__driver = webdriver.Chrome(ChromeDriverManager().install())

    def __search_the_pycon(self) -> None:
        search_element = self.__driver.find_element_by_name("q")
        search_element.clear()

        search_element.send_keys("pycon")
        search_element.send_keys(Keys.RETURN)

    def run(self) -> None:
        self.__driver.get("http://www.python.org")
        self.__search_the_pycon()
        sleep(5)

        self.__driver.close()


if __name__ == "__main__":
    SampleScraping().run()
