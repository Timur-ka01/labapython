import sys
from PySide6.QtWidgets import *
from calculations.models import Room, Apartment, Building
from calculations.area import square
from calculations.heat import power

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 450)
        self.setWindowTitle("Лаба 7")
        
        w = QWidget()
        self.setCentralWidget(w)
        l = QVBoxLayout(w)
        
        # Радиокнопки
        self.rb = []
        for t in ["Комната", "Квартира", "Дом"]:
            rb = QRadioButton(t)
            rb.toggled.connect(self.switch)
            l.addWidget(rb)
            self.rb.append(rb)
        self.rb[0].setChecked(True)
        
        # Поля ввода
        self.w = QLineEdit(); self.w.setPlaceholderText("Ширина")
        self.l = QLineEdit(); self.l.setPlaceholderText("Длина")
        self.txt = QTextEdit(); self.txt.setPlaceholderText("5 4\n3 2"); self.txt.hide()
        self.f = QLineEdit(); self.f.setPlaceholderText("Этажи"); self.f.hide()
        self.c = QLineEdit(); self.c.setPlaceholderText("Квартир"); self.c.hide()
        self.a = QLineEdit(); self.a.setPlaceholderText("Площадь"); self.a.hide()
        
        for x in [self.w, self.l, self.txt, self.f, self.c, self.a]:
            l.addWidget(x)
        
        QPushButton("Рассчитать").clicked.connect(self.calc).l中添加?实际上需要单独添加按钮, 我修正一下

        # Кнопка
        btn = QPushButton("Рассчитать")
        btn.clicked.connect(self.calc)
        l.addWidget(btn)
        
        self.res = QLabel()
        self.res.setWordWrap(True)
        l.addWidget(self.res)
    
    def switch(self):
        t = [r.isChecked() for r in self.rb]
        self.w.setVisible(t[0])
        self.l.setVisible(t[0])
        self.txt.setVisible(t[1])
        self.f.setVisible(t[2])
        self.c.setVisible(t[2])
        self.a.setVisible(t[2])
    
    def calc(self):
        try:
            if self.rb[0].isChecked():
                obj = Room(float(self.w.text()), float(self.l.text()))
                self.res.setText(f"{obj}\nТепло: {power(obj):.0f} Вт\n__mul__(2): {obj*2}")
            
            elif self.rb[1].isChecked():
                obj = Apartment()
                for line in self.txt.toPlainText().strip().split('\n'):
                    if line.strip():
                        w, l = map(float, line.split())
                        obj.rooms.append(Room(w, l))
                self.res.setText(f"{obj}\nТепло: {power(obj):.0f} Вт\n__len__: {len(obj)}")
            
            else:
                obj = Building()
                side = (float(self.a.text()) ** 0.5)
                for _ in range(int(self.c.text())):
                    apt = Apartment()
                    apt.rooms.append(Room(side, side))
                    obj.apartments.append(apt)
                self.res.setText(f"{obj}\nТепло: {power(obj):.0f} Вт\n__len__: {len(obj)}")
        
        except:
            QMessageBox.critical(self, "Ошибка", "Неверные данные")

app = QApplication(sys.argv)
app.exec_() # В PySide6 запуск немного другой, исправлю

# Правильный запуск:
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())