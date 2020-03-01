Feature: Register an account at gmail.com
As a new user
I want to register a new account

Scenario: Succesfully registering an account
Given The user is on login page
When The user press "Create account" button
Then A list should be displayed
When The user choose from the list "For myself"
Then A new form should be displayed called "Create your Google Account"
When The user fill the "First name" input field with "Bart"
When The user fill the "Last name" input field with "Moritzson"
Then A suggested email box name should be displayed in the "Username" input field
When The user fill the "Password" input field with "GoodPassword1"
When The user fill the "Confirm" input field with "GoodPAssword1" 
And Press "Next" input field
Then Next form called "Welcom to Google" should be displayed
When The user fill the "Day" input field with "10"
When The user press on the "Month" list
And Choose from the list "December" 
When The user fill the "Year" input field with "1992"
When The user press on the "Gender" list 
And Choose from the list "Male"
And Press the "Next" button
Then the new form called "Privacy and Terms" should be displayed
When the user scroll down till the end of the document
And Press on the button next to the "I agree to the Google Terms of Service"
And Press on the button next to the "I agree to the processing of my information [...]"
And Press "Create Account"
Then Popup called "Just to confirm..." should be displayed
When The user press "Confirm" button an account should be displayed 

Scenario: Creating an account, the password is incorrect
Given The user is on login page
When The user press "Create account" button
Then A list should be displayed
When The user choose from the list "For myself"
Then A new form should be displayed called "Create your Google Account"
When The user fill the "First name" input field with "Bart"
When The user fill the "Last name" input field with "Moritzson"
Then A suggested email box name should be displayed in the "Username" input field
When The user fill the "Password" input field with <passowrd1>
When The user fill the "Confirm" input field with <password2>
And Press "Next" input field
Then an <error message> should be displayed

Examples:
| password1 | password2 | error message                                                                 |
| NULL      | NULL      | Enter a password                                                              |
| 1234567   | NULL      | Use 8 character or more for your passowrd                                     |
| 12345678  | NULL      | Confirm your passowrd                                                         |
| 12345678  | 12345678  | Please choose a stronger password. Try mix of letters, numbers and symbols.   |
| NULL      | 12345678  | Enter a passowrd                                                              |
| aaaaaaaa  | aaaaaaaa  | Please choose a stronger password. Try mix of letters, numbers and symbols.   |
| GoodPass1 | BadPass2  | Those passowrds didn't match. Try again                                       |

Scenario: Creating an account, the First and Last Name is incorrect
Given The user is on login page
When The user press "Create account" button
Then A list should be displayed
When The user choose from the list "For myself"
Then A new form should be displayed called "Create your Google Account"
When The user fill the "First name" input field with <first name>
When The user fill the "Last name" input field with <last name>
Then A suggested email box name should be displayed in the "Username" input field
When The user fill the "Password" input field with "GoodPassowrd1"
When The user fill the "Confirm" input field with "GoodPassword1"
And Press "Next" input field
Then an <error message> should be displayed

Examples:
| first name    | last name | error message                                         |
| NULL          | NULL      | Enter first name & Enter last name                    |
| Bart          | NULL      | Enter last name                                       |
| NULL          | Moritzson | Enter first name                                      |
| !             | Moritzson | Are you sure that you've entered your name correctly? |
