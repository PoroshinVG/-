import sys
import random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import * 

#окно авторизации(1)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(320, 200)
        self.setWindowTitle("Войти")

        self.first_lbl = QLabel("Логин")
        self.first_lineEdit = QLineEdit()
        self.first_lb2 = QLabel("Пароль")
        self.first_lineEdit2 = QLineEdit()

        self.btn = QPushButton("Вход")
        self.btn2 = QPushButton("Выход")
        self.btn.clicked.connect(self.btn_clicked)
        self.btn2.clicked.connect(self.exit)
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
    #кнопки действия
    def btn_clicked(self):
        self.window2 = TestWindow()
        if self.first_lineEdit.text() == "user" and self.first_lineEdit2.text() == "user":
            self.window2.show()
        
        else:
            self.kapcha = KapchaWindow()
            self.kapcha.show()
            
    def exit(self):
        self.close()

#капча(2)
class KapchaWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Kapcha")
            self.resize(320, 240)
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
        #кнопка в два действия
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
            self.timer_label.setText(f"Блокировка: {self.timer_counter}")
            
            if  self.timer_counter == 0:
                self.timer.stop()
                self.timer_counter = 4
                self.btn.setEnabled(True)
                rnd = random.randint(1111,9999)
                self.second_lbl.setText(str(rnd))      
