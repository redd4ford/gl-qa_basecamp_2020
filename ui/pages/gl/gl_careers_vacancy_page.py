from urllib.parse import urljoin

from selenium.webdriver.common.by import By

from ui.config import Config, GlobalLogicEndpoints
from ui.pages.base_page import BasePage


class GLCareersVacancyPage(BasePage):
    URL = urljoin(Config.GLOBAL_LOGIC_BASE_URL, GlobalLogicEndpoints.GLOBAL_LOGIC_CAREERS_URL)

    VACANCY_TITLE = (By.XPATH, '/html/body/div[2]/section[4]/div/h1')

    def __init__(self, browser, urn: str = None):
        super().__init__(browser)
        if urn is not None:
            self.open(urn)

    def open(self, urn: str = None):
        self.browser.implicitly_wait(Config.DEFAULT_TIMEOUT)
        self.browser.get(f'{GLCareersVacancyPage.URL}{urn}')

    @property
    def vacancy_title(self):
        return self.browser.find_element(*self.VACANCY_TITLE).text
