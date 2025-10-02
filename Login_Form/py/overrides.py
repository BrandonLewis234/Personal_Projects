from PyQt6.QtWidgets import QLabel, QApplication
from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QCursor

# ---------------------------------------------------------------
# When the user clicks on lblLogin:
# Redirect the user to the login form to login 
# instead of signing in
# ---------------------------------------------------------------
class clickableLabel(QLabel):
        def __init__(self, root, app, type=0):
                QLabel.__init__(self)
                self.root   = root
                self.app    = app
                self.type   = type

        def mousePressEvent(self, event):
                self.point = QCursor.pos()
                if self.type == 0:
                   from loginform import winLogin
                   # Spawn a login window
                   self.winLogin = winLogin(self.app, position=self.point)
                   self.winLogin.show()
                   # And destroy the signup window
                   self.root.destroy()
                elif self.type == 1:
                   from registerform import winRegister
                   # Spawn a signup window
                   self.winRegister = winRegister(self.app, position=self.point)
                   self.winRegister.show()
                   # And destroy the login window
                   self.root.destroy()


# ---------------------------------------------------------------
# Set position of window based on mouse position, plus offset
# ---------------------------------------------------------------
class set_position():
        def __init__(self, parent, position):
                screen = QApplication.screenAt(position)
                screenGeometry = screen.geometry()

                # Calculate top-left corner so bottom-right aligns with cursor
                x = position.x() - parent.width() + 100
                y = position.y() - parent.height() + 20

                # Clamp to screen bounds
                x = max(x, screenGeometry.left())
                y = max(y, screenGeometry.top())

                parent.move(QPoint(x, y))