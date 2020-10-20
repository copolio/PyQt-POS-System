from PyQt5.QtWidgets import QApplication
import admin
import user

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    e = user.UserAuth()
    sys.exit(app.exec_())
