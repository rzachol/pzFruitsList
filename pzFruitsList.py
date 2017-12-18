import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class StringListDlg(QDialog):

    def __init__(self, title, stringList, parent=None):
        super(StringListDlg, self).__init__(parent)
        #
        self.name = title
        self.stringListWidget = QListWidget()
        self.stringListWidget.addItems(stringList)
        if stringList:
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

        ##        self.connect(self.rateSpinBox, SIGNAL("valueChanged(double)"),
        ##                     self.updateUi)
        ##        self.connect(self.yearsComboBox, SIGNAL("currentIndexChanged(int)"),
        ##                     self.updateUi)
        ##

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

##    def updateUi(self):
##        amount = self.principalSpinBox.value() * \
##                ((1 + self.rateSpinBox.value()/100) ** (self.yearsComboBox.currentIndex() + 1))
##        self.amountResult.setText("{0:.2f}".format(amount))
##       
if __name__ == "__main__":
    fruit = ["Banana", "Apple", "Elderberry", "Clementine", "Fig",
             "Guava", "Mango", "Honeydew Mellon", "Date", "Watermelon",
             "Tangerine", "Ugli Fruit", "Juniperberry", "Kiwi",
             "Lemon", "Nectarine", "Plum", "Raspberry", "Strawberry", "Orange"]

    app = QApplication(sys.argv)
    form = StringListDlg("Fruit", fruit)
    form.exec_()
    print("\n".join(x for x in form.stringlist))
