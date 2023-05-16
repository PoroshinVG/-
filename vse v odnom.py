import sys
import random
from PyQt6.QtWidgets import QApplication,QWidget, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QRadioButton
from PyQt6.QtCore import QTimer, Qt  

#окно авторизации
class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(320, 200)
        self.setWindowTitle("Войти")

        self.first_lbl = QLabel("Логин")
       # self.first_lbl.setAlignment(Qt.Alignmentflag.Center)
        self.first_lineEdit = QLineEdit()
        self.first_lb2 = QLabel("Пароль")
        self.first_lineEdit2 = QLineEdit()

        self.btn = QPushButton("Вход")
        self.btn2 = QPushButton("Выход")
        self.btn2.clicked.connect(self.exit)
        self.btn.clicked.connect(self.btn_clicked)
        self.layout = QVBoxLayout()
        widget = QWidget()

        self.layout.addWidget(self.first_lbl)
        self.layout.addWidget(self.first_lineEdit)
        self.layout.addWidget(self.first_lb2)
        self.layout.addWidget(self.first_lineEdit2)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn2)
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn2)

    def btn_clicked(self):
        self.window2 = Test_Window0()
        if self.first_lineEdit.text() == "1" and self.first_lineEdit2.text() == "1":
            self.window2.show()

        else:
            self.kapcha = Kapcha_Window0()
            self.kapcha.show()
            
    def exit(self):
        self.close()

#капча
#доделать модальное окно
class Kapcha_Window0(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowModality(Qt.WindowModality.ApplicationModal)
            self.setWindowTitle("Kapcha")
            self.resize(640, 480)
            self.rnd = random.randint(1111,9999)
            self.first_lbl = QLabel("введите цифры")
            self.first_lineEdit = QLineEdit()
            self.second_lbl = QLabel(str(self.rnd))
            self.btn = QPushButton("Continue")
            self.btn.clicked.connect(self.btn_clicked)
            
#таймер
            self.timer_label = QLabel("Таймер:")
            self.timer = QTimer()
            self.timer_counter = 11
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.timer_tick)
            
            self.layout = QVBoxLayout()
            widget = QWidget()
            
            self.layout.addWidget(self.first_lbl)
            self.layout.addWidget(self.timer_label)
            self.layout.addWidget(self.first_lineEdit)
            self.layout.addWidget(self.second_lbl)
            self.layout.addWidget(self.btn)
            self.setCentralWidget(widget)
            widget.setLayout(self.layout)
            
        def btn_clicked(self):
            if self.first_lineEdit.text() == self.second_lbl.text():
                self.close()
            else:
                self.timer.start()
                self.btn.setEnabled(False)
                
        def timer_start(self):
            self.timer_counter = 11
            self.timer.start()
        
        def timer_tick(self):
            self.timer.start(1000)
            self.timer_counter -= 1
            self.timer_label.setText(f"Блокировка {self.timer_counter}")
            
            if  self.timer_counter == 0:
                self.timer.stop()
                self.timer_counter = 4
                self.btn.setEnabled(True)
                rnd = random.randint(1111,9999)
                self.second_lbl.setText(str(rnd))    
            
        
#тест
class Test_Window0(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640, 480)
        self.question_label = QLabel(self)
        self.answer1_radio = QRadioButton(self)
        self.answer2_radio = QRadioButton(self)
        self.answer3_radio = QRadioButton(self)
        self.check_button = QPushButton(self)
        self.check_button2 = QPushButton(self)
        self.check_button3 = QPushButton(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Тест ")

        self.question_label.setGeometry(50, 50, 500, 100)
        self.question_label.setText('Вопрос 1: ...')
        self.question_label.setWordWrap(True)

        self.answer1_radio.setGeometry(100, 150, 400, 30)
        self.answer1_radio.setText('...')
        self.answer1_radio.setChecked(False)

        self.answer2_radio.setGeometry(100, 200, 400, 30)
        self.answer2_radio.setText('...')
        self.answer2_radio.setChecked(False)

        self.answer3_radio.setGeometry(100, 250, 400, 30)
        self.answer3_radio.setText('...')
        self.answer3_radio.setChecked(False)

        self.check_button.setGeometry(200, 350, 200, 30)
        self.check_button.setText('Проверить')
        self.check_button2.setGeometry(0, 350, 250, 30)
        self.check_button2.setText('Назад')
        self.check_button3.setGeometry(400, 350, 250, 30)
        self.check_button3.setText('Далее')
        self.check_button.clicked.connect(self.checkAnswer)
        
    def checkAnswer(self):
        if self.answer2_radio.isChecked():
            self.question_label.setText('Ответ верный!')
        else:
            self.question_label.setText('Ответ неверный!')
        



      
app = QApplication(sys.argv)
#css
app.setStyleSheet("""
                  QWidget {
        background-color: "lightblue";
        color: "black";
    }
    QPushButton {
        font-size: 16px;
        background-color: "indigo";
    }
    QLineEdit {
        background-color: "black";
        color: "black";
                  
                  
                  #""") 
first_window = Main_Window()
Second_window = Kapcha_Window0()
Fourth_window = Test_Window0()
first_window.show()
app.exec()
