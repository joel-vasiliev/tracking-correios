def clearConsole():
    print(chr(27) + "[2J")

def welcome():
    from termcolor import colored
    from pyfiglet import Figlet

    f = Figlet(font='standard')

    print(colored(f.renderText('Rastreio Correios API'), 'yellow'))