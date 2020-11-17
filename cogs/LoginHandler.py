from colorama import Fore, Style
import getpass as gp

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
            '''
                  Write code to check for username and password in the db.

                  Select data from the db where email == self.email and password == self.password.
                  Check for how many records it could retrieve. If there are no records then the username/password is incorrect.
                  If theres one record then the details are correct and the user is logged in.
                  If theres more than one record then something is wrong.
            '''
            return