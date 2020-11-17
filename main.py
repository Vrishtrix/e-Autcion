import os
from getpass import getuser
from colorama import Fore, Style
from cogs import MenuHandler
from cogs.LoginHandler import userLogin
from cogs.RegisterHandler import userRegister

def clear():
      if os.name == 'nt':
            _ = os.system('cls')
      else:
            _ = os.system('clear')

def main():
      if 'USER' in os.environ:
            name = getuser()
      else:
            menuChoice = MenuHandler.lor()
            print(Style.RESET_ALL)
            clear()
            
            if menuChoice == 'login':
                  userContext = userLogin()
                  userContext.loginScreen()
                  userContext.doLogin()

            elif menuChoice == 'register':
                  userContext = userRegister()
                  userContext.registerScreen()
                  userContext.doRegister()

            else:
                  print(Fore.RED + 'Invalid option provided!' + Style.RESET_ALL)
      
if __name__ == '__main__':
      clear()
      print(Fore.CYAN + '''
            +------------------------------------------------+
            |          Online Auction System V1.0.0          |
            +------------------------------------------------+
      ''' + Style.RESET_ALL + '''
                           By Vrishin and Soumo
      '''
      )

      main()