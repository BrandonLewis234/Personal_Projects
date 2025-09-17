"""
------------------------------------------------------------------
A portion of this form was implemented by
generating a python file by reading ui file 'loginform.ui'.

Created with: PyQt6 UI code generator 6.4.2
    (pyuic5 -x layout.ui -o layout.py)

Edited to add additional logic and comments.
------------------------------------------------------------------
"""

##############################################################
#
#                loginform.py
#
#         Author: Brandon Lewis
#           Date: 9/17/2025
#
#        Summary: A simple login form with the purpose of
#                 learning PyQt6 and PyQt6-tools.
# 
##############################################################

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout


# ************************************************************************************
# Window display and configuration functions
# ************************************************************************************

# ------------------------------------------------------------------------------------
# Displays a window as the main window for the application.
# Displays the winLogin window as the main window.
# ------------------------------------------------------------------------------------
class winMain(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_winLogin()
        self.ui.setupUI(self)

# ------------------------------------------------------------------------------------
# Displays a window as a QWidget to act as a confirmation window.
# ------------------------------------------------------------------------------------
class winConfirmation(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
        self.ui = Ui_winConfirmation()
        self.ui.setupUI(self, self.parent.username, self.parent.password)
        self.setLayout(self.ui.layout)


# ************************************************************************************
# UI Setup Classes
# ************************************************************************************

# ------------------------------------------------------------------------------------
# Configures the UI for a login window for use with any other application.
# ------------------------------------------------------------------------------------
class Ui_winLogin(object):
    def setupUI(self, winLogin):
        # Main window
        WIN_SIZE       = [300, 250] # Window size parameters
        WIN_RIGHT_DIST = 26         # Distrance from the right side of the window
                                    # that is desired for certain widgets to follow

        winLogin.setObjectName("winLogin")
        winLogin.resize(WIN_SIZE[0], WIN_SIZE[1])
        winLogin.setMinimumSize(QtCore.QSize(WIN_SIZE[0], WIN_SIZE[1]))
        winLogin.setMaximumSize(QtCore.QSize(WIN_SIZE[0], WIN_SIZE[1]))

        # Main window frame
        self.centralwidget = QtWidgets.QWidget(parent=winLogin)
        self.centralwidget.setObjectName("centralwidget")

        # Button widget
        ## Variables for storing button width and positional parameters in order to keep the same position
        ## for the button if a different width is desired
        btnLogin_WIDTH     = 90
        ## Calculate left position so the button stays btnLogin_RIGHT_DIST from the right edge
        btnLogin_LEFT_DIST = WIN_SIZE[0] - btnLogin_WIDTH - WIN_RIGHT_DIST

        self.btnLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(btnLogin_LEFT_DIST, 160, btnLogin_WIDTH, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLogin.sizePolicy().hasHeightForWidth())
        self.btnLogin.setSizePolicy(sizePolicy)
        self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnLogin.setObjectName("btnLogin")

        # Define button signal
        self.btnLogin.clicked.connect(self.submit_form)

        # Formatting for the login fields
        self.verticalFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.verticalFrame.setGeometry(QtCore.QRect(17, 80, 266, 60))
        self.verticalFrame.setObjectName("verticalFrame")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Label for the username
        self.lblUser = QtWidgets.QLabel(parent=self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblUser.sizePolicy().hasHeightForWidth())
        self.lblUser.setSizePolicy(sizePolicy)
        self.lblUser.setObjectName("lblUser")
        self.horizontalLayout_2.addWidget(self.lblUser)

        # Entry field for the username
        self.lineUser = QtWidgets.QLineEdit(parent=self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineUser.sizePolicy().hasHeightForWidth())
        self.lineUser.setSizePolicy(sizePolicy)
        self.lineUser.setMinimumSize(QtCore.QSize(180, 0))
        self.lineUser.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineUser.setDragEnabled(False)
        self.lineUser.setClearButtonEnabled(False)
        self.lineUser.setObjectName("lineUser")

        # Automatically set the username input as the focus when window is opened
        self.lineUser.setFocus()

        # Formatting for user fields
        self.horizontalLayout_2.addWidget(self.lineUser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(3, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Label for the password
        self.lblPass = QtWidgets.QLabel(parent=self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPass.sizePolicy().hasHeightForWidth())
        self.lblPass.setSizePolicy(sizePolicy)
        self.lblPass.setObjectName("lblPass")
        self.horizontalLayout.addWidget(self.lblPass)

        # Entry field for the password
        self.linePass = QtWidgets.QLineEdit(parent=self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linePass.sizePolicy().hasHeightForWidth())
        self.linePass.setSizePolicy(sizePolicy)
        self.linePass.setMinimumSize(QtCore.QSize(180, 0))
        self.linePass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.linePass.setDragEnabled(False)
        self.linePass.setObjectName("linePass")

        # Set up logic for when return is hit on password entry line
        self.linePass.returnPressed.connect(self.btnLogin.click)

        self.horizontalLayout.addWidget(self.linePass)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Label for the header
        self.lblHeader = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblHeader.setGeometry(QtCore.QRect(19, 20, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lblHeader.setFont(font)
        self.lblHeader.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblHeader.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblHeader.setObjectName("label")

        # Set the window in the center of the layout
        winLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(winLogin)
        
    # ------------------------------------------------------------------------------------
    # Sets the text for the widgets and
    # translates the window title, button, labels and entry fields used.
    # ------------------------------------------------------------------------------------
    def retranslateUi(self, winLogin):
        # Support for multiple languages
        _translate = QtCore.QCoreApplication.translate
        winLogin.setWindowTitle(_translate("winLogin", "Log-in Form"))
        self.btnLogin.setText(_translate("winLogin", "Log in"))
        self.lblUser.setText(_translate("winLogin", "Username:"))
        self.lineUser.setPlaceholderText(_translate("winLogin", "username"))
        self.lblPass.setText(_translate("winLogin", "Password:"))
        self.linePass.setPlaceholderText(_translate("winLogin", "password"))
        self.lblHeader.setText(_translate("winLogin", "Enter Login Information"))

    # ------------------------------------------------------------------------------------
    # Activates when the button is clicked, or when enter is pressed within the 
    # password entry field.
    #
    # Saves the username and password information and then calls show_submission_window().
    # ------------------------------------------------------------------------------------
    def submit_form(self):
        self.username = self.lineUser.text()
        self.password = self.linePass.text()

        self.show_submission_window()

    # ------------------------------------------------------------------------------------
    # Creates and shows the submission window 
    # and keeps it from being garbage collected.
    # ------------------------------------------------------------------------------------
    def show_submission_window(self):
        self.w = winConfirmation(self)
        self.w.show()

# ------------------------------------------------------------------------------------
# Configures the UI for a confirmation window, that shows a login was successful.
# ------------------------------------------------------------------------------------
class Ui_winConfirmation(object):
    def setupUI(self, winConfirmation, username, password):
        winConfirmation.setObjectName("winConfirmation")
        winConfirmation.resize(400,100)
        winConfirmation.setMinimumSize(QtCore.QSize(400, 100))
        winConfirmation.setMaximumSize(QtCore.QSize(400, 100))
        
        # Submission window frame
        self.layout = QVBoxLayout()
        self.lblNotif = QtWidgets.QLabel()
        self.lblNotif.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.lblNotif)        
        
        self.retranslateUi(winConfirmation)
        
    # ------------------------------------------------------------------------------------
    # Sets the text for the widgets and
    # translates the window title and label used.
    # ------------------------------------------------------------------------------------
    def retranslateUi(self, winConfirmation):
        # Support for multiple languages
        _translate = QtCore.QCoreApplication.translate
        winConfirmation.setWindowTitle(_translate("winConfirmation", "Login Confirmed!"))
        self.lblNotif.setText(_translate("winConfirmation", "Successfully logged in!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle("") # windows, windowsvista, fusion, or custom styles

    window = winMain()
    window.show()

    sys.exit(app.exec())
