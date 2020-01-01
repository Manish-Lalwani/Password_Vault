
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

class GUIApp:
	def __init__(self,ui_filepath):
		self.ui_filepath = ui_filepath

		app = QApplication([])
		dlg = uic.loadUi(self.ui_filepath)
		dlg.show()
		app.exec()



if __name__ == "__main__":
	gui_obj = GUIApp("gui.ui")
