import sys

from PySide2.QtCore import QDateTime, QTimeZone
from PySide2.QtWidgets import QApplication

from main_window import MainWindow
from stats import StatTab

if __name__ == "__main__":

    # Qt Application
    app = QApplication(sys.argv)

    # Tab creation
    stat_widget = StatTab("Stats")
    # QMainWindow using QWidget as central widget
    window = MainWindow([stat_widget])

    window.show()
    sys.exit(app.exec_())
