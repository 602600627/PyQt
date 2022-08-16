from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeView, QDirModel


class QTreeViewDemo(QMainWindow):
    def __init__(self):
        super(QTreeViewDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QtreeView")
        self.resize(500, 300)

        self.treeView = QTreeView(self)
        model = QDirModel()
        print(model)
        self.treeView.setModel(model)
        self.setCentralWidget(self.treeView)


if __name__ == '__main__':
    app = QApplication([])
    window = QTreeViewDemo()
    window.show()
    app.exec_()
