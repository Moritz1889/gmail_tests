Feature: Send email
As a logged user
I want to send email
So I can communicate with others

Scenario: Succesfully sending an email
Given The user already has an account at the gmail.com
Given The user is already logged in
Given The user is on the main gmail page
When The user press "Compose" that is located in the upper left corner
Then A new window should be displayed
When The user fill the "To" input field with "b.babirecki@gmail.com"
When The user fill the "Subject" input field with "Sample title"
Then the basic requirements to send an email are fullfilled
When the user choose from the bottom list the "Attach files" option
Then A file browser should be opened
When the user choose a file named "sample_file.pdf" and press "Open"
Then that filed should be uploaded to the server and attached to the mail
When the user press "Send" located on the bottom left corner
Then the mail should be send