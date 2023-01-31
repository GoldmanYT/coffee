import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget
from ui1 import Ui_MainWindow
from ui2 import Ui_Form


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('data/coffee.sqlite')

        self.btn.clicked.connect(self.add_edit)
        self.table_widget.currentCellChanged.connect(self.select_id)
        self.selected_row = None
        self.selected_id = None
        self.form = None
        self.update_table()

    def update_table(self):
        cur = self.con.cursor()
        table = cur.execute('SELECT * FROM coffee').fetchall()
        self.table_widget.setRowCount(len(table))
        for i, row in enumerate(table):
            for j, col in enumerate(row):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(col)))

    def select_id(self, current_row):
        self.selected_row = current_row
        self.selected_id = self.table_widget.item(current_row, 0).text()

    def add_edit(self):
        if self.selected_id is None:
            self.form = AddEditFrom(self, self.con)
        else:
            args = [self.table_widget.item(self.selected_row, i).text()
                    for i in range(1, self.table_widget.columnCount())]
            self.form = AddEditFrom(self, self.con, self.selected_id, *args)
        self.form.show()


class AddEditFrom(QWidget, Ui_Form):
    def __init__(self, main_window, con, _id=None, *args):
        super().__init__()
        self.setupUi(self)

        self.main_window = main_window
        self.con = con
        self.id = _id
        self.btn_clear.clicked.connect(self.clear)
        self.btn_add.clicked.connect(self.add)
        self.btn_edit.clicked.connect(self.edit)

        for le, value in zip((self.le1, self.le2, self.le3, self.le4, self.le5, self.le6), args):
            le.setText(str(value))

    def add(self):
        cur = self.con.cursor()
        cur.execute(f'''INSERT INTO coffee(
                            sort_name, roast_degree, ground__in_grains, 
                            taste_description, price, packing_volume) 
                        VALUES
                        (?, ?, ?, ?, ?, ?)''', (self.le1.text(), self.le2.text(), self.le3.text(),
                                                self.le4.text(), self.le5.text(), self.le6.text()))

        self.con.commit()
        self.main_window.update_table()

    def clear(self):
        for le in (self.le1, self.le2, self.le3, self.le4, self.le5, self.le6):
            le.setText('')

    def edit(self):
        cur = self.con.cursor()
        cur.execute(f'''UPDATE coffee
                        SET sort_name = ?,
                            roast_degree = ?,
                            ground__in_grains = ?, 
                            taste_description = ?,
                            price = ?,
                            packing_volume = ? 
                        WHERE id = ?''', (self.le1.text(), self.le2.text(), self.le3.text(),
                                          self.le4.text(), self.le5.text(), self.le6.text(), self.id))

        self.con.commit()
        self.main_window.update_table()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
