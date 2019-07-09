from PySide2.QtCore import Slot, qApp
from PySide2.QtWidgets import (QMainWindow, QAction, QTabWidget, QDesktopWidget)

class MainWindow(QMainWindow):
    def __init__(self, widget_tabs):
        self.width = 800
        self.height = 450

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

        # Creating tabs
        tabWidget = QTabWidget()
        for widget_tab in widget_tabs:
            tabWidget.addTab(widget_tab, widget_tab.name)

        # Window dimensions
        # self.setFixedSize(self.width, self.height)
        self.setCentralWidget(tabWidget)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @Slot()
    def exit_app(self, checked):
        sys.exit()
