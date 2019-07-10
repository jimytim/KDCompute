import sys

from PySide2.QtCore import QDateTime, QTimeZone
from PySide2.QtWidgets import QApplication

from sb_main_window import MainWindow
from sb_tab import Tab

if __name__ == "__main__":

    # Qt Application
    app = QApplication(sys.argv)

    table_tab = Tab()
    # QMainWindow using QWidget as central widget
    window = MainWindow([table_tab])

    window.show()
    sys.exit(app.exec_())
