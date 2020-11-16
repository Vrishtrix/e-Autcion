from connector import mycursor
from colorama import Fore, Style
import getpass as gp

class userRegister:
      def __init__(self):
            pass

      def registerScreen(self):
            print(Fore.CYAN + '''
                  +----------------------------+
                  |           Register         |
                  +----------------------------+
            '''
            )

            print(Style.RESET_ALL)

            self.email = input('E-mail: ')
            self.name = input('Full Name: ')
            self.password = gp.getpass(prompt='Password' + Fore.GREEN + '(input hidden)' + Style.RESET_ALL + ': ', stream=None)

      def doRegister():
            '''
                  Write code to register the user in the db.

                  First select everything from the database and check if the email doesnt exist already.
                  If it exists then print an error or else insert all the data into the db.
            '''
            return