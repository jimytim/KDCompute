import sys
from PySide2.QtCore import Slot
from PySide2.QtWidgets import (QMainWindow, QDialog, QFormLayout, QSpinBox, QAction, 
                                QTabWidget, QDesktopWidget, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self, widget_tabs):
        self.width = 800
        self.height = 450

        QMainWindow.__init__(self)
        self.setWindowTitle("KD Analysis")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        init_action = QAction("Initialize", self)
        init_action.setShortcut("Ctrl+I")
        init_action.triggered.connect(self.initialize_stats)

        self.file_menu.addAction(init_action)

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
    def initialize_stats(self):
        dialog = QDialog()
        dialog_layout = QFormLayout()
        kill_spinbox, death_spinbox = QSpinBox(), QSpinBox()
        dialog_layout.addRow("Kills", kill_spinbox)
        dialog_layout.addRow("Deaths", death_spinbox)
        dialog.addLayout = dialog_layout
        dialog.exec()
        # self.messageBox = QMessageBox()
        # self.messageBox.setText("You're about to initialize me!")
        # self.messageBox.exec()