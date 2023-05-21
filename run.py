from openpyxl import load_workbook
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
from colorama import init
import os
import platform 
import re


EXCEL_SHEET_NAME = 'test_e_i.xlsx'
BANNER = """                                                      
.---..   ..---..--.  .--.   --.--.   ..---..--.  .--.   .---..---..-..---.
|     \ /   |  |   ):    :    |  |\  |  |  |   ):    :    |  |   (   ) |  
|---   /    |  |--' |    |    |  | \ |  |  |--' |    |    |  |--- `-.  |  
|     / \   |  |  \ :    ;    |  |  \|  |  |  \ :    ;    |  |   (   ) |  
'---''   '  '  '   ` `--'   --'--'   '  '  '   ` `--'     '  '---'`-'  '  
                                                                                                                                                             
"""
THANK_YOU = """                                              
                                               
.---..   .    .    .   ..   .  .   ..--. .   ..
  |  |   |   / \   |\  ||  /    \ /:    :|   ||
  |  |---|  /- -\  | \ ||-'      : |    ||   ||
  |  |   | /     \ |  \||  \     | :    ;:   ;'
  '  '   ''       `'   ''   `    '  `--'  `-' o
                                               
                                               
"""

just_fix_windows_console()
init(autoreset=True)
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
cursor_shape = '\x1b[3 q'
print(cursor_shape, end='')


def clear():
    plt = platform.system()

    if plt == "Windows":
        clear = lambda: os.system('cls')
    elif plt == "Linux":
        clear = lambda: os.system('clear')    
    clear()
    

# Class for the questions and answer key instances and used question flag

class QuestionsAnswers:
    def __init__(self, questions, answers, question_used):
        self.questions = questions
        self.answers = answers
        self.question_used = question_used

def check_data_workbook(name_used, email_used):
    """
    Check if user's data is already in the worksheet.
    If yes, print user's last test result.
    """
    try:
        wb2 = load_workbook(EXCEL_SHEET_NAME)                     
    except FileNotFoundError as fnf_error:
        print(Fore.RED + Style.BRIGHT + fnf_error)
    else:
        ws = wb2["Users"]

        for row in ws:
            name = row[0].value
            email = row[1].value 
            result = row[2].value           
            if name.lower() == name_used.lower() and email == email_used:
                if result > -3 and result < 3:
                    print(f"Welcome again {name_used}! Your last result was mostly AMBIVERT")
                elif result <= -3:
                    print(f"Welcome again {name_used}! Your last result was mostly INTROVERT")
                elif result >= 3:
                    print(f"Welcome again {name_used}! Your last result was mostly EXTROVERT")                
                return True            


print(Fore.YELLOW + Style.BRIGHT + BANNER + "WELCOME TO EXTROVERSION INTROVERSION TEST! \n ")


def check_data():

    # Check input for valid user's name and e-mail. If yes call start_test function.

    while True:
        name = input("\nPlease enter your name:\n")
        name_valid = validate_name(name)        
        
        if name_valid:
            print(Fore.GREEN + Style.BRIGHT + f"\nHello, {name}!")            
            while True:
                email_str = input("\nPlease enter your email: \n")                
                if validate_email(email_str):
                    #insert_user_data(name, email_str) 
                    while True:
                        clear()                        
                        start_test(name, email_str)                        
                    break            
        else:
            print(Fore.RED + Style.BRIGHT + " ❌ Invalid data, please try again.\n")        
    
            
       
def validate_name(name_val):
    """     
    Splits a string (name) into a list and then join the list back into one string without spaces.
    Check if all the characters are alphabet letters.         
    """    
    
    name_check = "".join(name_val.split())     
    if name_check.isalpha() and len(name_check) > 1 :         
        return True  
    else:        
        print(Fore.RED + Style.BRIGHT + f" ❌ Invalid name {name_val}... Please enter correct name\n")        
        print("\n")        
        return False  
    

def validate_email(email_val):
    """ 
    Check if email address is valid or not.       
    """
    x = re.fullmatch(regex, email_val)
    if x:
        return True    
        
    else:        
        print(Fore.RED + Style.BRIGHT + f" ❌ Invalid e-mail {email_val}... Please enter correct e-mail\n")       
        return False   
      
 

