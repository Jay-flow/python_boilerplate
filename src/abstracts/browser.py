from abc import ABCMeta, abstractmethod
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from src.errors.no_popup_error import NoPopupError
from src.utils.env import get


class Browser(metaclass=ABCMeta):
    def __init__(self):
        self.EC = expected_conditions
        self.By = By
        self.__url = None
        self.__web_driver: webdriver.Chrome
        self.chrome_options = webdriver.ChromeOptions()

    @property
    def web_driver(self):
        self.__raise_property(self.__web_driver)

        return self.__web_driver

    @property
    def url(self):
        if self.__url is None:
            raise NotImplementedError

        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @abstractmethod
    def run(self, should_keep_open=False):
        self.chrome_options.add_argument("--start-maximized")

        if should_keep_open:
            self.chrome_options.add_experimental_option("detach", True)

        self.start_chrome()

    def __raise_property(self, value):
        if value is None:
            raise ValueError("Available after calling the start_chrome function.")

    def start_chrome(self, chrome_options=None):
        try:
            web_driver = webdriver.Chrome(options=self.chrome_options)
            web_driver.get(self.url)
            self.__web_driver = web_driver

            return self
        except PermissionError:
            return self.start_chrome(chrome_options)

    def __terminate_all_except_match_url_window(self, handle, url):
        main_window = self.__web_driver.window_handles[0]

        if self.__web_driver.current_url == url:
            main_window = handle
        else:
            self.__web_driver.close()

        return main_window

    def clear_child_window(self, remain_url=None) -> None:
        is_exist_child = 1 < len(self.__web_driver.window_handles)

        if is_exist_child:
            main_window = self.__web_driver.window_handles[0]

            for handle in self.__web_driver.window_handles:
                self.__web_driver.switch_to.window(handle)

                if remain_url is None:
                    main_window = self.__terminate_all_except_match_url_window(
                        handle, self.url
                    )
                else:
                    main_window = self.__terminate_all_except_match_url_window(
                        handle, remain_url
                    )

            return self.__web_driver.switch_to.window(main_window)

    def web_driver_wait(
        self,
        target: tuple[By, str],
        wait_type=expected_conditions.element_to_be_clickable,
    ) -> WebDriverWait:
        return WebDriverWait(self.__web_driver, get("WEB_DRIVER_WAIT_TIME")).until(
            wait_type(target)
        )

    def close_alert(self, is_accept: bool, callback=lambda alert: alert):
        try:
            alert = self.__web_driver.switch_to.alert
            result = callback(alert)

            if is_accept:
                alert.accept()
            else:
                alert.dismiss()

            return result
        except NoAlertPresentException:
            pass

    def switch_window(self, current_window_close: bool = False):
        current_window = self.__web_driver.current_window_handle

        if current_window_close:
            self.__web_driver.close()
        for handle in self.__web_driver.window_handles:
            if handle != current_window:
                return self.__web_driver.switch_to.window(handle)

        raise NoPopupError()

    def wait_page_load(self):
        count = 0
        while True:
            web_condition = self.__web_driver.execute_script(
                "return document.readyState"
            )

            if web_condition == "complete":
                return
            if count > 20:
                raise TimeoutError("페이지가 로딩되지 않았습니다.")

            count += 1
            sleep(0.2)

    def is_find_element(self, by: By, path: str) -> bool:
        try:
            if by == self.By.XPATH:
                self.web_driver.find_element_by_xpath(path)
            elif by == self.By.ID:
                self.web_driver.find_element_by_id(path)
            elif by == self.By.CLASS_NAME:
                self.web_driver.find_element_by_class_name(path)
            elif by == self.By.NAME:
                self.web_driver.find_element_by_name(path)
            elif by == self.By.LINK_TEXT:
                self.web_driver.find_element_by_link_text(path)
            elif by == self.By.PARTIAL_LINK_TEXT:
                self.web_driver.find_element_by_partial_link_text(path)
            elif by == self.By.TAG_NAME:
                self.web_driver.find_element_by_tag_name(path)

            return True
        except NoSuchElementException:
            return False

    def save_web_page(self, title):
        with open(f"{title}.html", "w", encoding="utf8") as f:
            f.write(self.web_driver.page_source)
