###############################################################
#
#
#                 buttontriggers.py
#
#         Author: Brandon Lewis
#           Date: 11/26/2025
#        Updated: 11/26/2025
#
#        Summary: Holds the callback functions for all of the
#                 button triggers in the application.
#
#
#
################################################################

from userregistration import UserRegistration
from passwordvisibility import PasswordVisibility

class ButtonTriggers():

    def confirmation_button_callback(parent, type='login'):
        UserRegistration.confirmation_button_trigger(parent, type)

    def password_visibility_button_callback(parent):
        PasswordVisibility.password_visibility_button_trigger(parent)