import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import io

class PenguinCommunityTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()# laddar ner rätt ver.

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
        submit = self.driver.find_element_by_id("submit")

        first_name_field.send_keys('Hans')
        last_name_field.send_keys('Hans')
        email_field.send_keys('hans@hans.de')
        password_field.send_keys('hans')
        confirm_password_field.send_keys('hans')
        picture_field._upload("penguin.png")
        picture_field.find_elements_by_xpath()
        submit.click()


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
        search_results = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'suggestion-list')))
        search_field.send_keys('Simon')
        print("sleep")
        print(search_results.find_elements_by_xpath('S'))
        results = [item.text for item in search_results.find_elements_by_xpath('S')]
        print(results)

    def test_add_huddle(self):
        self.driver.get('http://127.0.0.1:5000/sign_in')
        email_field = self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password')
        submit = self.driver.find_element_by_id('submit')

        email_field.send_keys('qq@qq.qq')
        password_field.send_keys('qq')
        submit.click()

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
