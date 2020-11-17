from colorama import Fore, Style
import getpass as gp

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

            self.email = input('E-mail: ' + Fore.GREEN)
            print(Style.RESET_ALL)
            self.name = input('Full Name: ')
            self.password = gp.getpass(prompt='Password' + Fore.WHITE + Style.DIM + '[hidden]' + Style.RESET_ALL + ': ', stream=None)

      def doRegister(self):
            '''
                  Write code to register the user in the db.

                  First select everything from the database and check if the email doesnt exist already.
                  If it exists then print an error or else insert all the data into the db.
            '''
            return