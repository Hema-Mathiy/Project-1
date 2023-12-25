from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from Locators.locators import orangehrm_xpaths


class Test_PIM_2:

    def __init__(self, driver):
        self.driver = driver
    # Create a method called editing_empl to edit the employee details
    def editing_empl (self):
        try:
            # Click on the "PIM" tab
            Pim_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, orangehrm_xpaths().PIM_tab)))
            Pim_button.click()
            # Click on the "Edit" icon button to edit existing employee detail
            edit = self.driver.find_element(By.XPATH, orangehrm_xpaths().edit_existing_emp)
            edit.click()
            # Enter employee details
            lst_name = self.driver.find_element(By.XPATH, orangehrm_xpaths().First_name)
            lst_name.send_keys("Manav")
            mid_name = self.driver.find_element(By.XPATH, orangehrm_xpaths().Middle_name)
            mid_name.send_keys("Raj")
            last_name = self.driver.find_element(By.XPATH, orangehrm_xpaths().Last_name)
            last_name.send_keys("M")
            nick_name = self.driver.find_element(By.XPATH, orangehrm_xpaths().Empl_ID)
            nick_name.send_keys("Laddu")

            contact_details_tab = self.driver.find_element(By.XPATH, orangehrm_xpaths().contact_detail)
            contact_details_tab.click()

            street1 = self.driver.find_element(By.XPATH, orangehrm_xpaths().st1)
            street1.send_keys("No:1/3, new jercy")
            street2 = self.driver.find_element(By.XPATH, orangehrm_xpaths().Empl_ID)
            street2.send_keys("456 Elm AvenueSuite 301")
            city = self.driver.find_element(By.XPATH, orangehrm_xpaths().city)
            city.send_keys("Townsville")
            state = self.driver.find_element(By.XPATH, orangehrm_xpaths().state)
            state.send_keys("Washington")
            # email_contact = self.driver.find_element(By.XPATH, orangehrm_xpaths().email)
            # email_contact.send_keys("manav@gmail.com")
            mobile = self.driver.find_element(By.XPATH, orangehrm_xpaths().mobile_no)
            mobile.send_keys("0987654321")
            # Click on the "Save" button to save the details
            self.driver.find_element(By.XPATH, orangehrm_xpaths().save_buuton).click()
        except NoSuchElementException as selenium_error:
            print(selenium_error)