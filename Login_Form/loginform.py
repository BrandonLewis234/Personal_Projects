"""
------------------------------------------------------------------
A portion of this form was implemented by
generating a python file from reading ui file 'loginform.ui'.
Created by: PyQt6 UI code generator 6.4.2

Heavily edited to add additional logic and comments.
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
#                 learning PyQt6 and PyQt6-tools
# 
##############################################################


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

class winMain(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_winLogin()
        self.ui.setupUI(self)

class winConfirmation(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
        self.ui = Ui_winConfirmation()
        self.ui.setupUI(self, self.parent.username, self.parent.password)
        self.setLayout(self.ui.layout)


class Ui_winLogin(object):
    def setupUI(self, winLogin):
        # Main window
        winLogin.setObjectName("winLogin")
        winLogin.resize(300, 250)
        winLogin.setMinimumSize(QtCore.QSize(300, 250))
        winLogin.setMaximumSize(QtCore.QSize(300, 250))

        # Main window frame
        self.centralwidget = QtWidgets.QWidget(parent=winLogin)
        self.centralwidget.setObjectName("centralwidget")

        # Button widget
        self.btnLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(164, 160, 121, 31))
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
        self.lineUser.setMinimumSize(QtCore.QSize(200, 0))
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
        self.linePass.setMinimumSize(QtCore.QSize(200, 0))
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

    def submit_form(self):
        self.username = self.lineUser.text()
        self.password = self.linePass.text()

        self.show_submission_window()

    def show_submission_window(self):
        self.w = winConfirmation(self)
        self.w.show()

class Ui_winConfirmation(object):
    def setupUI(self, winConfirmation, username, password):
        winConfirmation.setObjectName("winConfirmation")
        winConfirmation.setWindowTitle("Login Confirmed!")
        winConfirmation.resize(400,100)
        winConfirmation.setMinimumSize(QtCore.QSize(400, 100))
        winConfirmation.setMaximumSize(QtCore.QSize(400, 100))
        
        # Submission window frame
        self.layout = QVBoxLayout()
        self.label = QtWidgets.QLabel(f"Succesfully logged in!")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.label)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle("") # windows, windowsvista, fusion, or custom styles

    window = winMain()
    window.show()

    sys.exit(app.exec())
