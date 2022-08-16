from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem, QApplication, QPushButton, QWidget, QHBoxLayout, \
    QVBoxLayout


class QTreeWidgetDemo(QMainWindow):
    def __init__(self):
        super(QTreeWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTreeWidget')

        self.tree = QTreeWidget()
        # 设置多少列
        # self.tree.setColumnCount(2)
        # self.tree.setHeaderLabels(['key', 'value'])
        # 隐藏列表头
        self.tree.setHeaderHidden(True)
        root = QTreeWidgetItem(self.tree)
        root.setText(0, '根节点')
        # root.setText(1, '我是value')
        root.setIcon(0, QIcon('../../image/logo.ico'))
        root.setCheckState(0, Qt.Unchecked)
        # 添加子节点
        child = QTreeWidgetItem(root)
        child.setText(0, '子节点')
        child.setCheckState(0, Qt.Unchecked)

        child1 = QTreeWidgetItem(root)
        child1.setText(0, '子节点2')
        child1.setCheckState(0, Qt.Unchecked)

        child_1 = QTreeWidgetItem(child)
        child_1.setText(0, '子子节点1')
        child_1.setIcon(0, QIcon('../../image/logo.ico'))
        child_1.setCheckState(0, Qt.Unchecked)

        addBtn = QPushButton('添加')
        addBtn.clicked.connect(self.addBtn_click)

        removeBtn = QPushButton('删除')
        removeBtn.clicked.connect(self.removeBtn_click)

        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        layout.addWidget(addBtn)
        layout.addWidget(removeBtn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setLayout(layout)
        self.resize(300, 500)

        self.tree.itemChanged.connect(self.handleChanged)
        self.tree.clicked.connect(self.tree_click)

    def handleChanged(self, item, column):
        # print(item.parent().text(0))

        count = item.childCount()
        if item.checkState(column) == Qt.Checked:
            for index in range(count):
                item.child(index).setCheckState(0, Qt.Checked)
        if item.checkState(column) == Qt.Unchecked:
            for index in range(count):
                item.child(index).setCheckState(0, Qt.Unchecked)

    def tree_click(self, index):
        item = self.tree.currentItem()
        print(item.text(0))
        print(index.row(), index.column())

    def addBtn_click(self):
        item = self.tree.currentItem()
        child = QTreeWidgetItem(item)
        child.setText(0, '新增节点')

    def removeBtn_click(self):
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)


if __name__ == '__main__':
    app = QApplication([])
    w = QTreeWidgetDemo()
    w.show()
    app.exec_()
