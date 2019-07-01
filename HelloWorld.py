from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QHBoxLayout()

        self.MyLabel = QLabel("Hello World")
        MyLineEdit = QLineEdit()
        MyButton = QPushButton("Close")

        layout.addwidget(self.MyLabel)
        layout.addwidget(MyLineEdit)
        layout.addwidget(MyButton)

        self.setLayout(layout)

        MyButton.clicked.connect(self.close)
        MyLineEdit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self, text):
        self.MyLabel.setText(text)

app = QApplication(sys.argv)
dialog = QDialog()
dialog.show()
app.exec_()   #sys.exit(app.exec_())
