###############################################################
#
#
#                shared.py
#
#         Author: Brandon Lewis
#           Date: 10/4/2025
#        Updated: 10/8/2025
#
#        Summary: Shared styles and functions between forms
#
# 
#           NOTE: Any "if True:" blocks are just for formatting
#                 and for better visualization.
#
#
#
################################################################

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtWidgets import QFrame, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QSizePolicy
from PyQt6.QtGui import QPalette

from overrides import clickableLabel

# ---------------------------------------------------------------
# Defines the styles to be used across multiple forms and
# windows in order to keep consistent styles and to avoid
# unnecesarily repeating them.
# ---------------------------------------------------------------
class share_styles():
    def __init__(self, parent):
        app = parent
        #parent.setStyle("") # windows, windowsvista, fusion, or custom styles

        # Fetch the app's palette in order to set colors that derive from the applied theme
        self.palette = parent.palette()
        app.color_highlight = self.get_qpallete_colorrole('Highlight')
    
        # Define styles
        # src: https://doc.qt.io/qt-6/stylesheet-examples.html
        app.setStyleSheet(
           f"""
            QLineEdit            {{ background-color: {(self.get_qpallete_colorrole('Base', as_name=False).lighter(120)).name()};
                                    border-radius: 5px;height: 30px; }}
            clickableLabel       {{ color: {self.get_qpallete_colorrole('Link')}; }}
            clickableLabel:focus {{ color: {self.get_qpallete_colorrole('Link')};
                                    border-radius: 2px;padding: 2px;
                                    border: 1px dashed {self.get_qpallete_colorrole('Text')}; }}
            QLabel#lblError      {{ color: {app.color_highlight} }}
            """)


    # ------------------------------------------------------------------------------------------------------------------    
    # Returns either the hex value or the QPallete.ColorRole object
    # that matches the 'color_role' argument if it exists.
    #
    # srcs:
    #    https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QApplication.html#PySide6.QtWidgets.QApplication.palette
    #    https://doc.qt.io/qtforpython-6/PySide6/QtGui/QPalette.html
    #
    # Available colors at the link below:
    # src: https://doc.qt.io/qtforpython-6/PySide6/QtGui/QPalette.html#PySide6.QtGui.QPalette.ColorRole
    # -----------------------------------------------------------------------------------------------------------------    
    def get_qpallete_colorrole(self, color_role="", as_name=True):
         try: 
            if hasattr(QPalette.ColorRole, color_role):
                 color = getattr(QPalette.ColorRole, color_role)
                 color = self.palette.color(color)

                 return color.name() if as_name else color          
            else:
                 return "-1: Color not found"
         except Exception as e:
              print(f"Failure to retrieve provided color role! Exception raised:\n{e}")


# ---------------------------------------------------------------
# Initializes a window and provides additional functions for
# adding in additional widgets and elements, such as credential
# fields for login/signup forms. 
# ---------------------------------------------------------------
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
    # Create the main layout widgets
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
    # Create credential fields
    # ---------------------------------------------------------------
    def add_credential_fields(self, type='login'):
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
        self.layoutCred.addWidget(self.lblUser)
        self.layoutCred.addWidget(self.lineUser)    
        self.layoutMain.addLayout(self.layoutConfirm)
        self.layoutConfirm.addWidget(self.btnConfirm)  

        # Set text and translations for universal widgets
        txtUser = "username or email" if type=='login' else "username"

        self.lblUser.setText(self.translate(f"{self.window}",             self.mandatory_field(txtUser)))
        self.lineUser.setPlaceholderText(self.translate(f"{self.window}", txtUser))
        self.btnConfirm.setText(self.translate(f"{self.window}",          f"{type[:1].upper()}{type[1:]}"))

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
                # Hide input
                self.linePass.setEchoMode(QLineEdit.EchoMode.Password)

            # Add elements to vertical layout
            self.layoutCred.addWidget(self.lblPass)
            self.layoutCred.addWidget(self.linePass)

            # Fix tab order
            self.window.setTabOrder(self.lineUser, self.linePass)

            # Set login text and translations
            # Add a red * character at the end of required fields
            self.lblPass.setText(self.translate(f"{self.window}",             self.mandatory_field("Password")))
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

            # Fix tab order
            self.window.setTabOrder(self.lineEmail, self.lineUser)
            self.lineEmail.setFocus()

            # Set registration text and translations        
            self.lblEmail.setText(self.translate(f"{self.window}",                  self.mandatory_field("Email")))
            self.lineEmail.setPlaceholderText(self.translate(f"{self.window}",      "email"))
            self.lblPassCreate.setText(self.translate(f"{self.window}",             self.mandatory_field("Create password")))
            self.linePassCreate.setPlaceholderText(self.translate(f"{self.window}", "password"))
            self.pbtnToggleVis.setToolTip(self.translate(f"{self.window}",          "show/hide password"))
            self.pbtnToggleVis.setText(self.translate(f"{self.window}",             "..."))
            self.lblPassConf.setText(self.translate(f"{self.window}",               self.mandatory_field("Confirm password")))
            self.linePassConf.setPlaceholderText(self.translate(f"{self.window}",   "password"))


    # ---------------------------------------------------------------    
    # Craete redirect widgets
    # ---------------------------------------------------------------
    def add_redirect_label(self, redirect_to='signup'):
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
            # Cursor Change
            self.lblRedirect.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
 
        # Add to main layout
        self.layoutMain  .addWidget(self.frmRedirect, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.hboxRedirect.addWidget(self.lblAskAcc)
        self.hboxRedirect.addWidget(self.lblRedirect) 

        # Add to tab order
        self.window.setTabOrder(self.btnConfirm, self.lblRedirect)

        # Set text and translations
        descRedirect = "Don't have an account?" if redirect_to == 'signup' else "Already have an account?"
        linkRedirect = "Sign Up"                if redirect_to == 'signup' else "Log in"

        self.lblAskAcc  .setText(self.translate(f"{self.window}", descRedirect))
        self.lblRedirect.setText(self.translate(f"{self.window}", linkRedirect))


    # ---------------------------------------------------------------     
    # Create an error label
    # ---------------------------------------------------------------  
    def _set_error_label(self):

        self.lblErrors = QLabel(parent=self.centralwidget)
        if True:
            # Styling (set id to reference in style sheet)
            self.lblErrors.setObjectName('lblError')
            # Hide by default
            self.lblErrors.setVisible(False)

        self.layoutMain.addWidget(self.lblErrors, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        
        # Set text and translation
        self.lblErrors.setText(self.translate(f"{self.window}", "Error messages go here"))
    

    # ---------------------------------------------------------------
    # Returns provided string with a highlighted '*' after it
    # ---------------------------------------------------------------
    def mandatory_field(self, text):
        return f"<html><head/><body><p>{text}<span style=\" color:{self.app.color_highlight};\">*</span></p></body></html>"


    # ---------------------------------------------------------------
    # Add titles for widgets and ensure they 
    # translate to the user's set langauge
    # (Given that a translation file is created and set)
    # ---------------------------------------------------------------
    def translate(self, window, text) -> QtCore.QCoreApplication.translate:
        self.translate = QtCore.QCoreApplication.translate

        return self.translate(window, text)