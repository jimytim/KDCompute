from PySide2 import QtWidgets

class TabWidget(QtWidgets.QTabWidget):
    def __init__(self):
        QtWidgets.QTabWidget.__init__(self)

        # TAB Stats:
        button = QtWidgets.QPushButton("Stats")
        stat_widget = QtWidgets.QWidget()
        stat_layout = QtWidgets.QVBoxLayout()

        #Goal
        goal_label = QtWidgets.QLabel("Your goal")
        goal_input = QtWidgets.QLineEdit()
        goal_layout = QtWidgets.QHBoxLayout()
        goal_layout.addStretch()
        goal_layout.addWidget(goal_label)
        goal_layout.addWidget(goal_input)
        goal_layout.addStretch()

        # Game input
        input_box = QtWidgets.QGroupBox("New Game")

        # Stats display
        stats_box = QtWidgets.QGroupBox("Stats")

        # Save Game button
        SaveGame_button = QtWidgets.QPushButton("Save Game")
        save_game_layout = QtWidgets.QHBoxLayout()
        save_game_layout.addStretch()
        save_game_layout.addWidget(SaveGame_button)


        stat_layout.addLayout(goal_layout)
        stat_layout.addWidget(input_box)
        stat_layout.addWidget(stats_box)
        stat_layout.addLayout(save_game_layout)
        stat_widget.setLayout(stat_layout)



        textEdit = QtWidgets.QTextEdit()
        textEdit.setPlaceholderText("Tab Two!!")

        self.addTab(stat_widget, "Tab One")
        self.addTab(textEdit, "Tab Two")


