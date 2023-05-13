from openpyxl import load_workbook
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored, cprint
import re

just_fix_windows_console()
# init(autoreset=True)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class QuestionsAnswers:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers

list = []

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
            cprint(f"Invalid data, please try again.\n", "white", "on_red")          
    
            
       
def validate_name(name_val):
    """
    Splits a string into a list and then join the list back into one string without spaces.
    Check if all the characters are alphabet letters.         
    """    
    
    name_check = "".join(name_val.split())     
    if name_check.isalpha():         
        return True  
    else:        
        cprint(f"Invalid name {name_val}... Please enter correct name", "white", "on_red")        
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
        cprint(f"Invalid e-mail {email_val}... Please enter correct e-mail", "white", "on_red")       
        return False 

def start_test(name_tested):
    print(Fore.WHITE + Back.BLUE + f"\nThank you, {name_tested}. Let's start. Are you oriented more towards the outer world or the inner world?\n ")    
    print(f"This easy test can give you a clear answer and help you understand your personality.\n ")
    print(f"Please enter Y for 'Yes' answer and N for 'No' answer. ")
    print(Style.RESET_ALL)
    wsheet = workbook_loaded() 
    answers = list_answers(wsheet)
    questions = list_questions(wsheet)
       
    for a, n in zip(questions, answers): 
        print(a, n)        
        list.append(QuestionsAnswers(a, n))
    # print(list[0].questions)      
    check_answers(list)

def list_questions(worksheet):
    questions = []    
    for column in worksheet.iter_cols():          
        column_name = column[0].value
        if column_name == "Questions":                     
            for cell in column:
               questions.append(cell.value)
            questions.pop(0)
            return questions 

def list_answers(worksheet):
    answers = [] 
    for column in worksheet.iter_cols():          
        column_name = column[0].value       
        if column_name == "Answers":             
            for cell in column:
               answers.append(cell.value)
            answers.pop(0)
            return answers       


def check_answers(test_check):
    i = 0
    while True:
        test_item = test_check[i]            
        
        print(Fore.WHITE + Back.BLUE + f"\n {test_item.questions}")        
        print(Style.RESET_ALL)                

        user_answer = input(" Y/N ?\n")
        if (user_answer.lower() == "y"):
            i+=1
            continue       
        elif (user_answer.lower() == "n"):
            i+=1
            continue
        elif (user_answer.lower() == "q"):                
            break
        
            
                    
def workbook_loaded():
    try:
        wb2 = load_workbook('C:/My websites/Project_3_Test/test_e_i.xlsx')                     
    except FileNotFoundError as fnf_error:
        print(Fore.WHITE + Back.RED + fnf_error)
    else:
        ws = wb2['Test']
    return ws               


check_data() 

 