#тест(3)
class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Самый лёгкий тест")
        self.setFixedSize(600,240)
        #инициалы 
        self.name = QLabel("Введите ФИО")
        self.edit = QLineEdit()
        box = QVBoxLayout()
        wid = QWidget()
        wid.setLayout(box)
        box.addWidget(self.name)
        box.addWidget(self.edit)
        
        #сам тест :3
        lbl1 = QLabel("1. Что такое CS 1.6 ?")
        rb1_0 = QRadioButton(text="Отдельная игра")
        rb2_0 = QRadioButton(text="Чисто в компьютерном под пивко с мужиками покатать")
        self.rb3_0 = QRadioButton(text="Мод для культовой игры Half life")
        vbox = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(vbox)
        vbox.addWidget(lbl1)
        vbox.addWidget(rb2_0)
        vbox.addWidget(rb1_0)
        vbox.addWidget(self.rb3_0)
        
        lbl2 = QLabel("2. Почему Valve пришлось почти полностью переделывать Half Life:2 ?")
        self.rb1_1 = QRadioButton(text="Из-за взлома и утечки данных своих серверов")
        rb2_1 = QRadioButton(text="Проект был не готов к выходу")
        rb3_1 = QRadioButton(text="Гейб любит Макдональдс")
        vbox2 = QVBoxLayout()
        widget2 = QWidget()
        widget2.setLayout(vbox2)
        vbox2.addWidget(lbl2)
        vbox2.addWidget(self.rb1_1)
        vbox2.addWidget(rb2_1)
        vbox2.addWidget(rb3_1)

        lbl3 = QLabel("3. На каком движке делали проекты Valve ?")
        rb1_2 = QRadioButton(text="CryEngine")
        self.rb2_2 = QRadioButton(text="Source")
        rb3_2 = QRadioButton(text="Не шарю")
        vbox3 = QVBoxLayout()
        widget3 = QWidget()
        widget3.setLayout(vbox3)
        vbox3.addWidget(lbl3)
        vbox3.addWidget(rb1_2)
        vbox3.addWidget(self.rb2_2)
        vbox3.addWidget(rb3_2)

        lbl4 = QLabel("4. Зачем Valve создаёт свою ОС на ядре Linux и выпускает свою продукцию и оптимизацию ?")
        rb1_3 = QRadioButton(text="Ради денег")
        rb2_3 = QRadioButton(text="Хочу Жрать")
        self.rb3_3 = QRadioButton(text="Чтобы доказать что Linux тоже могёт и работает не хуже шиндовс")
        vbox4 = QVBoxLayout()
        widget4 = QWidget()
        widget4.setLayout(vbox4)
        vbox4.addWidget(lbl4)
        vbox4.addWidget(rb1_3)
        vbox4.addWidget(rb2_3)
        vbox4.addWidget(self.rb3_3)

        lbl5 = QLabel("5. Почему в этом году Valve решают разработать CS:2 ?")
        rb1_4 = QRadioButton(text="Чтобы заработать больше денег с людей, которые будут тратить всю жизнь на эту игру")
        self.rb2_4 = QRadioButton(text="Чтобы залатать баги и прочие дыры CS:GO и старой версии движка Source")
        rb3_4 = QRadioButton(text="Чтобы порадовать фанатов новой частью")
        vbox5 = QVBoxLayout()
        widget5 = QWidget()
        widget5.setLayout(vbox5)
        vbox5.addWidget(lbl5)
        vbox5.addWidget(rb1_4)
        vbox5.addWidget(self.rb2_4)
        vbox5.addWidget(rb3_4)

        #табель результатов
        lbl6 = QLabel("Показать результаты?")
        lbl6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rb3_5 = QPushButton("Да")
        rb3_5.clicked.connect(self.activate_plus)
        rb3_5.clicked.connect(self.results)
        vbox6 = QVBoxLayout()
        widget6 = QWidget()
        widget6.setLayout(vbox6)
        vbox6.addWidget(lbl6)
        vbox6.addWidget(rb3_5)


        lbl7 = QLabel("Результаты теста:")
        self.v6 = QLabel()
        self.v2 = QLabel()
        self.v3 = QLabel()
        self.v4 = QLabel()
        self.v5 = QLabel()
        self.res = QLabel()
        vbox7 = QVBoxLayout()
        widget7 = QWidget()
        widget7.setLayout(vbox7)
        vbox7.addWidget(lbl7)
        vbox7.addWidget(self.v6)
        vbox7.addWidget(self.v2)
        vbox7.addWidget(self.v3)
        vbox7.addWidget(self.v4)
        vbox7.addWidget(self.v5)
        vbox7.addWidget(self.res)
        btn_save = QPushButton("Сохранить")
        btn_save.clicked.connect(self.save)
        vbox7.addWidget(btn_save)


        pagelayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(self.stacklayout)
        pagelayout.addLayout(self.button_layout)

        self.btnB = QPushButton("Назад")
        self.btnA = QPushButton("Вперёд")

        self.btnB.clicked.connect(self.activate_minus)
        self.btnA.clicked.connect(self.activate_plus)
        self.stacklayout.addWidget(wid)
        self.button_layout.addWidget(self.btnB)
        self.button_layout.addWidget(self.btnA)
        self.stacklayout.addWidget(widget)
        self.stacklayout.addWidget(widget2)
        self.stacklayout.addWidget(widget3)
        self.stacklayout.addWidget(widget4)
        self.stacklayout.addWidget(widget5)
        self.stacklayout.addWidget(widget6)
        self.stacklayout.addWidget(widget7)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)
    #функция начисления/вычисления
    def activate_plus(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()+1)



    def activate_minus(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()-1)
        
    #ответы
    def results(self):
        if self.rb3_0.isChecked():
            self.v6.setText("1.Верно")
            a = 1
        else:
            self.v6.setText("1.Не верно")
            a = 0
        if self.rb1_1.isChecked():
            self.v2.setText("2.Верно")
            b = a + 1
        else:
            self.v2.setText("2.Не верно")
            b = a
        if self.rb2_2.isChecked():
            self.v3.setText("3.Верно")
            t = b + 1
        else:
            self.v3.setText("3.Не верно")
            t = b
        if self.rb3_3.isChecked():
            self.v4.setText("4.Верно")
            d = t + 1
        else:
            self.v4.setText("4.Не верно")
            d = t
        if self.rb2_4.isChecked():
            self.v5.setText("5.Верно")
            self.e = d + 1
        else:
            self.v5.setText("5.Не верно")
            self.e = d

        self.setFixedSize(600, 240)
        self.res.setText(f"Ваш результат:{self.e}")
    def save(self):
        info = f"ФИО:{self.edit.text()} \n"
        txt = f"{self.v6.text()} \n"
        txt1 = f"{self.v2.text()} \n"
        txt2 = f"{self.v3.text()} \n"
        txt3 = f"{self.v4.text()} \n"
        txt4 = f"{self.v5.text()} \n"
        txt5 = f"Ваша оценка:{self.e} \n"

        with open("РЕЗУЛЬТАТЫ.txt", "w", encoding="utf-8") as f:
            f.write(info)
            f.write(txt)
            f.write(txt1)
            f.write(txt2)
            f.write(txt3)
            f.write(txt4)
            f.write(txt5)

app = QApplication(sys.argv)
#стильШИИИИТ
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
first_window = MainWindow()
Second_window = KapchaWindow()
Third_window = TestWindow()
first_window.show()
app.exec()
