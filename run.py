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
    """
    Starting test, loading lists of questions 
    """
    print(Fore.WHITE + Back.BLUE + f"\nThank you, {name_tested}. Let's start. Are you oriented more towards the outer world or the inner world?\n ")    
    print(f"This easy test can give you a clear answer and help you understand your personality.\n ")
    print(f"Please enter Y for 'Yes' answer and N for 'No' answer. ")
    print(Style.RESET_ALL)

    List_test_normal = load_from_workbook("Test1")
    List_test_intra = load_from_workbook("Test2")
    List_test_extra = load_from_workbook("Test3")

    """ 
    normalTestSheetName = "Test1"
    wsheet1 = load_from_workbook(normalTestSheetName)
    answers = list_answers(wsheet1)
    questions = list_questions(wsheet1)    
       
    for a, n in zip(questions, answers):               
        list.append(QuestionsAnswers(a, n, 0)) 
    """ """
    for a in range(len(list)):   
        print(list[a].questions) 
        print(list[a].answers) 
        print(list[a].question_used)
    """    
    check_answers(List_test_normal, List_test_intra, List_test_extra)

def list_questions(worksheet):
    # get column of questions from worksheet to the list
    questions = []    
    for column in worksheet.iter_cols():          
        column_name = column[0].value
        if column_name == "Questions":                     
            for cell in column:
               questions.append(cell.value)
            questions.pop(0)
            return questions 

def list_answers(worksheet):
    # get column of answers score from worksheet to the list
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
                cprint(f"Invalid data... Please enter  Y/N or Q to Quit ", "white", "on_red")          
    
def check_results(score):
    
    #Check results depending on score and print them.
    
    if score >= -3 and score <= 3:
        print(Fore.RED + Back.WHITE + "Congratulations! You finished the test. You are mostly AMBIVERT, ") 
        print(Fore.RED + Back.WHITE + "exhibit qualities of both introversion and extroversion,") 
        print(Fore.RED + Back.WHITE + "you can flip into either depending on their mood, context, and goals.")
        print(Style.RESET_ALL) 
    elif score < -3:
        print(Fore.RED + Back.WHITE + "Congratulations! You finished the test. You are mostly INTROVERT,") 
        print(Fore.RED + Back.WHITE + "you enjoy spending time alone and you feel more comfortable ") 
        print(Fore.RED + Back.WHITE + "focusing on your inner thoughts and ideas.") 
        print(Style.RESET_ALL)
    elif score > 3:
        print(Fore.RED + Back.WHITE + "Congratulations! You finished the test. You are mostly EXTROVERT,") 
        print(Fore.RED + Back.WHITE + "you enjoy being around other people and you gain energy from them.") 
        print(Style.RESET_ALL)
    
              
def load_from_workbook(test_sheet):
    # open worksheet
    try:
        wb2 = load_workbook('C:/My websites/Project_3_Test/test_e_i.xlsx')                     
    except FileNotFoundError as fnf_error:
        print(Fore.WHITE + Back.RED + fnf_error)
    else:
        ws = wb2[test_sheet]
    
    # populate list of answer scores
    answers = list_answers(ws)

    # populate list of questions
    questions = list_questions(ws)    

    # populate list with object which contains questions and answer scores  
    list = [] 
    for a, n in zip(questions, answers):               
        list.append(QuestionsAnswers(a, n, 0)) 
    
    # return populated list 
    return list               


check_data() 

 




