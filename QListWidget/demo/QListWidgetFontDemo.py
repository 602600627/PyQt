import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QListWidget, QListWidgetItem, QLabel, QHBoxLayout, \
    QPushButton
from PyQt5.uic.properties import QtCore


class QListWidgetFontDemo(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.setupUi(self)

        self.listWidget.clicked.connect(self.tree_item_changed)

    def setupUi(self, widget):
        self.setWindowTitle("QListWidgetFontDem")
        self.resize(640, 480)
        layout = QVBoxLayout()

        self.listWidget = QListWidget()

        for i in range(10):
            item = QListWidgetItem(self.listWidget)
            label = QLabel("Item %d" % i)
            label.setFont(QFont('宋体', 18, QFont.Bold))
            if i % 2 == 0:
                label.setStyleSheet("color:red")
            else:
                label.setStyleSheet("color:green")
            # hbLayout = QHBoxLayout()
            # hbLayout.addWidget(label)
            # _widget = QWidget()
            # _widget.setLayout(hbLayout)
            self.listWidget.setItemWidget(item, label)

        layout.addWidget(self.listWidget)

        clearBtn = QPushButton("清空")
        deleteBtn = QPushButton("删除")
        layout.addWidget(clearBtn)
        layout.addWidget(deleteBtn)

        clearBtn.clicked.connect(self.clearBtn_click)
        deleteBtn.clicked.connect(self.deleteBtn_click)

        self.setLayout(layout)

    def tree_item_changed(self, index):
        currentIndex = self.listWidget.indexWidget(index)
        print(currentIndex.text())
        print(index.row())

    # 清空所有列表
    def clearBtn_click(self):
        self.listWidget.clear()

    # 删除当前列表ITEM
    def deleteBtn_click(self):
        item = self.listWidget.currentItem()
        self.listWidget.removeItemWidget(item)

        # self.listWidget.currentItem().setHidden(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QListWidgetFontDemo()
    window.show()
    sys.exit(app.exec_())
