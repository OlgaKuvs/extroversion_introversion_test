from openpyxl import load_workbook
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored, cprint

just_fix_windows_console()
init(autoreset=True)

wb2 = load_workbook('C:/My websites/Project_3_Test/test_e_i.xlsx')

ws = wb2.active
ws2 = ws['A4'].value
ws3 = ws['B4'].value

""" 
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)

text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)
cprint("Hello, World!", "green", "on_red")

print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
print_red_on_cyan("Hello, World!")
print_red_on_cyan("Hello, Universe!")
"""

# print(Fore.RED + Back.YELLOW  + "Welcome to Extroversion Introversion Test")
cprint(" Welcome to Extroversion Introversion Test! ", "white", "on_blue")

name = input("Please enter your name:\n")
# email_str = input("Please enter your email:\n")
name_str = name.split()
name_str = ''.join(name_str)

if name_str.isalpha():
    cprint(f" Hello, {name}! Would you like to start test? Please type Y/N ", "blue","on_light_grey")
else:
     print(Fore.WHITE + Back.RED + f"Invalid data... Please enter correct name:")




