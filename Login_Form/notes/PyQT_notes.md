###### **Keybinds**

Ctrl + R : Window Preview



**To convert from ui to py:**

pyuic6 -x layout.ui -o layout.py

might have to instead use:

C:\\Python\\Python311\\python.exe -m PyQt6.uic.pyuic layout.ui -o layout.py



**To make translations work:**

(Replace de (german) for any other select languages)

pylupdate5 loginform.py -ts winLogin\_de.ts 

