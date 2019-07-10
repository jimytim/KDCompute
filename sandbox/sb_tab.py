import pandas as pd
from functools import partial
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, 
    QGroupBox, QLabel, QLineEdit, QPushButton, QSpinBox)

from sb_dataframe_widget import DataFrameWidget

class Tab(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.name = "NewTab"
        self.df = self.create_data()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.df_widget = DataFrameWidget(self.df)

        self.v_layout.addStretch()
        self.v_layout.addWidget(self.df_widget)
        self.v_layout.addStretch()

        self.h_layout.addStretch()
        self.h_layout.addLayout(self.v_layout)
        self.h_layout.addStretch()
        self.setLayout(self.h_layout)

    def create_data(self):
        df = pd.DataFrame({"Kills":[500,510], "Deaths":[249,255]}, index=["Before", "After"])
        df["K/D"] = (df.Kills / df.Deaths).round(7)
        df["K/D rounded"] = df["K/D"].round(2)
        return df