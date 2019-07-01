from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class helloPy(QDialog):
    def __init__(self): # initializing or calling the constractor
        QDialog.__init__(self)
       # super(helloPy, self).__init__()
        # super is the same as previous line

        #layout = QVBoxLayout()
        #layout = QHBoxLayout()
        layout = QGridLayout()

        self.label = QLabel("HELLO MURIUNGI")
        lineEdit = QLineEdit()
        button = QPushButton("CLOSE")

        layout.addWidget(self.label, 0, 0)
        layout.addWidget(lineEdit, 0, 1)
        layout.addWidget(button, 1, 1)

        self.setLayout(layout)

        button.clicked.connect(self.close)
        lineEdit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self, text):
        self.label.setText(text)

app = QApplication(sys.argv)
dialog = helloPy()
dialog.show()
sys.exit(app.exec_())