import sys
import psycopg2
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Todo")
        self.resize(600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.vbox_layout = QVBoxLayout()
        self.central_widget.setLayout(self.vbox_layout)

        self.todo_label = QLabel('Добавить задание:')
        self.todo_edit = QLineEdit()
        self.todo_edit.setPlaceholderText('Введите описание задания')
        self.vbox_layout.addWidget(self.todo_label)
        self.vbox_layout.addWidget(self.todo_edit)
        self.status_label = QLabel('')

        self.create_button = QPushButton('Создать задание')
        self.create_button.clicked.connect(self.create_todo)
        self.vbox_layout.addWidget(self.create_button)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['ID', 'Задание'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.vbox_layout.addWidget(self.table)

        self.load_todos()

    def create_todo(self):
        description = self.todo_edit.text()

        with psycopg2.connect(
            user="postgres",
            password="28031989",
            host="127.0.0.1",
            port="5432",
            database="exam"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO public.todo (description) VALUES (%s);",
                    (description,)
                )
            connection.commit()

        self.todo_edit.clear()
        self.load_todos()

    def load_todos(self):
        with psycopg2.connect(
                user="postgres",
                password="28031989",
                host="127.0.0.1",
                port="5432",
                database="exam"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.todo;")
                todos = cursor.fetchall()
                num_todos = len(todos)
                self.status_label.setText(f'Найдено заданий: {num_todos}')

                self.table.setRowCount(num_todos)
                for i, (todo_id, description) in enumerate(todos):
                    self.table.setItem(i, 0, QTableWidgetItem(str(todo_id)))
                    self.table.setItem(i, 1, QTableWidgetItem(description))

        num_todos = self.table.rowCount()
        self.status_label.setText(f'Найдено заданий: {num_todos}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

