import sys
from PySide2.QtCore import Slot
from PySide2.QtWidgets import (QMainWindow, QAction, QTabWidget, QDesktopWidget, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self, stats_widget=None, records_widget=None, analysis_widget=None):
        self.width = 800
        self.height = 450

        QMainWindow.__init__(self)
        self.setWindowTitle("KD Analysis")

        # Creating tabs
        tabWidget = QTabWidget()
        if stats_widget is not None:
            self.stats_widget = stats_widget
            tabWidget.addTab(stats_widget, stats_widget.name)
        if records_widget is not None:
            self.records_widget = records_widget
            tabWidget.addTab(records_widget, records_widget.name)
        if analysis_widget is not None:
            self.analysis_widget = analysis_widget
            tabWidget.addTab(analysis_widget, analysis_widget.name)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        if self.stats_widget is not None:
            init_action = QAction("Initialize", self)
            init_action.setShortcut("Ctrl+I")
            init_action.triggered.connect(self.stats_widget.exec_init_input_dialog)
            self.file_menu.addAction(init_action)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("Ready")
        
        # Window dimensions
        # self.setFixedSize(self.width, self.height)
        self.setCentralWidget(tabWidget)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())