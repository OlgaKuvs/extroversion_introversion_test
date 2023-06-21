import os
import platform
import re
import gspread
from google.oauth2.service_account import Credentials
from colorama import just_fix_windows_console
from colorama import Fore, Style
from colorama import init
import time
from sys import stdout


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

try:
    SHEET_NAME = GSPREAD_CLIENT.open("test_e_i")
except gspread.exceptions.SpreadsheetNotFound as e:
    print(Fore.RED + "Trying to open non-existent or inaccessible spreadsheet document.")
    exit()


BANNER = """

         ######   #####  #     #  #####  #     # #######
         #     # #     #  #   #  #     # #     # #     #
         #     # #         # #   #       #     # #     #
         ######   #####     #    #       ####### #     #
         #             #    #    #       #     # #     #
         #       #     #    #    #     # #     # #     #
         #        #####     #     #####  #     # #######

         ####### #######  #####  #######
            #    #       #     #    #
            #    #       #          #
            #    #####    #####     #
            #    #             #    #
            #    #       #     #    #
            #    #######  #####     #
"""


THANK_YOU = """

 ####### #     #    #    #     # #    #    #     # ####### #     #   ###
    #    #     #   # #   ##    # #   #      #   #  #     # #     #   ###
    #    #     #  #   #  # #   # #  #        # #   #     # #     #   ###
    #    ####### #     # #  #  # ###          #    #     # #     #    #
    #    #     # ####### #   # # #  #         #    #     # #     #
    #    #     # #     # #    ## #   #        #    #     # #     #   ###
    #    #     # #     # #     # #    #       #    #######  #####    ###

"""

just_fix_windows_console()
init(autoreset=True)
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
cursor_shape = '\x1b[3 q'
print(cursor_shape, end='')


def clear_terminal():
    # Check os and clear the terminal
    plt = platform.system()

    if plt == "Windows":
        def clear():
            return os.system('cls')
    elif plt == "Linux":
        def clear():
            return os.system('clear')
    clear()


class Questions_Answers:
    """
    Class for the questions and answer key instances and used question flag
    """
    def __init__(self):
        self.questions = ""
        self.answers = ""
        self.question_used = 0


class User:
    """
    Class for each user to store name, email and flag for returning user
    """
    def __init__(self):
        self.name = ""
        self.email = ""
        self.exists = False


print(Fore.YELLOW + Style.BRIGHT + BANNER +
      " WELCOME TO EXTROVERSION INTROVERSION TEST! \n ")


def check_data_workbook():
    """
    Check if user's data is already in the worksheet.
    If yes, print user's last test result.
    Ask the user if they want to try the test again
    """
    try:
        ws = SHEET_NAME.worksheet("Users").get_values()
    except gspread.exceptions.WorksheetNotFound as e:
        print(Fore.RED + "Trying to open non-existent sheet. Verify that the sheet name exists.")
        exit()

    for row in ws:
        name = row[0]
        email = row[1]
        """
        Have to define new variables because of error E501:
        line too long (if statement)
        """
        c_name = CURRENT_USER.name
        c_email = CURRENT_USER.email

        if name.lower() == c_name.lower() and email == c_email:
            CURRENT_USER.exists = True
            result = int(row[2])
            if result > -3 and result < 3:
                print(f" Welcome again {CURRENT_USER.name}!" +
                      " Your most recent result was AMBIVERT")
            elif result <= -3:
                print(f" Welcome again {CURRENT_USER.name}!" +
                      " Your most recent result was INTROVERT")
            elif result >= 3:
                print(f" Welcome again {CURRENT_USER.name}!" +
                      " Your most recent result was EXTROVERT")
            return True


def check_data():

    """
    Check input for user's name and e-mail validation.
    If valid, call start_test function.
    """

    while True:
        name_str = input("\n Please enter your name:\n")
        name_valid = validate_name(name_str)

        if name_valid:
            print(Fore.GREEN + Style.BRIGHT +
                  f"\n Hello, {name_str}!\n")
            while True:
                email_str = input(" Please enter your email: \n")
                if validate_email(email_str):
                    while True:
                        clear_terminal()
                        start_test(name_str, email_str)
                else:
                    print(Fore.RED + Style.BRIGHT +
                          f" ❌ Invalid e-mail {email_str}..." +
                          " Please enter correct e-mail\n")
        else:
            print(Fore.RED + Style.BRIGHT +
                  f" ❌ Invalid name {name_str}... Please enter correct name\n")


