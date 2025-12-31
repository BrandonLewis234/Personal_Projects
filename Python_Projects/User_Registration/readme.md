## Note
Functionality is slowly being added to the signup and login form.

### Currently, to signup, the fields are run through various forms of verification. 
The email is verified to be in correct email format and the domain provided is able to receive email. <br />
The username is verified to be longer than 3 characters in length. <br />
The created password is verified to be the same as the confirmed password. <br />

Further verification is done to check the email and username against the existing database for if they are already in use. <br />
If all is entered correctly, the user will be registered into a users.json file stored locally in the directory. <br />

### To login, users can use the credentials they previously entered.
If entered correctly, login will be successful (Currently just a prompt denoting as such).

## If running for yourself
ensure that the requirements in requirements.txt are met, otherwise the window may not appear as it should, and deprecation warnings may appear. 

This configuration avoids any warnings and syncs the theme with your windows theme.

