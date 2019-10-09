import unittest
import pyperclip
from user import User
from  credentials import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('Cheryl', 'Muli', 'test123') # create user object


    def test__init__(self):
        '''
        Test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_user.first_name, "Cheryl")
        self.assertEqual(self.new_user.last_name, "Muli")
        self.assertEqual(self.new_user.password, "test123")


    def test_save_user(self):
        '''
        Test case to test if the user object is saved to the users list.
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)



class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def test_check_user(self):
        '''
        Test case to test whether login feature is functional.
        '''
        self.new_user = User('Cheryl', 'Muli', 'test123')
        self.new_user.save_user()
        user2 = User('Cheryl', 'Muli', 'test123')
        user2.save_user()

        for user in User.users_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user = user.first_name
        return current_user

        self.assertEqual(current_user, Credentials.check_user(user2.password, user2.first_name))

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_credential = Credentials('Cheryl', 'Twitter','Muli', 'test123')


    def test__init__(self):
        '''
        Test case to check if creation of credential instances is properly done.
        '''

        self.assertEqual(self.new_credential.user_name, "Cheryl")
        self.assertEqual(self.new_credential.site_name, "Twitter")
        self.assertEqual(self.new_credential.account_name, "Muli")
        self.assertEqual(self.new_credential.password, "test123")


    def test_save_credentials(self):
        '''
        Test case to check if we can save credentials to the credentials list.
        '''

        self.new_credential.save_credential()
        facebook = Credentials('Cheryl', 'Twitter','Muli', 'test123')
        facebook.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 2)


    def tearDown(self):
        '''
        A method that clears the users credentials list after every test.
        '''

        Credentials.credentials_list = []
        User.users_list = []

    def test_display_credentials(self):
        '''
        Test case to test if our objects show.
        '''

        self.new_credential.save_credential()
        facebook = Credentials('Cheryl', 'Facebook','Muli', 'test123')
        facebook.save_credential()
        gmail = Credentials('Cheryl', 'Twitter','Gmail', 'test123')
        gmail.save_credential()
        self.assertEqual(len(Credentials.display_credential(facebook.user_name)), 1)


    def test_find_by_site_name(self):
        '''
        Test case to test if we can search credential by site_name and return the correct credential.
        '''

        self.new_credential.save_credential()
        gmail = Credentials('Cheryl', 'Twitter','Gmail', 'test123')
        gmail.save_credential()
        credential_exists = Credentials.find_by_site_name('Gmail')
        self.assertEqual(credential_exists, gmail)


    def test_copy_credential(self):
        '''
        Test case to test if the copy credential function copies the correct credential.
        '''

        self.new_credential.save_credential()
        instagram = Credentials('Cheryl', 'Twitter','Instagram', 'test123')
        instagram.save_credential()
        find_credential = None
        for credential in Credentials.users_credentials_list:
            find_credential = Credentials.find_by_site_name(credential.site_name)
            return pyperclip.copy(find_credential.password)
        Credentials.copy_credential(self.new_credential.site_name)
        self.assertEqual('test123s', pyperclip.paste())
        print(pyperclip.paste())



if __name__ == '__main__':
    unittest.main()
