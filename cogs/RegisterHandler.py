import os
import getpass as gp
from colorama import Fore, Style
from connector import mycursor
from time import sleep

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
            try:
                  mycursor.execute(f'INSERT INTO users(email, name, password) VALUES ("{self.email}", "{self.name}", "{self.password}")')
                  os.environ['AUCUSER'] = self.name
            except:
                  print(Fore.RED + 'Something went wrong! Redirecting back to main menu.' + Style.RESET_ALL)
                  sleep(5)

            return