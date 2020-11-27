import os
from colorama import Fore, Style
from connector import mycursor
from time import sleep

class itemsManager:
      def __init__(self):
            pass

      def prodList(self):
            mycursor.execute('SELECT * FROM objects WHERE sold="false"')
            result = mycursor.fetchall()

            for i in result:
                  print(i)

            return

      def addProd(self):
            mycursor.execute(f'SELECT ID FROM users WHERE email = "{str(os.environ["AUCMAIL"])}"')
            result = mycursor.fetchone()

            self.name = str(input('Enter name of the product: ' + Fore.GREEN))
            print(Style.RESET_ALL)
            self.price = int(input('Enter start price' + Fore.WHITE + Style.DIM + '[without commas]' + Style.RESET_ALL + ': ' + Fore.GREEN))
            print(Style.RESET_ALL)

            mycursor.execute(f'INSERT INTO objects(name, highest_bid, product_owner, highest_bidder, sold) VALUES ("{self.name}", {self.price}, {int(result[0])}, {int(result[0])}, "false")')
            
            print('Your product, ' + Fore.CYAN + self.name + Style.RESET_ALL + ' was successfully put up for sale! Redirecting back to main menu.')
            sleep(5)
            return

      def manageListings(self):
            mycursor.execute(f'SELECT ID FROM users WHERE email = "{str(os.environ["AUCMAIL"])}"')
            result = mycursor.fetchone()

            mycursor.execute(f'SELECT ID, name, highest_bid, highest_bidder FROM objects WHERE product_owner = {result[0]}')
            result = mycursor.fetchall()

            return