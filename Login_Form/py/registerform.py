###############################################################
#
#
#                registerform.py
#
#         Author: Brandon Lewis
#           Date: 9/24/2025
#        Updated: 10/4/2025
#
#        Summary: A simple signup form with the purpose of
#                 learning PyQt6 and PyQt6-tools.
# 
#           NOTE: Any "if True:" blocks are just for formatting
#                 and for better visualization.
#
#
#
#
################################################################

# -------------------------------------------------------------
# A portion of this form was implemented by
# generating a python file by reading ui file 'loginform.ui'.
#
# Created with: PyQt6 UI code generator 6.4.2
#     (pyuic5 -x layout.ui -o layout.py)
#
# Edited to add additional logic and comments.
# -------------------------------------------------------------

from PyQt6.QtWidgets import QApplication, QMainWindow

from overrides import set_position
from shared import share_styles, make_window

# ---------------------------------------------------------------
# Displays the winRegister window as the main window.
# ---------------------------------------------------------------
class winRegister(QMainWindow):
    def __init__(self, app, position=None):
        super().__init__()
        self.ui = Ui_winRegister()
        
        self.ui.setupUi(self, app)
        
        if position:
            set_position(self, position, adjustments=[80,20])


# ------------------------------------------------------------------------------------
# Configures the UI for a signup window for use with any other application.
# ------------------------------------------------------------------------------------
class Ui_winRegister(object):
    def setupUi(self, winRegister, app):
        window = make_window(app, winRegister, title="Signup Form", header_text="Signup",
                              size=[300, 440], max_size=[450,600])

        window.add_credential_fields(type='signup')

        window.add_redirect_label(redirect_to='login')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    share_styles(parent=app)
    
    window = winRegister(app)
    window.show()

    sys.exit(app.exec())