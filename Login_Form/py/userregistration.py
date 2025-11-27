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

from utilityfunctions import ErrorField, AllFields

class UserRegistration():

    def confirmation_button_trigger(parent, type):
        missing_fields = ErrorField.show_missing_fields(parent)

        if missing_fields:
            return

        user_database = UserRegistration.__load_users_from_file()
        username      = parent.lineUser.text()

        if type == 'signup':
            signup_failed        = False

            email                = parent.lineEmail.text()
            created_pass         = parent.linePassCreate.text()

            confirmed_pass_field = parent.linePassConf
            confirmed_pass       = confirmed_pass_field.text()


            try:    
                validated_email = validate_email(email, strict=True, dns_resolver=caching_resolver(cache=None, timeout=10))
            except EmailNotValidError as e: 
                ErrorField.show_error(parent, error_message=f"Email is not vaild. Please input a valid email:\n{str(e)}")
                signup_failed = True


            if created_pass != confirmed_pass and not confirmed_pass_field.isReadOnly():
                ErrorField.show_error(parent, error_message="Password do not match.", append=True)
                signup_failed = True
            

            existing_user = None; existing_email = None
            existing_user = UserRegistration.__check_if_user_in_database(username, user_database)
            if 'validated_email' in locals(): 
                existing_email = UserRegistration.__check_if_user_in_database(validated_email.original, user_database)

            if existing_user or existing_email:
                if existing_user is not None and existing_email is not None:                                                     
                    type = "Username and email are"
                elif existing_user is not None and existing_email is None : 
                    type = "Username is"
                elif existing_user is None and existing_email is not None : 
                    type = "Email is"

                txt_to_show  = f"{type} already in use. Please try another."

                ErrorField.show_error(parent, error_message=txt_to_show)
                signup_failed = True


            if signup_failed: return

            hashed_password = UserRegistration.__hash_password(confirmed_pass)
            UserRegistration.__save_user_to_file(username, hashed_password, email)
            print("signup success")

            ErrorField.clear_errors(parent)
            AllFields .clear_all(parent)

        elif type == 'login':
            password = parent.linePass.text()
            username = UserRegistration.__check_if_user_in_database(username, user_database)

            if username == None: print("login fail"); return

            stored_hash = user_database.get(username, {}).get('password')
            if stored_hash and UserRegistration.__check_password_against_hash(password, stored_hash):
                print("login success")
            else:
                print("login fail")


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