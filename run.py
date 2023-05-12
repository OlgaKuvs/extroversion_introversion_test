from openpyxl import load_workbook
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored, cprint
import re

just_fix_windows_console()
init(autoreset=True)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

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
    cprint(f"\nThank you, {name_tested}. Let's start. Are you oriented more towards the outer world or the inner world? ", "blue","on_light_grey")
    cprint("This easy test can give you a clear answer and help you understand your personality.  ", "blue","on_light_grey")
    cprint("Please enter Y for 'Yes' answer and N for 'No' answer.  ", "blue","on_light_grey")
    cprint("If you want to quit test, please enter Q  ", "blue","on_light_grey")   
    wsheet = workbook_loaded() 
    answers = list_answers(wsheet)
    questions = list_questions(wsheet)
    test_dictionary = dict(zip(questions, answers)) 
    print(test_dictionary) 
    # check_answers(questions, answers)  

def list_questions(worksheet):
    questions = []    
    for column in worksheet.iter_cols():          
        column_name = column[0].value
        if column_name == "Questions":                     
            for cell in column:
               questions.append(cell.value)
            return questions 

def list_answers(worksheet):
    answers = [] 
    for column in worksheet.iter_cols():          
        column_name = column[0].value       
        if column_name == "Answers": 
            for cell in column:
               answers.append(cell.value)
            return answers        


def check_answers(questions_all, answers_all):
    # while True:
        for i, n in range(0, len(questions_all)):
            print(questions_all[i+1])

            user_answer = input("\n Y/N ?\n")
            if (user_answer.lower() == "y"):
                return True       
            elif (user_answer.lower() == "n"):
                return False
            elif (user_answer.lower() == "q"):
                break
            else:
                print(Fore.WHITE + Back.RED + f"Invalid input {user_answer}... Please enter Y/N ") 
        

def workbook_loaded():
    try:
        wb2 = load_workbook('C:/My websites/Project_3_Test/test_e_i.xlsx')                     
    except FileNotFoundError as fnf_error:
        print(Fore.WHITE + Back.RED + fnf_error)
    else:
        ws = wb2['Test']
    return ws               


check_data() 

 




