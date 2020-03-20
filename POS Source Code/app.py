from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    import user
    # 프로그램 시작: 사용자 인증 호출
    e = user.UserAuth()
    sys.exit(app.exec_())
