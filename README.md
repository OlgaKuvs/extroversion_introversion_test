# Extroversion Introversion Test 

### [Live site](https://extro-intro-test.herokuapp.com/)

![screenshot](documentation/screenshot.png)

## Contents:

- <a href="#introduction">Introduction</a>
- <a href="#flow">Flowchart</a>
- <a href="#experience">User Experience Design</a>
    - <a href="#first_time_user">First Time User</a>
    - <a href="#returning_user">Returning User</a>
- <a href="#features">Features</a>
    - <a href="#message">Introductory Message</a>
    - <a href="#validation">Data Validation</a>
    - <a href="#passing">Passing the Test</a>
    - <a href="#result">Test Result</a>
- <a href="#model">Data Model</a>
    - <a href="#database">Writing to Database</a>
    - <a href="#class">Questions_Answers Class</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#testing">Testing</a>
    - <a href="#validation">Validation</a>
    - <a href="#manual_testing">Manual Testing</a>
    - <a href="#bugs">Bugs</a>
- <a href="#deployment">Deployment</a>


## <div id="introduction">Introduction</div>

The Extroversion-Introversion test is a psychological assessment tool designed to measure an individual's personality traits related to extroversion and introversion. Extroversion and introversion are fundamental dimensions of personality proposed by Swiss psychologist Carl Jung.

Extroversion refers to a person's tendency to seek external stimulation and derive energy from social interactions. Extroverts are often outgoing, assertive, and enjoy being around people. They tend to be talkative, energetic, and may exhibit a preference for engaging in activities involving others.

Introversion, on the other hand, reflects a preference for internal reflection and solitude. Introverts tend to be more reserved, thoughtful, and prefer quiet environments. They may feel drained by excessive social interactions and require alone time to recharge their energy.

Ambiversion refers to a psychological concept that describes individuals who exhibit a balance between extroversion and introversion. An ambivert is someone who does not strongly lean towards either extreme of the extroversion-introversion spectrum but rather falls somewhere in the middle.

Unlike strict extroverts or introverts who lean heavily towards one end of the spectrum, ambiverts can adapt their behavior and energy levels to different social settings. They may enjoy and feel energized by social interactions, but also value and seek out periods of solitude and reflection.

This very simple test will allow the user to check whether he is an extrovert, an introvert or, like most people, an ambivert.

## <div id="flow">Flowchart</div>

The below flowchart shows the order in which actions are taken and how the program works.

![View flowchart](documentation/flowchart.png)

## <div id="experience">User Experience Design</div>
### <div id="first_time_user">First Time User</div>

- As a person who like likes to take tests, I would like some test with psychological questions but not too  long and difficult.
- As someone unfamiliar with the psychology, I would like something new and interesting  to pick up.
- As someone who is well-versed in psychology, I would like to compare this test with other tests I know to form my opinion.

### <div id="returning_user">Returning User</div>

- As a returning user, I would like to see my most recent result.
- I would like to be able to take the test again and compare the results. 
- I wish the questions were different every time I take the test.


## <div id="features">Features</div>
### <div id="message">Introductory Message</div>
When the user runs the system, they will be greeted with a logo and a welcome message.

### <div id="validation">Data Validation</div>
![](documentation/screenshot_test2.png)
The user is asked to enter their name and email. The data will only be classified as valid if the name contains at least 2 letters and the email address is in the correct format.
The data is validated, and it is checked whether the user exists in the database.
For the new user, a description of the test is displayed. For the returning user, the program shows the most recent result and asks if they want to take the test again.
![](documentation/screenshot_test1.png) 

### <div id="passing">Passing the Test</div>
![](documentation/screenshot_test3.png)
There are 3 groups of questions in the database: general questions, specific questions to determine introversion, and specific questions to determine extroversion. 
The test begins with a general group of questions.
For each answer in the direction of extroversion the user receives 1 point, in the direction of introversion the user receives -1 point. 
If user reaches -4 or 4 points, the program switches to specific questions from the extroversion or introversion section, respectively. If the number of points goes back to the zone between -3 and 3, then the user returns to the list of basic questions. The test continues until the end of the list of questions.

### <div id="result">Test Result</div>
The final result of the test is determined by the score: if the score is less than -3, then the result is an introverted user. If the score is greater than 3, then the result is the extrovert user. If the score is between -3 and 3, the user is ambivert. 

## <div id="model">Data Model</div>

