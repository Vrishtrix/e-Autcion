import os
import getpass as gp
from colorama import Fore, Style

class userRegister:
      def __init__(self):
            pass

      def registerScreen(self):
            print(Fore.CYAN + '''
                  +----------------------------+
                  |          Register          |
                  +----------------------------+
            ''' + Style.RESET_ALL
            )

            self.email = str(input('E-mail: ' + Fore.GREEN))
            print(Style.RESET_ALL)
            self.name = str(input('Full Name: '))
            self.password = gp.getpass(prompt='Password' + Fore.WHITE + Style.DIM + '[hidden]' + Style.RESET_ALL + ': ', stream=None)

      def doRegister(self):
            '''
                  Write code to register the user in the db.

                  First select everything from the database and check if the email doesnt exist already.
                  If it exists then print an error or else insert all the data into the db.
            '''
            os.environ['USER'] = self.name
            return