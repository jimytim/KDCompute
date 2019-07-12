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
        self.vertical_header.setSectionResizeMode(QHeaderView.Fixed)
        self.vertical_header.setDefaultSectionSize(19)
        # self.verticalResizeTableViewToContents()
        # self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.setMinimumWidth(400)
        self.setMaximumWidth(400)
        self.setMinimumHeight(59)
        self.setMaximumHeight(59)

    def showSizeInfo(self):
        print("Widget minimum size => MinimumHeight  = {} | MinimumWidth  = {}".format(self.minimumHeight(), self.minimumWidth()))
        print("Widget maximum size => MaximumHeight  = {} | MaximumWidth  = {}".format(self.maximumHeight(), self.maximumWidth()))
        print("MininumSectionSize: H -> {} | V -> {}".\
            format(self.horizontal_header.minimumSectionSize(), self.vertical_header.minimumSectionSize()))
        print("MaximumSectionSize : H -> {} | V -> {}".\
            format(self.horizontal_header.maximumSectionSize(), self.vertical_header.maximumSectionSize()))
        print("defaultSectionSize: H -> {} | V -> {}".\
            format(self.horizontal_header.defaultSectionSize(), self.vertical_header.defaultSectionSize()))
        print("Horizontal header: count = {}, length = {}".\
            format(self.horizontal_header.count(), self.horizontal_header.length()))
        print("Vertical header:   count = {}, length = {}".\
            format(self.vertical_header.count(), self.vertical_header.length()))
        print("Horizontal section sizes = {}".format([self.horizontal_header.sectionSize(i) for i in range(self.horizontal_header.count())]))
        print("Vertical section sizes   = {}".format([self.vertical_header.sectionSize(i) for i in range(self.vertical_header.count())]))
        print("Horizontal section size hints = {}".format([self.horizontal_header.sectionSizeHint(i) for i in range(self.horizontal_header.count())]))
        print("Vertical section sizes hints  = {}".format([self.vertical_header.sectionSizeHint(i) for i in range(self.vertical_header.count())]))
        print("Horizontal section size contents = {}".format([self.horizontal_header.sectionSizeFromContents(i).toTuple() for i in range(self.horizontal_header.count())]))
        print("Vertical section sizes contents  = {}".format([self.vertical_header.sectionSizeFromContents(i).toTuple() for i in range(self.vertical_header.count())]))
        
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