### <div id="database">Writing to Database</div> 
After the end of the test, the username, email and test result are entered into the database. Excel sheets were used to store the test questions, user's data and test results. The workbook consists of 4 worksheets: 'Test1', 'Test2', 'Test3' and 'Users'.

Each test sheet consists of questions and keys to answers.
![](documentation/excel_sheet_sample1.png)

'Users' sheet consists of user's name, email and test result.
![](documentation/excel_sheet_sample2.png)

### <div id="class">Questions_Answers Class</div>
- A Questions_Answers Class was created to contain the data of the test questions and the flag if the question has already been used. 
- A Questions_Answers has the following attributes:
    - questions: list of questions
    - answers: list of answer keys
    - question_used: a flag that indicates whether the question has already been used in the test

## <div id="technologies">Technologies Used</div>
- The application was developed with Python
    - Python Packages:
        - [Openpyxl](https://pypi.org/project/openpyxl/) as a Python library to read/write Excel files.
        - [Colorama](https://pypi.org/project/colorama/) to print colored terminal text 
        - Platform module and OS Module to check the system/OS name and interact with the underlying operating system
- [Heroku](https://www.heroku.com/platform) was used for deployment
- [Flowchart Maker and Online Diagram Software](https://app.diagrams.net/) was used to generate the flowchart
- [VS Code](https://code.visualstudio.com/) was used for development

## <div id="testing">Testing</div>
### <div id="manual_testing">Manual Testing</div>
|  Testing |  Result |   
|---|---|
| Testing all instances where user input is required. Entering valid and invalid data. | Invalid input is handled correctly. An error message is displayed. The user is prompted to try again. |
| Application navigation. Checking that the correct actions are being taken according to user input. | Navigation works as expected. Invalid inputs are handled.
| Check switching between lists of test questions. | Switching occurs correctly when the user reaches -4 or 4 points. If the score goes back to zone from -3 to 3, the program goes back to questions from the base list.
| Correct scoring. | Counting occurs in accordance with the key to the answers (+1 for a question towards extraversion, -1 for a question towards introversion). The final result is calculated correctly.
| Calculation and display of the test result. | The test result (extroversion, introversion or ambiversion) is calculated and displayed as expected. 
| Write user data and test result to the database table. | The user's name, e-mail and the final number of points are recorded correctly, in the first empty row and in the corresponding columns of the table. |  
| Reading data of returning user. | Right checking if the name and email address of the returning user is in the database. The most recent test result is displayed as expected.


### <div id="validation">Validation</div>


### <div id="bugs">Bugs</div>


|  Issue |  Solution |   
|---|---|
| User data was written to the data table incorrectly. | Edit the <span style="background-color:lightgray">insert_user_data</span> function to find the last empty row and insert data into it. Add the <span style="background-color:lightgray">user_found</span> flag to check if the user exists and overwrite the test result. If not, insert the new user's data into the table.  |
| Bug in the function that selects the question category. | Add <span style="background-color:lightgray">question_used</span> flag to check if the question was already used and set it's default value to 0. Change the flag value to 1 for used questions.  

## <div id="deployment">Deployment</div>
Heroku Deployment Steps:
1. Make sure all dependencies are listed in your requirements.txt file. To do this, type in your python terminal pip3 freeze > requirements.txt.
2. Now all your requirements will be added to the requirements file.
3. Go to the Heroku website and navigate to the sign up button in the top right-hand corner.
4. Next, click "New" in the top right-hand corner and select "Create new app".
5. Then choose an app name. It must be unique.
6. Then select "Europe" as your region.
7. Click "Create app".
8. Navigate to the "Settings" tab.
9. Click on "Config Vars".
10. For the first "KEY", input "CREDS".
11. For "VALUE", input your entire creds.json file including the curly braces. Click "Add".
12. For the second "KEY", input "PORT".
13. For the second "PORT", input "8000". Click "Add".
14. Scroll down to Buildpacks and select "Add buildpack".
15. Select Python first and then add another buildpack and select Node JS. Python must be listed above Node JS for this to work.
16. Scroll back to the top and select the "Deploy" tab.
17. From Deployment method, select "GitHub".
18. Now search for your GitHub repository name and select the correct repository.
19. Now scroll down to Automatic deploys and choose the "main" branch. Therefore, any changes that have been pushed through to GitHub will update the Heroku app.
20. Then scroll down to Manual deploy and click "Deploy Branch".
21. When complete, click on "View", which will open a new tab and display your program.





    











 















 