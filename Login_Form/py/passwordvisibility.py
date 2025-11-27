###############################################################
#
#
#                 buttontriggerse.py
#
#         Author: Brandon Lewis
#           Date: 11/26/2025
#        Updated: 11/26/2025
#
#        Summary: Class for toggling password field visibility
#                 when a push button is triggered
#
#
#
################################################################

from PyQt6.QtWidgets import QLineEdit

class PasswordVisibility():

    def password_visibility_button_trigger(parent):
        line_created_pass    = parent.linePassCreate

        is_hidden = False
        if line_created_pass.echoMode() == QLineEdit.EchoMode.Password:
            is_hidden = True

        PasswordVisibility.__toggle_visibility(parent, line_created_pass, is_hidden)


    def __toggle_visibility(parent, created_password_field, visible=True):
        line_confirmed_pass  = parent.linePassConf

        echo_state = QLineEdit.EchoMode.Normal if visible else QLineEdit.EchoMode.Password
        edit_state = visible

        created_password_field.setEchoMode(echo_state)

        line_confirmed_pass   .clear()
        line_confirmed_pass   .setReadOnly(edit_state)

