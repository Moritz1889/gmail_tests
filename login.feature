Feature: Login to gmail.com
As a registered user
I want to log in into my account

Scenario: Succesfully log in to my account
Given The user already has an account at the gmail.com
Given The user is on login page
When The user press on the "Email or phone" input field
Then The user should be able to enter his email into that input field
When The user fill the "Email or phone" input field with "b.babirecki@gmail.com"
And Press "Next" button
Then The user should be moved to the next form
When The user press on the "Enter your password" input field
Then The user should be able to enter his password into that input field
When The user fill the "Enter your password" input field with "goodPassord1"
And Press "Next" button
Then The user should be moved to his mail box and has an oportuninty to sent email to other peple


Scenario: The user could not proceed after entering his email
Given The user already has an account at the gmail.com
Given The user is on login page
When The user press on the "Email or phone" input field
Then The user should be able to enter his email into that input field
When The user fill the "Email or phone" input field with <mail>
And Press "Next" button
Then The error message "Couldn't find your Google Account" should be displayed

Examples:
| mail                      |
| b.babirecki@gmail.comm    |
| b.babirecki@gmai.com      |
| babirecki@gmail.com       |


Scenario: The user could not login after entering his password
Given The user already has an account at the gmail.com
Given The user is on login page
When The user press on the "Email or phone" input field
Then The user should be able to enter his email into that input field
When The user fill the "Email or phone" input field with "b.babirecki@gmail.com"
And Press "Next" button
Then The user should be moved to the next form
When The user press on the "Enter your password" input field
Then The user should be able to enter his password into that input field
When The user fill the "Enter your password" input field with <password>
And Press "Next" button
Then The error message "Wrong password. Try again or click Forgot password to reset it." should be displayed

Examples:
| password          |
| wrongPassword1    |
| wrongPassword2    |
| toolongPassword123|

Scenario: The user is able to change his password after forgetting it
Given The user already has an account at the gmail.com
Given The user is on login page
When The user press on the "Email or phone" input field
Then The user should be able to enter his email into that input field
When The user fill the "Email or phone" input field with "b.babirecki@gmail.com"
And Press "Next" button
Then The user should be moved to the next form
When The user press the "Forgot password?" button
Then An account recovery form should be displayed
When The user press on the "Enter last password" input field
Then The user should be able to enter his password into that input field
When The user fill the "Enter last password" input field with "goodPassword1"
And Press "Next" button
Then The user should be moved to the next form with "New password" and "Confirm new password" input fields
When the user fill the "New password" input field with "goodPassword2" 
When the user fill the "Confirm new password" input field with "goodPassword2" 
And press "Change password" button
Then the password should be changed to the "goodPassword2"
