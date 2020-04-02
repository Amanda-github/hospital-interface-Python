import re
from colorama import Fore, Back, Style


class Hospital ():
    def __init__(self, user_name, password, status):
        self.user_name = user_name
        self.password = password
        self.status = 0

    def login_name(self, name, password):
        self.user_name = self.user_name + str(name)
        self.password = self.password + password

    def login_menu():

    print("Welcome to Next Hospital Portal")
         input("Please enter username: ")
         input("Please enter password: ")

        if self.user_name == "Nic":
            self.status += 1
        else:
            print("Incorrect Username, please try again")

        # self.password = 12345
        # match_re = r"\d{5}"
        # hide_password = re.sub(match_re, "*****", self.password)
        # print(hide_password)
