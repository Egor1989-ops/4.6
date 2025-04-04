from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestImput:
    def test_send_keys(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.XPATH, '//button[@id="query-builder-twet-clear-button"]') / click()
        driver.find_elements(By.CLASS_NAME, 'span[class="flex-1"]').send_keys('in:title bug')
        pass


class Tests:
    def test_2(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.XPATH, '(//div[@data-sestid="action-bar-autors"]/descendant::button"]') / click()
        driver.find_elements(By.XPATH, '(//span/input[@type="text"]').send_keys("bpasero")
        driver.find_elements(By.XPATH, '(//div[@aria-lable="User results"]').click()
        pass


class Tests:
    def test_3(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.XPATH, '(//select[@id="search_language"]').send_keys("Python")
        driver.find_element(By.XPATH, '(//*[@id="search_stars"]').send_keys("2000")
        driver.find_element(By.XPATH, '(//*[@id="search_filename"]').send_keys("environment.yml")
        pass


class TestRadiobutton:
    def test_radio_button(self, set_up_browser):
        driver.get('https://skillbox.ru/code/')
        driver.find_element(By.CSS_SELECTOR, input[value = 'profession']).click()
        pass


class TestSlider:
    def test_tooltip(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        driver.set_window_size(1400, 770)
        action_chains = webdriver.ActionChains(driver)
        time.sleep(3)
        action_chains.move_to_element(driver.find_element(By.XPATH, "//*[@id='commit-activity-master']")).perform()
        driver.find_element(By.XPATH, '//*[@id="js-repo-pjax-container"]')
        pass

class TestSlider:
    def test_slider(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://skillbox.ru/code/')
        el = driver.find_element(By.XPATH //*[contains(@class, 'slider-ltr')])
        action_chains = webdriver.ActionChains(driver)
        action_chains.click_and_hold(el)
            .click_and_hold(el)\
            .move_by_offset(xoffset=6, yoffset=12)\
            .perform()
        pass