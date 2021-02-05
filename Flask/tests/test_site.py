import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import io
import time

class PenguinCommunityTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()# laddar ner rätt ver.
        self.driver.maximize_window()

    def test_login(self):
        self.driver.get('http://127.0.0.1:5000/sign_in')
        email_field = self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password')
        submit = self.driver.find_element_by_id('submit')

        email_field.send_keys('qq@qq.qq')
        password_field.send_keys('qq')
        submit.click()

        welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'factDisplay')))
        self.assertEqual("Did you know?", welcome.text)



    def test_register(self):
        self.driver.get('http://127.0.0.1:5000/sign_up')
        first_name_field = self.driver.find_element_by_id("first_name")
        last_name_field = self.driver.find_element_by_id("last_name")
        email_field = self.driver.find_element_by_id("email")
        password_field = self.driver.find_element_by_id("password")
        confirm_password_field = self.driver.find_element_by_id("confirm_password")
        picture_field = self.driver.find_element_by_id("file")
        submit = self.driver.find_element_by_id("submit_reg")

        first_name_field.send_keys('Hans')
        last_name_field.send_keys('Hans')
        email_field.send_keys('hans@hans.de')
        password_field.send_keys('hans')
        confirm_password_field.send_keys('hans')
        picture_field.send_keys("C:\\Users\Admin\Pictures\ping_selfie2.jpg")
        submit.click()
        time.sleep(10)


    def test_search(self):
        self.driver.get('http://127.0.0.1:5000/sign_in')
        email_field = self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password')
        submit = self.driver.find_element_by_id('submit')

        email_field.send_keys('qq@qq.qq')
        password_field.send_keys('qq')
        submit.click()

        welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "Penguin-Com")))
        self.assertEqual("Penguin Community", welcome.text)

        search_field = self.driver.find_element_by_id('nameInput')
        #search_field.clear()
        search_results = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'search-result')))
        search_field.send_keys('Hans')

        search_results = [item.text for item in search_results.find_elements_by_tag_name('a')]
        self.assertIn('Hans', search_results)
        self.assertEqual(len(search_results), 2)

        print("sleep")




    def test_visit_profile(self):
        self.driver.get('http://127.0.0.1:5000/sign_in')
        email_field = self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password')
        submit = self.driver.find_element_by_id('submit')

        email_field.send_keys('qq@qq.qq')
        password_field.send_keys('qq')
        submit.click()

        welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'myNavbar')))
        self.assertEqual("Feed\nCreate post\nProfile\nLogout", welcome.text)
        profile_field = self.driver.find_element_by_id("Profile")
        profile_field.click()
        welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'myNavbar')))
        self.assertEqual("Feed\nCreate post\nProfile\nLogout", welcome.text)


    def test_update_profile(self):
        self.driver.get('http://127.0.0.1:5000/sign_in')
        self.driver.maximize_window()
        email_field = self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password')
        submit = self.driver.find_element_by_id('submit')

        email_field.send_keys('qq@qq.qq')
        password_field.send_keys('qq')
        submit.click()

        welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'myNavbar')))
        self.assertEqual("Feed\nCreate post\nProfile\nLogout", welcome.text)
        profile_field = self.driver.find_element_by_id("Profile")
        profile_field.click()
        welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'myNavbar')))
        self.assertEqual("Feed\nCreate post\nProfile\nLogout", welcome.text)
        update_button = self.driver.find_element_by_id("update_button")
        update_button.click()
        first_name_field = self.driver.find_element_by_id("first_name")
        last_name_field = self.driver.find_element_by_id("last_name")
        update = self.driver.find_element_by_id('update')
        first_name_field.send_keys('Hans')
        last_name_field.send_keys('Hans')
        update.click()

        welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'alert')))
        self.assertEqual("Your account has been updated", welcome.text)


    def test_create_post(self):
        self.driver.get('http://127.0.0.1:5000/sign_in')
        email_field = self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password')
        submit = self.driver.find_element_by_id('submit')

        email_field.send_keys('qq@qq.qq')
        password_field.send_keys('qq')
        submit.click()

        welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'myNavbar')))
        self.assertEqual("Feed\nCreate post\nProfile\nLogout", welcome.text)
        profile_field = self.driver.find_element_by_id("create_post")
        profile_field.click()
        create_button = self.driver.find_element_by_id("myBtn")
        create_button.click()

        description_field = self.driver.find_element_by_id("description")
        file_upload_field = self.driver.find_element_by_id("file")
        upload_btn = self.driver.find_element_by_id("upload_btn")

        description_field.send_keys('Photo of a lovely penguin')
        file_upload_field.send_keys("C:\\Users\Admin\Pictures\ping_selfie2.jpg")
        upload_btn.click()


    """
    def test_add_friend(self):
        self.driver.get('http://127.0.0.1:5000')
        username_field = self.driver.find_element_by_id('username')
        password_field = self.driver.find_element_by_id('password')
        submit = self.driver.find_element_by_name('submit')

        username_field.send_keys('admin')
        password_field.send_keys('superstar')
        submit.send_keys(Keys.RETURN)

        welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'welcome')))

        num_friends_before = len(self.driver.find_elements_by_class_name('friend'))

        friend_field = self.driver.find_element_by_id('friend')
        friend_field.send_keys('Bosse')
        friend_field.send_keys(Keys.RETURN)

        welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'welcome')))
        num_friends_after = len(self.driver.find_elements_by_class_name('friend'))

        self.assertEqual(num_friends_before + 1, num_friends_after)
    """

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