def start_test(name_tested, email_tested):
    """
    Starting test, loading lists of questions 
    """    
    user_exists = check_data_workbook(name_tested, email_tested)  

    while True: 
         
        result = finish_test(user_exists)

        if result:   
            print(" - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            print(Fore.GREEN + f"Welcome, {name_tested} 🙂 Let's start. 🚀\nAre you oriented more towards \nthe outer world or the inner world? 🤔\n ")    
            print(Fore.GREEN + f"This easy test can give you a clear answer and help you understand \nyour personality.🧑\n ")
            print(Fore.GREEN + Style.BRIGHT + f"Please enter Y for 'YES' answer or N for 'NO' answer. Enter Q to Quit")
            print(" - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")    

            list_t_normal = load_from_workbook("Test1")
            list_t_intra = load_from_workbook("Test2")
            list_t_extra = load_from_workbook("Test3")
            
            final_score = check_answers(list_t_normal, list_t_intra, list_t_extra)

            check_results(final_score)

            insert_user_data(name_tested, email_tested, final_score)
            user_exists = True      
                
        else:
            print(Fore.YELLOW + Style.BRIGHT + THANK_YOU)
            exit()


def insert_user_data(name_in, email_in, result_in):
    # open worksheet
    try:
        wb2 = load_workbook(EXCEL_SHEET_NAME)                     
    except FileNotFoundError as fnf_error:
        print(Fore.RED  + fnf_error)
    else:
        ws = wb2["Users"] 

    # find if user exists and overwrite test result
    row = ws.max_row + 1 
    user_found = 0    
    for i in range(1,row):
        s = str(ws.cell(i,1).value)
        e = str(ws.cell(i,2).value)
        if s.lower() == name_in.lower() and e == email_in:
            ws.cell(i,3).value = result_in
            user_found = row
        # insert data to the find first empty row
    if user_found != row:
            ws.cell(row=row, column=1).value = name_in
            ws.cell(row=row, column=2).value = email_in
            ws.cell(row=row, column=3).value = result_in                  
    wb2.save(EXCEL_SHEET_NAME) 


def list_questions(worksheet):
    # Get column of the questions from worksheet to the list
    questions = []    
    for column in worksheet.iter_cols():          
        column_name = column[0].value
        if column_name == "Questions":                     
            for cell in column:
               questions.append(cell.value)
            questions.pop(0)
            return questions 

def list_answers(worksheet):
    # Get column of the answer key from worksheet to the list
    answers = [] 
    for column in worksheet.iter_cols():          
        column_name = column[0].value       
        if column_name == "Answers":             
            for cell in column:
               answers.append(cell.value)
            answers.pop(0)
            return answers       

def get_next_question(inner_score, list_test_normal, list_test_intra, list_test_extra):
    """
    Сhoose a category of questions depending on the score.

    """     
    if inner_score > -3 and inner_score < 3:
        for i in range(len(list_test_normal)):
            if list_test_normal[i].question_used == 0:
                #print(inner_score)                               
                return list_test_normal[i]
    elif inner_score <= -3:
        for i in range(len(list_test_intra)):
            if list_test_intra[i].question_used == 0:                                               
                return list_test_intra[i]
    elif inner_score >= 3:
        for i in range(len(list_test_extra)):
            if list_test_extra[i].question_used == 0:                                              
                return list_test_extra[i]
    return None


def check_answers(list_test_normal, list_test_intra, list_test_extra): 
    """
    Run a while loop to check user's answers, if 'Yes' or 'No', continue test, if 'Q' - quit.
    The loop will repeatedly print questions, until the end of questions list.
    Check invalid input (any character except 'Y', 'N' or 'Q') and return the error.
    """   
    score = 0  
   
    while True:         
            test_item = get_next_question(score, list_test_normal, list_test_intra, list_test_extra)            

            if test_item == None:                
                return score
            key_answer = test_item.answers 

            print(Fore.YELLOW + f" {test_item.questions}  Enter  Y / N , Q to Quit")             
            user_answer = input("🔻\n")                               
           
            if user_answer.lower() == "q":
                print(Fore.YELLOW + Style.BRIGHT + THANK_YOU)                
                exit() 
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
                print(Fore.RED + f"❌ Invalid data... Please enter  Y / N or Q to Quit \n")          
    
def check_results(score):     
    
    #Check results depending on score and print them.
    
    clear()

    print(" - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    if score >= -3 and score <= 3:
        
        print(Fore.GREEN + Style.BRIGHT + "\nCongratulations! You finished the test.\n\nYou are mostly AMBIVERT, \nexhibit qualities of both introversion and extroversion,\nyou can flip into either depending on their mood, context and goals.") 
        
    elif score < -3:
        print(Fore.GREEN + Style.BRIGHT + "\nCongratulations! You finished the test.\n\nYou are mostly INTROVERT, \nyou enjoy spending time alone and you feel more comfortable \nfocusing on your inner thoughts and ideas. ") 
        
    elif score > 3:
        print(Fore.GREEN + Style.BRIGHT + "\nCongratulations! You finished the test.\n\nYou are mostly EXTROVERT, \nyou enjoy being around other people and you gain energy from them.")
    print(" - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

def finish_test(user_is): 

    if not user_is:        
        return True
    else:
        print(Fore.YELLOW + "\nWould you like to try the test again?")

        while True:
            repeat_test = input("Enter Y or N\n")

            if repeat_test.lower() == "y":
                clear()
                return True            
            elif repeat_test.lower() == "n":
                clear()
                return False  
            else:
                print(Fore.RED + f" ❌ Invalid data... Please enter Y or N \n")           
        
  
def load_from_workbook(test_sheet):
    # open worksheet
    try:
        wb2 = load_workbook(EXCEL_SHEET_NAME)                     
    except FileNotFoundError as fnf_error:
        print(Fore.WHITE + Back.RED + fnf_error)
    else:
        ws = wb2[test_sheet]
    
    # populate list of answer keys
    answers = list_answers(ws)

    # populate list of questions
    questions = list_questions(ws)    

    # populate list with object which contains questions and answer keys 
    list = [] 
    for a, n in zip(questions, answers):               
        list.append(QuestionsAnswers(a, n, 0)) 
    
    # return populated list 
    return list                            

check_data() 

 




