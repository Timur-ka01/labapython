import sys
from PySide6.QtWidgets import *
from calculations.models import Room, Apartment, Building   


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350, 400)
        
        w = QWidget()
        self.setCentralWidget(w)
        layout = QVBoxLayout(w)
        
        # Радиокнопки
        self.rb1 = QRadioButton("Комната")
        self.rb2 = QRadioButton("Квартира")
        self.rb3 = QRadioButton("Дом")
        
        self.rb1.toggled.connect(self.switch)
        self.rb2.toggled.connect(self.switch)
        self.rb3.toggled.connect(self.switch)
        
        layout.addWidget(self.rb1)
        layout.addWidget(self.rb2)
        layout.addWidget(self.rb3)
        
        # Поля ввода
        self.w = QLineEdit()
        self.w.setPlaceholderText("Ширина")
        layout.addWidget(self.w)
        
        self.l = QLineEdit()
        self.l.setPlaceholderText("Длина")
        layout.addWidget(self.l)
        
        self.txt = QTextEdit()
        self.txt.setPlaceholderText("5 4\n3 2")
        self.txt.hide()
        layout.addWidget(self.txt)
        
        self.c = QLineEdit()
        self.c.setPlaceholderText("Количество квартир")
        self.c.hide()
        layout.addWidget(self.c)
        
        self.a = QLineEdit()
        self.a.setPlaceholderText("Площадь квартиры")
        self.a.hide()
        layout.addWidget(self.a)
        
        # Кнопка и результат
        btn = QPushButton("Рассчитать")
        btn.clicked.connect(self.calc)
        layout.addWidget(btn)
        
        self.res = QLabel()
        self.res.setWordWrap(True)
        layout.addWidget(self.res)
        
        self.rb1.setChecked(True)
        self.switch()
    
    def switch(self):
        # Просто показываем/скрываем поля
        self.w.setVisible(self.rb1.isChecked())
        self.l.setVisible(self.rb1.isChecked())
        self.txt.setVisible(self.rb2.isChecked())
        self.c.setVisible(self.rb3.isChecked())
        self.a.setVisible(self.rb3.isChecked())
    
    def calc(self):
        try:
            if self.rb1.isChecked():  # Комната
                obj = Room(float(self.w.text()), float(self.l.text()))
                self.res.setText(f"{obj}\nТепло: {obj.area() * 100:.0f} Вт\nУмножение: {obj * 2}")
            
            elif self.rb2.isChecked():  # Квартира
                obj = Apartment()
                for line in self.txt.toPlainText().strip().split('\n'):
                    if line.strip():
                        w, l = map(float, line.split())
                        obj.rooms.append(Room(w, l))
                self.res.setText(f"{obj}\nТепло: {obj.area() * 100:.0f} Вт")
            
            else:  # Дом
                obj = Building()
                side = float(self.a.text()) ** 0.5
                for _ in range(int(self.c.text())):
                    apt = Apartment()
                    apt.rooms.append(Room(side, side))
                    obj.apartments.append(apt)
                self.res.setText(f"{obj}\nТепло: {obj.area() * 100:.0f} Вт")
        
        except:
            QMessageBox.critical(self, "Ошибка", "Неверные данные")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())