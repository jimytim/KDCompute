import pandas as pd
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, 
    QGroupBox, QLabel, QLineEdit, QPushButton, QSpinBox)

from dataframe_widget import DataFrameWidget

class StatTab(QWidget):
    def __init__(self, tab_name):
        QWidget.__init__(self)
        self.name = tab_name
        self.layout = QVBoxLayout()

        #Goal
        goal_label = QLabel("Your goal")
        goal_input = QLineEdit()
        goal_layout = QHBoxLayout()
        goal_layout.addStretch()
        goal_layout.addWidget(goal_label)
        goal_layout.addWidget(goal_input)
        goal_layout.addStretch()

        # Game input
        input_box = QGroupBox("New Game")
        input_box_layout = QHBoxLayout()
        kill_input = QSpinBox()
        death_input = QSpinBox()
        KD_display = QLineEdit()
        KD_rounded_display = QLineEdit()
        KD_display_style = """QLineEdit {border: 1px solid silver; color: black; background-color: LightGray;}"""
        KD_display.setStyleSheet(KD_display_style)
        KD_rounded_display.setStyleSheet(KD_display_style)
        KD_rounded_display.setReadOnly(True)
        KD_display.setReadOnly(True)
        input_box_layout.addWidget(kill_input)
        input_box_layout.addWidget(QLabel("Kills"))
        input_box_layout.addStretch()
        input_box_layout.addWidget(death_input)
        input_box_layout.addWidget(QLabel("Deaths"))
        input_box_layout.addStretch()
        input_box_layout.addWidget(KD_display)
        input_box_layout.addWidget(QLabel("K/D"))
        input_box_layout.addStretch()
        input_box_layout.addWidget(KD_rounded_display)
        input_box_layout.addWidget(QLabel("K/D rounded"))
        input_box.setLayout(input_box_layout)

        # Stats display
        stats_box = QGroupBox("Stats")
        stats_box_layout = QVBoxLayout()
        stats_box_df_layout = QHBoxLayout()
        stats_box_progression_layout = QHBoxLayout()

        stats_box_df_layout.addStretch(0)
        stats_df = pd.DataFrame({"Kills":[500,510], "Deaths":[250,255]}, index=["Before", "After"])
        stats_df["K/D"] = stats_df.Kills / stats_df.Deaths
        stats_df["K/D rounded"] = stats_df["K/D"].round(2)
        stats_df_widget = DataFrameWidget(stats_df)
        stats_box_df_layout.addWidget(stats_df_widget, stretch=2)
        stats_box_df_layout.addStretch(0)
        
        
        progression_display = QLineEdit()
        KD_difference_display = QLineEdit()
        progression_display.setReadOnly(True)
        KD_difference_display.setReadOnly(True)
        stats_box_progression_layout.addWidget(QLabel("Last game progression"))
        stats_box_progression_layout.addWidget(progression_display)
        stats_box_progression_layout.addWidget(QLabel("K/D Difference"))
        stats_box_progression_layout.addWidget(KD_difference_display)

        stats_box_layout.addLayout(stats_box_df_layout,stretch=1)
        stats_box_layout.addLayout(stats_box_progression_layout,stretch=1)
        stats_box.setLayout(stats_box_layout)

        # Save Game button
        save_game_button = QPushButton("Save Game")
        save_game_layout = QHBoxLayout()
        save_game_layout.addStretch()
        save_game_layout.addWidget(save_game_button)


        self.layout.addLayout(goal_layout)
        self.layout.addWidget(input_box)
        self.layout.addStretch()
        self.layout.addWidget(stats_box)
        self.layout.addLayout(save_game_layout)
        self.setLayout(self.layout)

