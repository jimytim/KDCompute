import pandas as pd
from functools import partial
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, 
    QGroupBox, QLabel, QLineEdit, QPushButton, QSpinBox)

from dataframe_widget import DataFrameWidget

class StatTab(QWidget):
    def __init__(self, initials_stats):
        QWidget.__init__(self)
        self.name = "Stats"
        self.layout = QVBoxLayout()

        #Goal
        goal_label = QLabel("Your goal")
        goal_input = QLineEdit()
        goal_layout = QHBoxLayout()
        goal_layout.addStretch()
        goal_layout.addWidget(goal_label)
        goal_layout.addWidget(goal_input)
        goal_layout.addStretch()

        input_box = self.create_input_widget()
        stats_box = self.create_stats_widget(initials_stats)

        # Save Game button
        save_game_button = QPushButton("Save Game")
        save_game_layout = QHBoxLayout()
        save_game_layout.addStretch()
        save_game_layout.addWidget(save_game_button)


        self.layout.addLayout(goal_layout)
        self.layout.addWidget(input_box)
        self.layout.addWidget(stats_box)
        self.layout.addLayout(save_game_layout)
        self.layout.addStretch()
        self.setLayout(self.layout)

    def create_input_widget(self):
        input_box = QGroupBox("New Game")
        input_box_layout = QHBoxLayout()

        self.kill_input = QSpinBox()
        self.kill_input.valueChanged.connect(partial(self.stat_input_update, "Kills"))
        self.death_input = QSpinBox()
        self.death_input.valueChanged.connect(partial(self.stat_input_update, "Deaths"))

        self.kd_display = QLineEdit("0")
        self.kd_rounded_display = QLineEdit("0")

        display_style = """QLineEdit {border: 1px solid silver; color: black; background-color: LightGray;}"""
        self.kd_display.setAlignment(Qt.AlignHCenter)
        self.kd_display.setStyleSheet(display_style)
        self.kd_display.setReadOnly(True)
        self.kd_rounded_display.setAlignment(Qt.AlignHCenter)
        self.kd_rounded_display.setStyleSheet(display_style)
        self.kd_rounded_display.setReadOnly(True)
        

        input_box_layout.addWidget(QLabel("Kills"))
        input_box_layout.addWidget(self.kill_input)
        
        input_box_layout.addStretch()

        input_box_layout.addWidget(QLabel("Deaths"))
        input_box_layout.addWidget(self.death_input)
        
        input_box_layout.addStretch()

        input_box_layout.addWidget(QLabel("K/D"))
        input_box_layout.addWidget(self.kd_display)
        
        input_box_layout.addStretch()

        input_box_layout.addWidget(QLabel("K/D rounded"))
        input_box_layout.addWidget(self.kd_rounded_display)
        
        input_box.setLayout(input_box_layout)
        return input_box

    def create_stats_widget(self, initial_stats):
        kills_0, deaths_0 = initial_stats
        stats_box = QGroupBox("Stats")
        stats_box_layout = QVBoxLayout()
        stats_box_df_layout = QHBoxLayout()
        stats_box_progression_layout = QHBoxLayout()

        stats_box_df_layout.addStretch(0)
        stats_df = pd.DataFrame({"Kills":[kills_0,kills_0], "Deaths":[deaths_0,deaths_0]}, index=["Before", "After"])
        stats_df["K/D"] = (stats_df.Kills / stats_df.Deaths).round(7)
        stats_df["K/D rounded"] = stats_df["K/D"].round(2)
        self.stats_df_widget = DataFrameWidget(stats_df, editable=False)
        stats_box_df_layout.addWidget(self.stats_df_widget, stretch=2)
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
        return stats_box

    def stat_input_update(self, input_type, value):
        print("Editing terminé for {} -> {}".format(input_type, value))

        if self.death_input.value() != 0:
            self.kd_display.setText(str(round(self.kill_input.value() / self.death_input.value(), 7)))
            self.kd_rounded_display.setText(str(round(self.kill_input.value() / self.death_input.value(), 2)))
        else:
            self.kd_display.setText(str(self.kill_input.value()))
            self.kd_rounded_display.setText(str(self.kill_input.value()))

        # Updating the stats table
        self.stats_df_widget.model.layoutAboutToBeChanged.emit()
        df = self.stats_df_widget.model.df
        df.loc["After", input_type] = df.loc["Before", input_type] + int(value)
        df.loc["After", "K/D"] = (df.loc["After", "Kills"] / df.loc["After", "Deaths"]).round(7)
        df.loc["After", "K/D rounded"] = df.loc["After", "K/D"].round(2)
        self.stats_df_widget.model.layoutChanged.emit()

        


