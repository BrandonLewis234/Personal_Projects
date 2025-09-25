###############################################################
#
#
#                registerform.py
#
#         Author: Brandon Lewis
#           Date: 9/24/2025
#
#        Summary: A simple signup form with the purpose of
#                 learning PyQt6 and PyQt6-tools.
# 
#          NOTE: Any "if True:" blocks are just for formatting
#                and for better visualization.
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
from PyQt6.QtWidgets import QFrame, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt6.QtGui import QPalette

from overrides import clickableLabel, set_position

# ---------------------------------------------------------------
# Displays the winLogin window as the main window.
# ---------------------------------------------------------------
class winRegister(QMainWindow):
    def __init__(self, app, position=None):
        super().__init__()
        self.ui = Ui_winRegister()
        
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


# ------------------------------------------------------------------------------------
# Configures the UI for a login window for use with any other application.
# ------------------------------------------------------------------------------------
class Ui_winRegister(object):
    def setupUi(self, winRegister, styles, app):
        # Configure main window properties
        winRegister.setObjectName("winRegister")
        winRegister.setFixedSize(300, 450)

        # ---------------------------------------------------------------
        # Main layout widgets
        # ---------------------------------------------------------------
        
        # Central frame for widgets
        self.centralwidget = QWidget(parent=winRegister)
        winRegister.setCentralWidget(self.centralwidget)
        
        # Frame for line edit fields
        self.vframeCred = QFrame(parent=self.centralwidget)
        if True:
                # Sizing
                self.vframeCred.setGeometry(QtCore.QRect(30, 70, 241, 231))
                # Styling
                self.vframeCred.setFrameShape(QFrame.Shape.StyledPanel)
                self.vframeCred.setFrameShadow(QFrame.Shadow.Plain)

        # Vertical layout for line edit fields
        self.vboxCred = QVBoxLayout(self.vframeCred)
        if True:
                # Margins and spacing 
                self.vboxCred.setContentsMargins(-1, 6, -1, -1)
                self.vboxCred.setSpacing(5)

        # Header label
        self.lblHeader = QLabel(parent=self.centralwidget)
        if True:
                # Font
                font = QtGui.QFont(); font.setPointSize(16); font.setBold(True); self.lblHeader.setFont(font)
                # Sizing
                self.lblHeader.setGeometry(QtCore.QRect(20, 20, 261, 41))
                # Alignment
                self.lblHeader.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        # Signup button
        self.btnSignup = QPushButton(parent=self.centralwidget)
        if True:
                # Font
                font = QtGui.QFont(); font.setPointSize(10); self.btnSignup.setFont(font)
                # Sizing
                self.btnSignup.setGeometry(QtCore.QRect(39, 340, 221, 41))
                # Cursor change
                self.btnSignup.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        # ---------------------------------------------------------------
        # Credential fields
        # ---------------------------------------------------------------
        # Variables for credential fields
        alignCred = QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter
        sizeCred  = QtCore.QSize(200,0)

        # ------------------------------
        # Email widgets
        # ------------------------------
        self.lblEmail = QLabel(parent=self.vframeCred)
        if True:
                # Font
                font = QtGui.QFont(); font.setBold(True); self.lblEmail.setFont(font)

        self.lineEmail = QLineEdit(parent=self.vframeCred)
        if True:
                # Sizing
                self.lineEmail.setMinimumSize(sizeCred)
                # Alignment
                self.lineEmail.setAlignment(alignCred)
                # Styling
                self.lineEmail.setStyleSheet(styles["lineEdit"])
                # Hide input
                self.lineEmail.setEchoMode(QLineEdit.EchoMode.Normal)

        # ------------------------------
        # Username widgets
        # ------------------------------        
        self.lblUser = QLabel(parent=self.vframeCred)
        if True:
                # Font:
                font = QtGui.QFont(); font.setBold(True); self.lblUser.setFont(font)

        self.lineUser = QLineEdit(parent=self.vframeCred)
        if True:
                # Sizing
                self.lineUser.setMinimumSize(sizeCred)
                # Alignment
                self.lineUser.setAlignment(alignCred)
                # Styling
                self.lineUser.setStyleSheet(styles["lineEdit"])
                # Hide input
                self.lineUser.setEchoMode(QLineEdit.EchoMode.Normal)
        
        # ------------------------------        
        # Password creation widgets
        # ------------------------------        

        ## Horizontal widget for password creation and show/hide button
        self.hzwigPassCreate = QWidget(parent=self.vframeCred)
        
        ## Horizontal layout for password creation and show/hide button
        self.hboxPassCreate = QHBoxLayout(self.hzwigPassCreate)
        if True:
                self.hboxPassCreate.setContentsMargins(0, 0, 0, 0)
                self.hboxPassCreate.setSpacing(5)


        self.lblPassCreate = QLabel(parent=self.vframeCred)
        if True:
                font = QtGui.QFont(); font.setBold(True); self.lblPassCreate.setFont(font)

        self.linePassCreate = QLineEdit(parent=self.hzwigPassCreate)
        if True:
                # Sizing
                self.linePassCreate.setMinimumSize(QtCore.QSize(180, 30))
                # Alignment
                self.linePassCreate.setAlignment(alignCred)
                # Styling
                self.linePassCreate.setStyleSheet(styles["lineEdit"])
                # Hide input
                self.linePassCreate.setEchoMode(QLineEdit.EchoMode.Password)

        ## Button for toggling visibility for passCreate and disabling passConf
        self.pbtnToggleVis = QPushButton(parent=self.hzwigPassCreate)
        if True:        
                # Sizing
                self.pbtnToggleVis.setMinimumSize(QtCore.QSize(30, 30))
                # Cursor change
                self.pbtnToggleVis.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))


        self.lblPassConf = QLabel(parent=self.vframeCred)
        if True:
                # Font
                font = QtGui.QFont(); font.setBold(True); self.lblPassConf.setFont(font)

        self.linePassConf = QLineEdit(parent=self.vframeCred)
        if True:
                # Sizing
                self.linePassConf.setMinimumSize(QtCore.QSize(200, 0))
                # Styling
                self.linePassConf.setStyleSheet(styles["lineEdit"])
                # Hide input
                self.linePassConf.setEchoMode(QLineEdit.EchoMode.Password)

        # ------------------------------        
        # Redirect widgets
        # ------------------------------     

        # Main frame
        self.hzwigRedirect = QWidget(parent=self.centralwidget)
        if True:
                # Sizing
                self.hzwigRedirect.setGeometry(QtCore.QRect(50, 380, 225, 31))

        # Main layout
        self.hboxRedirect = QHBoxLayout(self.hzwigRedirect)
        if True:
                self.hboxRedirect.setContentsMargins(0, 0, 0, 0)

        self.lblAskAcc = QLabel(parent=self.hzwigRedirect)
        if True:
                # Font
                font = QtGui.QFont(); font.setPointSize(8); self.lblAskAcc.setFont(font)
                # Sizing
                self.lblAskAcc.setMinimumSize(QtCore.QSize(140, 0))
                # Alignment
                self.lblAskAcc.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignVCenter)
                # Cursor change
                self.lblAskAcc.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))

        self.lblLogin = clickableLabel(parent=self.hzwigRedirect, root=winRegister, app=app)
        if True:
                # Font
                font = QtGui.QFont(); font.setUnderline(True); self.lblLogin.setFont(font)
                # Sizing
                self.lblLogin.setMinimumSize(QtCore.QSize(50, 0))
                # Alignment
                self.lblLogin.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
                # Styling
                self.lblLogin.setStyleSheet("color: rgb(0, 170, 255); padding-bottom: 2px;")
                # Cursor Change
                self.lblLogin.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        # ------------------------------        
        # Error label
        # ------------------------------    

        self.lblErrors = QLabel(parent=self.centralwidget)
        if True:
                # Hide by default
                self.lblErrors.setVisible(False)
                # Font
                font = QtGui.QFont(); font.setBold(False); self.lblErrors.setFont(font)
                # Sizing
                self.lblErrors.setGeometry(QtCore.QRect(40, 305, 241, 31))
                # Alignment
                self.lblErrors.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
                # Styling
                self.lblErrors.setStyleSheet("color: red;")

                
        # ------------------------------
        # Add widgets to layout
        # ------------------------------
        # Add elements to vertical layout
        self.vboxCred.          addWidget(self.lblEmail)
        self.vboxCred.          addWidget(self.lineEmail)
        self.vboxCred.          addWidget(self.lblUser)
        self.vboxCred.          addWidget(self.lineUser)
        self.vboxCred.          addWidget(self.lblPassCreate)
        self.vboxCred.          addWidget(self.hzwigPassCreate)
        self.vboxCred.          addWidget(self.lblPassConf)
        self.vboxCred.          addWidget(self.linePassConf)
        # Add password creation elements to horizontal layout
        self.hboxPassCreate.    addWidget(self.linePassCreate)
        self.hboxPassCreate.    addWidget(self.pbtnToggleVis)
        # Add redirect elements to horizontal layout
        self.hboxRedirect.      addWidget(self.lblAskAcc)
        self.hboxRedirect.      addWidget(self.lblLogin)

        # ---------------------------------------------------------------
        # Set translation
        # ---------------------------------------------------------------
        self.retranslateUi(winRegister)


    # ---------------------------------------------------------------
    # Add titles for widgets and ensure they 
    # translate to the user's set langauge
    # ---------------------------------------------------------------
    def retranslateUi(self, winRegister):
        _translate = QtCore.QCoreApplication.translate
        winRegister.setWindowTitle(_translate("winRegister", "Signup Form"))

        self.lblHeader.setText(_translate("winRegister", "Signup"))
        self.btnSignup.setText(_translate("winRegister", "Signup"))

        # Add a red * character at the end of required fields
        self.lblEmail.setText(_translate("winRegister", "<html><head/><body><p>Email:<span style=\" color:red;\">*</span></p></body></html>"))
        self.lineEmail.setPlaceholderText(_translate("winRegister", "email"))
        self.lblUser.setText(_translate("winRegister", "<html><head/><body><p>Username:<span style=\" color:red;\">*</span></p></body></html>"))
        self.lineUser.setPlaceholderText(_translate("winRegister", "username"))

        self.lblPassCreate.setText(_translate("winRegister", "<html><head/><body><p>Create password:<span style=\" color:red;\">*</span></p></body></html>"))
        self.linePassCreate.setPlaceholderText(_translate("winRegister", "password"))
        self.pbtnToggleVis.setToolTip(_translate("winRegister", "show/hide password"))
        self.pbtnToggleVis.setText(_translate("winRegister", "..."))
        self.lblPassConf.setText(_translate("winRegister", "<html><head/><body><p>Confirm password:<span style=\" color:red;\">*</span></p></body></html>"))
        self.linePassConf.setPlaceholderText(_translate("winRegister", "password"))

        self.lblAskAcc.setText(_translate("winRegister", "Already have an account?"))
        self.lblLogin.setText(_translate("winRegister", "Log in"))

        self.lblErrors.setText(_translate("winRegister", "Error messages go here"))




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyle("") # windows, windowsvista, fusion, or custom styles

    window = winRegister(app)
    window.show()

    sys.exit(app.exec())