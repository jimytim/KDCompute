import sys

from PySide2.QtCore import QDateTime, QTimeZone
from PySide2.QtWidgets import QApplication

from main_window import MainWindow
from tabs import TabWidget

if __name__ == "__main__":

    # Qt Application
    app = QApplication(sys.argv)

    # QWidget
    tab_widget = TabWidget()
    # QMainWindow using QWidget as central widget
    window = MainWindow(tab_widget)

    window.show()
    sys.exit(app.exec_())
