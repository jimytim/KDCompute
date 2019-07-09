from PySide2.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, 
    QGroupBox, QLabel, QLineEdit, QPushButton)

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

        # Stats display
        stats_box = QGroupBox("Stats")

        # Save Game button
        SaveGame_button = QPushButton("Save Game")
        save_game_layout = QHBoxLayout()
        save_game_layout.addStretch()
        save_game_layout.addWidget(SaveGame_button)


        self.layout.addLayout(goal_layout)
        self.layout.addWidget(input_box)
        self.layout.addWidget(stats_box)
        self.layout.addLayout(save_game_layout)
        self.setLayout(self.layout)

