from PySide2.QtGui import QColor
from PySide2.QtCore import (QAbstractTableModel, QModelIndex, Qt)
from PySide2.QtWidgets import (QHBoxLayout, QHeaderView, QSizePolicy, QAbstractItemView, QTableView, QWidget)

class CustomTableModel(QAbstractTableModel):
    def __init__(self, df=None):
        QAbstractTableModel.__init__(self)
        self.df = df

    def rowCount(self, parent=QModelIndex()):
        return self.df.shape[0]

    def columnCount(self, parent=QModelIndex()):
        return self.df.shape[1]

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return str(self.df.columns[section])
        elif orientation == Qt.Vertical:
            return str(self.df.index[section])

    def data(self, index, role = Qt.DisplayRole):
        row = index.row()
        column = index.column()
        
        if role == Qt.DisplayRole:
            return str(self.df.iloc[row,column])
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        return None

class DataFrameWidget(QTableView):
    def __init__(self, df):
        QTableView.__init__(self)

        # Getting the Model
        self.model = CustomTableModel(df)
        self.setModel(self.model)

        # QTableView Headers
        self.horizontal_header = self.horizontalHeader()
        self.vertical_header = self.verticalHeader()
        self.horizontal_header.setSectionResizeMode(QHeaderView.Stretch)
        self.vertical_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        # self.verticalResizeTableViewToContents()
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)


    def verticalResizeTableViewToContents(self):
        print("Resizing the stats table..")
        height = 0
        row_count = self.vertical_header.count()
        print("Number of rows = {}".format(row_count))
        for i in range(row_count):
            if not self.vertical_header.isSectionHidden(i):
                row_height = self.vertical_header.sectionSizeHint(i)
                print("The row {} has this size = {}".format(i, row_height))
                height += row_height

        print("Height sum = {}".format(height))

        # if not self.horizontalScrollBar.isHidden():
        #     height += self.horizontalScrollBar().height()

        # if not self.horizontal_header.isHidden():
        #     height += self.horizontal_header().height()
        
        # self.setMinimumHeight(height)
