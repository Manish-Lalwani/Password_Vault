
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


app = QApplication([])
dlg = uic.loadUi("gui.ui")

dlg.show()
app.exec()
