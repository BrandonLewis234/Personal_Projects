###############################################################
#
#
#                shared.py
#
#         Author: Brandon Lewis
#           Date: 10/4/2025
#
#        Summary: Shared styles and functions between forms
#
#
#
#
################################################################

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt6.QtWidgets import QFrame, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QSizePolicy
from PyQt6.QtGui import QPalette

from overrides import clickableLabel

class share_styles():
    def __init__(self, parent):
        app = parent
        #parent.setStyle("") # windows, windowsvista, fusion, or custom styles

        # Fetch the app's palette in order to set colors that derive from the applied theme
        palette = parent.palette()
        app.baseColor = palette.color(QPalette.ColorRole.Base)  # Get base color
        app.lighterColor = app.baseColor.lighter(120) # 120% lighter than base color
        
        # Define styles
        app.styles = {
             "lineEdit": f"background-color: {app.lighterColor.name()};border-radius: 5px;height: 30px;" 
        }

class make_window():
    def __init__(self, app, window, title="", size=[], max_size=[],
                 header_text=""):
        self.app = app
        self.size = size
        self.window = window
        self.headerText = header_text
        
        self.window.setMinimumSize(size[0], size[1] + 30)
        self.window.setMaximumSize(max_size[0], max_size[1])

        # Central frame for widgets
        self.centralwidget = QWidget(parent=self.window)
        self.window.setCentralWidget(self.centralwidget)

        self._set_main_layout()        
        
        # Set title and define translation implementation
        self.window.setWindowTitle(self.translate(f"{self.window}", title))


    # ---------------------------------------------------------------
    # Main layout widgets
    # ---------------------------------------------------------------
    def _set_main_layout(self):
        # Main vertical layout
        self.layoutMain = QVBoxLayout(self.centralwidget)
        if True:
            # Formatting
            self.layoutMain.setContentsMargins(20, 20, 20, 20)

        # Header label        
        if self.headerText != "":
            self.lblHeader = QLabel(parent=self.centralwidget)
            if True:
                # Font
                font = QtGui.QFont(); font.setPointSize(16); font.setBold(True); self.lblHeader.setFont(font)
                # Formatting
                self.lblHeader.setContentsMargins(0, 10, 0, 10)
                self.lblHeader.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                # Alignment
                self.lblHeader.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Frame for line edit fields
        self.vframeCred = QFrame(parent=self.centralwidget)
        if True:
            # Styling
            self.vframeCred.setFrameShape(QFrame.Shape.StyledPanel)
            self.vframeCred.setFrameShadow(QFrame.Shadow.Plain)
            # Sizing
            self.vframeCred.setMinimumSize(100, int(self.size[1] / 3))
            self.vframeCred.setMaximumSize(450, self.size[1] - 100)
            # Expansion Policy
            self.vframeCred.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)

        # Add and set header text and translation
        if hasattr(self, 'lblHeader'):
            self.layoutMain.addWidget(self.lblHeader)
            self.lblHeader.setText(self.translate(f"{self.window}", self.headerText))

        # Add to layouts
        self.layoutMain.addWidget(self.vframeCred)
        self.layoutCred = QVBoxLayout(self.vframeCred)


    # ---------------------------------------------------------------
    # Credential fields
    # ---------------------------------------------------------------
    def set_credential_fields(self, type='login'):
        # ---------------------------------------------------------------
        # Universal Widgets
        # ---------------------------------------------------------------

        # ------------------------------
        # Username widgets
        # ------------------------------        
        self.lblUser = QLabel(parent=self.vframeCred)
        if True:
                # Font:
                font = QtGui.QFont(); font.setBold(True); self.lblUser.setFont(font)

        self.lineUser = QLineEdit(parent=self.vframeCred)
        if True:
            # Styling
            self.lineUser.setStyleSheet(self.app.styles["lineEdit"])
        
        # Add error checking
        self._set_error_label()

        # ------------------------------
        # Confirmation button
        # ------------------------------     
        self.btnConfirm = QPushButton(parent=self.centralwidget)
        if True: 
            # Font
            font = QtGui.QFont(); font.setPointSize(10); self.btnConfirm.setFont(font)
            # Formatting
            self.btnConfirm.setMinimumHeight(40)
            self.btnConfirm.setMaximumHeight(60)
            # Cursor change
            self.btnConfirm.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            # Expansion Policy
            self.btnConfirm.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)

        # Horizontal layout for confirmation button
        self.layoutConfirm = QHBoxLayout()
        if True:
            # Padding to make button ~16px narrower than full width
            self.layoutConfirm.setContentsMargins(8, 0, 8, 0)

        # Spacing between credential frame and confirmation button
        self.layoutMain.addSpacing(50)

        # Add elements to main layouts
        self.layoutConfirm.addWidget(self.btnConfirm)
        self.layoutMain.addLayout(self.layoutConfirm)
        self.layoutCred.addWidget(self.lblUser)
        self.layoutCred.addWidget(self.lineUser)      

        # Set text and translations for universal widgets
        self.lblUser.setText(self.translate(f"{self.window}", "<html><head/><body><p>Username:<span style=\" color:red;\">*</span></p></body></html>"))
        self.lineUser.setPlaceholderText(self.translate(f"{self.window}", "username or email"))
        self.btnConfirm.setText(self.translate(f"{self.window}", f"{type[:1].upper()}{type[1:]}"))

        # ---------------------------------------------------------------
        # Widgets for specified implementation
        # ---------------------------------------------------------------
        if type == 'login':
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
                self.linePass.setStyleSheet(self.app.styles["lineEdit"])
                # Hide input
                self.linePass.setEchoMode(QLineEdit.EchoMode.Password)


            # Add elements to vertical layout
            self.layoutCred.addWidget(self.lblPass)
            self.layoutCred.addWidget(self.linePass)


            # Set login text and translations
            # Add a red * character at the end of required fields
            self.lblPass.setText(self.translate(f"{self.window}", "<html><head/><body><p>Password:<span style=\" color:red;\">*</span></p></body></html>"))
            self.linePass.setPlaceholderText(self.translate(f"{self.window}", "password"))


        if type=='signup':            
            # ------------------------------
            # Email widgets
            # ------------------------------
            self.lblEmail = QLabel(parent=self.vframeCred)
            if True:
                    # Font
                    font = QtGui.QFont(); font.setBold(True); self.lblEmail.setFont(font)

            self.lineEmail = QLineEdit(parent=self.vframeCred)
            if True:
                # Styling
                self.lineEmail.setStyleSheet(self.app.styles["lineEdit"])
            
            # ------------------------------        
            # Password creation widgets
            # ------------------------------        

            # Horizontal widget for password creation and show/hide button
            self.frmPassCreate = QWidget(parent=self.vframeCred)
            
            # Horizontal layout for password creation and show/hide button
            self.hboxPassCreate = QHBoxLayout(self.frmPassCreate)
            if True:
                    self.hboxPassCreate.setContentsMargins(0, 0, 0, 0)
                    self.hboxPassCreate.setSpacing(5)

            self.lblPassCreate = QLabel(parent=self.vframeCred)
            if True:
                    font = QtGui.QFont(); font.setBold(True); self.lblPassCreate.setFont(font)

            self.linePassCreate = QLineEdit(parent=self.frmPassCreate)
            if True:
                # Styling
                self.linePassCreate.setStyleSheet(self.app.styles["lineEdit"])
                # Hide input
                self.linePassCreate.setEchoMode(QLineEdit.EchoMode.Password)

            # Button for toggling visibility for passCreate and disabling passConf
            self.pbtnToggleVis = QPushButton(parent=self.frmPassCreate)
            if True:        
                    # Sizing
                    self.pbtnToggleVis.setFixedSize(QtCore.QSize(30, 30))
                    # Cursor change
                    self.pbtnToggleVis.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

            self.lblPassConf = QLabel(parent=self.vframeCred)
            if True:
                    # Font
                    font = QtGui.QFont(); font.setBold(True); self.lblPassConf.setFont(font)

            self.linePassConf = QLineEdit(parent=self.vframeCred)
            if True:
                # Styling
                self.linePassConf.setStyleSheet(self.app.styles["lineEdit"])
                # Hide input
                self.linePassConf.setEchoMode(QLineEdit.EchoMode.Password)

            # ------------------------------
            # Add widgets to layout
            # ------------------------------
            # Add elements to vertical layout
            self.layoutCred.          addWidget(self.lblEmail)
            self.layoutCred.          addWidget(self.lineEmail)
            self.layoutCred.          addWidget(self.lblUser)
            self.layoutCred.          addWidget(self.lineUser)
            self.layoutCred.          addWidget(self.lblPassCreate)
            self.layoutCred.          addWidget(self.frmPassCreate)
            self.layoutCred.          addWidget(self.lblPassConf)
            self.layoutCred.          addWidget(self.linePassConf)
            # Add password creation elements to horizontal layout
            self.hboxPassCreate.    addWidget(self.linePassCreate)
            self.hboxPassCreate.    addWidget(self.pbtnToggleVis)

            # Set registration text and translations        
            self.lblEmail.setText(self.translate(f"{self.window}", "<html><head/><body><p>Email:<span style=\" color:red;\">*</span></p></body></html>"))
            self.lineEmail.setPlaceholderText(self.translate(f"{self.window}", "email"))
            self.lblPassCreate.setText(self.translate(f"{self.window}", "<html><head/><body><p>Create password:<span style=\" color:red;\">*</span></p></body></html>"))
            self.linePassCreate.setPlaceholderText(self.translate(f"{self.window}", "password"))
            self.pbtnToggleVis.setToolTip(self.translate(f"{self.window}", "show/hide password"))
            self.pbtnToggleVis.setText(self.translate(f"{self.window}", "..."))
            self.lblPassConf.setText(self.translate(f"{self.window}", "<html><head/><body><p>Confirm password:<span style=\" color:red;\">*</span></p></body></html>"))
            self.linePassConf.setPlaceholderText(self.translate(f"{self.window}", "password"))


    # ------------------------------        
    # Redirect widgets
    # ------------------------------     
    def set_redirect_label(self, redirect_to='signup'):
        # Main Frame
        self.frmRedirect = QFrame()

        # Main Layout
        self.hboxRedirect = QHBoxLayout(self.frmRedirect)

        self.lblAskAcc = QLabel()
        if True:
            # Font
            font = QtGui.QFont(); font.setPointSize(8); self.lblAskAcc.setFont(font)
            # Cursor change
            self.lblAskAcc.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
    
        self.lblRedirect = clickableLabel(root=self.window, app=self.app, type=redirect_to)
        if True:
            # Font
            font = QtGui.QFont(); font.setUnderline(True); self.lblRedirect.setFont(font)
            # Styling
            self.lblRedirect.setStyleSheet("color: rgb(0, 170, 255);")
            # Cursor Change
            self.lblRedirect.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
 
        # Add to main layout
        self.layoutMain.addWidget(self.frmRedirect, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.hboxRedirect.addWidget(self.lblAskAcc)
        self.hboxRedirect.addWidget(self.lblRedirect) 

        # Set text and translations
        text = "Don't have an account?" if redirect_to == 'register' else "Already have an account?"
        self.lblAskAcc.setText(self.translate(f"{self.window}", text))
        self.lblAskAcc.setText(self.translate(f"{self.window}", text))
        self.lblRedirect.setText(self.translate(f"{self.window}", "Sign Up"))


    def _set_error_label(self):
        # ------------------------------        
        # Error label
        # ------------------------------     

        self.lblErrors = QLabel(parent=self.centralwidget)
        if True:
            # Styling
            self.lblErrors.setStyleSheet("color: red;")
            # Hide by default
            self.lblErrors.setVisible(False)

        self.layoutMain.addWidget(self.lblErrors, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        
        # Set text and translation
        self.lblErrors.setText(self.translate(f"{self.window}", "Error messages go here"))
    
    
    # ---------------------------------------------------------------
    # Add titles for widgets and ensure they 
    # translate to the user's set langauge
    # (Given that a translation file is created and set)
    # ---------------------------------------------------------------
    def translate(self, window, text) -> QtCore.QCoreApplication.translate:
        self.translate = QtCore.QCoreApplication.translate

        return self.translate(window, text)