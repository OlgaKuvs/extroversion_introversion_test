from openpyxl import load_workbook
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored, cprint
import re

just_fix_windows_console()
# init(autoreset=True)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Class for the questions and answer key instances and used question flag

class QuestionsAnswers:
    def __init__(self, questions, answers, question_used):
        self.questions = questions
        self.answers = answers
        self.question_used = question_used



# print(Fore.RED + Back.YELLOW  + "Welcome to Extroversion Introversion Test")
cprint(" Welcome to Extroversion Introversion Test! ", "white", "on_blue")

def check_data():

    # Check input for valid user's name and e-mail. If yes call start_test function.

    while True:
        name = input("\n Please enter your name:\n")
        name_valid = validate_name(name)        
        
        if name_valid:
            cprint(f"\n Hello, {name}!", "white", "on_blue")            
            while True:
                email_str = input("\n Please enter your email: \n")                
                if validate_email(email_str):
                    insert_user_data(name, email_str) 
                    start_test(name) 
                    break
            break            
        else:
            cprint(f" Invalid data, please try again.\n", "white", "on_red")          
    
            
       
def validate_name(name_val):
    """     
    Splits a string (name) into a list and then join the list back into one string without spaces.
    Check if all the characters are alphabet letters.         
    """    
    
    name_check = "".join(name_val.split())     
    if name_check.isalpha() and len(name_check) > 1 :         
        return True  
    else:        
        cprint(f" Invalid name {name_val}... Please enter correct name", "white", "on_red")        
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
        cprint(f" Invalid e-mail {email_val}... Please enter correct e-mail", "white", "on_red")       
        return False 
    
def insert_user_data(name_in, email_in):
    # open worksheet
    try:
        wb2 = load_workbook('test_e_i.xlsx')                     
    except FileNotFoundError as fnf_error:
        print(Fore.WHITE + Back.RED + fnf_error)
    else:
        ws = wb2["Users"]     

    for column in ws.iter_cols(min_row=2):         
        # print(column)        
        #column_name = column[0].value 
        #print(column_name)      
        # if column_name == "Name":             
        for c in column:               
            mycell_n = ws.cell(row=2, column=1)
            mycell_n.value= name_in
            mycell_e = ws.cell(row=2, column=2)
            mycell_e.value= email_in
            # print(email_in)            
            wb2.save('test_e_i.xlsx')       
        
    
           




def start_test(name_tested):
    """
    Starting test, loading lists of questions 
    """
    print(Fore.WHITE + Back.BLUE + f"\n Thank you, {name_tested}. Let's start.\n Are you oriented more towards \n the outer world or the inner world?\n ")    
    print(f" This easy test can give you a clear answer and help you understand \n your personality.\n ")
    print(f" Please enter Y for 'Yes' answer and N for 'No' answer. ")
    print(Style.RESET_ALL)

    list_t_normal = load_from_workbook("Test1")
    list_t_intra = load_from_workbook("Test2")
    list_t_extra = load_from_workbook("Test3")
       
    check_answers(list_t_normal, list_t_intra, list_t_extra)

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
                print(inner_score)                               
                return list_test_normal[i]
    elif inner_score <= -3:
        for i in range(len(list_test_intra)):
            if list_test_intra[i].question_used == 0:
                print(inner_score)                                
                return list_test_intra[i]
    elif inner_score >= 3:
        for i in range(len(list_test_extra)):
            if list_test_extra[i].question_used == 0:
                print(inner_score)                                
                return list_test_extra[i]
    check_results(inner_score)
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
                cprint(f" Invalid data... Please enter  Y/N or Q to Quit ", "white", "on_red")          
    
def check_results(score):
    
    #Check results depending on score and print them.
    
    if score >= -3 and score <= 3:
        print(Fore.WHITE + Back.BLUE + " Congratulations! You finished the test. You are mostly AMBIVERT, \n exhibit qualities of both introversion and extroversion,\n you can flip into either depending on their mood, context, and goals.") 
        print(Style.RESET_ALL) 
    elif score < -3:
        print(Fore.WHITE + Back.BLUE + " Congratulations! You finished the test. You are mostly INTROVERT, \n you enjoy spending time alone and you feel more comfortable \n focusing on your inner thoughts and ideas. ") 
        print(Style.RESET_ALL)
    elif score > 3:
        print(Fore.WHITE + Back.BLUE + " Congratulations! You finished the test. You are mostly EXTROVERT, \n you enjoy being around other people and you gain energy from them.") 
        print(Style.RESET_ALL)
        
  
def load_from_workbook(test_sheet):
    # open worksheet
    try:
        wb2 = load_workbook('test_e_i.xlsx')                     
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

 




