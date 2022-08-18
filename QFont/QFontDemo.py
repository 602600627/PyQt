from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget


class QFontDemo(QWidget):
    def __init__(self):
        super(QFontDemo, self).__init__()

        self.font = QFont('宋体', 30)
        # self.font.setPixelSize(18)
        # self.font.setBold(True)
        # self.font.setItalic(True)
        layout = QVBoxLayout()

        label = QLabel("Hello World")
        label.setFont(self.font)
        # 设置颜色
        label.setStyleSheet("color:red")
        layout.addWidget(label)

        self.setLayout(layout)
        self.resize(200, 200)


if __name__ == '__main__':
    app = QApplication([])
    window = QFontDemo()
    window.show()
    app.exec_()
