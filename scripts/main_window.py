from PySide2.QtCore import Slot, qApp
from PySide2.QtWidgets import QMainWindow, QAction

class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("KD Analysis")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("Ready")

        # Window dimensions
        geometry = qApp.desktop().availableGeometry(self)
        print("Available geometry: {}".format(geometry))
        print("Available Width: {}\nAvailable Height: {}".format(geometry.width(), geometry.height()))
        self.width = 800
        self.height = 600
        self.setGeometry(geometry.width()//2 - self.width//2, 
                         geometry.height()//2 - self.height//2, 
                         self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self, checked):
        sys.exit()
