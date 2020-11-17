from colorama import Fore, Style

def lor():
      return str(input('Please type ' + Fore.GREEN + 'login ' + Style.RESET_ALL + 'to login or type ' + Fore.GREEN + 'register ' + Style.RESET_ALL + 'to register: ' + Fore.CYAN))

def optionmenu(name):
      print(Fore.CYAN + '''
            +-----------------------------+
            |          Dashboard          |
            +-----------------------------+
      ''' + Style.RESET_ALL + f'''
                 Welcome back {Fore.RED + name + Style.RESET_ALL}!
      '''
      )

      print(f'''

{Fore.GREEN} 1) {Style.RESET_ALL} Browse products
{Fore.GREEN} 2) {Style.RESET_ALL} List a new product
{Fore.GREEN} 3) {Style.RESET_ALL} Manage current listings
{Fore.GREEN} 4) {Style.RESET_ALL} View sold products
{Fore.GREEN} 5) {Style.RESET_ALL} Log out

      ''')

      return str(input('Please select an option' + Fore.GREEN + '(0/1/2/3/4/5): ' + Fore.CYAN))