def validate_name(name_val):
    """
    Splits a string (name) into a list and then join
    the list back into one string without spaces.
    Check if all the characters are alphabet letters.
    """

    name_check = "".join(name_val.split())
    if name_check.isalpha() and len(name_check) > 1:
        return True
    else:
        return False


def validate_email(email_val):
    """
    Check if email address is valid or not.
    """
    x = re.fullmatch(regex, email_val)
    if x:
        return True
    else:
        return False


def start_test(name_tested, email_tested):
    """
    Starting test, creating user instance from User class,
    printing welcome message and test description,
    loading lists of questions.
    """
    global CURRENT_USER
    CURRENT_USER = User()
    CURRENT_USER.name = name_tested
    CURRENT_USER.email = email_tested

    check_data_workbook()

    while True:

        go_test = test_again()

        if go_test:

            print(" - - - - - - - - -  - - - - - " +
                  "- - - - - - - - - - - - - - - - - - - - - - ")
            print(Fore.GREEN +
                  f" Welcome, {CURRENT_USER.name} 🙂 ! Let's start. 🚀 \n")
            In = " Are you oriented more towards the outer world"
            for x in In:
                print(Fore.GREEN + x, end='')
                stdout.flush()
                time.sleep(0.04)
            In = " or the inner world? 🤔\n"
            for x in In:
                print(Fore.GREEN + x, end='')
                stdout.flush()
                time.sleep(0.04)
            In = " This easy test can give you a clear answer"
            for x in In:
                print(Fore.GREEN + x, end='')
                stdout.flush()
                time.sleep(0.04)
            In = "\n and help you understand your personality.🧑\n"
            for x in In:
                print(Fore.GREEN + x, end='')
                stdout.flush()
                time.sleep(0.04)
            print("\n")

            print(Fore.GREEN + Style.BRIGHT + " Please enter Y for 'YES'" +
                  " answer or N for 'NO' answer. Enter Q to Quit")
            print(" - - - - - - - - -  - - - - - - - - -" +
                  " - - - - - - - - - - - - - - - - - - \n")
            print("Loading test questions... \n")

            list_t_normal = load_from_workbook("Test1")
            list_t_intra = load_from_workbook("Test2")
            list_t_extra = load_from_workbook("Test3")

            final_score = check_answers(list_t_normal,
                                        list_t_intra, list_t_extra)

            check_results(final_score)
            insert_user_data(final_score)
        else:
            restart()


def insert_user_data(result_in):

     # Open sheet from worksheet

    try:
        sheet1 = SHEET_NAME.worksheet("Users")
    except gspread.exceptions.WorksheetNotFound as e:
        print(Fore.RED + "Trying to open non-existent sheet. Verify that the sheet name exists.")
        exit()

    # Get data from 'Users' table

    ws = sheet1.get_values()

    # Find if user exists and overwrite test result

    len1 = len(ws)
    user_found = 0
    for i in range(1, len1):
        name = ws[i][0]
        email = ws[i][1]
        """
        Have to define new variables because of error E501:
        line too long (if statement)
        """
        c_name = CURRENT_USER.name
        c_email = CURRENT_USER.email

        if name.lower() == c_name.lower() and email == c_email:
            sheet1.update_cell(i+1, 3, result_in)
            user_found = len(ws)

    # If it is a new user insert data to the find first empty row

    if user_found != len(ws):
        sheet1.append_rows(values=[[c_name, c_email, result_in]])
        CURRENT_USER.exists = True


