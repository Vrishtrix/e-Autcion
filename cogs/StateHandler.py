from time import sleep
from colorama import Fore, Style
from connector import mycursor

def isSold(id, action):
      if action == 'sold':
            try:
                  mycursor.execute(f'UPDATE objects SET sold="true" WHERE ID={id}')
                  print('Your Product with ID ' + Fore.GREEN + str(id) + Style.RESET_ALL + ' was successfully marked as sold.')
                  sleep(5)

            except:
                  print(Fore.RED + 'Something went wrong. Redirecting back to dashboard.' + Style.RESET_ALL)
                  sleep(5)

      elif action == 'delete':
            try:
                  mycursor.execute(f'DELETE FROM objects WHERE ID={id}')
                  print('Your Product with ID ' + Fore.GREEN + str(id) + Style.RESET_ALL + ' was successfully deleted.')
                  sleep(5)

            except:
                  print(Fore.RED + 'Something went wrong. Redirecting back to dashboard.' + Style.RESET_ALL)
                  sleep(5)
      
      else:
            print(Fore.RED + 'Something went wrong. Redirecting back to dashboard.' + Style.RESET_ALL)
            sleep(5)

      return