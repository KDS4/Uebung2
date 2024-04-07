from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QAction, QMenu, QMainWindow
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Daten speichern")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        self.labels = ["Vorname:", "Nachname:", "Geburtsdatum:", "Adresse:", "PLZ:", "Ort:", "Land:"]
        self.line_edits = []
        for label in self.labels:
            hbox = QHBoxLayout()
            hbox.addWidget(QLabel(label))
            line_edit = QLineEdit()
            hbox.addWidget(line_edit)
            self.line_edits.append(line_edit)
            layout.addLayout(hbox)

        self.countries = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"])
        layout.addWidget(self.countries)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_data)
        layout.addWidget(save_button)

        # Menu
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("File")

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_data)
        file_menu.addAction(save_action)

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

    def save_data(self):
        data = [line_edit.text() for line_edit in self.line_edits]
        data.append(self.countries.currentText())

        with open("output.txt", "w") as f:
            f.write(",".join(data))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())