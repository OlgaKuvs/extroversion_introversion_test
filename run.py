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
    def __init__(self, questions, answers, question_used):
        self.questions = questions
        self.answers = answers
        self.question_used = question_used

list = []

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
    if name_check.isalpha() and len(name_check) > 1 :         
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
        list.append(QuestionsAnswers(a, n, 0)) 
    
    for a in range(len(list)):      

        print(list[a].questions) 
        print(list[a].answers) 
        print(list[a].question_used)  
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

def get_next_question(inner_score, test_check_inner):      
    
    if inner_score >= -3 and inner_score <= 3: 
        for i in range(len(test_check_inner)):
            print(test_check_inner[i].questions)
            print(test_check_inner[i].answers)
            print(f"used = {test_check_inner[i].question_used}")
            print(inner_score)
            if test_check_inner[i].question_used == 0:
                print("a")
                #test_check_inner
                #test-item = test_check[i]
                return test_check_inner[i]
            
        
    return None


def check_answers(test_check):    
    score = 0  
   
    while True:         
            test_item = get_next_question(score, test_check)            

            if test_item == None:                
                break 
            key_answer = test_item.answers                             
            
            print(Fore.WHITE + Back.BLUE + f"\n {test_item.questions}")        
            print(Style.RESET_ALL)                

            user_answer = input(" Y/N ?\n")                      
           
            if user_answer.lower() == "q":                
                break 
            elif (user_answer.lower() == "y" and key_answer == 1) :       
                score += 1               
                test_item.question_used = 1      
            elif (user_answer.lower() == "y" and key_answer == 0):
                score -= 1               
                test_item.question_used = 1               
            elif (user_answer.lower() == "n" and key_answer == 1) :          
                score -= 1                
                test_item.question_used = 1                
            elif (user_answer.lower() == "n" and key_answer == 0):
                score += 1               
                test_item.question_used = 1               
            else:
                cprint(f"Invalid data... Please enter  Y/N or Q to Quit ", "white", "on_red")          
    

              
def workbook_loaded():
    try:
        wb2 = load_workbook('C:/My websites/Project_3_Test/test_e_i.xlsx')                     
    except FileNotFoundError as fnf_error:
        print(Fore.WHITE + Back.RED + fnf_error)
    else:
        ws = wb2['Test']
    return ws               


check_data() 

 




