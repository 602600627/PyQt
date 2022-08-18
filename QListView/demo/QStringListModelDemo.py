from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QListWidget, QListView, QWidget


class QStringListModelDemo(QWidget):
    def __init__(self, parent=None):
        super(QStringListModelDemo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QStringListModel Demo")
        self.resize(640, 480)

        qListView = QListView()
        model = QStringListModel()
        qListView.setModel(model)
        qListView.setFont(QFont('宋体', 18, QFont.Bold))
        qListView.setStyleSheet("color:red")
        # 设置不能编辑
        qListView.setEditTriggers(QListView.NoEditTriggers)

        for i in range(10):
            model.insertRow(i)
            model.setData(model.index(i), 'Item %d' % i)
            model.setObjectName('red')

        layout = QVBoxLayout()
        layout.addWidget(qListView)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])
    window = QStringListModelDemo()
    window.show()
    app.exec_()
