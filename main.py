from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from pageobject.TC_PIM_01 import Test_PIM_1
from pageobject.TC_PIM_02 import Test_PIM_2
from pageobject.TC_PIM_03 import Test_PIM_3
from webdriver_manager.chrome import ChromeDriverManager
from Locators.locators import orangehrm_xpaths
from report.excel_function import orangehrm_test_cases
# Define the URL and Dashboard URL
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

# Specify the Excel file and sheet number for storing test results
excel_file = "testcases.xlsx"
sheet_number = "Sheet1"
# Create an instance for excel functions and get toal no. in the sheet
e = orangehrm_test_cases(excel_file, sheet_number)
row = e.row_count()

# Initialize the ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)


for row in range(2, row+1):
   # Extract username and password from the Excel sheet
   username = e.read_data(row, 6)
   password = e.read_data(row, 7)
    # Find the usernam & password elements and Perform Login 
   time.sleep(5)
   driver.find_element(by=By.XPATH, value=orangehrm_xpaths().username_input_box).send_keys(username)
   driver.find_element(by=By.XPATH, value=orangehrm_xpaths().password_input_box).send_keys(password)
   driver.find_element(by=By.XPATH, value=orangehrm_xpaths().login_submit).click()


   driver.implicitly_wait(10)


   # Check if the current URL matches the dashboard URL
   if dashboard_url in driver.current_url:
       print("SUCCESS : Login success with username {a}".format(a=username))
       e.write_data(row, 8, "TEST PASS")
    
       # Create instances of Test_PIM_1, Test_PIM_2, and Test_PIM_3 classes and call their methods
       test1= Test_PIM_1(driver)
       test1.Adding_empl()
       test2= Test_PIM_2(driver)
       test2.editing_empl()
       test3= Test_PIM_3(driver)
       test3.deleting_empl()

       # Find the logout emelement and perform logout
       driver.find_element(by=By.XPATH, value=orangehrm_xpaths().logout_dropdown).click()
       logout_button = driver.find_element(by=By.XPATH, value=orangehrm_xpaths().logout_button).click()

   # If the URL doesn't match the dashboard URL, consider it a login failure  
   elif(url in driver.current_url):
       print("FAIL : Login failure with username {a}".format(a=username))
       e.write_data(row, 8, "TEST FAIL")
       driver.refresh()

# close the web browser
driver.quit()
