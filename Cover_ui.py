from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 670)
        MainWindow.setAutoFillBackground(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1101, 641))
        self.stackedWidget.setObjectName("stackedWidget")

        self.page_1 = QtWidgets.QWidget()
        self.page_1.setAutoFillBackground(False)
        self.page_1.setObjectName("page_1")

        self.label_title = QtWidgets.QLabel(self.page_1)
        self.label_title.setGeometry(QtCore.QRect(390, 130, 591, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")

        self.label_notice = QtWidgets.QLabel(self.page_1)
        self.label_notice.setGeometry(QtCore.QRect(260, 290, 611, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_notice.setFont(font)
        self.label_notice.setObjectName("label_notice")

        self.login = QtWidgets.QToolButton(self.page_1)
        self.login.setGeometry(QtCore.QRect(480, 510, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.login.setFont(font)
        self.login.setAutoRaise(False)
        self.login.setObjectName("login")

        self.Signup = QtWidgets.QPushButton(self.page_1)
        self.Signup.setGeometry(QtCore.QRect(1000, 310, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Signup.setFont(font)
        self.Signup.setObjectName("Signup")

        self.Edit = QtWidgets.QPushButton(self.page_1)
        self.Edit.setGeometry(QtCore.QRect(1000, 370, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Edit.setFont(font)
        self.Edit.setObjectName("Edit")

        self.Analysis = QtWidgets.QPushButton(self.page_1)
        self.Analysis.setGeometry(QtCore.QRect(1000, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Analysis.setFont(font)
        self.Analysis.setObjectName("Analysis")

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")

        self.camera_site = QtWidgets.QLabel(self.page_2)
        self.camera_site.setGeometry(QtCore.QRect(30, 40, 701, 581))
        self.camera_site.setText("")
        self.camera_site.setObjectName("camera_site")

        self.name_label = QtWidgets.QLabel(self.page_2)
        self.name_label.setGeometry(QtCore.QRect(790, 60, 58, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")

        self.open_camera = QtWidgets.QPushButton(self.page_2)
        self.open_camera.setGeometry(QtCore.QRect(870, 110, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.open_camera.setFont(font)
        self.open_camera.setObjectName("open_camera")


        #blink
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(790, 190, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.blink_th = QtWidgets.QDoubleSpinBox(self.page_2)
        self.blink_th.setEnabled(True)
        self.blink_th.setGeometry(QtCore.QRect(980, 190, 61, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blink_th.sizePolicy().hasHeightForWidth())
        self.blink_th.setSizePolicy(sizePolicy)
        self.blink_th.setDecimals(1)
        self.blink_th.setMinimum(0.0)
        self.blink_th.setMaximum(10.0)
        self.blink_th.setSingleStep(0.1)
        self.blink_th.setProperty("value", 4.0)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.blink_th.setFont(font)
        self.blink_th.setObjectName("blink_th")

        #brightness
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(790, 230, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.bright_th = QtWidgets.QDoubleSpinBox(self.page_2)
        self.bright_th.setEnabled(True)
        self.bright_th.setGeometry(QtCore.QRect(980, 230, 61, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bright_th.sizePolicy().hasHeightForWidth())
        self.bright_th.setSizePolicy(sizePolicy)
        self.bright_th.setMinimum(0)
        self.bright_th.setMaximum(1000)
        self.bright_th.setSingleStep(1)
        self.bright_th.setProperty("value", 80.0)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bright_th.setFont(font)
        self.bright_th.setObjectName("bright_th")

        #distance
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(790, 270, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.distance_th = QtWidgets.QDoubleSpinBox(self.page_2)
        self.distance_th.setEnabled(True)
        self.distance_th.setGeometry(QtCore.QRect(980, 270, 61, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distance_th.sizePolicy().hasHeightForWidth())
        self.distance_th.setSizePolicy(sizePolicy)
        self.distance_th.setDecimals(2)
        self.distance_th.setMinimum(0.0)
        self.distance_th.setMaximum(2.0)
        self.distance_th.setSingleStep(0.01)
        self.distance_th.setProperty("value", 0.88)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.distance_th.setFont(font)
        self.distance_th.setObjectName("distance_th")

        #眨眼數字
        self.blink_num = QtWidgets.QLabel(self.page_2)
        self.blink_num.setGeometry(QtCore.QRect(790, 310, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.blink_num.setFont(font)
        self.blink_num.setObjectName("blink_num")

        self.blink_num_th = QtWidgets.QSpinBox(self.page_2)
        self.blink_num_th.setEnabled(True)
        self.blink_num_th.setGeometry(QtCore.QRect(980, 310, 61, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blink_num_th.sizePolicy().hasHeightForWidth())
        self.blink_num_th.setSizePolicy(sizePolicy)
        self.blink_num_th.setMinimum(0)
        self.blink_num_th.setMaximum(120)
        self.blink_num_th.setSingleStep(1)
        self.blink_num_th.setProperty("value", 15)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.blink_num_th.setFont(font)
        self.blink_num_th.setObjectName("blink_num_th")

        #working
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(790, 375, 111, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.working_time = QtWidgets.QSpinBox(self.page_2)
        self.working_time.setEnabled(True)
        self.working_time.setGeometry(QtCore.QRect(980, 375, 61, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.working_time.sizePolicy().hasHeightForWidth())
        self.working_time.setSizePolicy(sizePolicy)
        self.working_time.setMinimum(0)
        self.working_time.setMaximum(60)
        self.working_time.setSingleStep(1)
        self.working_time.setProperty("value", 25)
        font = QtGui.QFont()
        font.setFamily("Arial")
        #font.setPointSize(14)
        self.working_time.setFont(font)
        self.working_time.setObjectName("working_time")

        #min
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(1050, 375, 31, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        #rest
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(790, 415, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.resting_time = QtWidgets.QSpinBox(self.page_2)
        self.resting_time.setEnabled(True)
        self.resting_time.setGeometry(QtCore.QRect(980, 415, 61, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resting_time.sizePolicy().hasHeightForWidth())
        self.resting_time.setSizePolicy(sizePolicy)
        self.resting_time.setMinimum(0)
        self.resting_time.setMaximum(60)
        self.resting_time.setSingleStep(1)
        self.resting_time.setProperty("value", 5.0)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.resting_time.setFont(font)
        self.resting_time.setObjectName("resting_time")

        #min下
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(1050, 415, 31, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        #type
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(790, 475, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.nameBox = QtWidgets.QComboBox(self.page_2)
        self.nameBox.setGeometry(QtCore.QRect(870, 60, 171, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.nameBox.setFont(font)
        self.nameBox.setObjectName("nameBox")

        self.exercise_type = QtWidgets.QComboBox(self.page_2)
        self.exercise_type.setGeometry(QtCore.QRect(925, 475, 121, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exercise_type.sizePolicy().hasHeightForWidth())
        self.exercise_type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.exercise_type.setFont(font)
        self.exercise_type.setObjectName("exercise_type")

        #number
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(790, 515, 111, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.excerise_count = QtWidgets.QSpinBox(self.page_2)
        self.excerise_count.setEnabled(True)
        self.excerise_count.setGeometry(QtCore.QRect(980, 515, 61, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excerise_count.sizePolicy().hasHeightForWidth())
        self.excerise_count.setSizePolicy(sizePolicy)
        self.excerise_count.setMinimum(0)
        self.excerise_count.setMaximum(1000)
        self.excerise_count.setSingleStep(1)
        self.excerise_count.setProperty("value", 80.0)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.excerise_count.setFont(font)
        self.excerise_count.setObjectName("excerise_count")

        self.suggestion = QtWidgets.QToolButton(self.page_2)
        self.suggestion.setGeometry(QtCore.QRect(785, 565, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.suggestion.setFont(font)
        self.suggestion.setObjectName("suggestion")

        self.start = QtWidgets.QToolButton(self.page_2)
        self.start.setEnabled(True)
        self.start.setGeometry(QtCore.QRect(940, 565, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setObjectName("start")

        #Log in （點login進去後的頁面 要選擇使用者的頁面）
        self.login1_homebutton = QtWidgets.QPushButton(self.page_2)
        self.login1_homebutton.setGeometry(QtCore.QRect(1060, 10, 31, 31))
        self.login1_homebutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/ryan9/Downloads/專題/0923周/home_photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login1_homebutton.setIcon(icon)
        self.login1_homebutton.setIconSize(QtCore.QSize(30,30))
        self.login1_homebutton.setObjectName("login1_homebutton")

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")

        self.camera_site_2 = QtWidgets.QLabel(self.page_3)
        self.camera_site_2.setGeometry(QtCore.QRect(30, 40, 701, 581))
        self.camera_site_2.setText("")
        self.camera_site_2.setObjectName("camera_site_2")

        self.name_label_2 = QtWidgets.QLabel(self.page_3)
        self.name_label_2.setGeometry(QtCore.QRect(790, 60, 58, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.name_label_2.setFont(font)
        self.name_label_2.setObjectName("name_label_2")

        self.nameBox_2 = QtWidgets.QComboBox(self.page_3)
        self.nameBox_2.setGeometry(QtCore.QRect(870, 60, 171, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.nameBox_2.setFont(font)
        self.nameBox_2.setObjectName("nameBox_2")

        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(790, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(790, 120, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(790, 200, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.blink_th_2 = QtWidgets.QDoubleSpinBox(self.page_3)
        self.blink_th_2.setEnabled(True)
        self.blink_th_2.setGeometry(QtCore.QRect(980, 120, 61, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blink_th_2.sizePolicy().hasHeightForWidth())
        self.blink_th_2.setSizePolicy(sizePolicy)
        self.blink_th_2.setDecimals(1)
        self.blink_th_2.setMinimum(0.0)
        self.blink_th_2.setMaximum(10.0)
        self.blink_th_2.setSingleStep(0.1)
        self.blink_th_2.setProperty("value", 4.0)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.blink_th_2.setFont(font)
        self.blink_th_2.setObjectName("blink_th_2")

        self.bright_th_2 = QtWidgets.QDoubleSpinBox(self.page_3)
        self.bright_th_2.setEnabled(True)
        self.bright_th_2.setGeometry(QtCore.QRect(980, 160, 61, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bright_th_2.sizePolicy().hasHeightForWidth())
        self.bright_th_2.setSizePolicy(sizePolicy)
        self.bright_th_2.setMinimum(0)
        self.bright_th_2.setMaximum(1000)
        self.bright_th_2.setSingleStep(1)
        self.bright_th_2.setProperty("value", 80.0)        
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bright_th_2.setFont(font)
        self.bright_th_2.setObjectName("bright_th_2")

        self.distance_th_2 = QtWidgets.QDoubleSpinBox(self.page_3)
        self.distance_th_2.setEnabled(True)
        self.distance_th_2.setGeometry(QtCore.QRect(980, 200, 61, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distance_th_2.sizePolicy().hasHeightForWidth())
        self.distance_th_2.setSizePolicy(sizePolicy)
        self.distance_th_2.setDecimals(2)
        self.distance_th_2.setMinimum(0.0)
        self.distance_th_2.setMaximum(2.0)
        self.distance_th_2.setSingleStep(0.01)
        self.distance_th_2.setProperty("value", 0.88)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.distance_th_2.setFont(font)
        self.distance_th_2.setObjectName("distance_th_2")

        self.blink_num_1 = QtWidgets.QLabel(self.page_3)
        self.blink_num_1.setGeometry(QtCore.QRect(790, 240, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.blink_num_1.setFont(font)
        self.blink_num_1.setObjectName("blink_num_1")

        self.blink_num_th_1 = QtWidgets.QSpinBox(self.page_3)
        self.blink_num_th_1.setEnabled(True)
        self.blink_num_th_1.setGeometry(QtCore.QRect(980, 240, 61, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blink_num_th_1.sizePolicy().hasHeightForWidth())
        self.blink_num_th_1.setSizePolicy(sizePolicy)
        self.blink_num_th_1.setMinimum(0)
        self.blink_num_th_1.setMaximum(120)
        self.blink_num_th_1.setSingleStep(1)
        self.blink_num_th_1.setValue(self.blink_num_th.value())
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.blink_num_th_1.setFont(font)
        self.blink_num_th_1.setObjectName("blink_num_th_1")

        self.pushButton_sve = QtWidgets.QPushButton(self.page_3)
        self.pushButton_sve.setGeometry(QtCore.QRect(880, 280, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sve.sizePolicy().hasHeightForWidth())
        self.pushButton_sve.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sve.setFont(font)
        self.pushButton_sve.setObjectName("pushButton_sve")

        self.line = QtWidgets.QFrame(self.page_3)
        self.line.setGeometry(QtCore.QRect(770, 325, 311, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.lcdNumber_sec = QtWidgets.QLCDNumber(self.page_3)
        self.lcdNumber_sec.setGeometry(QtCore.QRect(980, 355, 64, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_sec.sizePolicy().hasHeightForWidth())
        self.lcdNumber_sec.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lcdNumber_sec.setFont(font)
        self.lcdNumber_sec.setDigitCount(2)
        self.lcdNumber_sec.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_sec.setObjectName("lcdNumber_sec")

        self.lcdNumber_min = QtWidgets.QLCDNumber(self.page_3)
        self.lcdNumber_min.setGeometry(QtCore.QRect(880, 355, 64, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_min.sizePolicy().hasHeightForWidth())
        self.lcdNumber_min.setSizePolicy(sizePolicy)
        self.lcdNumber_min.setDigitCount(2)
        self.lcdNumber_min.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_min.setObjectName("lcdNumber_min")

        self.lcdNumber_hour = QtWidgets.QLCDNumber(self.page_3)
        self.lcdNumber_hour.setGeometry(QtCore.QRect(770, 355, 64, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_hour.sizePolicy().hasHeightForWidth())
        self.lcdNumber_hour.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber_hour.setFont(font)
        self.lcdNumber_hour.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber_hour.setSmallDecimalPoint(False)
        self.lcdNumber_hour.setDigitCount(2)
        self.lcdNumber_hour.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_hour.setProperty("value", 0.0)
        self.lcdNumber_hour.setObjectName("lcdNumber_hour")

        self.Hour = QtWidgets.QLabel(self.page_3)
        self.Hour.setGeometry(QtCore.QRect(840, 355, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Hour.sizePolicy().hasHeightForWidth())
        self.Hour.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Hour.setFont(font)
        self.Hour.setObjectName("Hour")

        self.Second = QtWidgets.QLabel(self.page_3)
        self.Second.setGeometry(QtCore.QRect(1050, 355, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Second.sizePolicy().hasHeightForWidth())
        self.Second.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Second.setFont(font)
        self.Second.setObjectName("Second")

        self.Minute = QtWidgets.QLabel(self.page_3)
        self.Minute.setGeometry(QtCore.QRect(950, 355, 31, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Minute.sizePolicy().hasHeightForWidth())
        self.Minute.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Minute.setFont(font)
        self.Minute.setObjectName("Minute")

        self.Progress_progressBar = QtWidgets.QProgressBar(self.page_3)
        self.Progress_progressBar.setGeometry(QtCore.QRect(780, 400, 291, 23))
        self.Progress_progressBar.setProperty("value", 0)
        self.Progress_progressBar.setObjectName("Progress_progressBar")

        self.pushButton_Exhausted = QtWidgets.QPushButton(self.page_3)
        self.pushButton_Exhausted.setGeometry(QtCore.QRect(770, 470, 121, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Exhausted.sizePolicy().hasHeightForWidth())
        self.pushButton_sve.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Exhausted.setFont(font)
        self.pushButton_Exhausted.setObjectName("pushButton_Exhausted")

        self.listView = QtWidgets.QListView(self.page_3)
        self.listView.setGeometry(QtCore.QRect(900, 440, 181, 121))
        self.listView.setObjectName("listView")

        self.toolButton_finish = QtWidgets.QToolButton(self.page_3)
        self.toolButton_finish.setGeometry(QtCore.QRect(860, 590, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_finish.setFont(font)
        self.toolButton_finish.setObjectName("toolButton_finish")

        #Log in （按了start鍵之後開始測 要跳出一個警示匡說紀錄不保留喔）
        self.login2_homebutton = QtWidgets.QPushButton(self.page_3)
        self.login2_homebutton.setGeometry(QtCore.QRect(1060, 10, 31, 31))
        self.login2_homebutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/ryan9/Downloads/專題/0923周/home_photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login2_homebutton.setIcon(icon)
        self.login2_homebutton.setIconSize(QtCore.QSize(30,30))
        self.login2_homebutton.setObjectName("login2_homebutton")

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")

        self.label = QtWidgets.QLabel(self.page_4)
        self.label.setGeometry(QtCore.QRect(500, 60, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.calendarWidget = QtWidgets.QCalendarWidget(self.page_4)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 240, 321, 241))
        self.calendarWidget.setObjectName("calendarWidget")

        self.use_time_graph = QtWidgets.QGraphicsView(self.page_4)
        self.use_time_graph.setGeometry(QtCore.QRect(410, 150, 281, 221))
        self.use_time_graph.setObjectName("use_time_graph")

        self.distance_graph = QtWidgets.QGraphicsView(self.page_4)
        self.distance_graph.setGeometry(QtCore.QRect(740, 150, 281, 221))
        self.distance_graph.setObjectName("distance_graph")

        self.blink_graph = QtWidgets.QGraphicsView(self.page_4)
        self.blink_graph.setGeometry(QtCore.QRect(410, 400, 281, 221))
        self.blink_graph.setObjectName("blink_graph")

        self.brightness_graph = QtWidgets.QGraphicsView(self.page_4)
        self.brightness_graph.setGeometry(QtCore.QRect(740, 400, 281, 221))
        self.brightness_graph.setObjectName("brightness_graph")

        self.send_to_line = QtWidgets.QToolButton(self.page_4)
        self.send_to_line.setGeometry(QtCore.QRect(810, 70, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.send_to_line.setFont(font)
        self.send_to_line.setObjectName("send_to_line")

        '''self.back_to_home = QtWidgets.QPushButton(self.page_4)
        self.back_to_home.setGeometry(QtCore.QRect(910, 60, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.back_to_home.setFont(font)
        self.back_to_home.setObjectName("back_to_home")'''


        self.choose_user = QtWidgets.QLabel(self.page_4)
        self.choose_user.setGeometry(QtCore.QRect(50, 190, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.choose_user.setFont(font)
        self.choose_user.setObjectName("choose_user")

        self.nameBox_3 = QtWidgets.QComboBox(self.page_4)
        self.nameBox_3.setGeometry(QtCore.QRect(190, 190, 161, 22))
        self.nameBox_3.setObjectName("nameBox_3")

        #analysis：analysis_homebutton，之後可以把back的功能換掉
        self.analysis_homebutton = QtWidgets.QPushButton(self.page_4)
        self.analysis_homebutton.setGeometry(QtCore.QRect(1060, 10, 31, 31))
        self.analysis_homebutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/ryan9/Downloads/專題/0923周/home_photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analysis_homebutton.setIcon(icon)
        self.analysis_homebutton.setIconSize(QtCore.QSize(30,30))
        self.analysis_homebutton.setObjectName("analysis_homebutton")

        self.stackedWidget.addWidget(self.page_4)

        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")

        #「姓名」標籤
        self.name_label3 = QtWidgets.QLabel(self.page_5)
        self.name_label3.setGeometry(QtCore.QRect(40, 45, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_label3.setFont(font)
        self.name_label3.setObjectName("name_label3") 

        #「姓名」輸入匡
        self.name_input = QtWidgets.QLineEdit(self.page_5)
        self.name_input.setGeometry(QtCore.QRect(130, 45, 113, 21))
        self.name_input.setObjectName("name_input")
        self.name_input.setPlaceholderText("範例：王大明")

        #「」
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.page_5)
        self.doubleSpinBox.setGeometry(QtCore.QRect(280, 790, 68, 24))
        self.doubleSpinBox.setObjectName("doubleSpinBox")

        #「使用者名稱」輸入匡
        self.user_name_input = QtWidgets.QLineEdit(self.page_5)
        self.user_name_input.setGeometry(QtCore.QRect(390, 45, 113, 21))
        self.user_name_input.setObjectName("user_name_input")
        self.user_name_input.setPlaceholderText("範例：Albert")

        #「使用者名稱」標籤
        self.user_name_label = QtWidgets.QLabel(self.page_5)
        self.user_name_label.setGeometry(QtCore.QRect(300, 45, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.user_name_label.setFont(font)
        self.user_name_label.setObjectName("user_name_label")

        #「生日」標籤
        self.birthday_label = QtWidgets.QLabel(self.page_5)
        self.birthday_label.setGeometry(QtCore.QRect(40, 90, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.birthday_label.setFont(font)
        self.birthday_label.setObjectName("birthday_label")

        #「生日」輸入匡
        self.birthday_input = QtWidgets.QLineEdit(self.page_5)
        self.birthday_input.setGeometry(QtCore.QRect(130, 90, 113, 21))
        self.birthday_input.setObjectName("birthday_input")
        self.birthday_input.setPlaceholderText("範例：20030722")

        #「性別」標籤
        self.sex_label = QtWidgets.QLabel(self.page_5)
        self.sex_label.setGeometry(QtCore.QRect(40, 135, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sex_label.setFont(font)
        self.sex_label.setObjectName("sex_label")

        #「性別」-男生按鈕
        self.sex_man_button = QtWidgets.QRadioButton(self.page_5)
        self.sex_man_button.setGeometry(QtCore.QRect(130, 135, 51, 20))
        self.sex_man_button.setObjectName("sex_man_button")

        #「性別」-女生按鈕
        self.sex_women_button = QtWidgets.QRadioButton(self.page_5)
        self.sex_women_button.setGeometry(QtCore.QRect(190, 135, 51, 20))
        self.sex_women_button.setObjectName("sex_women_button")

        #「性別」總按鈕
        self.sex_group = QtWidgets.QButtonGroup(self.page_5)
        self.sex_group.addButton(self.sex_women_button)
        self.sex_group.addButton(self.sex_man_button)

        #「line token」標籤
        self.line_token_label = QtWidgets.QLabel(self.page_5)
        self.line_token_label.setGeometry(QtCore.QRect(300, 90, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.line_token_label.setFont(font)
        self.line_token_label.setObjectName("line_token_label")

        #「line token」輸入匡
        self.line_token_input = QtWidgets.QLineEdit(self.page_5)
        self.line_token_input.setGeometry(QtCore.QRect(390, 90, 113, 21))
        self.line_token_input.setObjectName("line_token_input")
        self.line_token_input.setPlaceholderText("請複製貼上")

        #「虛線7」
        self.line_7 = QtWidgets.QFrame(self.page_5)
        self.line_7.setGeometry(QtCore.QRect(30, 170, 441, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        #「右眼」標籤
        self.right_eye_label = QtWidgets.QLabel(self.page_5)
        self.right_eye_label.setGeometry(QtCore.QRect(40, 235, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.right_eye_label.setFont(font)
        self.right_eye_label.setObjectName("right_eye_label")

        #「右眼」遠視按鈕
        self.right_eye_out_button = QtWidgets.QRadioButton(self.page_5)
        self.right_eye_out_button.setGeometry(QtCore.QRect(85, 225, 51, 20))
        self.right_eye_out_button.setObjectName("right_eye_out_button")

        #「右眼」近視按鈕
        self.right_eye_in_button = QtWidgets.QRadioButton(self.page_5)
        self.right_eye_in_button.setGeometry(QtCore.QRect(85, 205, 51, 20))
        self.right_eye_in_button.setObjectName("right_eye_in_button")

        # 「右眼」近遠視總按鈕
        self.right_eye_group = QtWidgets.QButtonGroup(self.page_5)
        self.right_eye_group.addButton(self.right_eye_out_button)
        self.right_eye_group.addButton(self.right_eye_in_button)

        #「右眼度數」輸入匡
        self.right_eye_degree_input = QtWidgets.QLineEdit(self.page_5)
        self.right_eye_degree_input.setGeometry(QtCore.QRect(145, 215, 71, 20))
        self.right_eye_degree_input.setObjectName("right_eye_degree_input")
        self.right_eye_degree_input.setPlaceholderText("範例：200")

        #「右眼」閃光按鈕
        #還是有放按鈕鍵！如果按到無法取消，直接輸入0即可（預設也是0）
        self.right_eye_shine_button = QtWidgets.QRadioButton(self.page_5)
        self.right_eye_shine_button.setGeometry(QtCore.QRect(85, 265, 51, 20))
        self.right_eye_shine_button.setObjectName("right_eye_shine_button")

        # 「右眼」閃光總按鈕
        self.right_eye_shine_group = QtWidgets.QButtonGroup(self.page_5)
        self.right_eye_shine_group.addButton(self.right_eye_shine_button)

        #「右眼閃光」輸入匡
        self.right_eye_shine_input = QtWidgets.QLineEdit(self.page_5)
        self.right_eye_shine_input.setGeometry(QtCore.QRect(145, 265, 71, 20))
        self.right_eye_shine_input.setObjectName("right_eye_shine_input")
        self.right_eye_shine_input.setPlaceholderText("若無請填0")

        #「左眼」標籤
        self.left_eye_label = QtWidgets.QLabel(self.page_5)
        self.left_eye_label.setGeometry(QtCore.QRect(290, 235, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.left_eye_label.setFont(font)
        self.left_eye_label.setObjectName("left_eye_label")

        #「左眼」遠視按鈕
        self.left_eye_out_button = QtWidgets.QRadioButton(self.page_5)
        self.left_eye_out_button.setGeometry(QtCore.QRect(330, 225, 51, 20))
        self.left_eye_out_button.setObjectName("left_eye_out_button")

        #「左眼閃光」輸入匡
        self.left_eye_shine_input = QtWidgets.QLineEdit(self.page_5)
        self.left_eye_shine_input.setGeometry(QtCore.QRect(390, 265, 71, 20))
        self.left_eye_shine_input.setObjectName("left_eye_shine_input")
        self.left_eye_shine_input.setPlaceholderText("若無請填0")

        #「左眼度數」輸入匡
        self.left_eye_degree_input = QtWidgets.QLineEdit(self.page_5)
        self.left_eye_degree_input.setGeometry(QtCore.QRect(390, 215, 71, 20))
        self.left_eye_degree_input.setObjectName("left_eye_degree_input")
        self.left_eye_degree_input.setPlaceholderText("範例：200")

        #「左眼」近視按鈕
        self.left_eye_in_button = QtWidgets.QRadioButton(self.page_5)
        self.left_eye_in_button.setGeometry(QtCore.QRect(330, 205, 51, 20))
        self.left_eye_in_button.setObjectName("left_eye_in_button")

        #「左眼」近遠視總按鈕
        self.left_eye_group = QtWidgets.QButtonGroup(self.page_5)
        self.left_eye_group.addButton(self.left_eye_out_button)
        self.left_eye_group.addButton(self.left_eye_in_button)

        #「左眼」閃光按鈕
        self.left_eye_shine_button = QtWidgets.QRadioButton(self.page_5)
        self.left_eye_shine_button.setGeometry(QtCore.QRect(330, 265, 51, 20))
        self.left_eye_shine_button.setObjectName("left_eye_shine_button")

        # 「左眼」閃光總按鈕
        self.left_eye_shine_group = QtWidgets.QButtonGroup(self.page_5)
        self.left_eye_shine_group.addButton(self.left_eye_shine_button)

        #「用眼狀況問題1」滑桿
        self.eye_situation_slider1 = QtWidgets.QSlider(self.page_5)
        self.eye_situation_slider1.setGeometry(QtCore.QRect(310, 340, 161, 22))
        self.eye_situation_slider1.setOrientation(QtCore.Qt.Horizontal)
        self.eye_situation_slider1.setObjectName("eye_situation_slider1")

        #「用眼狀況問題1」標籤
        self.eye_situation_label1 = QtWidgets.QLabel(self.page_5)
        self.eye_situation_label1.setGeometry(QtCore.QRect(40, 340, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.eye_situation_label1.setFont(font)
        self.eye_situation_label1.setObjectName("eye_situation_label1")

        #
        self.line_8 = QtWidgets.QFrame(self.page_5)
        self.line_8.setGeometry(QtCore.QRect(30, 305, 441, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")

        #「用眼狀況問題2」滑桿
        self.eye_situation_slider2 = QtWidgets.QSlider(self.page_5)
        self.eye_situation_slider2.setGeometry(QtCore.QRect(310, 380, 161, 22))
        self.eye_situation_slider2.setOrientation(QtCore.Qt.Horizontal)
        self.eye_situation_slider2.setObjectName("eye_situation_slider2")

        #「用眼狀況問題2」標籤
        self.eye_situation_label2 = QtWidgets.QLabel(self.page_5)
        self.eye_situation_label2.setGeometry(QtCore.QRect(40, 380, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.eye_situation_label2.setFont(font)
        self.eye_situation_label2.setObjectName("eye_situation_label2")

        #「用眼狀況問題3」滑桿(眼睛乾澀頻率：)
        self.eye_situation_slider3 = QtWidgets.QSlider(self.page_5)
        self.eye_situation_slider3.setGeometry(QtCore.QRect(310, 420, 161, 22))
        self.eye_situation_slider3.setOrientation(QtCore.Qt.Horizontal)
        self.eye_situation_slider3.setObjectName("eye_situation_slider3")

        #「用眼狀況問題3」標籤(眼睛乾澀頻率：)
        self.eye_situation_label3 = QtWidgets.QLabel(self.page_5)
        self.eye_situation_label3.setGeometry(QtCore.QRect(40, 420, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.eye_situation_label3.setFont(font)
        self.eye_situation_label3.setObjectName("eye_situation_slider3")

        #「用眼狀況問題4」滑桿(頭痛暈眩頻率)
        self.eye_situation_slider4 = QtWidgets.QSlider(self.page_5)
        self.eye_situation_slider4.setGeometry(QtCore.QRect(310, 460, 161, 22))
        self.eye_situation_slider4.setOrientation(QtCore.Qt.Horizontal)
        self.eye_situation_slider4.setObjectName("eye_situation_slider4")

        #「用眼狀況問題4」標籤(頭痛暈眩頻率)
        self.eye_situation_label4 = QtWidgets.QLabel(self.page_5)
        self.eye_situation_label4.setGeometry(QtCore.QRect(40, 460, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.eye_situation_label4.setFont(font)
        self.eye_situation_label4.setObjectName("eye_situation_label4")

        #「用眼狀況問題5」標籤
        self.eye_situation_label5 = QtWidgets.QLabel(self.page_5)
        self.eye_situation_label5.setGeometry(QtCore.QRect(40, 500, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.eye_situation_label5.setFont(font)
        self.eye_situation_label5.setObjectName("eye_situation_label5")

        #「用眼狀況問題5」滑桿
        self.eye_situation_slider5 = QtWidgets.QSlider(self.page_5)
        self.eye_situation_slider5.setGeometry(QtCore.QRect(310, 500, 161, 22))
        self.eye_situation_slider5.setOrientation(QtCore.Qt.Horizontal)
        self.eye_situation_slider5.setObjectName("eye_situation_slider5")

        #
        self.line_9 = QtWidgets.QFrame(self.page_5)
        self.line_9.setGeometry(QtCore.QRect(30, 540, 441, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")

        #「是否長時間使用電子產品」-yes按鈕
        self.use_situation_yes_button1 = QtWidgets.QRadioButton(self.page_5)
        self.use_situation_yes_button1.setGeometry(QtCore.QRect(870, 40, 51, 20))
        self.use_situation_yes_button1.setObjectName("use_situation_yes_button1")

        #「是否長時間使用電子產品」不，按鈕
        self.use_situation_no_button1 = QtWidgets.QRadioButton(self.page_5)
        self.use_situation_no_button1.setGeometry(QtCore.QRect(930, 40, 51, 20))
        self.use_situation_no_button1.setObjectName("use_situation_no_button1")

        #「是否長時間使用電子產品」總按鈕
        self.use_situation1_group = QtWidgets.QButtonGroup(self.page_5)
        self.use_situation1_group.addButton(self.use_situation_yes_button1)
        self.use_situation1_group.addButton(self.use_situation_no_button1)

        #「是否長時間使用電子產品」標籤
        self.use_situation_label1 = QtWidgets.QLabel(self.page_5)
        self.use_situation_label1.setGeometry(QtCore.QRect(560, 40, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.use_situation_label1.setFont(font)
        self.use_situation_label1.setObjectName("use_situation_label1")

        #「使用設備時間」標籤
        self.use_situation_label2 = QtWidgets.QLabel(self.page_5)
        self.use_situation_label2.setGeometry(QtCore.QRect(560, 80, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.use_situation_label2.setFont(font)
        self.use_situation_label2.setObjectName("use_situation_label2")

        #「使用設備時間」下拉式選單
        self.use_situation2_combobox = QtWidgets.QComboBox(self.page_5)
        self.use_situation2_combobox.setGeometry(QtCore.QRect(867, 80, 104, 26))
        self.use_situation2_combobox.setObjectName("use_situation2_combobox")
        self.use_situation2_combobox.addItem("")
        self.use_situation2_combobox.addItem("")
        self.use_situation2_combobox.addItem("")
        self.use_situation2_combobox.addItem("")
        self.use_situation2_combobox.addItem("")

        #「防藍光設備」標籤
        self.use_situation_label3 = QtWidgets.QLabel(self.page_5)
        self.use_situation_label3.setGeometry(QtCore.QRect(560, 120, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.use_situation_label3.setFont(font)
        self.use_situation_label3.setObjectName("use_situation_label3")

        #「防藍光設備」是，按鈕
        self.use_situation_yes_button3 = QtWidgets.QRadioButton(self.page_5)
        self.use_situation_yes_button3.setGeometry(QtCore.QRect(870, 120, 51, 20))
        self.use_situation_yes_button3.setObjectName("use_situation_yes_button3")

        #「防藍光設備」不，按鈕
        self.use_situation_no_button3 = QtWidgets.QRadioButton(self.page_5)
        self.use_situation_no_button3.setGeometry(QtCore.QRect(930, 120, 51, 20))
        self.use_situation_no_button3.setObjectName("use_situation_no_button3")

        #「電子產品使用情況3」總按鈕
        self.use_situation3_group = QtWidgets.QButtonGroup(self.page_5)
        self.use_situation3_group.addButton(self.use_situation_yes_button3)
        self.use_situation3_group.addButton(self.use_situation_no_button3)

        #「調整顯示器頻率」標籤
        self.use_situation_label4 = QtWidgets.QLabel(self.page_5)
        self.use_situation_label4.setGeometry(QtCore.QRect(560, 160, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.use_situation_label4.setFont(font)
        self.use_situation_label4.setObjectName("use_situation_label4")

        #「調整顯示器頻率」滑桿
        self.use_situation_slider4 = QtWidgets.QSlider(self.page_5)
        self.use_situation_slider4.setGeometry(QtCore.QRect(820, 160, 161, 22))
        self.use_situation_slider4.setOrientation(QtCore.Qt.Horizontal)
        self.use_situation_slider4.setObjectName("use_situation_slider4")

        #「光線情形」標籤
        self.use_situation_label5 = QtWidgets.QLabel(self.page_5)
        self.use_situation_label5.setGeometry(QtCore.QRect(560, 200, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.use_situation_label5.setFont(font)
        self.use_situation_label5.setObjectName("use_situation_label5")

        #「光線情形」滑桿
        self.use_situation_slider5 = QtWidgets.QSlider(self.page_5)
        self.use_situation_slider5.setGeometry(QtCore.QRect(820, 200, 161, 22))
        self.use_situation_slider5.setOrientation(QtCore.Qt.Horizontal)
        self.use_situation_slider5.setObjectName("use_situation_slider5")

        #「右中」虛線
        self.line_10 = QtWidgets.QFrame(self.page_5)
        self.line_10.setGeometry(QtCore.QRect(550, 230, 441, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")

        #「保健食品」標籤
        self.habit_label1 = QtWidgets.QLabel(self.page_5)
        self.habit_label1.setGeometry(QtCore.QRect(560, 260, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.habit_label1.setFont(font)
        self.habit_label1.setObjectName("habit_label1")

        #「保健食品」不，按鈕
        self.habit_no_button1 = QtWidgets.QRadioButton(self.page_5)
        self.habit_no_button1.setGeometry(QtCore.QRect(860, 260, 51, 20))
        self.habit_no_button1.setObjectName("habit_no_button1")

        #「保健食品」是，按鈕
        self.habit_yes_button1 = QtWidgets.QRadioButton(self.page_5)
        self.habit_yes_button1.setGeometry(QtCore.QRect(800, 260, 51, 20))
        self.habit_yes_button1.setObjectName("habit_yes_button1")

        #「保健食品」總按鈕
        self.habit1_group = QtWidgets.QButtonGroup(self.page_5)
        self.habit1_group.addButton(self.habit_yes_button1)
        self.habit1_group.addButton(self.habit_no_button1)

        #「檢查眼睛頻率」標籤
        self.habit_label2 = QtWidgets.QLabel(self.page_5)
        self.habit_label2.setGeometry(QtCore.QRect(560, 300, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.habit_label2.setFont(font)
        self.habit_label2.setObjectName("habit_label2")

        #「檢查眼睛頻率」下拉式選單
        self.habit_combobox2 = QtWidgets.QComboBox(self.page_5)
        self.habit_combobox2.setGeometry(QtCore.QRect(730, 300, 104, 26))
        self.habit_combobox2.setObjectName("habit_combobox2")
        self.habit_combobox2.addItem("")
        self.habit_combobox2.addItem("")
        self.habit_combobox2.addItem("")
        self.habit_combobox2.addItem("")

        #「右上」虛線
        self.line_6 = QtWidgets.QFrame(self.page_5)
        self.line_6.setGeometry(QtCore.QRect(550, 10, 441, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        #「左上」虛線
        self.line_1 = QtWidgets.QFrame(self.page_5)
        self.line_1.setGeometry(QtCore.QRect(30, 10, 441, 20))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")

        #「睡眠時長」標籤
        self.habit_label3 = QtWidgets.QLabel(self.page_5)
        self.habit_label3.setGeometry(QtCore.QRect(560, 340, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.habit_label3.setFont(font)
        self.habit_label3.setObjectName("habit_label3")

        #「睡眠時長」下拉式選單
        self.habit_combobox3 = QtWidgets.QComboBox(self.page_5)
        self.habit_combobox3.setGeometry(QtCore.QRect(730, 340, 104, 26))
        self.habit_combobox3.setObjectName("habit_combobox3")
        self.habit_combobox3.addItem("")
        self.habit_combobox3.addItem("")
        self.habit_combobox3.addItem("")
        self.habit_combobox3.addItem("")

        #「每週運動次數」標籤
        self.habit_label4 = QtWidgets.QLabel(self.page_5)
        self.habit_label4.setGeometry(QtCore.QRect(560, 380, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.habit_label4.setFont(font)
        self.habit_label4.setObjectName("habit_label4")

        #「每週運動次數」下拉式選單
        self.habit_combobox4 = QtWidgets.QComboBox(self.page_5)
        self.habit_combobox4.setGeometry(QtCore.QRect(730, 380, 104, 26))
        self.habit_combobox4.setObjectName("habit_combobox4")
        self.habit_combobox4.addItem("")
        self.habit_combobox4.addItem("")
        self.habit_combobox4.addItem("")
        self.habit_combobox4.addItem("")

        #「多久會休息」標籤
        self.habit_label5 = QtWidgets.QLabel(self.page_5)
        self.habit_label5.setGeometry(QtCore.QRect(560, 420, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.habit_label5.setFont(font)
        self.habit_label5.setObjectName("habit_label5")

        #「多久會休息」下拉式選單
        self.habit_combobox5 = QtWidgets.QComboBox(self.page_5)
        self.habit_combobox5.setGeometry(QtCore.QRect(830, 420, 104, 26))
        self.habit_combobox5.setObjectName("habit_combobox5")
        self.habit_combobox5.addItem("")
        self.habit_combobox5.addItem("")
        self.habit_combobox5.addItem("")
        self.habit_combobox5.addItem("")
        self.habit_combobox5.addItem("")
        self.habit_combobox5.addItem("")
        self.habit_combobox5.addItem("")

        #「平均休息持續時間」標籤
        self.habit_label6 = QtWidgets.QLabel(self.page_5)
        self.habit_label6.setGeometry(QtCore.QRect(560, 460, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.habit_label6.setFont(font)
        self.habit_label6.setObjectName("habit_label6")

        #「休息持續時間」下拉式選單
        self.habit_combobox6 = QtWidgets.QComboBox(self.page_5)
        self.habit_combobox6.setGeometry(QtCore.QRect(830, 460, 104, 26))
        self.habit_combobox6.setObjectName("habit_combobox6")
        self.habit_combobox6.addItem("")
        self.habit_combobox6.addItem("")
        self.habit_combobox6.addItem("")
        self.habit_combobox6.addItem("")

        #「休息習慣7」標籤
        self.habit_label7 = QtWidgets.QLabel(self.page_5)
        self.habit_label7.setGeometry(QtCore.QRect(560, 500, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.habit_label7.setFont(font)
        self.habit_label7.setObjectName("habit_label7")

        #「生活習慣7-閉目養神」複選
        self.habit_close_checkbox7 = QtWidgets.QCheckBox(self.page_5)
        self.habit_close_checkbox7.setGeometry(QtCore.QRect(800, 500, 87, 20))
        self.habit_close_checkbox7.setObjectName("habit_close_checkbox7")

        #「生活習慣7-眼部運動」複選
        self.habit_exercise_checkbox7 = QtWidgets.QCheckBox(self.page_5)
        self.habit_exercise_checkbox7.setGeometry(QtCore.QRect(880, 500, 87, 20))
        self.habit_exercise_checkbox7.setObjectName("habit_exercise_checkbox7")

        #「生活習慣7-其他」複選
        self.habit_other_checkbox7 = QtWidgets.QCheckBox(self.page_5)
        self.habit_other_checkbox7.setGeometry(QtCore.QRect(960, 500, 87, 20))
        self.habit_other_checkbox7.setObjectName("habit_other_checkbox7")

        #「右下」虛線
        self.line_11 = QtWidgets.QFrame(self.page_5)
        self.line_11.setGeometry(QtCore.QRect(550, 540, 441, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")

        #「確定儲存」按鈕
        self.Savefile = QtWidgets.QPushButton(self.page_5)
        self.Savefile.setGeometry(QtCore.QRect(470, 570, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Savefile.setFont(font)
        self.Savefile.setObjectName("Savefile")

        #Sign up：signup_homebutton（要跳出一個警示匡說紀錄不保留喔）（save雖然會回去，但你填寫到一半沒有辦法回去）
        self.signup_homebutton = QtWidgets.QPushButton(self.page_5)
        self.signup_homebutton.setGeometry(QtCore.QRect(1060, 10, 31, 31))
        self.signup_homebutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/ryan9/Downloads/專題/0923周/home_photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signup_homebutton.setIcon(icon)
        self.signup_homebutton.setIconSize(QtCore.QSize(30,30))
        self.signup_homebutton.setObjectName("signup_homebutton")



        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")


        self.line_90 = QtWidgets.QFrame(self.page_6)
        self.line_90.setGeometry(QtCore.QRect(335, 530, 441, 20))
        self.line_90.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_90.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_90.setObjectName("line_90")

        self.line_30 = QtWidgets.QFrame(self.page_6)
        self.line_30.setGeometry(QtCore.QRect(335, 70, 441, 20))
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        
        #Edit title
        self.Edit_title = QtWidgets.QLabel(self.page_6)
        self.Edit_title.setEnabled(True)
        self.Edit_title.setGeometry(QtCore.QRect(475, 40, 160, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        self.Edit_title.setFont(font)
        self.Edit_title.setObjectName("Edit_title")

        #choose user
        self.User_1 = QtWidgets.QToolButton(self.page_6)
        self.User_1.setGeometry(QtCore.QRect(415, 110, 271, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.User_1.setFont(font)
        self.User_1.setObjectName("User_1")

        self.User_2 = QtWidgets.QToolButton(self.page_6)
        self.User_2.setGeometry(QtCore.QRect(415, 170, 271, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.User_2.setFont(font)
        self.User_2.setObjectName("User_2")

        self.User_3 = QtWidgets.QToolButton(self.page_6)
        self.User_3.setGeometry(QtCore.QRect(415, 230, 271, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.User_3.setFont(font)
        self.User_3.setObjectName("User_3")

        self.User_4 = QtWidgets.QToolButton(self.page_6)
        self.User_4.setGeometry(QtCore.QRect(415, 300, 271, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.User_4.setFont(font)
        self.User_4.setObjectName("User_4")

        self.User_5 = QtWidgets.QToolButton(self.page_6)
        self.User_5.setGeometry(QtCore.QRect(415, 360, 271, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.User_5.setFont(font)
        self.User_5.setObjectName("User_5")

        self.Change_detail = QtWidgets.QPushButton(self.page_6)
        self.Change_detail.setGeometry(QtCore.QRect(388, 550, 141, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Change_detail.sizePolicy().hasHeightForWidth())
        self.Change_detail.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Change_detail.setFont(font)
        self.Change_detail.setObjectName("Change_detail")

        self.Delete = QtWidgets.QPushButton(self.page_6)
        self.Delete.setGeometry(QtCore.QRect(580, 550, 141, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Delete.sizePolicy().hasHeightForWidth())
        self.Delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Delete.setFont(font)
        self.Delete.setObjectName("Delete")

        self.homebutton = QtWidgets.QPushButton(self.page_6)
        self.homebutton.setGeometry(QtCore.QRect(1060, 10, 31, 31))
        self.homebutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/ryan9/Downloads/專題/0923周/home_photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebutton.setIcon(icon)
        self.homebutton.setIconSize(QtCore.QSize(30,30))
        self.homebutton.setObjectName("homebutton")

        #edit（選擇使用者時的頁面）：edit1_homebutton
        self.edit1_homebutton = QtWidgets.QPushButton(self.page_6)
        self.edit1_homebutton.setGeometry(QtCore.QRect(1060, 10, 31, 31))
        self.edit1_homebutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/ryan9/Downloads/專題/0923周/home_photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit1_homebutton.setIcon(icon)
        self.edit1_homebutton.setIconSize(QtCore.QSize(30,30))
        self.edit1_homebutton.setObjectName("edit1_homebutton")

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")

        #「頂端文字說明」（那一大串的那個）
        self.top_label = QtWidgets.QLabel(self.page_7)
        self.top_label.setEnabled(True)
        self.top_label.setGeometry(QtCore.QRect(160, 30, 781, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.top_label.setFont(font)
        self.top_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.top_label.setOpenExternalLinks(False)
        self.top_label.setObjectName("top_label")

        #「虛線」（中間那條垂直虛線）
        self.line = QtWidgets.QFrame(self.page_7)
        self.line.setGeometry(QtCore.QRect(540, 150, 20, 441))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        #順序為由左至右，由上到下！
        #「問題1」標籤
        self.question_1_label = QtWidgets.QLabel(self.page_7)
        self.question_1_label.setGeometry(QtCore.QRect(100, 160, 234, 16))
        self.question_1_label.setObjectName("question_1_label")

        #「問題1」下拉式選單
        self.question_1_comboBox = QtWidgets.QComboBox(self.page_7)
        self.question_1_comboBox.setGeometry(QtCore.QRect(340, 160, 181, 26))
        self.question_1_comboBox.setObjectName("question_1_comboBox")
        self.question_1_comboBox.addItem("")
        self.question_1_comboBox.addItem("")
        self.question_1_comboBox.addItem("")
        self.question_1_comboBox.addItem("")

        #「問題2」標籤
        self.question_2_label = QtWidgets.QLabel(self.page_7)
        self.question_2_label.setGeometry(QtCore.QRect(100, 230, 234, 21))
        self.question_2_label.setObjectName("question_2_label")

        #「問題2」下拉式選單
        self.question_2_comboBox = QtWidgets.QComboBox(self.page_7)
        self.question_2_comboBox.setGeometry(QtCore.QRect(340, 230, 181, 26))
        self.question_2_comboBox.setObjectName("question_2_comboBox")
        self.question_2_comboBox.addItem("")
        self.question_2_comboBox.addItem("")
        self.question_2_comboBox.addItem("")
        self.question_2_comboBox.addItem("")
        self.question_2_comboBox.addItem("")
        self.question_2_comboBox.addItem("")
        self.question_2_comboBox.addItem("")

        #「問題3」標籤
        self.question_3_label = QtWidgets.QLabel(self.page_7)
        self.question_3_label.setGeometry(QtCore.QRect(100, 300, 234, 21))
        self.question_3_label.setObjectName("question_3_label")

        #「問題3」下拉式選單
        self.question_3_comboBox = QtWidgets.QComboBox(self.page_7)
        self.question_3_comboBox.setGeometry(QtCore.QRect(340, 300, 181, 26))
        self.question_3_comboBox.setObjectName("question_3_comboBox")
        self.question_3_comboBox.addItem("")
        self.question_3_comboBox.addItem("")
        self.question_3_comboBox.addItem("")
        self.question_3_comboBox.addItem("")
        self.question_3_comboBox.addItem("")
        self.question_3_comboBox.addItem("")

        #「問題4」標籤
        self.question_4_label = QtWidgets.QLabel(self.page_7)
        self.question_4_label.setGeometry(QtCore.QRect(100, 380, 234, 21))
        self.question_4_label.setObjectName("question_4_label")

        #「問題4」下拉式選單
        self.question_4_comboBox = QtWidgets.QComboBox(self.page_7)
        self.question_4_comboBox.setGeometry(QtCore.QRect(340, 380, 181, 26))
        self.question_4_comboBox.setObjectName("question_4_comboBox")
        self.question_4_comboBox.addItem("")
        self.question_4_comboBox.addItem("")
        self.question_4_comboBox.addItem("")

        #「問題5」標籤
        self.question_5_label = QtWidgets.QLabel(self.page_7)
        self.question_5_label.setGeometry(QtCore.QRect(100, 460, 236, 21))
        self.question_5_label.setObjectName("question_5_label")

        #「問題5」是，按鈕
        self.question_5yes_Button = QtWidgets.QRadioButton(self.page_7)
        self.question_5yes_Button.setGeometry(QtCore.QRect(350, 460, 41, 20))
        self.question_5yes_Button.setObjectName("question_5yes_Button")

        #「問題5」否，按鈕
        self.question_5no_Button = QtWidgets.QRadioButton(self.page_7)
        self.question_5no_Button.setGeometry(QtCore.QRect(430, 460, 41, 20))
        self.question_5no_Button.setObjectName("question_5no_Button")

        # 「問題5」總按鈕
        self.question5_group = QtWidgets.QButtonGroup(self.page_7)
        self.question5_group.addButton(self.question_5yes_Button)
        self.question5_group.addButton(self.question_5no_Button)

        #「問題6」標籤
        self.question_6_label = QtWidgets.QLabel(self.page_7)
        self.question_6_label.setGeometry(QtCore.QRect(100, 530, 234, 31))
        self.question_6_label.setObjectName("question_6_label")

        #「問題6」是，按鈕
        self.question_6yes_Button = QtWidgets.QRadioButton(self.page_7)
        self.question_6yes_Button.setGeometry(QtCore.QRect(350, 540, 41, 20))
        self.question_6yes_Button.setObjectName("question_6yes_Button")

        #「問題6」否，按鈕
        self.question_6no_Button = QtWidgets.QRadioButton(self.page_7)
        self.question_6no_Button.setGeometry(QtCore.QRect(430, 540, 41, 20))
        self.question_6no_Button.setObjectName("question_6no_Button")

        # 「問題6」總按鈕
        self.question6_group = QtWidgets.QButtonGroup(self.page_7)
        self.question6_group.addButton(self.question_6yes_Button)
        self.question6_group.addButton(self.question_6no_Button)

        #「問題7」標籤
        self.question_7_label = QtWidgets.QLabel(self.page_7)
        self.question_7_label.setGeometry(QtCore.QRect(600, 160, 275, 20))
        self.question_7_label.setObjectName("question_7_label")

        #「問題7」滑桿
        self.question_7_Slider = QtWidgets.QSlider(self.page_7)
        self.question_7_Slider.setGeometry(QtCore.QRect(910, 160, 160, 22))
        self.question_7_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.question_7_Slider.setObjectName("question_7_Slider")

        #以下為「問題7-數值呈現」
        self.label_question_7 = QtWidgets.QLabel(self.page_7)
        self.label_question_7.setGeometry(QtCore.QRect(890, 160, 100, 22))
        def update_label():
            self.label_question_7.setText(str(self.question_7_Slider.value()))
        self.question_7_Slider.valueChanged.connect(update_label)
        self.question_7_Slider.setRange(0, 10)

        #「問題8」標籤
        self.question_8_label = QtWidgets.QLabel(self.page_7)
        self.question_8_label.setGeometry(QtCore.QRect(600, 230, 273, 20))
        self.question_8_label.setObjectName("question_8_label")

        #「問題8」滑桿
        self.question_8_Slider = QtWidgets.QSlider(self.page_7)
        self.question_8_Slider.setGeometry(QtCore.QRect(910, 230, 160, 22))
        self.question_8_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.question_8_Slider.setObjectName("question_8_Slider")

        #以下為「問題8-數值呈現」
        self.label_question_8 = QtWidgets.QLabel(self.page_7)
        self.label_question_8.setGeometry(QtCore.QRect(890, 230, 100, 22))
        def update_label():
            self.label_question_8.setText(str(self.question_8_Slider.value()))
        self.question_8_Slider.valueChanged.connect(update_label)
        self.question_8_Slider.setRange(0, 10)

        #「問題9」標籤
        self.question_9_label = QtWidgets.QLabel(self.page_7)
        self.question_9_label.setGeometry(QtCore.QRect(600, 310, 273, 20))
        self.question_9_label.setObjectName("question_9_label")

        #「問題9」滑桿
        self.question_9_Slider = QtWidgets.QSlider(self.page_7)
        self.question_9_Slider.setGeometry(QtCore.QRect(910, 310, 160, 22))
        self.question_9_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.question_9_Slider.setObjectName("question_9_Slider")

        #以下為「問題9-數值呈現」
        self.label_question_9 = QtWidgets.QLabel(self.page_7)
        self.label_question_9.setGeometry(QtCore.QRect(890, 310, 100, 22))
        def update_label():
            self.label_question_9.setText(str(self.question_9_Slider.value()))
        self.question_9_Slider.valueChanged.connect(update_label)
        self.question_9_Slider.setRange(0, 10)

        #「問題10」標籤
        self.question_10_label = QtWidgets.QLabel(self.page_7)
        self.question_10_label.setGeometry(QtCore.QRect(600, 380, 273, 20))
        self.question_10_label.setObjectName("question_10_label")

        #「問題10」滑桿
        self.question_10_Slider = QtWidgets.QSlider(self.page_7)
        self.question_10_Slider.setGeometry(QtCore.QRect(910, 380, 160, 22))
        self.question_10_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.question_10_Slider.setObjectName("question_10_Slider")

        #以下為「問題10-數值呈現」
        self.label_question_10 = QtWidgets.QLabel(self.page_7)
        self.label_question_10.setGeometry(QtCore.QRect(890, 380, 100, 22))
        def update_label():
            self.label_question_10.setText(str(self.question_10_Slider.value()))
        self.question_10_Slider.valueChanged.connect(update_label)
        self.question_10_Slider.setRange(0, 10)

        #「問題11」標籤
        self.question_11_label = QtWidgets.QLabel(self.page_7)
        self.question_11_label.setGeometry(QtCore.QRect(600, 460, 273, 20))
        self.question_11_label.setObjectName("question_11_label")

        #「問題11」滑桿
        self.question_11_Slider = QtWidgets.QSlider(self.page_7)
        self.question_11_Slider.setGeometry(QtCore.QRect(910, 460, 160, 22))
        self.question_11_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.question_11_Slider.setObjectName("question_11_Slider")

        #以下為「問題11-數值呈現」
        self.label_question_11 = QtWidgets.QLabel(self.page_7)
        self.label_question_11.setGeometry(QtCore.QRect(890, 460, 100, 22))
        def update_label():
            self.label_question_11.setText(str(self.question_11_Slider.value()))
        self.question_11_Slider.valueChanged.connect(update_label)
        self.question_11_Slider.setRange(0, 10)

        #「問題12」標籤
        self.question_12_label = QtWidgets.QLabel(self.page_7)
        self.question_12_label.setGeometry(QtCore.QRect(600, 540, 161, 20))
        self.question_12_label.setObjectName("question_12_label")

        #「問題12」輸入匡
        self.question_12_input = QtWidgets.QLineEdit(self.page_7)
        self.question_12_input.setGeometry(QtCore.QRect(810, 540, 261, 21))
        self.question_12_input.setObjectName("question_12_input")

        #「送出」按鈕（最下面那個）
        self.Sendout_Button = QtWidgets.QPushButton(self.page_7)
        self.Sendout_Button.setGeometry(QtCore.QRect(478, 590, 141, 41))
        self.Sendout_Button.setObjectName("Sendout_Button")


        self.stackedWidget.addWidget(self.page_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eye myself"))
        self.label_title.setText(_translate("MainWindow", "EYE MYSELF"))
        self.label_notice.setText(_translate("MainWindow", "1.本系統會收集和分析使用者的基本資料與用眼數據，這些數據僅用於學術研究\n"
"及系統優化。所有收集個人資料將嚴格保密，並不會用於其他商業用途或外洩。\n"
"\n"
"2.本系統提供的用眼建議和提醒僅供參考，旨在幫助使用者改善用眼習慣並\n"
"減少眼睛疲勞。對於任何嚴重的眼部健康問題，請諮詢專業醫療人員。\n"
"\n"
"3.每次測試結束後，請務必填寫系統提供的簡易問卷，以反饋您的用眼感受和\n"
"身體狀況。這將幫助我們進一步優化系統，提供更精確的健康建議。\n"
""))
        self.login.setText(_translate("MainWindow", "Log in"))
        self.Signup.setText(_translate("MainWindow", "Sign up"))
        self.Edit.setText(_translate("MainWindow", "Edit"))
        self.Analysis.setText(_translate("MainWindow", "Analysis"))
        self.name_label.setText(_translate("MainWindow", "Name"))
        self.open_camera.setText(_translate("MainWindow", "Camera"))
        self.label_2.setText(_translate("MainWindow", "Blink Threshlod"))
        self.label_3.setText(_translate("MainWindow", "Brightness Threshold"))
        self.label_4.setText(_translate("MainWindow", "Distance Threshold"))
        self.blink_num.setText(_translate("MainWindow", "Blink per min"))
        self.label_5.setText(_translate("MainWindow", "Working Time"))
        self.label_6.setText(_translate("MainWindow", "min"))
        self.label_7.setText(_translate("MainWindow", "Resting Time"))
        self.label_8.setText(_translate("MainWindow", "min"))
        self.label_9.setText(_translate("MainWindow", "Exercise Type"))
        self.label_10.setText(_translate("MainWindow", "Number"))
        self.suggestion.setText(_translate("MainWindow", "Suggestion"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.name_label_2.setText(_translate("MainWindow", "Name"))
        self.label_11.setText(_translate("MainWindow", "Brightness Threshold"))
        self.label_12.setText(_translate("MainWindow", "Blink Threshlod"))
        self.label_13.setText(_translate("MainWindow", "Distance Threshold"))
        self.pushButton_sve.setText(_translate("MainWindow", "Save"))
        self.Hour.setText(_translate("MainWindow", "hour"))
        self.Second.setText(_translate("MainWindow", "sec"))
        self.Minute.setText(_translate("MainWindow", "min"))
        self.blink_num_1.setText(_translate("MainWindow","Blink per min"))
        self.pushButton_Exhausted.setText(_translate("MainWindow", "Exhausted"))
        self.toolButton_finish.setText(_translate("MainWindow", "Finish"))
        self.label.setText(_translate("MainWindow", "Analysis"))
        self.send_to_line.setText(_translate("MainWindow", "Send to line"))
        '''self.back_to_home.setText(_translate("MainWindow", "Back"))'''
        self.choose_user.setText(_translate("MainWindow", "Choose user"))
        self.name_label3.setText(_translate("MainWindow", "姓           名："))
        self.sex_man_button.setText(_translate("MainWindow", "男生"))
        self.user_name_label.setText(_translate("MainWindow", "使用者名稱："))
        self.birthday_label.setText(_translate("MainWindow", "生           日："))
        self.sex_label.setText(_translate("MainWindow", "性           別："))
        self.sex_women_button.setText(_translate("MainWindow", "女生"))
        self.line_token_label.setText(_translate("MainWindow", "line  token ："))
        self.right_eye_label.setText(_translate("MainWindow", "右眼："))
        self.right_eye_out_button.setText(_translate("MainWindow", "遠視"))
        self.right_eye_in_button.setText(_translate("MainWindow", "近視"))
        self.right_eye_shine_button.setText(_translate("MainWindow", "閃光"))
        self.left_eye_label.setText(_translate("MainWindow", "左眼："))
        self.left_eye_out_button.setText(_translate("MainWindow", "遠視"))
        self.left_eye_in_button.setText(_translate("MainWindow", "近視"))
        self.left_eye_shine_button.setText(_translate("MainWindow", "閃光"))
        self.eye_situation_label1.setText(_translate("MainWindow", "您使用電子產品時配戴「眼鏡」的頻率："))
        self.eye_situation_label2.setText(_translate("MainWindow", "您使用電子產品時配戴「隱眼」的頻率："))
        self.eye_situation_label4.setText(_translate("MainWindow", "頭痛暈眩頻率："))
        self.eye_situation_label3.setText(_translate("MainWindow", "眼睛乾澀頻率："))
        self.eye_situation_label5.setText(_translate("MainWindow", "眼睛疲勞頻率："))
        self.use_situation_label5.setText(_translate("MainWindow", "您工作或學習場所之光線情況為："))
        self.habit_label2.setText(_translate("MainWindow", "您定期檢查眼睛的頻率？"))
        self.use_situation_no_button1.setText(_translate("MainWindow", "否"))
        self.use_situation_label2.setText(_translate("MainWindow", "每次使用電子設備時間（以長時間活動為主）？"))
        self.use_situation_yes_button3.setText(_translate("MainWindow", "是"))
        self.habit_no_button1.setText(_translate("MainWindow", "否"))
        self.habit_yes_button1.setText(_translate("MainWindow", "是"))
        self.use_situation_label3.setText(_translate("MainWindow", "您是否有使用眼睛保護設備(如防藍光設備軟體)？"))
        self.habit_combobox2.setItemText(0, _translate("MainWindow", "無"))
        self.habit_combobox2.setItemText(1, _translate("MainWindow", "半年一次"))
        self.habit_combobox2.setItemText(2, _translate("MainWindow", "一年一次"))
        self.habit_combobox2.setItemText(3, _translate("MainWindow", "更頻繁"))
        self.use_situation_label4.setText(_translate("MainWindow", "您使用裝置期間調整顯示器設置頻率："))
        self.use_situation2_combobox.setItemText(0, _translate("MainWindow", "3小時以內"))
        self.use_situation2_combobox.setItemText(1, _translate("MainWindow", "3至6小時"))
        self.use_situation2_combobox.setItemText(2, _translate("MainWindow", "6至9小時"))
        self.use_situation2_combobox.setItemText(3, _translate("MainWindow", "9至12小時"))
        self.use_situation2_combobox.setItemText(4, _translate("MainWindow", "12小時以上"))
        self.use_situation_yes_button1.setText(_translate("MainWindow", "是"))
        self.use_situation_label1.setText(_translate("MainWindow", "您工作/學習性質是否需要長時間使用電子產品？"))
        self.habit_label1.setText(_translate("MainWindow", "您平常是否有在時用戶眼保健食品？"))
        self.use_situation_no_button3.setText(_translate("MainWindow", "否"))
        self.habit_label3.setText(_translate("MainWindow", "您平均每天睡眠時長為？"))
        self.habit_combobox3.setItemText(0, _translate("MainWindow", "低於4小時"))
        self.habit_combobox3.setItemText(1, _translate("MainWindow", "4至6小時"))
        self.habit_combobox3.setItemText(2, _translate("MainWindow", "6至8小時"))
        self.habit_combobox3.setItemText(3, _translate("MainWindow", "高於8小時"))
        self.habit_label4.setText(_translate("MainWindow", "您平均每週運動次數為？"))
        self.habit_combobox4.setItemText(0, _translate("MainWindow", "0或1次"))
        self.habit_combobox4.setItemText(1, _translate("MainWindow", "2或3次"))
        self.habit_combobox4.setItemText(2, _translate("MainWindow", "4或5次"))
        self.habit_combobox4.setItemText(3, _translate("MainWindow", "6次以上"))
        self.habit_combobox5.setItemText(0, _translate("MainWindow", "無休息"))
        self.habit_combobox5.setItemText(1, _translate("MainWindow", "1小時內"))
        self.habit_combobox5.setItemText(2, _translate("MainWindow", "1至2小時"))
        self.habit_combobox5.setItemText(3, _translate("MainWindow", "2至3小時"))
        self.habit_combobox5.setItemText(4, _translate("MainWindow", "3至4小時"))
        self.habit_combobox5.setItemText(5, _translate("MainWindow", "4至5小時"))
        self.habit_combobox5.setItemText(6, _translate("MainWindow", "5小時以上"))
        self.habit_label5.setText(_translate("MainWindow", "使用電子設備時，您通常使用多久會休息？"))
        self.habit_label6.setText(_translate("MainWindow", "平均每次休息的持續時間約持續多久？"))
        self.habit_combobox6.setItemText(0, _translate("MainWindow", "10分鐘內"))
        self.habit_combobox6.setItemText(1, _translate("MainWindow", "11至30分鐘"))
        self.habit_combobox6.setItemText(2, _translate("MainWindow", "31至60分鐘"))
        self.habit_combobox6.setItemText(3, _translate("MainWindow", "60分鐘以上"))
        self.habit_close_checkbox7.setText(_translate("MainWindow", "閉目養神"))
        self.habit_label7.setText(_translate("MainWindow", "您眼睛疲勞時，習慣的休息方式為何？"))
        self.habit_exercise_checkbox7.setText(_translate("MainWindow", "眼部運動"))
        self.habit_other_checkbox7.setText(_translate("MainWindow", "其他"))
        self.Savefile.setText(_translate("MainWindow", "Save"))
        self.Change_detail.setText(_translate("MainWindow", "修改"))
        self.User_1.setText(_translate("MainWindow", "Mandy"))
        self.Edit_title.setText(_translate("MainWindow", "選擇使用者"))
        self.User_2.setText(_translate("MainWindow", "Ryan"))
        self.User_3.setText(_translate("MainWindow", "Lin"))
        self.User_4.setText(_translate("MainWindow", "Joy"))
        self.User_5.setText(_translate("MainWindow", "Bun"))
        self.Delete.setText(_translate("MainWindow", "刪除"))

        self.Sendout_Button.setText(_translate("MainWindow", "送出"))
        self.top_label.setText(_translate("MainWindow", "本問卷旨在了解您在使用電子產品時的用眼狀況，以便我們的系統能夠更好地為您提供客制化的用眼健康提醒。\n"
"我們希望通過這些數據來改善您在使用電子產品過程中的視覺舒適度，並減少眼部疲勞。\n"
"請根據您的實際體感回答以下問題。我們承諾，所有的數據將僅用於本次研究，並會嚴格保密。謝謝您的合作！"))
        self.question_1_comboBox.setItemText(0, _translate("MainWindow", "電腦"))
        self.question_1_comboBox.setItemText(1, _translate("MainWindow", "手機"))
        self.question_1_comboBox.setItemText(2, _translate("MainWindow", "平板"))
        self.question_1_comboBox.setItemText(3, _translate("MainWindow", "其他"))
        self.question_2_comboBox.setItemText(0, _translate("MainWindow", "工作/實習用途"))
        self.question_2_comboBox.setItemText(1, _translate("MainWindow", "聆聽線上課程"))
        self.question_2_comboBox.setItemText(2, _translate("MainWindow", "完成學校作業"))
        self.question_2_comboBox.setItemText(3, _translate("MainWindow", "打電腦遊戲"))
        self.question_2_comboBox.setItemText(4, _translate("MainWindow", "觀看影音串流平台(如Youtube)"))
        self.question_2_comboBox.setItemText(5, _translate("MainWindow", "回覆訊息文字"))
        self.question_2_comboBox.setItemText(6, _translate("MainWindow", "其他"))
        self.question_5yes_Button.setText(_translate("MainWindow", "是"))
        self.question_5no_Button.setText(_translate("MainWindow", "否"))
        self.question_6yes_Button.setText(_translate("MainWindow", "是"))
        self.question_6no_Button.setText(_translate("MainWindow", "否"))
        self.question_4_comboBox.setItemText(0, _translate("MainWindow", "無"))
        self.question_4_comboBox.setItemText(1, _translate("MainWindow", "配戴眼鏡"))
        self.question_4_comboBox.setItemText(2, _translate("MainWindow", "配戴隱形眼鏡"))
        self.question_3_comboBox.setItemText(0, _translate("MainWindow", "僅室內共用燈光"))
        self.question_3_comboBox.setItemText(1, _translate("MainWindow", "僅室內專用燈光"))
        self.question_3_comboBox.setItemText(2, _translate("MainWindow", "室內共用與專用燈光皆有"))
        self.question_3_comboBox.setItemText(3, _translate("MainWindow", "戶外"))
        self.question_3_comboBox.setItemText(4, _translate("MainWindow", "光線明顯不足之環境"))
        self.question_3_comboBox.setItemText(5, _translate("MainWindow", "其他"))
        self.question_1_label.setText(_translate("MainWindow", "您此次施策時使用的電子產品為？"))
        self.question_2_label.setText(_translate("MainWindow", "您此次使用該電子產品的主要用途為？"))
        self.question_3_label.setText(_translate("MainWindow", "您此次紀錄時的環境光線有？"))
        self.question_4_label.setText(_translate("MainWindow", "您此次紀錄時有配戴眼鏡類產品？"))
        self.question_6_label.setText(_translate("MainWindow", "您此次紀錄是否有使用電腦增高架？"))
        self.question_5_label.setText(_translate("MainWindow", "您此次紀錄是否有產生眼睛疲勞等症狀？"))
        self.question_7_label.setText(_translate("MainWindow", "使用本系統後，您的眼睛疲勞程度是否有改善？"))
        self.question_8_label.setText(_translate("MainWindow", "此次紀錄時，關於\"眨眼\"的提醒是否準確？"))
        self.question_9_label.setText(_translate("MainWindow", "此次紀錄時，關於\"距離\"的提醒是否準確？"))
        self.question_12_label.setText(_translate("MainWindow", "備註/問題/是否有其他變因"))
        self.question_11_label.setText(_translate("MainWindow", "此次紀錄時，關於\"休息\"的提醒是否準確？"))
        self.question_10_label.setText(_translate("MainWindow", "此次紀錄時，關於\"亮度\"的提醒是否準確？"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
