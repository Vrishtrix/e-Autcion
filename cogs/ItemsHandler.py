import os
from colorama import Fore, Style
from tabulate import tabulate
from connector import mycursor
from time import sleep

class itemsManager:
      def __init__(self):
            pass

      def prodList(self):
            print(Fore.CYAN + '''
                  +----------------------------+
                  |      Browse  products      |
                  +----------------------------+
            ''' + Style.RESET_ALL + '''
Browse the marketplace for products that have been put up for sale.
            '''
            )

            mycursor.execute('SELECT objects.ID, objects.name, objects.highest_bid, users.name FROM objects INNER JOIN users ON objects.product_owner = users.ID WHERE sold="false"')
            result = mycursor.fetchall()

            print(tabulate(result, headers=['Product ID', 'Product Name', 'Highest Bid', 'Name of seller'], tablefmt='psql'))

            return

      def addProd(self):
            print(Fore.CYAN + '''
                  +----------------------------+
                  |     List a new product     |
                  +----------------------------+
            ''' + Style.RESET_ALL
            )

            mycursor.execute(f'SELECT ID FROM users WHERE email = "{str(os.environ["AUCMAIL"])}"')
            result = mycursor.fetchone()

            self.name = str(input('Enter name of the product: ' + Fore.GREEN))
            print(Style.RESET_ALL)
            self.price = int(input('Enter start price' + Fore.WHITE + Style.DIM + '[without commas]' + Style.RESET_ALL + ': ' + Fore.GREEN))
            print(Style.RESET_ALL)

            mycursor.execute(f'INSERT INTO objects(name, highest_bid, product_owner, highest_bidder, sold) VALUES ("{self.name}", {self.price}, {int(result[0])}, {int(result[0])}, "false")')
            
            print('Your product, ' + Fore.GREEN + self.name + Style.RESET_ALL + ' was successfully put up for sale!' + Fore.RED + ' Redirecting back to main menu.' + Style.RESET_ALL)
            sleep(5)
            return

      def manageListings(self):
            mycursor.execute(f'SELECT ID FROM users WHERE email = "{str(os.environ["AUCMAIL"])}"')
            result = mycursor.fetchone()

            mycursor.execute(f'SELECT objects.ID, objects.name, objects.highest_bid, users.name FROM objects INNER JOIN users ON objects.highest_bidder = users.ID WHERE product_owner = {result[0]}')
            result = mycursor.fetchall()

            print(tabulate(result, headers=['Product ID', 'Product Name', 'Highest Bid', 'Name of bidder'], tablefmt='psql'))

            return

      def soldProducts(self):
            print(Fore.CYAN + '''
                  +-----------------------------+
                  |      Your sold products     |
                  +-----------------------------+
            ''' + Style.RESET_ALL + '''
      Here's a list of all your products that were sold already.
            '''
            )

            mycursor.execute(f'SELECT objects.ID, objects.name, objects.highest_bid, users.name FROM objects INNER JOIN users ON objects.highest_bidder = users.ID WHERE sold = "true" AND users.email = "{os.environ["AUCMAIL"]}"')
            result = mycursor.fetchall()

            print(tabulate(result, headers=['Product ID', 'Product Name', 'Bid Amount', 'Name of buyer'], tablefmt='psql'))

            return