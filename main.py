import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from database.queries import insert_doctors_data

class doctorsApp(QDialog):
    def __init__(self):
        super(doctorsApp, self).__init__()
        loadUi("ui/window.ui", self)

        self.pushButton.clicked.connect(self.add_doctors)

    def add_doctors(self):
        FirstName = self.lineEdit.text()
        LastName = self.lineEdit_2.text()
        Specialty = self.lineEdit_3.text()  # Change to string
        ExperienceYears = int(self.lineEdit_4.text())
        Email = self.lineEdit_5.text()

        try:
            Specialty = str(Specialty)  # Ensure it's a string
        except ValueError:
            print("Ошибка!")
            return

        doctors_data = (FirstName, LastName, Specialty, ExperienceYears, Email)

        insert_doctors_data(doctors_data)

        print("Данные добавлены успешно!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = doctorsApp()
    window.show()
    sys.exit(app.exec_())
