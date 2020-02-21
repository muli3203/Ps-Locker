import pyperclip
import random
import string

class User:
    '''
    Class that generates instances of user credentials
    '''

    users_list = [] # Empty list where users will be saved

    def __init__(self, first_name, last_name, password):
        '''
        __init__ method that helps us define properties for our objects
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password


    def save_user(self):
        '''
        save_user method that saves user objects in the users_list
        '''
        User.users_list.append(self)
class Credentials:
    '''
    Class that generates instances of account credentials, generate passwords and save information
    '''

    credentials_list = []
    users_credentials_list = []

    @classmethod
    def check_user(cls, first_name, password):
        '''
        Method that checks if the name and the password entered match entries in the users list.
        '''
        current_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user

    def __init__(self, user_name, site_name, account_name, password):
        '''
        __init__ method that helps us define properties for our objects
        '''

        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password


    def save_credential(self):
        '''
        save_credential method that saves credential objects in the credentials_list
        '''

        Credentials.credentials_list.append(self)
        

    def generate_password(self):
        '''
        Function to generate a password where a user can generate a password based on their length of choice
        '''
        chars = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890^?!?$%&/()=?`'+#*'~';:_,.-<>|"
        password = ""

        print("Use Char list = %s \n" % chars)

        length = int(input("[*] Input Password Length: "))
        while len(password) != length:
            password = password + random.choice(chars)
            if len(password) == length:
                print("Password: %s" % password)
        return password
        

    @classmethod
    def display_credential(cls, user_name):
        '''
        Class method to show the list of credentials saved
        '''
        users_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                users_credentials_list.append(credential)
        return users_credentials_list


    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        Class method that takes a site name and returns the credential that matches that site
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential

        
    @classmethod
    def copy_credential(cls, site_name):
        '''
        Class method that copies a credentials details after the credentials site_name has been entered
        '''
        find_credential = Credentials.find_by_site_name(site_name)
        return pyperclip.copy(find_credential.password)
