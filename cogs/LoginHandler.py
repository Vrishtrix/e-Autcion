from colorama import Fore, Style
from connector import mycursor
from time import sleep
import getpass as gp
import os

class userLogin:
      def __init__(self):
            pass

      def loginScreen(self):
            print(Fore.CYAN + '''
                  +----------------------------+
                  |           Login            |
                  +----------------------------+
            ''' + Style.RESET_ALL
            )

            self.email = str(input('E-mail: ' + Fore.GREEN))
            print(Style.RESET_ALL)
            self.password = gp.getpass(prompt='Password' + Fore.WHITE + Style.DIM + '[hidden]' + Style.RESET_ALL + ': ', stream=None)

      def doLogin(self):
            mycursor.execute(f'SELECT name, email FROM users WHERE email = "{self.email}" AND password = "{self.password}"')
            result = mycursor.fetchone()

            if result == None:
                  print(Fore.RED + 'Invalid username or password. Redirecting back to the menu.' + Style.RESET_ALL)
                  sleep(5)

            else:
                  os.environ['AUCUSER'], os.environ['AUCMAIL'] = str(result[0]), str(result[1])
            
            return