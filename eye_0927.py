from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer, Qt 
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import (QApplication, QMessageBox, )
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5 import QtGui

import sqlite3
import cv2 as cv
import mediapipe as mp
import numpy as np
import time
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import matplotlib.dates 
import math
import Cover_ui as ui
import requests
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import shutil
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import logging


class Window(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.token = ''
        #self.line_token.setText(self.token)

        #self.camera = cv.VideoCapture(0)
        self.setupUi(self)
        self.nameBox.currentTextChanged.connect(lambda: self.user_list_onchange(1))
        self.nameBox_2.currentTextChanged.connect(lambda: self.user_list_onchange(2))
        self.nameBox_3.currentTextChanged.connect(lambda: self.user_list_onchange(3))
        #self.confirm_push.clicked.connect(self.confirm_push_onchange)
        self.Savefile.clicked.connect(self.add_push_onchange)

        self.distance_th.valueChanged.connect(self.update_threshold_values)
        self.bright_th.valueChanged.connect(self.update_threshold_values)
        self.blink_th.valueChanged.connect(self.update_threshold_values)
        
        self.blink_num_th.valueChanged.connect(self.update_threshold_values)
        self.blink_threshold_per_minute_value = self.blink_num_th.value()  # 默認設置為 slider 的初始值
        #self.blink_threshold_per_minute_value_1 = self.blink_num_th_1.value()
        
        self.camera_active = False

        #self.blink_bar.valueChanged.connect(self.blink_bar_onchange)
        #self.bright_bar.valueChanged.connect(self.bright_bar_onchange)
        #self.distance_bar.valueChanged.connect(self.distance_bar_onchange)

        self.working_time.valueChanged.connect(self.working_time_onchange)
        self.resting_time.valueChanged.connect(self.resting_time_onchange)
        self.start.clicked.connect(self.start_push_onchange)
        self.toolButton_finish.clicked.connect(self.finish_push_onchange)
        self.open_camera.clicked.connect(self.camera_onchange)
        self.suggestion.clicked.connect(self.suggestion_push_onchange)
        #self.want_line.clicked.connect(self.want_line_onchange)
        self.pushButton_sve.clicked.connect(self.save_numth_to_new_db)

        self.start.setEnabled(False)  # 禁用 Start 按鈕
        self.suggestion.setEnabled(False)  # 禁用 Start 按鈕

        self.login.clicked.connect(lambda: self.switch_page(1))
        self.Analysis.clicked.connect(lambda: self.switch_page(3))
        self.start.clicked.connect(lambda: self.switch_page(2))
        self.toolButton_finish.clicked.connect(lambda: self.switch_page(6))
        #self.back_to_home.clicked.connect(lambda: self.switch_page(0))
        self.Edit.clicked.connect(lambda: self.switch_page(5))
        self.Signup.clicked.connect(lambda: self.switch_page(4))
        #self.Savefile.clicked.connect(lambda: self.switch_page(0))
        #self.homebutton.clicked.connect(lambda: self.switch_page(0))
        self.login1_homebutton.clicked.connect(lambda: self.switch_page(0))
        self.login2_homebutton.clicked.connect(lambda: self.switch_page(0))
        self.analysis_homebutton.clicked.connect(lambda: self.switch_page(0))
        self.signup_homebutton.clicked.connect(lambda: self.switch_page(0))
        self.edit1_homebutton.clicked.connect(lambda: self.switch_page(0))
        #self.Sendout_Button.clicked.connect(lambda: self.switch_page(0))
        self.login1_homebutton.clicked.connect(self.shut_onchange)
        self.login2_homebutton.clicked.connect(self.shut_onchange)

        #timer
        self.timer_camera = QTimer() #初始化定時器
        self.timer_warm = QTimer() #初始化定時器
        self.timer_camera.timeout.connect(self.update_progress_value)
        self.timer_warm.timeout.connect(self.check_status)
        #self.tabWidget.currentChanged.connect(self.change_index)
        #self.main.tabBarClicked.connect(self.pushButton_func,0)
        #self.analyze.tabBarClicked.connect(self.pushButton_func,1)
        self.work_time = self.working_time.value()
        self.rest_time = self.resting_time.value()
        self.blink_thres = self.blink_th.value()
        self.bright_thres = self.bright_th.value()
        self.distance_thres = self.distance_th.value()
        self.blink_thres_2 = self.blink_th_2.value()
        self.bright_thres_2 = self.bright_th_2.value()
        self.distance_thres_2 = self.distance_th_2.value()
        self.exercise_type.addItem('None')
        self.exercise_type.addItem('close eye')
        self.exercise_type.addItem('jumping jack')

        self.blink_per_minute = 0 
        #self.blink_threshold_per_minute_value = self.blink_num_th.value()  # 默認設置為 slider 的初始值
        #self.blink_threshold_per_minute_value_1 = self.blink_num_th_1.value()  # 默認設置為 slider 的初始值
        
        #self.blink_num_th.valueChanged.connect(lambda: self.update_blink_threshold(self.blink_num_th.value()))
        #self.blink_num_th_1.valueChanged.connect(lambda: self.update_blink_threshold_1(self.blink_num_th_1.value()))


        # 初始化並監聽值的變化
        self.blink_th.valueChanged.connect(lambda: self.update_threshold(self.blink_th, self.blink_th_2))
        self.bright_th.valueChanged.connect(lambda: self.update_threshold(self.bright_th, self.bright_th_2))
        self.distance_th.valueChanged.connect(lambda: self.update_threshold(self.distance_th, self.distance_th_2))
        self.blink_num_th.valueChanged.connect(lambda: self.update_threshold(self.blink_num_th, self.blink_num_th_1))
        self.blink_num_th_1.valueChanged.connect(lambda: self.update_threshold(self.blink_num_th_1, self.blink_num_th))

    

        # 在 page_2 的初始化代碼中，監聽 user_name_input 的輸入變化
        #self.user_name_input.textChanged.connect(self.check_and_add_user)
        # 當使用者在 page_5 中輸入 line_token 時，連接信號到更新資料庫的函數
        #self.line_token_input.textChanged.connect(self.update_line_token_in_db)

        # 初始化疲勞狀態
        self.Exhausted_state = 0
        # 連接按鈕點擊事件
        self.pushButton_Exhausted.clicked.connect(self.pushButton_Exhausted_onchange)
        self.last_time_recorded = None  # 用來記錄上次的時間
        # 獲取 pushButton_Exhausted 和 listView 控件
        self.pushButton_Exhausted = self.findChild(QtWidgets.QPushButton, 'pushButton_Exhausted')
        self.listView = self.findChild(QtWidgets.QListView, 'listView')

        # 使用 QStandardItemModel 來管理 ListView 中的數據
        self.listView_model = QtGui.QStandardItemModel(self.listView)
        self.listView.setModel(self.listView_model)
        # variables 
        self.FONT_SIZE = 1
        # calendar
        #self.select_range.addItem('Every Minute')
        self.calendarWidget.selectionChanged.connect(self.calendar)

        self.frame_counter =0
        self.CEF_COUNTER =0
        self.total_blink =0
        self.eye_area= 800
        self.ratio = 0
        self.count = 0
        self.brightness_value = 0
        # constants
        self.eye_close_frame =1
        self.previous_time = 200
        self.area_record = np.ones(self.previous_time)
        self.FONTS =cv.FONT_HERSHEY_COMPLEX
        self.EYE_STATE = 0
        self.ratio_thres = 4.5
        self.eye_area_thres_high = 1500
        self.eye_area_thres_low = 200
        self.eye_area_record = 800
        self.eye_area_ratio = 0.7
        # face bounder indices 
        self.FACE_OVAL=[ 10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103,67, 109]
        self.FACE_OVAL_SIM = [156,383,397]
        # lips indices for Landmarks
        self.LIPS=[ 61, 146, 91, 181, 84, 17, 314, 405, 321, 375,291, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95,185, 40, 39, 37,0 ,267 ,269 ,270 ,409, 415, 310, 311, 312, 13, 82, 81, 42, 183, 78 ]
        self.LOWER_LIPS =[61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95]
        self.UPPER_LIPS=[ 185, 40, 39, 37,0 ,267 ,269 ,270 ,409, 415, 310, 311, 312, 13, 82, 81, 42, 183, 78] 
        # Left eyes indices 
        self.LEFT_EYE =[ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385,384, 398 ]
        self.LEFT_EYEBROW =[ 336, 296, 334, 293, 300, 276, 283, 282, 295, 285 ]
        # right eyes indices
        self.RIGHT_EYE=[ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ]  
        self.RIGHT_EYEBROW=[ 70, 63, 105, 66, 107, 55, 65, 52, 53, 46 ]
        # Center
        self.CENTER_POINT = [9,8,168]
        self.BODY = [22,20,18,16,14,12,24,23,11,13,15,17,19,21]
        self.HEAD = [8,6,5,4,0,1,2,3,7]
        self.map_face_mesh = mp.solutions.face_mesh
        self.status = 'run' # start # end
        self.blink_counter = 0
        self.area_counter = 0
        self.bright_counter = 0
        self.frame_counter = 0
        self.passing_time = 0

        #store minute information
        self.count_minute = 0 
        self.previous_minute = 0
        self.count_bright = 0
        self.count_blink = 0
        self.count_distance = 0

        #record time
        self.previous_time_step = 0
        self.now_time_step = 0
        self.pass_time = 0 
        self.time_status = 'start'
        

        #jump
        self.previous_state = -1
        self.count_hand = 0
        self.count_jump = 0
        self.shoulder_pos = []
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.current_user  = str(self.nameBox_2.currentText())
        # 連接主資料庫
        self.con = sqlite3.connect('C:/Users/ryan9/Downloads/專題/0923周/database.db')
        self.cursorObj = self.con.cursor()

        # 創建 `None` 和 `threshold` 表格
        self.cursorObj.execute('''
            CREATE TABLE IF NOT EXISTS None(
                year INTEGER, 
                month INTEGER, 
                day INTEGER, 
                hour INTEGER, 
                minute INTEGER, 
                distance REAL, 
                brightness INTEGER, 
                blink INTEGER, 
                state INTEGER, 
                Exhausted_state INTEGER
            );
        ''')
        self.cursorObj.execute('''
            CREATE TABLE IF NOT EXISTS threshold(
                user TEXT UNIQUE, 
                line_token TEXT, 
                distance_area REAL, 
                distance_ratio REAL, 
                brightness INTEGER, 
                blink INTEGER
            );
        ''')
        # 插入一筆初始數據
        self.cursorObj.execute('''
            INSERT OR IGNORE INTO threshold(
                user, line_token, distance_area, distance_ratio, brightness, blink
            ) VALUES (?, ?, ?, ?, ?, ?)''',
            ('None', '', self.eye_area_record, self.eye_area_ratio, 60, 4)
        )
        self.con.commit()

        # 讀取 threshold 表數據並更新界面
        cursor = self.cursorObj.execute("SELECT * FROM threshold").fetchall()
        for row in cursor:
            self.nameBox.addItem(row[0])
            self.nameBox_2.addItem(row[0])
            self.nameBox_3.addItem(row[0])
            print(row)

        # 創建 assessment 資料庫並建立 pretest 表格
        self.new_con = sqlite3.connect('C:/Users/ryan9/Downloads/專題/0923周/assessment_database.db')
        self.new_cursorObj = self.new_con.cursor()
        self.new_cursorObj.execute('''
            CREATE TABLE IF NOT EXISTS pretest (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                username TEXT,
                birthday TEXT,
                gender TEXT,
                right_eye_condition TEXT,
                right_eye_degree TEXT,
                right_eye_shine TEXT,
                right_eye_shine_degree REAL,
                left_eye_condition TEXT,
                left_eye_degree REAL,
                left_eye_shine TEXT,
                left_eye_shine_degree REAL,
                eye_situation_value1 INTEGER,
                eye_situation_value2 INTEGER,
                eye_situation_value3 INTEGER,
                eye_situation_value4 INTEGER,
                eye_situation_value5 INTEGER,
                use_situation1 TEXT,
                use_situation2 TEXT,
                use_situation3 TEXT,
                use_situation_value4 INTEGER,
                use_situation_value5 INTEGER,
                habit1 TEXT,
                habit2 TEXT,
                habit3 TEXT,
                habit4 TEXT,
                habit5 TEXT,
                habit6 TEXT,
                habit7 TEXT,
                line_token TEXT
            );
        ''')
        
        # 創建 posttest 表格
        self.new_cursorObj.execute('''
            CREATE TABLE IF NOT EXISTS posttest (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_1 TEXT,
                question_2 TEXT,
                question_3 TEXT,
                question_4 TEXT,
                question_5 TEXT,
                question_6 TEXT,        
                question_7 INTEGER,
                question_8 INTEGER,
                question_9 INTEGER,
                question_10 INTEGER,
                question_11 INTEGER,
                question_12 TEXT,
                submission_time TEXT  -- 填表的時間
            );
        ''')
        self.new_con.commit()

        # 嘗試查詢 posttest 表的 submission_time 欄位
        try:
            self.new_cursorObj.execute('SELECT submission_time FROM posttest LIMIT 1')
        except sqlite3.OperationalError:
            # 如果出現 OperationalError，說明表格或欄位不存在，嘗試修改
            self.new_cursorObj.execute('''
                ALTER TABLE posttest ADD COLUMN submission_time TEXT;
            ''')
            self.new_con.commit()
            print("submission_time 列已添加")

        # 設置按鈕點擊事件
        self.Sendout_Button.clicked.connect(self.sendout)
        self.Savefile.clicked.connect(self.Save)

        print("Save button connected to posttest and pretest")

    def shut_onchange(self):
        self.status = 'shutting_down'
    def save_data_to_new_db(self):
        try:
            # Collect data from the UI
            name = self.name_input.text()
            username = self.user_name_input.text()
            birthday = self.birthday_input.text()
            line_token = self.line_token_input.text()
            gender = '男生' if self.sex_man_button.isChecked() else '女生'

            right_eye_condition = '近視' if self.right_eye_in_button.isChecked() else '遠視'
            right_eye_degree = self.right_eye_degree_input.text()
            right_eye_shine = '有' if self.right_eye_shine_button.isChecked() else '無'
            right_eye_shine_degree = self.right_eye_shine_input.text()

            left_eye_condition = '近視' if self.left_eye_in_button.isChecked() else '遠視'
            left_eye_degree = self.left_eye_degree_input.text()
            left_eye_shine = '有' if self.left_eye_shine_button.isChecked() else '無'
            left_eye_shine_degree = self.left_eye_shine_input.text()

            eye_situation_value1 = self.eye_situation_slider1.value()
            eye_situation_value2 = self.eye_situation_slider2.value()
            eye_situation_value3 = self.eye_situation_slider3.value()
            eye_situation_value4 = self.eye_situation_slider4.value()
            eye_situation_value5 = self.eye_situation_slider5.value()

            use_situation1 = '是' if self.use_situation_yes_button1.isChecked() else '否'
            use_situation2 = self.use_situation2_combobox.currentText()
            use_situation3 = '是' if self.use_situation_yes_button3.isChecked() else '否'
            use_situation_value4 = self.use_situation_slider4.value()
            use_situation_value5 = self.use_situation_slider5.value()

            habit1 = '是' if self.habit_yes_button1.isChecked() else '否'
            habit2 = self.habit_combobox2.currentText()
            habit3 = self.habit_combobox3.currentText()
            habit4 = self.habit_combobox4.currentText()
            habit5 = self.habit_combobox5.currentText()
            habit6 = self.habit_combobox6.currentText()

            habit7 = []
            if self.habit_close_checkbox7.isChecked():
                habit7.append('閉目養神')
            if self.habit_exercise_checkbox7.isChecked():
                habit7.append('眼部運動')
            if self.habit_other_checkbox7.isChecked():
                habit7.append('其他')
            habit7_str = ', '.join(habit7)

            

            # Validation: Check if required fields are filled
            if not (name and username and birthday):
                QMessageBox.warning(self, "錯誤", "請填寫完整")
                return
            

            # Check if the username already exists in the database
            self.new_cursorObj.execute('SELECT * FROM pretest WHERE username = ?', (username,))
            username_result = self.new_cursorObj.fetchone()

            if username_result:
                # If a matching username is found, ask the user if they want to update the existing record
                reply = QMessageBox.question(self, "提示", "該使用者已存在，是否要更新資料?", 
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if reply == QMessageBox.Yes:
                    # User chose Yes, delete the existing record and proceed to save new data
                    self.new_cursorObj.execute('DELETE FROM pretest WHERE username = ?', (username,))
                    self.new_con.commit()  # Commit the deletion

                    # Now save the new data
                    self.new_cursorObj.execute('''
                        INSERT INTO pretest (
                            name, username, birthday, gender, 
                            right_eye_condition, right_eye_degree, right_eye_shine, right_eye_shine_degree,
                            left_eye_condition, left_eye_degree, left_eye_shine, left_eye_shine_degree,
                            eye_situation_value1, eye_situation_value2, eye_situation_value3, eye_situation_value4, eye_situation_value5,
                            use_situation1, use_situation2, use_situation3, use_situation_value4, use_situation_value5,
                            habit1, habit2, habit3, habit4, habit5, habit6, habit7, line_token
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        name, username, birthday, gender, 
                        right_eye_condition, right_eye_degree, right_eye_shine, right_eye_shine_degree,
                        left_eye_condition, left_eye_degree, left_eye_shine, left_eye_shine_degree,
                        eye_situation_value1, eye_situation_value2, eye_situation_value3, eye_situation_value4, eye_situation_value5,
                        use_situation1, use_situation2, use_situation3, use_situation_value4, use_situation_value5,
                        habit1, habit2, habit3, habit4, habit5, habit6, habit7_str, line_token
                    ))

                    # Commit the new data
                    self.new_con.commit()

                    # Show success message and switch page
                    success_msg = QMessageBox()
                    success_msg.setText("資料已更新")
                    success_msg.setIcon(QMessageBox.Information)
                    success_msg.setWindowTitle("成功")
                    success_msg.buttonClicked.connect(lambda: self.switch_page(0))  # Switch to page_0 after clicking "OK"
                    success_msg.exec()

                else:
                    # User chose No, do not save the data
                    QMessageBox.information(self, "取消", "儲存動作已取消")
                    return  # Exit the function without saving

            else:
                # If no matching username, proceed to save the new data
                self.new_cursorObj.execute('''
                    INSERT INTO pretest (
                        name, username, birthday, gender, 
                        right_eye_condition, right_eye_degree, right_eye_shine, right_eye_shine_degree,
                        left_eye_condition, left_eye_degree, left_eye_shine, left_eye_shine_degree,
                        eye_situation_value1, eye_situation_value2, eye_situation_value3, eye_situation_value4, eye_situation_value5,
                        use_situation1, use_situation2, use_situation3, use_situation_value4, use_situation_value5,
                        habit1, habit2, habit3, habit4, habit5, habit6, habit7, line_token
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    name, username, birthday, gender, 
                    right_eye_condition, right_eye_degree, right_eye_shine, right_eye_shine_degree,
                    left_eye_condition, left_eye_degree, left_eye_shine, left_eye_shine_degree,
                    eye_situation_value1, eye_situation_value2, eye_situation_value3, eye_situation_value4, eye_situation_value5,
                    use_situation1, use_situation2, use_situation3, use_situation_value4, use_situation_value5,
                    habit1, habit2, habit3, habit4, habit5, habit6, habit7_str, line_token
                ))

                # Commit the new data
                self.new_con.commit()

                # Show success message and switch page
                success_msg = QMessageBox()
                success_msg.setText("已存檔")
                success_msg.setIcon(QMessageBox.Information)
                success_msg.setWindowTitle("成功")
                success_msg.buttonClicked.connect(lambda: self.switch_page(0))  # Switch to page_0 after clicking "OK"
                success_msg.exec()

        except Exception as e:
            # Show error message in case of failure
            QMessageBox.warning(self, "錯誤", f"存檔失敗: {str(e)}")

    def sendout(self):
        # 獲取當下的時間
        current_time = datetime.now()
        
        # 查詢最近一次的提交時間
        self.new_cursorObj.execute('SELECT submission_time FROM posttest ORDER BY id DESC LIMIT 1')
        last_submission = self.new_cursorObj.fetchone()

        if last_submission:
            # 將 submission_time 字串轉換為 datetime 格式
            last_submission_time = datetime.strptime(last_submission[0], '%Y-%m-%d %H:%M:%S')
            
            # 計算距離上次提交的時間差
            time_difference = current_time - last_submission_time

            if time_difference < timedelta(minutes=2):
                # 如果時間差小於2分鐘，顯示提示訊息並返回
                msg_box = QtWidgets.QMessageBox(self)
                msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                msg_box.setText(f"請稍候 {int(2 - time_difference.total_seconds() // 60)} 分鐘再提交")
                msg_box.setWindowTitle("過於頻繁的提交")
                msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg_box.exec_()
                return  # 結束函數，避免提交
        else:
            print("沒有找到上次提交的記錄，允許提交。")

        # 繼續執行資料插入
        question_1_choice = self.question_1_comboBox.currentText()
        question_2_choice = self.question_2_comboBox.currentText()
        question_3_choice = self.question_3_comboBox.currentText()
        question_4_choice = self.question_4_comboBox.currentText()

        question_5_choice = '是' if self.question_5yes_Button.isChecked() else '否'
        question_6_choice = '是' if self.question_6yes_Button.isChecked() else '否'

        question_7_value = self.question_7_Slider.value()
        question_8_value = self.question_8_Slider.value()
        question_9_value = self.question_9_Slider.value()
        question_10_value = self.question_10_Slider.value()
        question_11_value = self.question_11_Slider.value()

        question_12_text = self.question_12_input.text()
        
        # 獲取當下的時間作為 submission_time
        submission_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

        # 插入新資料到資料庫
        self.new_cursorObj.execute('''
            INSERT INTO posttest (
                question_1, question_2, question_3, question_4, 
                question_5, question_6, question_7, question_8, 
                question_9, question_10, question_11, question_12, submission_time
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            question_1_choice, question_2_choice, question_3_choice, question_4_choice,
            question_5_choice, question_6_choice, question_7_value, question_8_value,
            question_9_value, question_10_value, question_11_value, question_12_text, submission_time
        ))
        self.new_con.commit()

        print(f"資料已存入 posttest，提交時間為 {submission_time}")

        # 顯示成功訊息
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setText("已送出")
        msg_box.setWindowTitle("確認")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.buttonClicked.connect(lambda: self.switch_page(0))
        msg_box.exec_()

    
    #def update_blink_thres_2(self):
    #    # 將 blink_th_2 的值設置為與 blink_th 相同
    #    self.blink_th_2.setValue(self.blink_th.value())
    #def update_bright_thres_2(self):
    #    self.bright_th_2.setValue(self.bright_th.value())
    #def update_distance_thres_2(self):
    #    self.distance_th_2.setValue(self.distance_th.value())
    # 讓 blink_th 和 blink_th_2 的值保持一致
        self.blink_th_2.setValue(self.blink_th.value())

    def update_threshold(self, source, target):
        # 更新 target 的值為 source 的值
        target.setValue(source.value())
    

    def check_and_add_user(self):
        # 獲取使用者輸入的 user_name
        user_name = self.user_name_input.text()

        # 如果 user_name 輸入框不為空
        if user_name:
            try:
                # 檢查該 user_name 是否已經存在於 threshold 表中
                query = "SELECT COUNT(*) FROM threshold WHERE user = ?"
                self.cursorObj.execute(query, (user_name,))
                result = self.cursorObj.fetchone()

                # 如果使用者不存在於資料庫中，則新增該使用者
                if result[0] == 0:
                    # 新增該使用者到 threshold 表
                    self.cursorObj.execute("INSERT INTO threshold (user) VALUES (?)", (user_name,))
                    self.con.commit()
                    print(f"New user {user_name} added to the database.")
                else:
                    print(f"User {user_name} already exists in the database.")

                # 將該 user_name 設為 current_user
                self.current_user = user_name
                print(f"Current user set to {self.current_user}")

            except sqlite3.Error as e:
                print(f"Database error: {e}")

        else:
            print("User name input is empty, no action taken.")



    
    def update_line_token_in_db(self):
        # 獲取使用者在 line_token_input 中輸入的值
        line_token = self.line_token_input.text()

        # 使用 self.current_user 作為資料庫更新的依據
        user_name = self.current_user  # 這應該是選中的使用者名稱

        # 檢查 line_token 是否有值，並且確保已選擇使用者名稱
        if line_token and user_name:
            try:
                # 更新資料庫中的 line_token 欄位，根據選擇的 user_name
                query = "UPDATE threshold SET line_token = ? WHERE user = ?"
                self.cursorObj.execute(query, (line_token, user_name))

                # 如果沒有該使用者的資料，則插入新的記錄
                if self.cursorObj.rowcount == 0:
                    self.cursorObj.execute(
                        "INSERT INTO threshold (user, line_token) VALUES (?, ?)",
                        (user_name, line_token)
                    )

                # 提交變更
                self.con.commit()
                print(f"Line token for user {user_name} updated successfully.")

            except sqlite3.Error as e:
                print(f"Database error: {e}")

        else:
            print("Line token is empty or no user selected, no update performed.")


    def Save(self):
        self.check_and_add_user()
        self.update_line_token_in_db()
        self.save_data_to_new_db()
    
        
    def switch_page(self, index):
        self.stackedWidget.setCurrentIndex(index)

    #def __del__(self):
        #self.update_database()
        #self.summary_report()
        #self.connection.close()
    #def closeEvent(self, event):
        #self.summary_report()

    def lineNotifyMessage(self,msg):
        try:
            headers = {
                "Authorization": "Bearer " + self.token, 
                "Content-Type" : "application/x-www-form-urlencoded"
            }
            
            payload = {'message': msg}
            r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
        except:
            pass

    def summary_report(self):
        # 取得今天的日期
        year = datetime.today().strftime("%Y")
        month = datetime.today().strftime("%m")
        day = datetime.today().strftime("%d")
        today_date = datetime.today().strftime("%Y-%m-%d")
        
        self.cursorObj = self.con.cursor()

        # 查詢當天所有的記錄
        cursor = self.cursorObj.execute(
            "SELECT year, month, day, hour, minute, distance, brightness, blink, state, Exhausted_state FROM %s WHERE year=%s AND month=%s AND day=%s ORDER BY hour, minute" 
            % (self.current_user, year, month, day)
        )
        
        records = cursor.fetchall()

        # 記錄開始時間
        start_time = self.init_time
        start_hour = int(datetime.fromtimestamp(start_time).strftime("%H"))
        start_minute = int(datetime.fromtimestamp(start_time).strftime("%M"))

        # 用於當次和當日的變量
        total_dis, total_bri, total_blink = [], [], []
        dis_session, bri_session, blink_session = [], [], []
        use_time_total, rest_time_total = 0, 0
        use_time_session, rest_time_session = 0, 0
        exercise_types = []  # 記錄當次的運動方式
        last_state = None

        # 當次使用計算起始flag
        in_session = False
        current_exercise = None

        # 迭代當天的所有記錄
        for i in records:
            current_time = datetime(int(i[0]), int(i[1]), int(i[2]), int(i[3]), int(i[4]))
            state = i[8]  # 狀態
            distance = float(i[5])
            brightness = int(i[6])
            blink = int(i[7])

            # 計算當日使用狀況
            if state == 2:  # 工作狀態
                use_time_total += 1
                total_dis.append(distance)
                total_bri.append(brightness)
                total_blink.append(blink)

            # 開始計算當次使用情形
            if (i[3] > start_hour or (i[3] == start_hour and i[4] >= start_minute)) and state == 2:
                # 如果當前時間是工作狀態且在開始時間之後，記錄當次使用情形
                use_time_session += 1
                dis_session.append(distance)
                bri_session.append(brightness)
                blink_session.append(blink)
                in_session = True
            elif in_session and state == 0:
                # 記錄休息狀態並加入運動方式
                rest_time_session += 1
                rest_time_total += 1
                if current_exercise:
                    exercise_types.append(current_exercise)

            # 記錄當前休息時選擇的運動方式
            if state == 0:
                current_exercise = self.exercise_type.currentText()  # 記錄當前運動類型
            else:
                current_exercise = None

        # 計算當次使用平均值
        avg_dis_session = round(sum(dis_session) / len(dis_session), 2) if dis_session else 0.00
        avg_bri_session = round(sum(bri_session) / len(bri_session), 2) if bri_session else 0.00
        avg_blink_session = round(sum(blink_session) / len(blink_session), 2) if blink_session else 0.00

        # 計算當日使用平均值
        avg_dis_total = round(sum(total_dis) / len(total_dis), 2) if total_dis else 0.00
        avg_bri_total = round(sum(total_bri) / len(total_bri), 2) if total_bri else 0.00
        avg_blink_total = round(sum(total_blink) / use_time_total, 2) if use_time_total > 0 else 0.00

        # 獲取所有不同的運動類型
        exercise_types_report = ', '.join(set(exercise_types)) if exercise_types else '無'

        # 組裝報告訊息
        message = (
            f"【EyesMyself】 {today_date}\n"
            f"--- 當次使用情形 ---\n"
            f"使用時間: {use_time_session} 分鐘\n"
            f"休息時間: {rest_time_session} 分鐘\n"
            f"平均距離: {avg_dis_session}\n"
            f"平均亮度: {avg_bri_session}\n"
            f"平均眨眼次數: {avg_blink_session}\n"
            f"休息方式: {exercise_types_report}\n\n"
            f"--- 今日使用情形 ---\n"
            f"使用時間: {use_time_total} 分鐘\n"
            f"休息時間: {rest_time_total} 分鐘\n"
            f"平均距離: {avg_dis_total}\n"
            f"平均亮度: {avg_bri_total}\n"
            f"平均眨眼次數: {avg_blink_total}"
        )

        # 發送LINE通知
        self.lineNotifyMessage(message)

        # 打印到控制台
        print(message)
    
    def want_line_onchange(self):
        # Check if the line_token_input has a value to enable LINE notifications automatically
        if self.line_token_input.text():  # If the line_token_input has a value
            self.line_token_input.setEnabled(True)  # Enable the line_token field
            self.line_token_input.setText(self.line_token_input.text())  # Set the line token text
            print("LINE notifications enabled for user:", self.current_user)
            # Optionally send a notification that LINE is set up
            #self.lineNotifyMessage("Notification setup complete for this user.")
        else:
            # If no line_token is found, disable the line_token input field
            self.line_token_input.setEnabled(False)
            self.line_token_input.clear()  # Clear the line token field if no token is found
            print("LINE notifications disabled (no token found) for user:", self.current_user)


    #新增blink per minute            
    def update_blink_threshold(self, value):
        self.blink_threshold_per_minute_value  = value
    def update_blink_threshold_1(self, value):
        self.blink_threshold_per_minute_value_1 = value  # 更新 self.blink_threshold_per_minute_value_1
    '''#新增tired
    def tired_button_onchange(self):
        if self.status == 'start':  # 仅在使用状态下允许更改疲劳状态
            self.tired_state = 1  # 设置为疲劳状态
            #self.record_tired_state()
            #self.tired_state = 0  # 重置疲劳状态
            self.showDialog("Tired state recorded")
        else:
            self.showDialog("Cannot record tired state during rest")'''
    
    def save_numth_to_new_db(self):
            try:
                # 取得 UI 中的閾值與選取的使用者名稱
                distance_record = self.distance_th_2.value()
                brightness_record = self.bright_th_2.value()
                blink_record = self.blink_th_2.value()
                user = self.nameBox_2.currentText()

                # 檢查該使用者是否已存在於資料庫中
                self.cursorObj.execute('SELECT * FROM threshold WHERE user = ?', (user,))
                username_result = self.cursorObj.fetchone()

                if username_result:
                    # 如果使用者存在，更新該使用者的數據
                    self.cursorObj.execute('''
                        UPDATE threshold
                        SET distance_ratio = ?, brightness = ?, blink = ?
                        WHERE user = ?
                    ''', (distance_record, brightness_record, blink_record, user))

                    # 提交更新數據
                    self.con.commit()

                    # 顯示成功訊息並切換頁面
                    success_msg = QMessageBox()
                    success_msg.setText("資料已更新")
                    success_msg.setIcon(QMessageBox.Information)
                    success_msg.setWindowTitle("成功")
                    success_msg.exec()

                else: 
                    # 如果使用者不存在，顯示錯誤訊息
                    QMessageBox.information(self, "錯誤", "使用者不存在")

            except Exception as e:
                # 在發生錯誤時顯示錯誤訊息
                QMessageBox.warning(self, "錯誤", f"存檔失敗: {str(e)}")

    def change_index(self,value):
        self.stackedWidget.setCurrentIndex(value)
                
    def user_list_onchange(self, user=1):
        # Update the current user based on the selection from the dropdown
        if user == 1:
            self.current_user = str(self.nameBox.currentText())
        elif user == 2:
            self.current_user = str(self.nameBox_2.currentText())
        elif user == 3:
            self.current_user = str(self.nameBox_3.currentText())

        # Synchronize all name boxes with the selected user
        self.nameBox_2.setCurrentText(self.current_user)
        self.nameBox.setCurrentText(self.current_user)

        # Connect to the SQLite database
        self.con = sqlite3.connect('C:/Users/ryan9/Downloads/專題/0923周/database.db')
        self.cursorObj = self.con.cursor()

        # Fetch distance_ratio, brightness, blink, and line_token values from threshold table for the selected user
        query = "SELECT distance_ratio, brightness, blink, line_token FROM threshold WHERE user = ?"
        self.cursorObj.execute(query, (self.current_user,))
        result = self.cursorObj.fetchone()

        # Update the UI fields with the values from the database
        if result:
            distance_ratio, brightness, blink, line_token = result
            self.distance_th.setValue(float(distance_ratio))
            self.bright_th.setValue(int(brightness))
            self.blink_th.setValue(float(blink))
            
            # Check if line_token exists, if so, set it and enable LINE Notify
            if line_token:
                self.token = line_token  # Store the token for LINE Notify
                self.line_token_input.setText(line_token)  # Set the token in the UI field
                self.want_line_onchange()  # Call the method to enable LINE notifications
            else:
                # No line_token found, disable the input field or clear it
                self.line_token_input.clear()
                print(f"No line_token found for user {self.current_user}")
            
        else:
            print(f"No data found for user {self.current_user}")

        # Commit and close the database connection
        self.con.commit()


    def update_threshold_values(self):
        # Get the updated values from the UI fields
        distance_ratio = self.distance_th.value()
        brightness = self.bright_th.value()
        blink = self.blink_th.value()
        blink_num_th = self.blink_num_th.value()
        # Get the current user from the dropdown
        current_user = self.current_user

        try:
            # Update the threshold values in the database
            update_query = """
            UPDATE threshold 
            SET distance_ratio = ?, brightness = ?, blink = ? 
            WHERE user = ?
            """
            self.cursorObj.execute(update_query, (distance_ratio, brightness, blink, current_user))
            
            # Commit the changes (do not close the connection)
            self.con.commit()
            print(f"Threshold values updated for user {current_user}")
        
        except sqlite3.Error as e:
            print(f"Error updating threshold: {e}")

        


    def add_user_onchange(self):
        pass

    def camera_onchange(self):
        self.start_time = time.time()
        self.status = 'run'
        self.camera = cv.VideoCapture(0)
        self.timer_camera.start(5)
        self.timer_warm.start(30)
        self.camera_active = True
        self.start.setEnabled(True)
        self.suggestion.setEnabled(True)
        self.update_progress_value()
        # Get the current user
        current_user = str(self.nameBox_2.currentText())  # Fetch current selected user from nameBox_2
        
        # Get the current threshold values
        distance_ratio = self.distance_th.value()
        brightness = self.bright_th.value()
        blink = self.blink_th.value()

        # Log the values for debug purposes (can remove in production)
        print(f"Distance Ratio: {distance_ratio}, Brightness: {brightness}, Blink: {blink}")

        # Update the database with the new threshold values
        try:
            self.cursorObj.execute('''
                UPDATE threshold 
                SET distance_ratio = ?, brightness = ?, blink = ? 
                WHERE user = ?
            ''', (distance_ratio, brightness, blink, current_user))

            # Commit the changes to the database
            self.con.commit()
            print(f"Threshold values updated for user {current_user}")

        except sqlite3.Error as e:
            print(f"Error updating threshold: {e}")
        
    def start_push_onchange(self): 
        self.line_token_input.setText(self.token)
        #if (self.want_line.isChecked()):
        self.lineNotifyMessage('start')
        self.counter = -1
        self.pass_time = 0.01
        self.status = 'start'
        self.time_status = 'work'
        self.previous_minute = 0
        self.init_time = time.time()
        self.previous_time_step = time.time()
        self.camera_active = False

    #新增Exhausted
    def pushButton_Exhausted_onchange(self):
        if self.status == 'start':  # 僅在使用狀態下允許更改疲勞狀態
            self.Exhausted_state = 1  # 設置為疲勞状態
            current_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
            
             # 如果當前時間與上次記錄的時間相同則不再添加
            if self.last_time_recorded != current_time:
                # 在 ListView 中添加新的時間條目
                item = QtGui.QStandardItem(f"  {current_time}")
                self.listView_model.appendRow(item)  # 添加時間到 ListView 中

                # 更新記錄的時間
                self.last_time_recorded = current_time
                # 顯示訊息
                message = 'Exhausted state recorded'
                self.lineNotifyMessage(message)

                self.showMainWindow(message,line=False)
                    # 發送LINE提醒，不依賴視窗點擊                        
                #self.lineNotifyMessage(message)
            else:
                self.showMainWindow(f"Already recorded at {current_time}")
        else:
            # 非工作狀態下提示無法記錄
            self.showMainWindow("Cannot record tired state during rest")

    def finish_push_onchange(self):
        self.time_status = 'finished'
        self.status = 'shutting_down'
        self.is_running = False  # 停止推理運行
        self.release_resources()  # 釋放與推理相關的資源
        logging.getLogger('tensorflow').setLevel(logging.ERROR)  # 停止時只顯示錯誤級別的日誌
        # 關閉相機和停止推理
        if self.camera is not None:
            self.camera.release()

    def run_inference(self):
        # 執行推理過程的函數
        if not self.is_running:
            return  # 停止推理
        # 進行推理的代碼


    def release_resources(self):
        '''# 如果有模型需要釋放，檢查模型是否存在
        if hasattr(self, 'model') and self.model is not None:
            del self.model'''
    
        # 如果有 session 或推理進程
        if hasattr(self, 'session') and self.session is not None:
            self.session.close()

        print("所有推理相關資源已釋放")


    def calendar(self):
        selectDay = self.calendarWidget.selectedDate()
        year = selectDay.toString("yyyy")
        month =  selectDay.toString("M")
        day =  selectDay.toString("d")
        print(year,month,day)

        self.cursorObj = self.con.cursor()
        #self.cursorObj.execute("SELECT EXISTS(SELECT 1 FROM threshold WHERE user=? LIMIT 1)", ('default',))
        cursor = self.cursorObj.execute("SELECT year, month, day, hour, minute, distance, brightness, blink, state from %s WHERE year= %s AND month=%s AND day=%s " %(self.current_user,year,month,day,))
        self.con.commit() 
        #print(cursor.fetchall())
        date = []
        dis = []
        bri = []
        blink = []
        use = []
        for i in cursor:
            date.append(datetime(i[0], i[1], i[2], i[3],i[4]))
            use.append(i[8])
            dis.append(float(i[5]))
            bri.append(int(i[6]))
            blink.append(int(i[7]))
        print(date)
        xfmt = matplotlib.dates.DateFormatter('%H:%M')
        datestime = matplotlib.dates.date2num(date)
        print((datestime, dis))
        plt.gca().xaxis.set_major_formatter(xfmt)
        plt.plot_date(datestime, use,linestyle='solid')
        plt.yticks([0, 1, 2])
        plt.ylim(-0.1, 2.1)
        plt.title('Using Time')
        plt.savefig('use.png')
        plt.close()

        plt.gca().xaxis.set_major_formatter(xfmt)
        self.display_image(cv.imread('use.png'),(400,270),self.use_time_graph )
        plt.plot_date(datestime, dis,linestyle='solid')
        plt.ylim(0,2)
        plt.title('Distance')
        plt.savefig('dis.png')
        plt.close()

        plt.gca().xaxis.set_major_formatter(xfmt)
        self.display_image(cv.imread('dis.png'),(400,270),self.distance_graph )
        plt.plot_date(datestime, bri,linestyle='solid')
        plt.ylim(0,255)
        plt.title('Brightness')
        plt.savefig('bri.png')
        plt.close()

        plt.gca().xaxis.set_major_formatter(xfmt)
        self.display_image(cv.imread('bri.png'),(400,270),self.brightness_graph )
        plt.plot_date(datestime, blink,linestyle='solid')
        plt.ylim(0,60)
        plt.title('Blinking')
        plt.savefig('blink.png')
        plt.close()
        self.display_image(cv.imread('blink.png'),(400,270),self.blink_graph )

    '''def display_image(self,img,size,target):
        show = cv.resize(img,size)
        #show = cv.cvtColor(show, cv.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1],show.shape[0],QImage.Format_RGB888)
        target.setPixmap(QPixmap.fromImage(showImage))'''
    
    def display_image(self, img, size, target):
        if img is None:
            print("Error: Could not load image.")
            return
    
        resized_image = cv.resize(img, size)
        # 將圖像轉換為 QImage 格式
        height, width, channel = resized_image.shape
        bytesPerLine = 3 * width
        q_img = QImage(resized_image.data, width, height, bytesPerLine, QImage.Format_RGB888)
    
        pixmap = QPixmap.fromImage(q_img)
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
    
        target.setScene(scene)
        target.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)



    def add_push_onchange(self):
        # 獲取使用者輸入的名稱
        text = str(self.user_name_input.text())

        # 檢查名稱是否為空
        if text == '':
            print('名稱為空，無法新增')
            return  # 名稱為空，直接返回

        # 檢查名稱是否已經存在於下拉選單中
        for i in range(self.nameBox.count()):
            if self.nameBox.itemText(i) == text:
                print(f'名稱 "{text}" 已經存在，無法新增')
                return  # 名稱已存在，直接返回

        # 名稱有效且未重複，新增到下拉選單
        self.nameBox.addItem(text)
        self.nameBox_2.addItem(text)
        self.nameBox_3.addItem(text)
        if (text != ''):
            self.con = sqlite3.connect('C:/Users/ryan9/Downloads/專題/0923周/database.db')
            self.cursorObj = self.con.cursor()
            try:
                self.cursorObj.execute('create table if not exists %s (year, month, day, hour, minute, distance, brightness, blink, state, Exhausted_state)' %(text))
                self.cursorObj.execute("insert or ignore into threshold(user,line_token,  distance_area, distance_ratio, brightness, blink) VALUES (?,?,?,?,?,?)" ,(text,self.line_token_input.text(),self.eye_area_record,self.eye_area_ratio,60,4))
                self.con.commit()
            except:
                self.showMainWindow('Not valid name!')
        else:
            print('empty')


    def working_time_onchange(self):
        self.work_time = self.working_time.value()

    def resting_time_onchange(self):
        self.rest_time = self.resting_time.value()

    def suggestion_push_onchange(self):
        br = self.ratio*1.08
        bv = self.brightness_value*0.65
        dis = 0.7
        self.blink_th.setValue(br)
        self.bright_th.setValue(bv)
        self.distance_th.setValue(dis)
        self.eye_area_record = self.eye_area
        self.update_database()
    
    def update_database(self):
        query = "UPDATE threshold SET distance_area = ?, distance_ratio = ?, brightness = ?, blink = ? WHERE user = ?"
        
        # 更新第一組閾值
        self.cursorObj.execute(query, (self.eye_area, self.distance_th.value(), self.bright_th.value(), self.blink_th.value(), self.current_user))
        
        # 更新第二組閾值
        self.cursorObj.execute(query, (self.eye_area, self.distance_th_2.value(), self.bright_th_2.value(), self.blink_th_2.value(), self.current_user))
        
        self.con.commit()



    '''def blink_threshold_onchange(self):
        self.blink_thres = self.blink_th.value()
        self.blink_thres_2 = self.blink_th_2.value()
        #self.blink_bar.setValue(int(self.blink_thres * 10))

    def bright_threshold_onchange(self):
        self.bright_thres = self.bright_th.value()
        self.bright_thres_2 = self.bright_th_2.value()
        #self.bright_bar.setValue(int(self.bright_thres))

    def distance_threshold_onchange(self):
        self.distance_thres = self.distance_th.value()
        self.distance_thres_2 = self.distance_th_2.value()
        #self.distance_bar.setValue(int(self.distance_thres*100))'''

    def check_status(self):
        if (self.status == 'start'):
            if(self.area_counter>2):
                self.showMainWindow('Too close',line=True)

                self.area_counter = 0
            if(self.bright_counter >20):
                self.showMainWindow('Too dim')
                self.bright_counter = 0
        

    ''' eye detection function '''

    def PolyArea(self,x,y):
        return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

    # landmark detection function 
    def landmarksDetection(self,img, results, draw=False,body=False):
        img_height, img_width= img.shape[:2]
        # list[(x,y), (x,y)....]
        if(body==False):
            mesh_coord = [(int(point.x * img_width), int(point.y * img_height)) for point in results.multi_face_landmarks[0].landmark]
        else:
            mesh_coord = [(int(point.x * img_width), int(point.y * img_height)) for point in results.pose_world_landmarks.landmark]
        if draw :
            [cv.circle(img, p, 2, (0,255,0), -1) for p in mesh_coord]
        # returning the list of tuples for each landmarks 
        return mesh_coord

    # Euclaidean distance 
    def euclaideanDistance(self,point, point1):
        x, y = point
        x1, y1 = point1
        distance = math.sqrt((x1 - x)**2 + (y1 - y)**2)
        return distance

    def blinkRatio(self,img, landmarks, right_indices, left_indices):
        # Right eyes 
        # horizontal line 
        rh_right = landmarks[right_indices[0]]
        rh_left = landmarks[right_indices[8]]
        # vertical line 
        rv_top = landmarks[right_indices[12]]
        rv_bottom = landmarks[right_indices[4]]
        # draw lines on right eyes 
        # LEFT_EYE 
        # horizontal line 
        lh_right = landmarks[left_indices[0]]
        lh_left = landmarks[left_indices[8]]
        # vertical line 
        lv_top = landmarks[left_indices[12]]
        lv_bottom = landmarks[left_indices[4]]
        rhDistance = self.euclaideanDistance(rh_right, rh_left)
        rvDistance = self.euclaideanDistance(rv_top, rv_bottom)
        lvDistance = self.euclaideanDistance(lv_top, lv_bottom)
        lhDistance = self.euclaideanDistance(lh_right, lh_left)
        reRatio = rhDistance/rvDistance
        leRatio = lhDistance/lvDistance
        ratio = (reRatio+leRatio)/2
        return ratio 


    def get_average_brightness(self,image,mesh_coords,frame_height,frame_width):
        lum = image[:,:,0]*0.144+image[:,:,1]*0.587+image[:,:,2]*0.299
        vals = np.average(lum)
        if math.isnan (vals) :
            return 0
        else:
            return vals

    def colorBackgroundText(self,img, text, font, fontScale, textPos, textThickness=1,textColor=(0,255,0), bgColor=(0,0,0), pad_x=3, pad_y=3):
        (t_w, t_h), _= cv.getTextSize(text, font, fontScale, textThickness) # getting the text size
        x, y = textPos
        cv.rectangle(img, (x-pad_x, y+ pad_y), (x+t_w+pad_x, y-t_h-pad_y), bgColor,-1) # draw rectangle 
        cv.putText(img,text, textPos,font, fontScale, textColor,textThickness ) # draw in text

        return img


    def showMainWindow(self,text,line=True):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(text)
        msgBox.setWindowTitle("Warning")
        # 設置視窗為最前顯示
        msgBox.setWindowFlags(msgBox.windowFlags() | Qt.WindowStaysOnTopHint)

        msgBox.exec()
        #if (line and self.want_line.isChecked()):
        #self.lineNotifyMessage(text)

    def get_state_body(self,results):
        up_state = 1
        down_state = -1
        left_wrist = results.pose_world_landmarks.landmark[15]
        left_pinky = results.pose_world_landmarks.landmark[17]
        right_wrist = results.pose_world_landmarks.landmark[16]
        right_pinky =  results.pose_world_landmarks.landmark[18]
        left_hip = results.pose_world_landmarks.landmark[23]
        right_hip = results.pose_world_landmarks.landmark[24]
        nose = results.pose_world_landmarks.landmark[0]
        if(left_wrist.y < nose.y and right_wrist.y < nose.y):
            return up_state
        elif(left_pinky.y > left_hip.y and right_pinky.y > right_hip.y):
            return down_state
        return 0

    def update_progress_value(self):
        try:  
            print(f"Current status: {self.status}, blink_per_minute: {self.blink_per_minute}")
            if(self.status != 'rest' and self.status != 'shutting_down'):
                with self.map_face_mesh.FaceMesh(min_detection_confidence =0.5, min_tracking_confidence=0.5) as face_mesh:
                    self.frame_counter += 1
                    ret, frame = self.camera.read() 
                    frame_height, frame_width= frame.shape[:2]
                    rgb_frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
                    results  = face_mesh.process(rgb_frame)
                    FONT = cv.FONT_HERSHEY_COMPLEX

                    ###
                    if results.multi_face_landmarks:
                        #self.record_state = 0
                        if(self.status == 'start'):
                            self.time_status = 'work'
                        mesh_coords = self.landmarksDetection(frame, results, False)
                        right_eye_area = self.PolyArea(np.array([mesh_coords[p] for p in self.RIGHT_EYE ])[:,0],np.array([mesh_coords[p] for p in self.RIGHT_EYE ])[:,1])
                        left_eye_area = self.PolyArea(np.array([mesh_coords[p] for p in self.LEFT_EYE ])[:,0],np.array([mesh_coords[p] for p in self.LEFT_EYE ])[:,1])
                        self.eye_area = (right_eye_area+left_eye_area)/2
                        self.ratio = self.blinkRatio(frame, mesh_coords, self.RIGHT_EYE, self.LEFT_EYE)
                        self.brightness_value = self.get_average_brightness(rgb_frame,mesh_coords,frame_height,frame_width) 
                        #self.eyestate = 0  # **初始化為未眨眼**
                        if self.camera_active:
                            if self.ratio > self.blink_th.value(): #close eye
                                self.colorBackgroundText(frame,  f'Blink', FONT, self.FONT_SIZE, (int(frame_height/2), 100), 2, (0,255,255), pad_x=6, pad_y=6, )

                            if (self.eye_area_record/self.eye_area)**0.5 < self.distance_th.value():
                                        self.showMainWindow('Too close',line=True)


                            if self.brightness_value <self.bright_th.value():
                                    self.colorBackgroundText(frame,  f'Too dim', FONT, self.FONT_SIZE, (int(frame_height/2), 150), 2, (0,255,255), pad_x=6, pad_y=6, )                           

                        cv.polylines(frame,  [np.array([mesh_coords[p] for p in self.LEFT_EYE ], dtype=np.int32)], True,(0,255,0), 1, cv.LINE_AA)
                        cv.polylines(frame,  [np.array([mesh_coords[p] for p in self.RIGHT_EYE ], dtype=np.int32)], True, (0,255,0), 1, cv.LINE_AA)
                        cv.polylines(frame,  [np.array([mesh_coords[p] for p in self.FACE_OVAL ], dtype=np.int32)], True, (0,0,255), 1, cv.LINE_AA)
                    else:
                        self.previous_time_step =  time.time()
                        self.record_state = 1 # do not detect people
                    self.fps_pass_time = time.time()-self.start_time
                    fps = self.frame_counter/self.fps_pass_time
                    self.colorBackgroundText(frame,  f'Eye area : {(self.eye_area)}', FONT, self.FONT_SIZE/2, (30,90),1)
                    self.colorBackgroundText(frame,  f'Eye Distance ratio: {round((self.eye_area_record/self.eye_area)**0.5,2)}', FONT, self.FONT_SIZE/2, (30,120),1)
                    self.colorBackgroundText(frame,  f'Eye Ratio: {round(self.ratio,2)}', FONT, self.FONT_SIZE/2, (30,150),1)
                    self.colorBackgroundText(frame,  f'Brightness: {round(self.brightness_value,1)}', FONT, self.FONT_SIZE/2, (30,180),1)
                    self.colorBackgroundText(frame,  f'FPS: {round(fps,1)}', FONT,self.FONT_SIZE/2, (30,60),1)
                    show = cv.resize(frame,(800,600))
                    show = cv.cvtColor(show, cv.COLOR_BGR2RGB)
                    showImage = QImage(show.data, show.shape[1],show.shape[0],QImage.Format_RGB888)
                    self.camera_site.setPixmap(QPixmap.fromImage(showImage))

                    if results.multi_face_landmarks:
                        self.record_state = 2
                        if (self.time_status == 'work'):
                            self.pass_time += (time.time() - self.previous_time_step)
                            self.previous_time_step =  time.time()
                        else:
                            self.pass_time += 0
                        if(self.status == 'start'):
                            self.time_status = 'work'
                        mesh_coords = self.landmarksDetection(frame, results, False)
                        right_eye_area = self.PolyArea(np.array([mesh_coords[p] for p in self.RIGHT_EYE ])[:,0],np.array([mesh_coords[p] for p in self.RIGHT_EYE ])[:,1])
                        left_eye_area = self.PolyArea(np.array([mesh_coords[p] for p in self.LEFT_EYE ])[:,0],np.array([mesh_coords[p] for p in self.LEFT_EYE ])[:,1])
                        self.eye_area = (right_eye_area+left_eye_area)/2
                        self.ratio = self.blinkRatio(frame, mesh_coords, self.RIGHT_EYE, self.LEFT_EYE)
                        self.brightness_value = self.get_average_brightness(rgb_frame,mesh_coords,frame_height,frame_width) 
                        self.eyestate = 0  # **初始化為未眨眼**

                        #area_record[counter] = eye_area 
                        #current_eye_ratio = (np.median(area_record)-eye_area)/np.median(area_record)
                        if self.camera_active == False :
                       
                            if self.ratio > self.blink_th_2.value(): #close eye
                                self.blink_counter +=1
                                self.colorBackgroundText(frame,  f'Blink', FONT, self.FONT_SIZE, (int(frame_height/2), 100), 2, (0,255,255), pad_x=6, pad_y=6, )
                            
                            else: #open eye
                                if self.blink_counter > self.eye_close_frame :
                                    self.blink_per_minute += 1  # **增加每分鐘眨眼次數**
                                    self.blink_counter =0

                            if (self.eye_area_record/self.eye_area)**0.5 < self.distance_th_2.value():
                                    self.colorBackgroundText(frame,  f'Too close', FONT, self.FONT_SIZE, (int(frame_height/2), 150), 2, (0,255,255), pad_x=6, pad_y=6, )

                                    self.showMainWindow('Too close',line=True)

                            if self.brightness_value <self.bright_th_2.value():
                                    self.colorBackgroundText(frame,  f'Too dim', FONT, self.FONT_SIZE, (int(frame_height/2), 150), 2, (0,255,255), pad_x=6, pad_y=6, )
                        self.colorBackgroundText(frame,  f'Total Blinks: {self.total_blink}', FONT, self.FONT_SIZE/2, (30,150),2)
                        cv.polylines(frame,  [np.array([mesh_coords[p] for p in self.LEFT_EYE ], dtype=np.int32)], True,(0,255,0), 1, cv.LINE_AA)
                        cv.polylines(frame,  [np.array([mesh_coords[p] for p in self.RIGHT_EYE ], dtype=np.int32)], True, (0,255,0), 1, cv.LINE_AA)
                        cv.polylines(frame,  [np.array([mesh_coords[p] for p in self.FACE_OVAL ], dtype=np.int32)], True, (0,0,255), 1, cv.LINE_AA)
                    else:
                        self.previous_time_step =  time.time()
                        self.record_state = 1 # do not detect people
                    self.fps_pass_time = time.time()-self.start_time
                    fps = self.frame_counter/self.fps_pass_time
                    self.colorBackgroundText(frame,  f'Eye area : {(self.eye_area)}', FONT, self.FONT_SIZE/2, (30,90),1)
                    self.colorBackgroundText(frame,  f'Eye Distance ratio: {round((self.eye_area_record/self.eye_area)**0.5,2)}', FONT, self.FONT_SIZE/2, (30,120),1)
                    self.colorBackgroundText(frame,  f'Eye Ratio: {round(self.ratio,2)}', FONT, self.FONT_SIZE/2, (30,150),1)
                    self.colorBackgroundText(frame,  f'Brightness: {round(self.brightness_value,1)}', FONT, self.FONT_SIZE/2, (30,180),1)
                    self.colorBackgroundText(frame,  f'FPS: {round(fps,1)}', FONT,self.FONT_SIZE/2, (30,60),1)
                    show = cv.resize(frame,(800,600))
                    show = cv.cvtColor(show, cv.COLOR_BGR2RGB)
                    showImage = QImage(show.data, show.shape[1],show.shape[0],QImage.Format_RGB888)
                    self.camera_site_2.setPixmap(QPixmap.fromImage(showImage))        
            elif(self.exercise_type.currentText() == 'jumping jack'):
                FONTS =cv.FONT_HERSHEY_COMPLEX
                self.record_state = 1
                with self.mp_pose.Pose(
                    min_detection_confidence=0.5,
                    min_tracking_confidence=0.5,model_complexity=0) as pose:
                    success, image = self.camera.read()
                    image = cv.resize(image, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
                    image.flags.writeable = False
                    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
                    results = pose.process(image)
                    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
                    if results.pose_world_landmarks:
                        self.record_state = 0
                        mesh_coords = self.landmarksDetection(image, results, False,True)
                        if (self.get_state_body(results)  == -self.previous_state):
                            self.previous_state = self.get_state_body(results)
                            self.count_hand += 1
                            print(self.count_hand,self.count_jump)

                        self.count = self.count_hand
                        image.flags.writeable = True
                        self.mp_drawing.draw_landmarks(
                            image,
                            results.pose_landmarks,
                            self.mp_pose.POSE_CONNECTIONS)
                    image = cv.flip(image, 1)
                    image = self.colorBackgroundText(image,  f'Total : {int(self.count/2)}', FONTS, 0.7, (30,200),1)        
                    show = cv.resize(image,(800,600))
                    show = cv.cvtColor(show, cv.COLOR_BGR2RGB)
                    showImage = QImage(show.data, show.shape[1],show.shape[0],QImage.Format_RGB888)
                    self.camera_site.setPixmap(QPixmap.fromImage(showImage))
                    self.camera_site_2.setPixmap(QPixmap.fromImage(showImage))

            elif((self.exercise_type.currentText() == 'close eye' and self.status != 'shutting_down') or (self.exercise_type.currentText() == 'None' and self.status != 'shutting_down')):
                with self.map_face_mesh.FaceMesh(min_detection_confidence =0.5, min_tracking_confidence=0.5) as face_mesh:
                    self.frame_counter += 1
                    ret, frame = self.camera.read() 
                    frame_height, frame_width= frame.shape[:2]
                    rgb_frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
                    results  = face_mesh.process(rgb_frame)
                    FONT = cv.FONT_HERSHEY_COMPLEX

                    if results.multi_face_landmarks and self.exercise_type.currentText() == 'close eye': 
                        self.record_state = 0
                        mesh_coords = self.landmarksDetection(frame, results, False)
                        right_eye_area = self.PolyArea(np.array([mesh_coords[p] for p in self.RIGHT_EYE ])[:,0],np.array([mesh_coords[p] for p in self.RIGHT_EYE ])[:,1])
                        left_eye_area = self.PolyArea(np.array([mesh_coords[p] for p in self.LEFT_EYE ])[:,0],np.array([mesh_coords[p] for p in self.LEFT_EYE ])[:,1])
                        self.eye_area = (right_eye_area+left_eye_area)/2
                        self.ratio = self.blinkRatio(frame, mesh_coords, self.RIGHT_EYE, self.LEFT_EYE)
                        self.brightness_value = self.get_average_brightness(rgb_frame,mesh_coords,frame_height,frame_width) 

                        if  self.ratio > self.blink_th_2.value(): #close eye
                            #self.eyestate = 1 # 1 = blink
                            self.pass_time += (time.time() - self.previous_time_step)
                            self.previous_time_step =  time.time()
                            self.colorBackgroundText(frame,  f'Close', FONT, self.FONT_SIZE, (int(frame_height/2), 100), 2, (0,255,255), pad_x=6, pad_y=6, )
                        else: #open eye
                            #self.eyestate = 0 # 0 = blink
                            #self.pass_time += 0
                            self.previous_time_step = time.time()    
                        cv.polylines(frame,  [np.array([mesh_coords[p] for p in self.LEFT_EYE ], dtype=np.int32)], True,(0,255,0), 1, cv.LINE_AA)
                        cv.polylines(frame,  [np.array([mesh_coords[p] for p in self.RIGHT_EYE ], dtype=np.int32)], True, (0,255,0), 1, cv.LINE_AA)
                        cv.polylines(frame,  [np.array([mesh_coords[p] for p in self.FACE_OVAL ], dtype=np.int32)], True, (0,0,255), 1, cv.LINE_AA)

                    elif self.exercise_type.currentText() == 'None':  # **None 模式下**
                        self.pass_time += (time.time() - self.previous_time_step)
                        self.previous_time_step = time.time()
                        self.record_state = 0  # 明確設置為休息狀態（0）
                    self.fps_pass_time = time.time()-self.start_time
                    fps = self.frame_counter/self.fps_pass_time
                    self.colorBackgroundText(frame,  f'Eye area : {(self.eye_area)}', FONT, self.FONT_SIZE/2, (30,90),1)
                    self.colorBackgroundText(frame,  f'Eye Distance ratio: {(self.eye_area_record/self.eye_area)**0.5}', FONT, self.FONT_SIZE/3, (30,120),1)
                    self.colorBackgroundText(frame,  f'Eye Ratio: {round(self.ratio,3)}', FONT, self.FONT_SIZE/2, (30,150),1)
                    self.colorBackgroundText(frame,  f'Brightness: {round(self.brightness_value,1)}', FONT, self.FONT_SIZE/2, (30,180),1)
                    self.colorBackgroundText(frame,  f'FPS: {round(fps,1)}', FONT, self.FONT_SIZE/2, (30,60),1)
                    show = cv.resize(frame,(800,600))
                    show = cv.cvtColor(show, cv.COLOR_BGR2RGB)
                    showImage = QImage(show.data, show.shape[1],show.shape[0],QImage.Format_RGB888)
                    self.camera_site.setPixmap(QPixmap.fromImage(showImage))
                    self.camera_site_2.setPixmap(QPixmap.fromImage(showImage))
                
            elif(self.exercise_type.currentText() == 'None' and self.status != 'shutting_down'):
                self.record_state = 0  # 明確設置為休息狀態（0）
                self.pass_time = (time.time() - self.previous_time_step)
                self.status = 'rest'
            elif(self.status == 'shutting_down'):
                self.record_state = 0
            if (self.status == 'start' or self.status== 'rest' ): # **工作或休息狀態下的時間管理**
                if(self.status == 'start'):
                    remain_time =  self.work_time*60 - self.pass_time # self.work_time*60 - ( time.time() - self.init_time)
                elif(self.status == 'rest'):
                    remain_time =  self.rest_time*60 - self.pass_time # self.work_time*60 - ( time.time() - self.init_time)
                hour = remain_time // 3600
                minute = (remain_time - (hour * 3600)) // 60
                second = (remain_time - (hour * 3600) - (minute * 60))

                # 更新進度條
                if self.status == 'start':
                    progress = int(self.pass_time / (self.work_time * 60) * 100)
                elif self.status == 'rest':
                    progress = int(self.pass_time / (self.rest_time * 60) * 100)
                self.Progress_progressBar.setValue(progress)

                self.lcdNumber_hour.display(str(int(hour)))
                self.lcdNumber_min.display(str(int(minute)))
                self.lcdNumber_sec.display(str(int(second)))
                
                self.count_minute += 1 
                self.count_bright += self.brightness_value
                self.count_blink += self.eyestate
                self.count_distance += (self.eye_area_record/self.eye_area)**0.5
                
                pass_minute = (time.time() - self.init_time) // 60
                print(f"pass_minute: {pass_minute}, previous_minute: {self.previous_minute}, status: {self.status}")
                if (pass_minute > self.previous_minute):
                    self.previous_minute = pass_minute
                    print(f"Minute updated: previous_minute = {self.previous_minute}")
                    blink_avg = self.blink_per_minute
                    self.blink_per_minute = 0
                    bright_avg = int(self.count_bright/self.count_minute)

                    distance_avg = round(self.count_distance/self.count_minute,3)

                    # **重置計數器**
                    self.count_bright = 0
                    self.count_blink = 0
                    self.count_distance = 0
                    self.count_minute = 0

                    result = time.localtime(time.time())
                    # 取得當前時間
                    current_hour = int(result.tm_hour)
                    current_minute = int(result.tm_min)
                    # 如果分鐘數是 0，則將其設置為 59，並減少小時數
                    if current_minute == 0:
                        current_minute = 59
                        current_hour -= 1
                        # 如果小時數變成負數，則調整為前一天的最後一小時（這應該根據具體需求來處理）
                        if current_hour < 0:
                            current_hour = 23
                            # 可以在這裡減少天數、月份或年份，根據具體需求來更新時間
                    if self.status == 'start':
                        print(f"Inserting into database: {self.status}, {current_hour}:{current_minute - 1}")
                        self.cursorObj.execute(
                            "insert or ignore into %s(year, month, day, hour, minute, distance, brightness, blink, state, Exhausted_state) VALUES (?,?,?,?,?,?,?,?,?,?)" % self.current_user,
                            (int(result.tm_year), int(result.tm_mon), int(result.tm_mday), current_hour, current_minute - 1, distance_avg, bright_avg, blink_avg, self.record_state, self.Exhausted_state)
                        )
                    elif self.status == 'rest':
                        print(f"Inserting into database: {self.status}, {current_hour}:{current_minute - 1}")
                        self.cursorObj.execute(
                            "insert or ignore into %s(year, month, day, hour, minute, distance, brightness, blink, state, Exhausted_state) VALUES (?,?,?,?,?,?,?,?,?,?)" % self.current_user,
                            (int(result.tm_year), int(result.tm_mon), int(result.tm_mday), current_hour, current_minute - 1, 1, 10, 0, self.record_state, 0)
                        )
                    self.con.commit()
                    # 插入數據後立即重置`Exhausted_state`
                    self.Exhausted_state = 0
                    
                    if self.status == 'start':  # 確保只有在工作狀態下才檢查眨眼次數
                   # **檢查每分鐘的眨眼次數是否達標**
                        print(f"Current blink_per_minute: {blink_avg}, Threshold: {self.blink_num_th_1.value()}")
                        if blink_avg < self.blink_num_th_1.value():
                            message = f'Low blink rate: {blink_avg} blinks/minute'
                            self.lineNotifyMessage(message)  # 確保只傳送一次
                           
                            self.showMainWindow(message,line=False)
                    print(f"Before reset - blink_per_minute: {blink_avg}, Threshold: {self.blink_num_th_1.value()}")
                    # **重置每分鐘的計數器**
                    self.blink_per_minute = 0                
            
                if (remain_time<0 and self.status=='start'):
                    print('rest')
                    self.status = 'rest'
                    self.pass_time = 0.01
                    self.previous_time_step = time.time()
                    self.blink_counter = 0
                    message = 'rest now'
                    self.showMainWindow(message,line=False)
                    # 發送LINE提醒，不依賴視窗點擊                        
                    self.lineNotifyMessage(message)                      
                elif((remain_time<0  or self.count >= self.excerise_count.value()) and self.status=='rest'):
                    message = 'finish rest'
                    self.showMainWindow(message,line=False)
                    # 發送LINE提醒，不依賴視窗點擊                        
                    self.lineNotifyMessage(message)                      
                    self.count = 0
                    self.count_hand = 0
                    self.status = 'start'
                    self.pass_time = 0.01
                    self.previous_time_step = time.time()
                    self.blink_counter = 0
                    self.finish_push_onchange()


        except Exception as e: 
            print(e)
            pass
        
    def __del__(self):
        self.update_database()
        self.summary_report()
        self.con.close()
    def closeEvent(self, event):
        self.summary_report()
        self.con.close()

def copy_and_rename_database_file(user_name):
    try:
        original_file_name = "database.db"
        new_file_name = f"{user_name}_database.db"
        
        # 使用 shutil 複製檔案並重新命名
        shutil.copyfile(original_file_name, new_file_name)
        print(f"Database file copied and renamed to {new_file_name}")
        return new_file_name
    except Exception as e:
        print(f"Failed to copy and rename database file: {e}")
        return None
def upload_to_google_drive(file_path):
    try:
        # 使用服務帳戶的 JSON 憑證檔案進行認證
        SERVICE_ACCOUNT_FILE = "/Users/chiahsin/Eye_Myself/連動成功/eyemyse-e62df01c3bc4.json"
        SCOPES = ['https://www.googleapis.com/auth/drive.file']
        
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # 建立 Google Drive API 服務
        service = build('drive', 'v3', credentials=credentials)

        # 指定目標資料夾的 ID
        folder_id = '1rowZJjh184Ogz5STLAGwms5utm2z8lsn'
        
        # 從檔案路徑中提取檔案名稱
        file_name = os.path.basename(file_path)

        # 檢查是否已有同名文件
        query = f"'{folder_id}' in parents and name = '{file_name}' and trashed=false"
        response = service.files().list(q=query, spaces='drive').execute()
        files = response.get('files', [])

        # 如果有同名文件，刪除它
        if files:
            file_id = files[0]['id']
            service.files().delete(fileId=file_id).execute()
            print(f"Deleted existing file: {file_name} (ID: {file_id})")

        # 定義檔案的元數據，包括父資料夾 ID
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }

        # 讀取並上傳檔案
        media = MediaFileUpload(file_path, resumable=True)
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        print(f"'{file_name}' 已成功上傳到 Google Drive 中的「畢業專題」資料夾。")
    except Exception as e:
        print(f"Failed to upload {file_name} to Google Drive: {e}")
if __name__ == '__main__':
    app = QApplication([])
    #apply_stylesheet(app, theme='dark_blue.xml')
    window = Window()
    window.show()
    app.exec()
    # 複製並重新命名檔案，然後上傳至 Google Drive
    if window.current_user:  # 使用 window.current_user 來獲取當前選中的使用者
        copied_file = copy_and_rename_database_file(window.current_user)
        if copied_file:
            upload_to_google_drive(copied_file)
