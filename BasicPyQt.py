from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


app = QApplication(sys.argv)
dialog = QDialog()
dialog.show()
sys.exit(app.exec_())