#pip install colorama


from colorama import init, Fore, Back, Style
init()

print(Fore.RED + 'some red text')
print(Back.MAGENTA + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
