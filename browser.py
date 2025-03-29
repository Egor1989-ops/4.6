import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions

path_to_driver = 'C:/Users/egors/Documents/driver/chromedriver.exe' # это пример пути как нужно указать а так driver нужно скачать от сюда https://googlechromelabs.github.io/chrome-for-testing/ и тут указать путь до него


@pytest.fixture()
def set_up_browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()