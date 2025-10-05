###############################################################
#
#
#                loginform.py
#
#         Author: Brandon Lewis
#           Date: 9/30/2025
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


from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtWidgets import QFrame, QPushButton, QHBoxLayout, QLineEdit, QSizePolicy

from overrides import set_position
from shared import share_styles, make_window

class winLogin(QMainWindow):
    def __init__(self, app, position=None):
        super().__init__()
        self.ui = Ui_winLogin()

        self.ui.setupUi(self, app)

        if position:
            set_position(self, position, adjustments=[250,120])
            


class Ui_winLogin(object):
    def setupUi(self, winLogin, app):
        window = make_window(app, winLogin, title="Login Form", header_text="Login",
                              size=[300, 330], max_size=[450,500])

        window.set_credential_fields(type='login')

        window.set_redirect_label(redirect_to='signup')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    share_styles(parent=app)
    
    window = winLogin(app)
    window.show()

    sys.exit(app.exec())