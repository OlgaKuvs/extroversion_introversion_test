from openpyxl import load_workbook
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored, cprint
import re

just_fix_windows_console()
init(autoreset=True)

wb2 = load_workbook('C:/My websites/Project_3_Test/test_e_i.xlsx')
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

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

def check_data():
    while True:
        name = input("\nPlease enter your name:\n")
        name_valid = validate_name(name)        
        
        if name_valid:
            cprint(f"\n Hello, {name}!", "blue","on_light_grey") 
            while True:
                email_str = input("\nPlease enter your email: \n")                
                if validate_email(email_str):
                    start_test(name) 
                    break
            break            
        else:
            print(f"Invalid data, please try again.\n")          
    
            
       
def validate_name(name_val):
    """
    Splits a string into a list and then join the list back into one string without spaces.
    Check if all the characters are alphabet letters.         
    """    
    
    name_check = "".join(name_val.split())     
    if name_check.isalpha():
        print("Name Valid")  
        return True  
    else:        
        print(Fore.WHITE + Back.RED + f"Invalid name {name_val}... Please enter correct name")
        print("\n")
        return False 
 
    

def validate_email(email_val):
    """ 
    Check if email address valid or not.       
    """
    x = re.fullmatch(regex, email_val)
    if x:
        return True    
        
    else:        
        print(Fore.WHITE + Back.RED + f"Invalid e-mail {email_val}... Please enter correct e-mail")       
        return False 

def start_test(name_tested):
    cprint(f"\n Thank you, {name_tested}. Would you like to start test? Please type Y/N ", "blue","on_light_grey")
    while True:
        starting_test = input("\n Y/N ?\n")
        val = validate_agreement(starting_test)    
        if val:
            workbook_loaded()
        break


def validate_agreement(agree):
    if (agree.lower() == "y"):
        return True       
    elif (agree.lower() == "n"):
        return False
    else:
        print(Fore.WHITE + Back.RED + f"Invalid input {agree}... Please enter Y/N ") 

def workbook_loaded():
    try:
        wb2 = load_workbook('C:/My websites/Project_3_Test/test_e_i.xlsx')        
    except FileNotFoundError as e:
        print(Fore.WHITE + Back.RED + f"File not found...")
    else:
        ws = wb2.active
        ws2 = ws['A4'].value
        print(ws2)
        


check_data() 

 