def get_next_question(inner_score, list_test_normal,
                      list_test_intra, list_test_extra):

    """
    Сhoose a category of questions depending on the score.
    """

    if inner_score > -3 and inner_score < 3:
        for i in range(len(list_test_normal)):
            if list_test_normal[i].question_used == 0:
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
    Run a while loop to check user's answers,
    if 'Yes' or 'No', continue test, if 'Q' - quit.
    The loop will repeatedly print questions,
    until the end of questions list.
    Check invalid input (any character except 'Y', 'N' or 'Q')
    and return the error.
    """
    score = 0

    while True:
        test_item = get_next_question(score, list_test_normal,
                                      list_test_intra, list_test_extra)

        if test_item is None:
            return score
        key_answer = int(test_item.answers)

        print(Fore.YELLOW +
              f" {test_item.questions}  Enter  Y / N , Q to Quit")
        user_answer = input("🔻\n")

        if user_answer.lower() == "q":
            restart()
        elif (user_answer.lower() == "y" and key_answer == 1):
            score += 1
            test_item.question_used = 1
        elif (user_answer.lower() == "y" and key_answer == 0):
            score -= 1
            test_item.question_used = 1
        elif (user_answer.lower() == "n" and key_answer == 1):
            score -= 1
            test_item.question_used = 1
        elif (user_answer.lower() == "n" and key_answer == 0):
            score += 1
            test_item.question_used = 1
        else:
            print(Fore.RED + "❌ Invalid data... " +
                  " Please enter  Y / N or Q to Quit \n")


def check_results(score):
    """
    Check results depending on score and print them.
    """

    clear_terminal()

    print(" - - - - - - - - -  - - - - - - - - " +
          "- - - - - - - - - - - - - - - - - - - ")
    print(Fore.GREEN + Style.BRIGHT +
              "\n Congratulations! You finished the test.\n\n")
    if score >= -3 and score <= 3:
        In = " You are mostly AMBIVERT \n exhibit "
        for x in In:
            print(Fore.GREEN + Style.BRIGHT + x, end='')
            stdout.flush()
            time.sleep(0.04)
        In = "qualities of both introversion and extroversion, you can "
        for x in In:
            print(Fore.GREEN + Style.BRIGHT + x, end='')
            stdout.flush()
            time.sleep(0.04)
        In = "flip into\n either depending on their mood, context and goals."
        for x in In:
            print(Fore.GREEN + Style.BRIGHT + x, end='')
            stdout.flush()
            time.sleep(0.04)
    elif score < -3:
        In = "\n You are mostly INTROVERT, \n you enjoy spending time"
        for x in In:
            print(Fore.GREEN + Style.BRIGHT + x, end='')
            stdout.flush()
            time.sleep(0.04)
        In = " alone and you feel more comfortable \n focusing "
        for x in In:
            print(Fore.GREEN + Style.BRIGHT + x, end='')
            stdout.flush()
            time.sleep(0.04)
        In = "on your inner thoughts and ideas."
        for x in In:
            print(Fore.GREEN + Style.BRIGHT + x, end='')
            stdout.flush()
            time.sleep(0.04)
    elif score > 3:
        In = " You are mostly EXTROVERT, \n you enjoy being around"
        for x in In:
            print(Fore.GREEN + Style.BRIGHT + x, end='')
            stdout.flush()
            time.sleep(0.04)
        In = " other people \n and you gain energy from them. \n"
        for x in In:
            print(Fore.GREEN + Style.BRIGHT + x, end='')
            stdout.flush()
            time.sleep(0.04)
    print("\n - - - - - - - - -  - - - - - - -" +
            "- - - - - - - - - - - - - - - - - - - - ")


def test_again():
    """
    Ask the user if they want to try the test again
    """
    if not CURRENT_USER.exists:
        return True
    else:
        print(Fore.YELLOW +
              "\n Would you like to try the test again?")

        while True:
            repeat_test = input(" Enter Y or N\n")

            if repeat_test.lower() == "y":
                clear_terminal()
                return True
            elif repeat_test.lower() == "n":
                clear_terminal()
                return False
            else:
                print(Fore.RED +
                      " ❌ Invalid data... Please enter Y or N \n")


def load_from_workbook(test_sheet):
    """
    Get test questions from the worksheet
    """
    try:
        ws = SHEET_NAME.worksheet(test_sheet).get_values()
    except gspread.exceptions.WorksheetNotFound as e:
        print(Fore.RED + "Trying to open non-existent sheet. Verify that the sheet name exists.")
        exit()

    list = []

    # populate list with object which contains questions, answer keys and flag

    for i in range(1, len(ws)):
        qa = Questions_Answers()
        qa.questions = ws[i][0]
        qa.answers = ws[i][1]
        qa.question_used = 0
        list.append(qa)

    return list


def restart():
    """
    When user exits the test, he can start the test again
    """
    clear_terminal()
    print(Fore.YELLOW + Style.BRIGHT + THANK_YOU)
    while True:
        print(Fore.YELLOW +
              "To start from the beginning, please enter S")
        user_answer = input("\n")
        if user_answer.lower() == "s":
            clear_terminal()
            start_test(CURRENT_USER.name, CURRENT_USER.email)
        else:
            print(Fore.RED +
                  " ❌ Invalid data... Please enter S to start from the beginning \n")


check_data()
