import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class StringListDlg(QDialog):

    def __init__(self, title, stringlist, parent=None):
        super(StringListDlg, self).__init__(parent)
        #
        self.name = title
        self.stringListWidget = QListWidget()
        self.stringListWidget.addItems(stringlist)
        if stringlist:
            self.stringListWidget.setCurrentRow(0)
        #
        self.addButton = QPushButton("&Add...")
        self.editButton = QPushButton("&Edit...")
        self.removeButton = QPushButton("&Remove")
        self.upButton = QPushButton("&Up")
        self.downButton = QPushButton("&Down")
        self.sortButton = QPushButton("&Sort")
        self.closeButton = QPushButton("&Close")
        self.closeButton.setDefault(True)
        #
        #
        grid = QGridLayout()
        grid.addWidget(self.stringListWidget, 0, 0, 7, 1)
        grid.addWidget(self.addButton, 0, 1)
        grid.addWidget(self.editButton, 1, 1)
        grid.addWidget(self.removeButton, 2, 1)
        grid.addWidget(self.upButton, 3, 1)
        grid.addWidget(self.downButton, 4, 1)
        grid.addWidget(self.sortButton, 5, 1)
        grid.addWidget(self.closeButton, 6, 1)
        self.setLayout(grid)
        #
        self.setWindowTitle(title)
        #
        self.connect(self.sortButton, SIGNAL("clicked()"), self.stringListWidget.sortItems)
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)
        self.connect(self.removeButton, SIGNAL("clicked()"), self.remove)
        self.connect(self.addButton, SIGNAL("clicked()"), self.add)
        self.connect(self.editButton, SIGNAL("clicked()"), self.edit)
        self.connect(self.upButton, SIGNAL("clicked()"), self.up)
        self.connect(self.downButton, SIGNAL("clicked()"), self.down)


    def reject(self):
        self.accept()

    def accept(self):
        self.stringlist = []
        for i in range(self.stringListWidget.count()):
            self.stringlist.append(self.stringListWidget.item(i).text())
        QDialog.accept(self)

    def remove(self):
        row = self.stringListWidget.currentRow()
        item = self.stringListWidget.item(row)
        if item is None:
            return
        reply = QMessageBox.question(self, "Remove {}".format(self.name), "Remove {} `{}'?".format(
            self.name, item.text()), QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            item = self.stringListWidget.takeItem(row)
            del item

    def add(self):
        text, ok = QInputDialog.getText(self, "Add {}".format(self.name), "Add {}".format(self.name))
        if ok and text:
            row = self.stringListWidget.currentRow()
            self.stringListWidget.insertItem(row, text)

    def edit(self):
        row = self.stringListWidget.currentRow()
        item = self.stringListWidget.item(row)
        if item is None:
            return
        txt, ok = QInputDialog.getText(self, "Edit {}".format(self.name), "Edit {}".format(self.name), text=item.text())
        if ok and txt:
            item.setText(txt)

    def up(self):
        row = self.stringListWidget.currentRow()
        item = self.stringListWidget.item(row)
        if item is None or not row:
            return
        item = self.stringListWidget.takeItem(row)
        self.stringListWidget.insertItem(row - 1, item)
        self.stringListWidget.setCurrentItem(item)

    def down(self):
        row = self.stringListWidget.currentRow()
        item = self.stringListWidget.item(row)
        if item is None or (row == self.stringListWidget.count() - 1):
            return
        item = self.stringListWidget.takeItem(row)
        self.stringListWidget.insertItem(row + 1, item)
        self.stringListWidget.setCurrentItem(item)


if __name__ == "__main__":
    fruit = ["Banana", "Apple", "Elderberry", "Clementine", "Fig",
             "Guava", "Mango", "Honeydew Mellon", "Date", "Watermelon",
             "Tangerine", "Ugli Fruit", "Juniperberry", "Kiwi",
             "Lemon", "Nectarine", "Plum", "Raspberry", "Strawberry", "Orange"]

    app = QApplication(sys.argv)
    form = StringListDlg("Fruit", fruit)
    form.exec_()
    print("\n".join(x for x in form.stringlist))
