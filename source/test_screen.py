import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QFont, QPalette
from PyQt5.QtCore import Qt, QRect, QSize

class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.is_dragging = False
        self.drag_position = None

        self.setMinimumSize(300, 200)

        self.close_button = QPushButton("X", self)
        self.close_button.setStyleSheet("background-color: transparent; border: none; color: white;")
        self.close_button.clicked.connect(self.close)

        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.setStyleSheet("background-color: transparent; border: none; color: white;")
        self.refresh_button.clicked.connect(self.refresh_window)

        self.row_num = 1
        self.table_widget = QTableWidget(self.row_num, 2, self)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.close_button)
        self.layout.addWidget(self.refresh_button)
        self.generate_table()
        self.layout.setContentsMargins(5, 35, 5, 5)

    def resizeEvent(self, event):
        window_width = self.width()
        self.close_button.setGeometry(window_width - 30, 5, 35, 20)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and event.pos().y() <= 30:
            self.is_dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            self.move(event.globalPos() - self.drag_position)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QColor(0, 0, 0, 100))
        painter.drawRect(self.rect())

        transparent_red = QColor(255, 0, 0, 100)
        painter.setBrush(transparent_red)
        painter.drawRect(0, 0, self.width(), 30)

    def generate_table(self):
        self.layout.removeWidget(self.table_widget)

        self.table_widget.clear()
        self.table_widget.setRowCount(self.row_num)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["操作", "数量"])

        for row in range(self.row_num):
            for col in range(2):
                item = QTableWidgetItem(f"Row {row+1}, Col {col+1}")
                item.setForeground(QColor("white"))
                self.table_widget.setItem(row, col, item)

        self.table_widget.setColumnWidth(0, 150)
        self.table_widget.setColumnWidth(1, 150)

        self.layout.addWidget(self.table_widget)

    def refresh_window(self):
        self.row_num += 1
        self.generate_table()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.setStyleSheet("background-color: transparent;")
    window.show()
    sys.exit(app.exec_())
