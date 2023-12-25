from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from Locators.locators import orangehrm_xpaths
class Test_PIM_3:

    def __init__(self, driver):
        self.driver = driver
    # Create a method called deleting_empl to delete the employee details
    def deleting_empl (self):
        try:
            # Click on the "PIM" tab
            Pim_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, orangehrm_xpaths().PIM_tab)))
            Pim_button.click()
            # Click on the "Delete" icon button to delete existing employee detail
            dlt = self.driver.find_element(By.XPATH, orangehrm_xpaths().delete)
            dlt.click()
            # Click on the "Yes" button to confirm delete
            yes_button = self.driver.find_element(By.XPATH, orangehrm_xpaths().del_sbutton)
            yes_button.click()
        except NoSuchElementException as selenium_error:
            print(selenium_error)