import os
from getpass import getuser
from colorama import Fore, Style
from cogs import MenuHandler
from cogs.ItemsHandler import itemsManager
from cogs.LoginHandler import userLogin
from cogs.RegisterHandler import userRegister

def clear():
      if os.name == 'nt':
            _ = os.system('cls')
      else:
            _ = os.system('clear')

def main():
      if 'AUCUSER' in os.environ:
            name, email = os.environ['AUCUSER'], os.environ['AUCMAIL']
            menuChoice = MenuHandler.optionmenu(name)
            print(Style.RESET_ALL)
            clear()

            itemManager = itemsManager()

            if menuChoice == '1':
                  itemManager.prodList()

            elif menuChoice == '2':
                  itemManager.addProd()
                  clear()
                  main()

            elif menuChoice == '3':
                  itemManager.manageListings()

            elif menuChoice == '5':
                  del os.environ['AUCUSER']
                  del os.environ['AUCMAIL']

            else:
                  print(Fore.RED + 'Invalid option provided!' + Style.RESET_ALL)

      else:
            menuChoice = MenuHandler.lor()
            print(Style.RESET_ALL)
            clear()
            
            if menuChoice == 'login':
                  userContext = userLogin()
                  userContext.loginScreen()
                  userContext.doLogin()
                  clear()
                  main()

            elif menuChoice == 'register':
                  userContext = userRegister()
                  userContext.registerScreen()
                  userContext.doRegister()
                  clear()
                  main()

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