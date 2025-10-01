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
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt6.QtWidgets import QFrame, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QSizePolicy
from PyQt6.QtGui import QPalette

from overrides import clickableLabel, set_position

class winLogin(QMainWindow):
    def __init__(self, app, position=None):
        super().__init__()
        self.ui = Ui_winLogin()
        # Fetch the app's palette in order to set colors that derive from the applied theme
        palette = app.palette()
        baseColor = palette.color(QPalette.ColorRole.Base)  # Get base color
        lighterColor = baseColor.lighter(120) # 120% lighter than base color
        
        # Define styles
        styles = {
             "lineEdit": f"background-color: {lighterColor.name()};border-radius: 5px;height: 30px;" 
        }

        self.ui.setupUi(self, styles, app)

        if position:
            set_position(self, position)
            


class Ui_winLogin(object):
    def setupUi(self, winLogin, styles, app):
        # Configure main window properties
        winLogin.setMinimumSize(300, 350)
        winLogin.setMaximumSize(450,525) # 1.5x min size

        # ---------------------------------------------------------------
        # Main layout widgets
        # ---------------------------------------------------------------

        # Central frame for widgets
        self.centralwidget = QWidget(parent=winLogin)
        winLogin.setCentralWidget(self.centralwidget)

        # Main vertical layout
        self.mainLayout = QVBoxLayout(self.centralwidget)
        if True:
            # Formatting
            self.mainLayout.setContentsMargins(20, 20, 20, 20)

        self.headerLayout = QVBoxLayout()
        if True:
            # Formatting
            self.headerLayout.setContentsMargins(0, 10, 0, 10)

        # Header label        
        self.lblHeader = QLabel(parent=self.centralwidget)
        if True:
            # Font
            font = QtGui.QFont(); font.setPointSize(16); font.setBold(True); self.lblHeader.setFont(font)
            # Alignment
            self.lblHeader.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Frame for line edit fields
        self.vframeCred = QFrame(parent=self.centralwidget)
        if True:
            # Styling
            self.vframeCred.setFrameShape(QFrame.Shape.StyledPanel)
            self.vframeCred.setFrameShadow(QFrame.Shadow.Plain)
            # Sizing
            self.vframeCred.setMaximumSize(600,200)
            # Expansion Policy
            self.vframeCred.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Add widgets to the main layout
        self.headerLayout.addWidget(self.lblHeader)
        self.mainLayout.addLayout(self.headerLayout)
        self.mainLayout.addWidget(self.vframeCred)

        # Vertical layout for line edit fields
        self.verticalLayout = QVBoxLayout(self.vframeCred)

        # ---------------------------------------------------------------
        # Credential fields
        # ---------------------------------------------------------------

        # ------------------------------
        # Username widgets
        # ------------------------------
        self.lblUser = QLabel(parent=self.vframeCred)
        if True:
            # Font
            font = QtGui.QFont(); font.setBold(True); self.lblUser.setFont(font)

        self.lineUser = QLineEdit(parent=self.vframeCred)
        if True:
            # Styling
            self.lineUser.setStyleSheet(styles["lineEdit"])

        # ------------------------------        
        # Password widgets
        # ------------------------------    
        self.lblPass = QLabel(parent=self.vframeCred)
        if True:
            # Font
            font = QtGui.QFont(); font.setBold(True); self.lblPass.setFont(font)
        
        self.linePass = QLineEdit(parent=self.vframeCred)
        if True:
            # Styling
            self.linePass.setStyleSheet(styles["lineEdit"])
            # Hide input
            self.linePass.setEchoMode(QLineEdit.EchoMode.Password)

        # ------------------------------
        # Add widgets to layout
        # ------------------------------
        # Add elements to vertical layout
        self.verticalLayout.addWidget(self.lblUser)
        self.verticalLayout.addWidget(self.lineUser)
        self.verticalLayout.addWidget(self.lblPass)
        self.verticalLayout.addWidget(self.linePass)

        # Spacing between credential frame and login button
        self.mainLayout.addSpacing(20)

        # Horizontal layout for login button
        self.hLayoutBtn = QHBoxLayout()
        if True:
            # Padding to make button ~16px narrower than full width
            self.hLayoutBtn.setContentsMargins(8, 0, 8, 0)

        # Login button
        self.btnLogin = QPushButton(parent=self.centralwidget)
        if True: 
            # Font
            font = QtGui.QFont(); font.setPointSize(10); self.btnLogin.setFont(font)
            # Formatting
            self.btnLogin.setMinimumHeight(40)
            # Cursor change
            self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            # Expansion Policy
            self.btnLogin.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        # Add to layout
        self.hLayoutBtn.addWidget(self.btnLogin)
        self.mainLayout.addLayout(self.hLayoutBtn)

        # ------------------------------        
        # Redirect widgets
        # ------------------------------     
        
        # Main Frame
        self.hzwigRedirect = QWidget(parent=self.centralwidget)

        # Main Layout
        self.hboxRedirect = QHBoxLayout(self.hzwigRedirect)

        self.lblAskAcc = QLabel(parent=self.hzwigRedirect)
        if True:
            # Font
            font = QtGui.QFont(); font.setPointSize(8); self.lblAskAcc.setFont(font)
            # Cursor change
            self.lblAskAcc.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))

        self.lblSignup = clickableLabel(parent=self.hzwigRedirect, root=winLogin, app=app, type=1)
        if True:
            # Font
            font = QtGui.QFont(); font.setUnderline(True); self.lblSignup.setFont(font)
            # Styling
            self.lblSignup.setStyleSheet("color: rgb(0, 170, 255);")
            # Cursor Change
            self.lblSignup.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.lblErrors = QLabel(parent=self.centralwidget)
        if True:
            # Styling
            self.lblErrors.setStyleSheet("color: red;")
            # Hide by default
            self.lblErrors.setVisible(False)

        # Add to layout
        self.mainLayout.addWidget(self.lblErrors, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.mainLayout.addWidget(self.hzwigRedirect, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.mainLayout.addLayout(self.hboxRedirect)
        self.hboxRedirect.addWidget(self.lblAskAcc)
        self.hboxRedirect.addWidget(self.lblSignup) 




        self.retranslateUi(winLogin)

    def retranslateUi(self, winLogin):
        _translate = QtCore.QCoreApplication.translate
        winLogin.setWindowTitle(_translate("winLogin", "Login Form"))
        self.btnLogin.setText(_translate("winLogin", "Login"))
        self.lblUser.setText(_translate("winLogin", "<html><head/><body><p>Username:<span style=\" color:red;\">*</span></p></body></html>"))
        self.lineUser.setPlaceholderText(_translate("winLogin", "username or email"))
        self.lblPass.setText(_translate("winLogin", "<html><head/><body><p>Password:<span style=\" color:red;\">*</span></p></body></html>"))
        self.linePass.setPlaceholderText(_translate("winLogin", "password"))
        self.lblHeader.setText(_translate("winLogin", "Login"))
        self.lblAskAcc.setText(_translate("winLogin", "Don\'t have an account?"))
        self.lblSignup.setText(_translate("winLogin", "Sign Up"))
        self.lblErrors.setText(_translate("winLogin", "Error messages go here"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    #app.setStyle("") # windows, windowsvista, fusion, or custom styles
    window = winLogin(app)
    window.show()

    sys.exit(app.exec())