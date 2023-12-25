from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from Locators.locators import orangehrm_xpaths


class Test_PIM_1:

    def __init__(self, driver):
        self.driver = driver
    # Create a method called Adding_empl to Adding employee details 
    def Adding_empl (self):
        try:
            # Click on the "PIM" tab  
            Pim_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, orangehrm_xpaths().PIM_tab)))
            Pim_button.click()
            # Click on the "Add" button to add a new employee
            Add = self.driver.find_element(By.XPATH, orangehrm_xpaths().Add_empl_button)
            Add.click()
            # Enter employee details
            lst_name = self.driver.find_element(By.XPATH, orangehrm_xpaths().First_name)
            lst_name.send_keys("Manav")
            mid_name = self.driver.find_element(By.XPATH, orangehrm_xpaths().Middle_name)
            mid_name.send_keys("Mathiy")
            last_name = self.driver.find_element(By.XPATH, orangehrm_xpaths().Last_name)
            last_name.send_keys("Kumar")

            empl_id = self.driver.find_element(By.XPATH, orangehrm_xpaths().Empl_ID)
            empl_id.send_keys("100001")

            self.driver.find_element(By.XPATH, orangehrm_xpaths().save_buuton).click()

            street1 = self.driver.find_element(By.XPATH, orangehrm_xpaths().st1)
            street1.send_keys("123 Main StreetApt 4B")
            street2 = self.driver.find_element(By.XPATH, orangehrm_xpaths().Empl_ID)
            street2.send_keys("No:1/3, new jercy old st")
            city = self.driver.find_element(By.XPATH, orangehrm_xpaths().city)
            city.send_keys("Cityville")
            state = self.driver.find_element(By.XPATH, orangehrm_xpaths().state)
            state.send_keys("Alaska")
            email_contact = self.driver.find_element(By.XPATH, orangehrm_xpaths().email)
            email_contact.send_keys("sample@gmail.com")
            mobile = self.driver.find_element(By.XPATH, orangehrm_xpaths().mobile_no)
            mobile.send_keys("1234567890")
            # Click on the "Save" button to save the details
            self.driver.find_element(By.XPATH, orangehrm_xpaths().save_buuton).click()

        except NoSuchElementException as selenium_error:
            print(selenium_error)