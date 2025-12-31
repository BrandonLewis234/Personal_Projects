###############################################################
#
#
#                overrides.py
#
#         Author: Brandon Lewis
#           Date: 10/4/2025
#        Updated: 10/4/2025
#
#        Summary: Provides overrides for existing PyQt6 widgets
#
#
#
#
################################################################


from PyQt6.QtWidgets import QLabel, QApplication
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QCursor, QKeyEvent

# ---------------------------------------------------------------
# When the user clicks on lblLogin:
# Redirect the user to the login form to login 
# instead of signing in
# ---------------------------------------------------------------
class clickableLabel(QLabel):
        def __init__(self, root, app, type='login'):
                QLabel.__init__(self)
                self.root   = root
                self.app    = app
                self.type   = type
                
                # Enable focus
                # src: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget.focusPolicy
                self.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        # src: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget.keyReleaseEvent
        def keyReleaseEvent(self, event: QKeyEvent):
               # src: https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.Key
               if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
                      self.activate()
        def mouseReleaseEvent(self, event):
                self.activate()

        def activate(self):
                self.point = QCursor.pos()
                if self.type == 'login':

                   from loginform import winLogin
                   # Spawn a login window
                   self.winLogin = winLogin(self.app, position=self.point)
                   self.winLogin.show()
                   # And destroy the signup window
                   self.root.destroy()
                elif self.type == 'signup':

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
        def __init__(self, parent, position, adjustments=[0,0]):
                screen = QApplication.screenAt(position)
                screenGeometry = screen.geometry()

                # Calculate top-left corner so bottom-right aligns with cursor
                x = position.x() - parent.width() + adjustments[0]
                y = position.y() - parent.height() + adjustments[1]

                # Clamp to screen bounds
                x = max(x, screenGeometry.left())
                y = max(y, screenGeometry.top())

                parent.move(QPoint(x, y))