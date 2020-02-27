from selenium import webdriver
from selenium.webdriver.support.ui import Select




class Browser():
    def __init__(self):
        set_options = webdriver.ChromeOptions()
        set_options.add_argument('headless')
        set_options.add_argument('window-size=640x480')
        self.driver = webdriver.Chrome(
            '/home/jhyun1000/Projects/pythonProgramming/driver/chromedriver', options=set_options)

    def close(self):
        self.driver.close()

    def click(self, CSS_selector):
        self.driver.find_element_by_css_selector(CSS_selector).click()

    def fill_field(self, CSS_selector, content):
        self.driver.find_element_by_css_selector(
            CSS_selector).send_keys(content)

    def move_location(self, url):
        self.driver.get(url)

    def get_current_page_url(self):
        return self.driver.current_url

    def take_screenshot(self, file_path):
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, time):
        self.driver.implicitly_wait(time)

    def get_current_html(self):
        return self.driver.page_source

    def execute_script(self, javascript: str):
        self.driver.execute_script(javascript)

    def select_dropdown_item(self,dropdown_tag, value):
        Select(self.driver.find_element_by_css_selector(dropdown_tag)).select_by_value(value)

