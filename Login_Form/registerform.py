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
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QSizePolicy, QLabel
from PyQt6.QtWidgets import QFrame, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMenuBar, QStatusBar
from PyQt6.QtGui import QPalette

class winRegister(QMainWindow):
    def __init__(self, app):
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

        self.ui.setupUi(self, styles)
  

class Ui_winRegister(object):
    def setupUi(self, winRegister, styles):
        # Configure main window properties
        winRegister.setObjectName("winRegister")
        winRegister.setFixedSize(QtCore.QSize(300, 450))
        winRegister.setStyleSheet("")

        # ---------------------------------------------------------------
        # Main layout widgets
        # ---------------------------------------------------------------
        
        # Central frame for widgets
        self.centralwidget = QWidget(parent=winRegister)

        # Frame for line edit fields
        self.vframeCred = QFrame(parent=self.centralwidget)
        if True:
                # Positioning
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
                # Positioning
                self.lblHeader.setGeometry(QtCore.QRect(20, 20, 261, 41))
                # Font
                font = QtGui.QFont(); font.setPointSize(16); font.setBold(True)
                self.lblHeader.setFont(font)
                # Alignment
                self.lblHeader.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        # Signup button
        self.btnSignup = QPushButton(parent=self.centralwidget)
        if True:
                # Positioning
                self.btnSignup.setGeometry(QtCore.QRect(39, 340, 221, 41))
                # Font
                font = QtGui.QFont(); font.setPointSize(10)
                self.btnSignup.setFont(font)
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

        # ------------------------------
        # Add widgets to layout
        # ------------------------------
        # Add elements to vertical layout
        self.vboxCred.          addWidget(self.lblEmail)
        self.vboxCred.          addWidget(self.lineEmail)
        self.vboxCred.          addWidget(self.lblUser)
        self.vboxCred.          addWidget(self.lineUser)
        self.vboxCred.          addWidget(self.lblPassCreate)
        # Add passion creation elements to horizontal layout
        self.hboxPassCreate.    addWidget(self.linePassCreate)
        self.hboxPassCreate.    addWidget(self.pbtnToggleVis)

        self.vboxCred.addWidget(self.hzwigPassCreate)
        self.lblPassConf = QLabel(parent=self.vframeCred)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPassConf.sizePolicy().hasHeightForWidth())
        self.lblPassConf.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        self.lblPassConf.setFont(font)
        self.lblPassConf.setObjectName("lblPassConf")
        self.vboxCred.addWidget(self.lblPassConf)
        self.linePassConf = QLineEdit(parent=self.vframeCred)
        self.linePassConf.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linePassConf.sizePolicy().hasHeightForWidth())
        self.linePassConf.setSizePolicy(sizePolicy)
        self.linePassConf.setMinimumSize(QtCore.QSize(200, 0))
        self.linePassConf.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.linePassConf.setEchoMode(QLineEdit.EchoMode.Password)
        self.linePassConf.setDragEnabled(False)
        self.linePassConf.setObjectName("linePassConf")
        self.linePassConf.setStyleSheet(styles["lineEdit"])
        self.vboxCred.addWidget(self.linePassConf)
        self.hzwigRedirect = QWidget(parent=self.centralwidget)
        self.hzwigRedirect.setGeometry(QtCore.QRect(40, 380, 221, 31))
        self.hzwigRedirect.setObjectName("hzwigRedirect")
        self.horizontalLayout_2 = QHBoxLayout(self.hzwigRedirect)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblAskAcc = QLabel(parent=self.hzwigRedirect)
        self.lblAskAcc.setMinimumSize(QtCore.QSize(135, 0))
        self.lblAskAcc.setMaximumSize(QtCore.QSize(135, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblAskAcc.setFont(font)
        self.lblAskAcc.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.lblAskAcc.setStyleSheet("")
        self.lblAskAcc.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblAskAcc.setIndent(-1)
        self.lblAskAcc.setObjectName("lblAskAcc")
        self.horizontalLayout_2.addWidget(self.lblAskAcc)
        self.lblLogin = QLabel(parent=self.hzwigRedirect)
        self.lblLogin.setEnabled(True)
        self.lblLogin.setMinimumSize(QtCore.QSize(50, 0))
        self.lblLogin.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lblLogin.setFont(font)
        self.lblLogin.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.lblLogin.setStyleSheet("color: rgb(0, 170, 255);")
        self.lblLogin.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblLogin.setWordWrap(False)
        self.lblLogin.setObjectName("lblLogin")
        self.horizontalLayout_2.addWidget(self.lblLogin)
        self.lblErrors = QLabel(parent=self.centralwidget)
        self.lblErrors.setEnabled(True)
        self.lblErrors.setGeometry(QtCore.QRect(40, 305, 241, 31))
        font = QtGui.QFont()
        font.setBold(False)
        self.lblErrors.setFont(font)
        self.lblErrors.setStyleSheet("color: red;")
        self.lblErrors.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lblErrors.setObjectName("lblErrors")
        winRegister.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(parent=winRegister)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        winRegister.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(parent=winRegister)
        self.statusbar.setObjectName("statusbar")
        winRegister.setStatusBar(self.statusbar)
        self.lblEmail.setBuddy(self.lineEmail)
        self.lblUser.setBuddy(self.lineUser)
        self.lblPassCreate.setBuddy(self.linePassCreate)
        self.lblPassConf.setBuddy(self.linePassConf)

        self.retranslateUi(winRegister)
        QtCore.QMetaObject.connectSlotsByName(winRegister)

    def retranslateUi(self, winRegister):
        _translate = QtCore.QCoreApplication.translate
        winRegister.setWindowTitle(_translate("winRegister", "Registration Form"))
        self.lblHeader.setText(_translate("winRegister", "Signup"))
        self.btnSignup.setText(_translate("winRegister", "Signup"))
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