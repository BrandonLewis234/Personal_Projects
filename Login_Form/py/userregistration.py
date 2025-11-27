###############################################################
#
#
#                 userregistration.py
#
#         Author: Brandon Lewis
#           Date: 11/26/2025
#        Updated: 11/26/2025
#
#        Summary: Class for verifying and completing user
#                 registration and login information.
#
#
#
################################################################

import json
import bcrypt

from email_validator import validate_email, EmailNotValidError, caching_resolver

class UserRegistration():

    def confirmation_button_trigger(parent, type='login'):
        missing_fields = UserRegistration.__show_missing_fields(parent)

        if missing_fields:
            return

        user_database = UserRegistration.__load_users_from_file()
        username      = parent.lineUser.text()

        if type == 'signup':
            signup_failed  = False

            email          = parent.lineEmail.text()
            created_pass   = parent.linePassCreate.text()
            confirmed_pass = parent.linePassConf.text()
            
            try:    
                validate_email(email, strict=True, dns_resolver=caching_resolver(cache=None, timeout=10))
            except EmailNotValidError as e: 
                UserRegistration.__show_error(parent, error_message=f"Email is not vaild. Please input a valid email:\n{str(e)}")
                signup_failed = True

            if created_pass != confirmed_pass:
                UserRegistration.__show_error(parent, error_message="Password do not match.", append=True)
                signup_failed = True

            if signup_failed: return

            hashed_password = UserRegistration.__hash_password(confirmed_pass)
            UserRegistration.__save_user_to_file(username, hashed_password, email)
            print("signup success")

            UserRegistration.__clear_errors(parent)

        elif type == 'login':
            password = parent.linePass.text()
            username = UserRegistration.__check_if_user_in_database(username, user_database)

            if username == None: print("login fail"); return

            stored_hash = user_database.get(username, {}).get('password')
            if stored_hash and UserRegistration.__check_password_against_hash(password, stored_hash):
                print("login success")
            else:
                print("login fail")

    
    def __show_missing_fields(parent):
        missing_fields = []
        for key, value in parent.required_fields.items():
            if key.text() == "":
                missing_fields.append(value)
            
            str_to_show = "Missing fields: "
            for i, field in enumerate(missing_fields):
                if i == len(missing_fields) - 1:
                    str_to_show += f"{field}"
                    continue
                str_to_show += f"{field}, "  

        if str_to_show == "Missing fields: ":
            UserRegistration.__clear_errors(parent)
            return False
        else:
            UserRegistration.__show_error(parent, str_to_show)
            return True
        
    def __show_error(parent, error_message, append=False):
        parent.lblErrors.setVisible(True)
        
        txt_to_show = error_message

        if append:
            previous_text = parent.lblErrors.text()
            txt_to_show += f"\n{previous_text}"

        parent.lblErrors.setText(txt_to_show)

    def __clear_errors(parent):
        parent.lblErrors.setVisible(False)
        parent.lblErrors.setText("")
        

    def __check_if_user_in_database(user_input, user_database):
        if user_input in user_database:
            return user_input
        
        try:
            for user in user_database.keys():
                email = user_database.get(user).get('email')
                if email == user_input:
                    return user
        except:
            pass

        return None


    def __save_user_to_file(username, hashed_password, email, filename='users.json'):
        try:
            with open(filename, 'r') as f:
                user_database = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            user_database = {}

        user_database[username] = {
            'password': hashed_password,
            'email':    email
        }

        with open(filename, 'w') as f:
            json.dump(user_database, f)

    def __load_users_from_file(filename='users.json'):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}


    #src: https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/
    def __hash_password(password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed.decode()

    def __check_password_against_hash(password, hashed):
        return bcrypt.checkpw(password.encode(), hashed.encode())