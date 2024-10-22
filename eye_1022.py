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
        self.init_time = time.time()
        self.setupUi(self)
        self.nameBox.currentTextChanged.connect(lambda: self.user_list_onchange(1))   #page1 的choose user選單
        self.nameBox_2.currentTextChanged.connect(lambda: self.user_list_onchange(2)) #page2 開始後的choose user選單
        self.nameBox_3.currentTextChanged.connect(lambda: self.user_list_onchange(3)) #page3 Analysis的choose user選單
        self.nameBox_4.currentIndexChanged.connect(self.edit_onchange)                #page5 編輯頁面的choose user選單
         
        self.distance_th.valueChanged.connect(self.update_threshold_values)   #距離的 UI 元素
        self.bright_th.valueChanged.connect(self.update_threshold_values)     #亮度的 UI 元素
        self.blink_th.valueChanged.connect(self.update_threshold_values)      #眨眼的 UI 元素
        self.blink_num_th.valueChanged.connect(self.update_threshold_values)  #最低眨眼的UI 元素
        
        self.camera_active = False

        self.working_time.valueChanged.connect(self.working_time_onchange)   
        self.resting_time.valueChanged.connect(self.resting_time_onchange)

        self.start.clicked.connect(self.start_push_onchange)               #page1的Start按紐
        self.open_camera.clicked.connect(self.camera_onchange)             #page1的Camera按紐
        self.suggestion.clicked.connect(self.suggestion_push_onchange)     #page1的Suggestion按紐
        self.pushButton_sve.clicked.connect(self.save_numth_to_new_db)     #page2的Save按紐
        self.toolButton_finish.clicked.connect(self.finish_push_onchange)  #page2的Finish按紐
        self.send_to_line.clicked.connect(self.send_images_to_line)

        self.start.setEnabled(False)       # page1 禁用 Start 按鈕(尚未開啟相機)
        self.suggestion.setEnabled(False)  # page1 禁用 Suggestion 按鈕(尚未開啟相機) 
        self.login1_homebutton.setEnabled(True)
        self.introduction_send_pushButton.setEnabled(False)  # page7 禁用 送出 按鈕(等他按下已看完資訊才可以按)
        self.introduction_agree_radioButton.toggled.connect(self.toggle_send_button) #連接到開啟按鈕的
        self.introduction_send_pushButton.clicked.connect(self.submit_action)


        self.Savefile.clicked.connect(self.add_push_onchange)              #page4註冊的Save按紐      

            #page5編輯:顯示用戶歷史user_info
        self.nameBox_4.activated.connect(self.edit_onchange)               #page5編輯:更新用戶user_info
        self.Savefile_edit.clicked.connect(self.cover_data_to_new_db)      #page5編輯的Save按紐   
        self.deletefile_edit.clicked.connect(self.edit_delete_all)         #page5編輯的刪除按紐  


        self.login.clicked.connect(lambda: self.switch_page(1))                 #page0首頁 按下Log in 跳轉至page1登入
        self.Analysis.clicked.connect(lambda: self.switch_page(3))              #page0首頁 按下Analysis 跳轉至page3查看日誌
        self.start.clicked.connect(lambda: self.switch_page(2))                 #page1 按下Start 跳轉至page2開始記錄
        self.toolButton_finish.clicked.connect(lambda: self.switch_page(6))     #page2 按下Finish 跳轉至page6填寫後測
        self.Edit.clicked.connect(lambda: self.switch_page(5))                  #page0 按下Edit 跳轉至page5編輯介面
        self.Signup.clicked.connect(lambda: self.switch_page(7))               #page0 按下Edit 跳轉至page4註冊介面
        self.login1_homebutton.clicked.connect(lambda: self.switch_page(0))     #page1 點選右上角返回首頁
        self.login2_homebutton.clicked.connect(lambda: self.switch_page(0))     #page2 點選右上角返回首頁
        self.login1_homebutton.clicked.connect(self.shut_onchange)              #page1 點選右上角返回首頁的同時關閉系統
        self.login2_homebutton.clicked.connect(self.shut_onchange)              #page2 點選右上角返回首頁的同時關閉系統
        self.analysis_homebutton.clicked.connect(lambda: self.switch_page(0))   #page3 點選右上角返回首頁
        self.signup_homebutton.clicked.connect(lambda: self.switch_page(0))     #page4 點選右上角返回首頁
        self.edit1_homebutton.clicked.connect(lambda: self.switch_page(0))      #page5 點選右上角返回首頁
        self.introduction_send_pushButton.clicked.connect(lambda: self.switch_page(4))   #page7 按下送出 跳轉至page4註冊介面


        #timer
        self.timer_camera = QTimer() #初始化定時器
        self.timer_warm = QTimer() #初始化定時器
        self.timer_camera.timeout.connect(self.update_progress_value)  
        self.timer_warm.timeout.connect(self.check_status)
        self.work_time = self.working_time.value()                         #page1獲取UI框框中的數值(work_time)
        self.rest_time = self.resting_time.value()                         #page1獲取UI框框中的數值(rest_time)
        self.blink_thres = self.blink_th.value()                           #page1獲取UI框框中的數值(blink_thres)
        self.bright_thres = self.bright_th.value()                         #page1獲取UI框框中的數值(bright_thres)
        self.distance_thres = self.distance_th.value()                     #page1獲取UI框框中的數值(distance_thres)
        self.blink_threshold_per_minute_value = self.blink_num_th.value()  #page1獲取UI框框中的數值(blink_threshold_per_minute_value)
        self.blink_thres_2 = self.blink_th_2.value()                           #page2獲取UI框框中的數值(blink_thres_2)
        self.bright_thres_2 = self.bright_th_2.value()                         #page2獲取UI框框中的數值(bright_thres_2)
        self.distance_thres_2 = self.distance_th_2.value()                     #page2獲取UI框框中的數值(distance_thres_2)
        self.blink_threshold_per_minute_value_2 = self.blink_num_th_2.value()  #page2獲取UI框框中的數值(blink_threshold_per_minute_value_2)

        self.exercise_type.addItem('None')
        self.exercise_type.addItem('close eye')
        self.exercise_type.addItem('jumping jack')

        self.blink_per_minute = 0 
        self.is_exhausted = False  
        self.exhausted_work_counter = 0
        self.too_close_count = 0 


        # 初始化並監聽值的變化
        self.blink_th.valueChanged.connect(lambda: self.update_threshold(self.blink_th, self.blink_th_2))
        self.bright_th.valueChanged.connect(lambda: self.update_threshold(self.bright_th, self.bright_th_2))
        self.distance_th.valueChanged.connect(lambda: self.update_threshold(self.distance_th, self.distance_th_2))
        self.blink_num_th.valueChanged.connect(lambda: self.update_threshold(self.blink_num_th, self.blink_num_th_2))
        #self.blink_num_th_2.valueChanged.connect(lambda: self.update_threshold(self.blink_num_th_2, self.blink_num_th))

        self.last_exhausted_time_str = None  # 初始化上次按下的時間


        # 初始化疲勞狀態
        self.Exhausted_state = 0
        self.Exhausted_count = 0
        self.next_threshold = 15
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
        self.con = sqlite3.connect('database.db')
        self.cursorObj = self.con.cursor()
        self.start_time_for_database = 0

        # 創建 `None` 和 `threshold` 表格
        self.cursorObj.execute(f'''
            CREATE TABLE IF NOT EXISTS None_data(
                year INTEGER, 
                month INTEGER, 
                day INTEGER, 
                hour INTEGER, 
                minute INTEGER, 
                distance REAL, 
                brightness INTEGER, 
                blink INTEGER, 
                state INTEGER, 
                Exhausted_state INTEGER,
                start_time_for_database TEXT 
            );
        ''')
        self.cursorObj.execute('''
            CREATE TABLE IF NOT EXISTS threshold(
                user TEXT UNIQUE, 
                line_token TEXT, 
                distance_area REAL, 
                distance_ratio REAL, 
                brightness INTEGER, 
                blink INTEGER,
                blink_num_th INTEGER                              
            );
        ''')
        # 插入一筆初始數據
        self.cursorObj.execute('''
            INSERT OR IGNORE INTO threshold(
                user, line_token, distance_area, distance_ratio, brightness, blink, blink_num_th
            ) VALUES (?, ?, ?, ?, ?, ?, ?)''',
            ('None', '', self.eye_area_record, self.eye_area_ratio, 60, 4, 15)
        )
        self.con.commit()

        # 讀取 threshold 表數據並更新界面
        cursor = self.cursorObj.execute("SELECT * FROM threshold").fetchall()
        for row in cursor:
            self.nameBox.addItem(row[0])
            self.nameBox_2.addItem(row[0])
            self.nameBox_3.addItem(row[0])  
            self.nameBox_4.addItem(row[0]) 
            print(row)

        #建立 user_info 表格
        self.con = sqlite3.connect('database.db')
        self.cursorObj = self.con.cursor()
        self.cursorObj.execute('''
            CREATE TABLE IF NOT EXISTS user_info (
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
                use_situation_value5 TEXT,
                habit1 TEXT,
                habit2 TEXT,
                habit3 TEXT,
                habit4 TEXT,
                habit5 TEXT,
                habit6 TEXT,
                habit7 TEXT,
                line_token TEXT,
                submission_time TEXT
            );
        ''')

        # 創建 posttest 表格
        self.cursorObj.execute('''
            CREATE TABLE IF NOT EXISTS None_posttest (
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
                submission_time TEXT  -- 填表的時間,
                start_time_for_database TEXT -- 按下start的時間
            );
        ''')
        self.con.commit()
# 創建 user_id 表格(關聯式資料庫)
        self.cursorObj.execute('''
            CREATE TABLE IF NOT EXISTS user_id (
                user_name TEXT,
                test_id TEXT --start_time_for_database
            );
        ''')
        self.con.commit()

        # 設置按鈕點擊事件
        self.Sendout_Button.clicked.connect(self.sendout)
        self.Savefile.clicked.connect(self.Save)

        print("Save button connected to posttest and user_info")
    
    def create_user_data(self):
        self.current_user  = str(self.nameBox_2.currentText())
        # 連接主資料庫
        self.con = sqlite3.connect('database.db')
        self.cursorObj = self.con.cursor()
        self.start_time_for_database = 0

        # 創建 `None` 和 `threshold` 表格
        self.cursorObj.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.current_user}_data(
                year INTEGER, 
                month INTEGER, 
                day INTEGER, 
                hour INTEGER, 
                minute INTEGER, 
                distance REAL, 
                brightness INTEGER, 
                blink INTEGER, 
                state INTEGER, 
                Exhausted_state INTEGER,
                start_time_for_database TEXT 
            );
        ''')
    
    def shut_onchange(self):
        self.status = 'shutting_down'

    # 註冊頁面存檔功能
    def save_data_to_new_db(self):   # 註冊頁面存檔功能
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

            eye_situation_value1 = self.eye_situation_button_group1.id(self.eye_situation_button_group1.checkedButton()) if self.eye_situation_button_group1.checkedButton() else None
            eye_situation_value2 = self.eye_situation_button_group2.id(self.eye_situation_button_group2.checkedButton()) if self.eye_situation_button_group2.checkedButton() else None
            eye_situation_value3 = self.eye_situation_button_group3.id(self.eye_situation_button_group3.checkedButton()) if self.eye_situation_button_group3.checkedButton() else None
            eye_situation_value4 = self.eye_situation_button_group4.id(self.eye_situation_button_group4.checkedButton()) if self.eye_situation_button_group4.checkedButton() else None
            eye_situation_value5 = self.eye_situation_button_group5.id(self.eye_situation_button_group5.checkedButton()) if self.eye_situation_button_group5.checkedButton() else None

            use_situation1 = '是' if self.use_situation_yes_button1.isChecked() else '否'
            use_situation2 = self.use_situation2_combobox.currentText()
            use_situation3 = '是' if self.use_situation_yes_button3.isChecked() else '否'
            use_situation_value4 = self.use_situation_button_group4.id(self.use_situation_button_group4.checkedButton()) if self.use_situation_button_group4.checkedButton() else None
            use_situation_value5 = self.use_situation5_combobox.currentText()

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
            submission_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
            # Validation: Check if required fields are filled
            if not (name and username and birthday):
                QMessageBox.warning(self, "錯誤", "請填寫完整")
                return

            # Check if the username already exists in the database
            self.cursorObj.execute('SELECT * FROM user_info WHERE username = ?', (username,))
            username_result = self.cursorObj.fetchone()

            if username_result:
                # If a matching username is found, notify the user that the username already exists
                QMessageBox.information(self, "提示", f"使用者 '{username}' 已經存在，無法新增重複使用者。")
                return  # Exit the function without saving    

            # Now save the new data
            self.cursorObj.execute('''
                INSERT INTO user_info (
                    name, username, birthday, gender, 
                    right_eye_condition, right_eye_degree, right_eye_shine, right_eye_shine_degree,
                    left_eye_condition, left_eye_degree, left_eye_shine, left_eye_shine_degree,
                    eye_situation_value1, eye_situation_value2, eye_situation_value3, eye_situation_value4, eye_situation_value5,
                    use_situation1, use_situation2, use_situation3, use_situation_value4, use_situation_value5,
                    habit1, habit2, habit3, habit4, habit5, habit6, habit7, line_token,submission_time
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                name, username, birthday, gender, 
                right_eye_condition, right_eye_degree, right_eye_shine, right_eye_shine_degree,
                left_eye_condition, left_eye_degree, left_eye_shine, left_eye_shine_degree,
                eye_situation_value1, eye_situation_value2, eye_situation_value3, eye_situation_value4, eye_situation_value5,
                use_situation1, use_situation2, use_situation3, use_situation_value4, use_situation_value5,
                habit1, habit2, habit3, habit4, habit5, habit6, habit7_str, line_token, submission_time
            ))

            # Commit the new data
            self.con.commit()

            # Show success message and switch page
            success_msg = QMessageBox()
            success_msg.setText("資料已存檔")
            success_msg.setIcon(QMessageBox.Information)
            success_msg.setWindowTitle("成功")
            success_msg.buttonClicked.connect(lambda: self.switch_page(0))  # Switch to page_0 after clicking "OK"
            success_msg.exec()
            
        except Exception as e:
            # Show error message in case of failure
            QMessageBox.warning(self, "錯誤", f"存檔失敗: {str(e)}")



    def update_threshold(self, source, target):
        # 更新 target 的值為 source 的值
        target.setValue(source.value())
    
    #插入&更換目前用戶
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

    #插入/更新用戶Line金鑰
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

    #按下註冊頁面的Save鍵
    def Save(self):
        self.check_and_add_user()
        self.update_line_token_in_db()
        self.save_data_to_new_db()

    #換頁功能      
    def switch_page(self, index):
        self.stackedWidget.setCurrentIndex(index)
        if index == 6:  # 當進入 page_6 編輯頁面時
            self.load_user_names_into_edit_dropdown()

    
    def load_user_names_into_edit_dropdown(self):
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
        self.nameBox_4.addItem(text)
        
        if (text != ''):
            self.con = sqlite3.connect('database.db')
            self.cursorObj = self.con.cursor()

            try:
                print(f"Creating table for user: {self.current_user}")

                self.cursorObj.execute(f'''CREATE TABLE IF NOT EXISTS {self.current_user}_data (
                    year INTEGER, 
                    month INTEGER, 
                    day INTEGER, 
                    hour INTEGER, 
                    minute INTEGER, 
                    distance REAL, 
                    brightness INTEGER, 
                    blink INTEGER, 
                    state INTEGER, 
                    Exhausted_state INTEGER, 
                    start_time_for_database TEXT
                )''')                
                self.cursorObj.execute(f'''
                    CREATE TABLE IF NOT EXISTS {self.current_user}_posttest (
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
                        submission_time TEXT,  -- 填表的時間
                        start_time_for_database TEXT -- 按下start的時間
                    );
                ''')

                self.cursorObj.execute("insert or ignore into threshold(user,line_token,  distance_area, distance_ratio, brightness, blink, blink_num_th) VALUES (?,?,?,?,?,?,?)" ,(text,self.line_token_input.text(),self.eye_area_record,self.eye_area_ratio,60,4,15))
                self.con.commit()
            except:
                self.showMainWindow('Not valid name!')
        else:
            print('empty')


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
        self.current_user  = str(self.nameBox_2.currentText())

        # 檢查當前使用者的表是否存在，避免操作不存在的表
        table_name = f"{self.current_user}_data"
        self.cursorObj.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        table_exists = self.cursorObj.fetchone()

        if not table_exists:
            print(f"資料表 {table_name} 不存在，無法生成報告。")
            return  # 若資料表不存在，則結束函數

        # 查詢當天所有的記錄
        cursor = self.cursorObj.execute(
            f"SELECT year, month, day, hour, minute, distance, brightness, blink, state, Exhausted_state "
            f"FROM {self.current_user}_data WHERE year=? AND month=? AND day=? ORDER BY hour, minute",
            (year, month, day)
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
                if current_exercise:
                    exercise_types.append(current_exercise)

            # 記錄當前休息時選擇的運動方式
            if state == 0:
                rest_time_total += 1
                current_exercise = self.exercise_type.currentText()  # 記錄當前運動類型
            else:
                current_exercise = None

        # 定義亮度描述函數
        def get_brightness_description(avg_brightness):
            if avg_brightness < 100:
                return "過暗"
            elif 100 <= avg_brightness < 120:
                return "普通"
            elif 120 <= avg_brightness <= 200:
                return "充足"
            else:
                return "過亮"

        # 計算當次使用平均值
        avg_dis_session = round(sum(dis_session) / len(dis_session), 2) if dis_session else 0.00
        avg_bri_session = round(sum(bri_session) / len(bri_session), 2) if bri_session else 0.00
        avg_blink_session = round(sum(blink_session) / len(blink_session), 2) if blink_session else 0.00
        brightness_description_session = get_brightness_description(avg_bri_session)

        # 計算當日使用平均值
        avg_dis_total = round(sum(total_dis) / len(total_dis), 2) if total_dis else 0.00
        avg_bri_total = round(sum(total_bri) / len(total_bri), 2) if total_bri else 0.00
        avg_blink_total = round(sum(total_blink) / use_time_total, 2) if use_time_total > 0 else 0.00
        brightness_description_total = get_brightness_description(avg_bri_total)

        # 獲取所有不同的運動類型
        exercise_types_report = ', '.join(set(exercise_types)) if exercise_types else '無'

        # 組裝報告訊息
        message = (
            f"【EyesMyself】 {today_date}\n"
            f"--- 當次使用情形 ---\n"
            f"使用時間: {use_time_session} 分鐘\n"
            f"休息時間: {rest_time_session} 分鐘\n"
            f"平均距離: {avg_dis_session}\n"
            f"光源情況: {brightness_description_session}（平均亮度: {avg_bri_session}）\n"
            f"平均眨眼次數: {avg_blink_session}\n"
            f"休息方式: {exercise_types_report}\n"
            f"距離過近提醒次數: {self.too_close_count}\n"
            f"--- 今日使用情形 ---\n"
            f"使用時間: {use_time_total} 分鐘\n"
            f"休息時間: {rest_time_total} 分鐘\n"
            f"平均距離: {avg_dis_total}\n"
            f"整體光源情況: {brightness_description_total}（平均亮度: {avg_bri_total}）\n"
            f"平均眨眼次數: {avg_blink_total}\n"
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
    
    def save_numth_to_new_db(self):    #page2開始後更新閾值功能
            try:
                # 取得 UI 中的閾值與選取的使用者名稱
                distance_record = self.distance_th_2.value()
                brightness_record = self.bright_th_2.value()
                blink_record = self.blink_th_2.value()
                blink_per_mininute_record = self.blink_num_th_2.value()
                user = self.nameBox_2.currentText()

                # 檢查該使用者是否已存在於資料庫中
                self.cursorObj.execute('SELECT * FROM threshold WHERE user = ?', (user,))
                username_result = self.cursorObj.fetchone()

                if username_result:
                    # 如果使用者存在，更新該使用者的數據
                    self.cursorObj.execute('''
                        UPDATE threshold
                        SET distance_ratio = ?, brightness = ?, blink = ? , blink_num_th=?
                        WHERE user = ?
                    ''', (distance_record, brightness_record, blink_record, blink_per_mininute_record, user))

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
        self.con = sqlite3.connect('database.db')
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


    def update_threshold_values(self):   #page1開始前調整閾值
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
            SET distance_ratio = ?, brightness = ?, blink = ? ,blink_num_th=?
            WHERE user = ?
            """
            self.cursorObj.execute(update_query, (distance_ratio, brightness, blink, blink_num_th, current_user))
            
            # Commit the changes (do not close the connection)
            self.con.commit()
            print(f"Threshold values updated for user {current_user}")
        
        except sqlite3.Error as e:
            print(f"Error updating threshold: {e}")

    def edit_onchange(self):  #編輯使用者介面 : 顯示用戶歷史資料
        selected_index = self.nameBox_4.currentIndex()# 獲取選擇的用戶索引
        if selected_index > 0:
            # 根據索引獲取選擇的用戶名稱
            selected_user = self.nameBox_4.currentText()        
            # 查詢資料庫，使用選中的用戶名
            self.cursorObj.execute('SELECT * FROM user_info WHERE username = ?', (selected_user,))
            user_data = self.cursorObj.fetchone()
            if user_data:
                self.name_input_edit.setText(user_data[1])  # 顯示姓名
                
                self.birthday_input_edit.setText(user_data[3])
                
                gender = user_data[4]  # 取出性別欄位值
                if gender == "男生":
                    self.sex_man_button_edit.setChecked(True)
                elif gender == "女生":
                    self.sex_women_button_edit.setChecked(True)
                    
                right_eye_condition = user_data[5]  
                if right_eye_condition == "近視":
                    self.right_eye_in_button_edit.setChecked(True)
                elif right_eye_condition == "遠視":
                    self.right_eye_out_button_edit.setChecked(True)
                    
                self.right_eye_degree_input_edit.setText(user_data[6])
                
                right_eye_shine_condition = user_data[7]  
                if right_eye_shine_condition == "閃光":
                    self.right_eye_shine_button_edit.setChecked(True)
                    
                #self.right_eye_shine_input_edit.setText(f"{user_data[8]:.1f}")  # 保留一位小數
                self.right_eye_shine_input_edit.setText(str(user_data[8]))
                

                
                left_eye_condition = user_data[9]  
                if left_eye_condition == "近視":
                    self.left_eye_in_button_edit.setChecked(True)
                elif left_eye_condition == "遠視":
                    self.left_eye_out_button_edit.setChecked(True)
                    
                #self.left_eye_degree_input_edit.setText(f"{user_data[10]:.1f}")  # 保留一位小數
                self.left_eye_degree_input_edit.setText(str(user_data[10]))
                
                left_eye_shine_condition = user_data[11]  
                if left_eye_shine_condition == "閃光":
                    self.left_eye_shine_button_edit.setChecked(True)
                    
                #self.left_eye_shine_input_edit.setText(f"{user_data[12]:.1f}")  # 保留一位小數
                self.left_eye_shine_input_edit.setText(str(user_data[12]))

                if user_data:
                    # 設置單選按鈕的選中狀態
                    eye_situation_value1 = user_data[13]  # 這是從資料庫中讀取到的數值
                    print(f"eye_situation_value1 from database: {eye_situation_value1}")
                    if eye_situation_value1:
                        button_to_select = self.eye_situation_button_group1_edit.button(int(eye_situation_value1))
                        if button_to_select:
                            button_to_select.setChecked(True)
                            self.update()

                        print(f"Button {button_to_select.objectName()} is now checked: {button_to_select.isChecked()}")

                    eye_situation_value2 = user_data[14]
                    if eye_situation_value2:
                        button_to_select = self.eye_situation_button_group2_edit.button(int(eye_situation_value2))
                        if button_to_select:
                            button_to_select.setChecked(True)
                            self.update()
                        print(f"Button {button_to_select.objectName()} is now checked: {button_to_select.isChecked()}")

                    eye_situation_value3 = user_data[15]
                    if eye_situation_value3:
                        button_to_select = self.eye_situation_button_group3_edit.button(int(eye_situation_value3))
                        if button_to_select:
                            button_to_select.setChecked(True)
                            self.update()

                    eye_situation_value4 = user_data[16]
                    if eye_situation_value4:
                        button_to_select = self.eye_situation_button_group4_edit.button(int(eye_situation_value4))
                        if button_to_select:
                            button_to_select.setChecked(True)
                            self.update()

                    eye_situation_value5 = user_data[17]
                    if eye_situation_value5:
                        button_to_select = self.eye_situation_button_group5_edit.button(int(eye_situation_value5))
                        if button_to_select:
                            button_to_select.setChecked(True)
                            self.update() 

                    use_situation_value4 = user_data[21]
                    if use_situation_value4:
                        button_to_select = self.use_situation_button_group4_edit.button(int(use_situation_value4))
                        if button_to_select:
                            button_to_select.setChecked(True)
                            self.update()                     
              
                use_situation1 = user_data[18]  
                if use_situation1 == "是":
                    self.use_situation_yes_button1_edit.setChecked(True)
                elif use_situation1 == "否":
                    self.use_situation_no_button1_edit.setChecked(True)
                    
                use_situation2 = user_data[19]
                # 設定當前選項
                if use_situation2 in ["3小時以內", "3至6小時", "6至9小時", "9至12小時", "12小時以上"]:
                    self.use_situation2_combobox_edit.setCurrentText(use_situation2)  # 設定為當前選項
                else:
                    self.use_situation2_combobox_edit.setCurrentText("3小時以內")  # 或其他預設值
                
                use_situation3 = user_data[20]  
                if use_situation3 == "是":
                    self.use_situation_yes_button3_edit.setChecked(True)
                elif use_situation3 == "否":
                    self.use_situation_no_button3_edit.setChecked(True)

                use_situation_value5 = user_data[22]  
                # 設定當前選項
                if use_situation_value5 in ["室內共用燈光", "室內專屬燈光", "室外自然光", "以上皆無"]:
                    self.use_situation5_combobox_edit.setCurrentText(use_situation_value5)  # 設定為當前選項
                else:
                    self.use_situation5_combobox_edit.setCurrentText("室內共用燈光")  # 或其他預設值    
                
                habit1 = user_data[23]  
                if habit1 == "是":
                    self.habit_yes_button1_edit.setChecked(True)
                elif habit1 == "否":
                    self.habit_no_button1_edit.setChecked(True)
                
                habit2 = user_data[24]
                # 設定當前選項
                if habit2 in ["無", "半年一次", "一年一次", "更頻繁"]:
                    self.habit_combobox2_edit.setCurrentText(habit2)  # 設定為當前選項
                else:
                    self.habit_combobox2_edit.setCurrentText("無")  # 或其他預設值
                    
                habit3 = user_data[25]
                if habit3 in ["低於4小時", "4至6小時", "6至8小時", "高於8小時"]:
                    self.habit_combobox3_edit.setCurrentText(habit3)  # 設定為當前選項
                else:
                    self.habit_combobox3_edit.setCurrentText("低於4小時")  # 或其他預設值
                    
                habit4 = user_data[26]
                # 設定當前選項
                if habit4 in ["0或1次", "2或3次", "4或5次", "6次以上"]:
                    self.habit_combobox4_edit.setCurrentText(habit4)  # 設定為當前選項
                else:
                    self.habit_combobox4_edit.setCurrentText("0或1次")  # 或其他預設值
                    
                habit5 = user_data[27]
                # 設定當前選項
                if habit5 in ["無休息", "1小時內", "1至2小時", "2至3小時", "3至4小時", "4至5小時", "5小時以上"]:
                    self.habit_combobox5_edit.setCurrentText(habit5)  # 設定為當前選項
                else:
                    self.habit_combobox5_edit.setCurrentText("無休息")  # 或其他預設值
                    
                habit6 = user_data[28]
                # 設定當前選項
                if habit6 in ["10分鐘內", "11至30分鐘", "31至60分鐘", "60分鐘以上"]:
                    self.habit_combobox6_edit.setCurrentText(habit6)  # 設定為當前選項
                else:
                    self.habit_combobox6_edit.setCurrentText("10分鐘內")  # 或其他預設值

                # 假設 user_data[8] 是包含所有 checkbox 狀態的欄位，格式為 "1,0,1"
                checkbox_data = user_data[29].split(",")  # 解析成 ["1", "0", "1"]

                if len(checkbox_data) >= 3:  # 確保有三個狀態值
                    # 設置 habit_close_checkbox7_edit 的狀態
                    if checkbox_data[0] == "1":
                        self.habit_close_checkbox7_edit.setChecked(True)
                    else:
                        self.habit_close_checkbox7_edit.setChecked(False)

                    # 設置 habit_exercise_checkbox7_edit 的狀態
                    if checkbox_data[1] == "1":
                        self.habit_exercise_checkbox7_edit.setChecked(True)
                    else:
                        self.habit_exercise_checkbox7_edit.setChecked(False)

                    # 設置 habit_other_checkbox7_edit 的狀態
                    if checkbox_data[2] == "1":
                        self.habit_other_checkbox7_edit.setChecked(True)
                    else:
                        self.habit_other_checkbox7_edit.setChecked(False)
                
                self.line_token_input_edit.setText(user_data[30])
                
            else:
                print("沒有找到該用戶的資料")
        
     
                
        input_fields = [
            self.name_input_edit,
            self.birthday_input_edit,
            self.line_token_input_edit,
            self.right_eye_degree_input_edit,
            self.left_eye_degree_input_edit,
            self.habit_combobox2_edit,
            self.habit_combobox3_edit,
            self.habit_combobox4_edit,
            self.habit_combobox5_edit,
            self.habit_combobox6_edit,]

        buttons = [
            self.sex_man_button_edit,
            self.sex_women_button_edit,
            self.right_eye_out_button_edit,
            self.right_eye_in_button_edit,
            self.right_eye_shine_button_edit,
            self.left_eye_out_button_edit,
            self.left_eye_in_button_edit,
            self.left_eye_shine_button_edit,
            self.use_situation_yes_button1_edit,
            self.use_situation_no_button1_edit,
            self.use_situation_yes_button3_edit,
            self.use_situation_no_button3_edit,
            self.habit_yes_button1_edit,
            self.habit_no_button1_edit,]
        
        all_buttons = self.temp_button1_edit + self.temp_button2_edit + self.temp_button3_edit + self.temp_button4_edit + self.temp_button5_edit + self.use_situation_temp_button1_edit + self.use_situation_temp_button2_edit

        checkboxes = [
            self.habit_close_checkbox7_edit,
            self.habit_other_checkbox7_edit,
            self.habit_exercise_checkbox7_edit,]

        comboboxes = [
            self.use_situation2_combobox_edit,]

        # 打開所有控件
        for field in input_fields + buttons + checkboxes + comboboxes + all_buttons:
            field.setEnabled(True)
        self.Savefile_edit.setEnabled(True)
        self.deletefile_edit.setEnabled(True)    

    def toggle_send_button(self):
        # 根據 radio button 的選擇狀態啟用或禁用 send button
        self.introduction_send_pushButton.setEnabled(self.introduction_agree_radioButton.isChecked())    

    def submit_action(self):
        # 清除勾選框的選中狀態並禁用送出按鈕
        self.introduction_agree_radioButton.setChecked(False)
        self.introduction_send_pushButton.setEnabled(False)

    def cover_data_to_new_db(self):  # 編輯使用者介面 : Save按鍵更新使用者user_info
        user_name = self.nameBox_4.currentText()  # 從 UI 中取得使用者標識符

        # 查詢資料庫以檢查是否已經有該使用者的資料
        query_check = "SELECT * FROM user_info WHERE username = ?"
        self.cursorObj.execute(query_check, (user_name,))
        result = self.cursorObj.fetchone()

        if result:  # 如果找到該使用者資料則進行覆蓋            
            # 從 UI 中提取最新的數據
            name = self.name_input_edit.text()
            birthday = self.birthday_input_edit.text()

            # 性別
            if self.sex_man_button_edit.isChecked():
                gender = "男生"
            elif self.sex_women_button_edit.isChecked():
                gender = "女生"

            # 右眼狀況
            if self.right_eye_in_button_edit.isChecked():
                right_eye_condition = "近視"
            elif self.right_eye_out_button_edit.isChecked():
                right_eye_condition = "遠視"

            right_eye_degree = self.right_eye_degree_input_edit.text()
            right_eye_shine = "閃光" if self.right_eye_shine_button_edit.isChecked() else "無"
            right_eye_shine_degree = self.right_eye_shine_input_edit.text()

            # 左眼狀況
            if self.left_eye_in_button_edit.isChecked():
                left_eye_condition = "近視"
            elif self.left_eye_out_button_edit.isChecked():
                left_eye_condition = "遠視"

            left_eye_degree = self.left_eye_degree_input_edit.text()
            left_eye_shine = "閃光" if self.left_eye_shine_button_edit.isChecked() else "無"
            left_eye_shine_degree = self.left_eye_shine_input_edit.text()

            # 從按鈕組中提取 eye_situation 值
            eye_situation_value1 = self.eye_situation_button_group1_edit.checkedId()
            eye_situation_value2 = self.eye_situation_button_group2_edit.checkedId()
            eye_situation_value3 = self.eye_situation_button_group3_edit.checkedId()
            eye_situation_value4 = self.eye_situation_button_group4_edit.checkedId()
            eye_situation_value5 = self.eye_situation_button_group5_edit.checkedId()
            use_situation_value4 = self.use_situation_button_group4_edit.checkedId()

            # 使用情況
            use_situation1 = "是" if self.use_situation_yes_button1_edit.isChecked() else "否"
            use_situation2 = self.use_situation2_combobox_edit.currentText()
            use_situation3 = "是" if self.use_situation_yes_button3_edit.isChecked() else "否"
            use_situation_value5 = self.use_situation5_combobox_edit.currentText()

            # 習慣值
            habit1 = "是" if self.habit_yes_button1_edit.isChecked() else "否"
            habit2 = self.habit_combobox2_edit.currentText()
            habit3 = self.habit_combobox3_edit.currentText()
            habit4 = self.habit_combobox4_edit.currentText()
            habit5 = self.habit_combobox5_edit.currentText()
            habit6 = self.habit_combobox6_edit.currentText()

            # 其他習慣（假設複選框）
            habit7 = []
            if self.habit_close_checkbox7_edit.isChecked():
                habit7.append("1")
            else:
                habit7.append("0")
            if self.habit_exercise_checkbox7_edit.isChecked():
                habit7.append("1")
            else:
                habit7.append("0")
            if self.habit_other_checkbox7_edit.isChecked():
                habit7.append("1")
            else:
                habit7.append("0")
            habit7_str = ",".join(habit7)  # 將多個習慣值連接成字串

            line_token = self.line_token_input_edit.text()
            submission_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())

            self.cursorObj.execute('''
                INSERT INTO user_info (
                    name, username, birthday, gender, 
                    right_eye_condition, right_eye_degree, right_eye_shine, right_eye_shine_degree,
                    left_eye_condition, left_eye_degree, left_eye_shine, left_eye_shine_degree,
                    eye_situation_value1, eye_situation_value2, eye_situation_value3, eye_situation_value4, eye_situation_value5,
                    use_situation1, use_situation2, use_situation3, use_situation_value4, use_situation_value5,
                    habit1, habit2, habit3, habit4, habit5, habit6, habit7, line_token,submission_time
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                name, user_name, birthday, gender, 
                right_eye_condition, right_eye_degree, right_eye_shine, right_eye_shine_degree,
                left_eye_condition, left_eye_degree, left_eye_shine, left_eye_shine_degree,
                eye_situation_value1, eye_situation_value2, eye_situation_value3, eye_situation_value4, eye_situation_value5,
                use_situation1, use_situation2, use_situation3, use_situation_value4, use_situation_value5,
                habit1, habit2, habit3, habit4, habit5, habit6, habit7_str, line_token, submission_time
            ))

            # Commit the new data
            self.con.commit()

            # 彈跳式視窗提示
            save_data_msg_box = QMessageBox()
            save_data_msg_box.setWindowTitle("更新提示")
            save_data_msg_box.setText("已更新完畢")
            save_data_msg_box.setIcon(QMessageBox.Information)
            save_data_msg_box.setStandardButtons(QMessageBox.Ok)
            save_data_msg_box.buttonClicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
            save_data_msg_box.exec_()

            print(f"使用者 {user_name} 的資料已更新")
        else:
            print(f"找不到使用者 {user_name} 的資料，無法更新")

    def edit_delete_all(self):  # 編輯使用者介面 : 刪除使用者
        # 從下拉選單中獲取選中的使用者名稱
        user_identifier = self.nameBox_4.currentText()

        # 檢查該使用者是否存在於 database  中
        query_check = "SELECT * FROM user_info WHERE username = ?"
        self.cursorObj.execute(query_check, (user_identifier,))
        result = self.cursorObj.fetchone()

        # 彈出確認視窗
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("確認刪除")
        msg_box.setText(f"確定要刪除使用者 {user_identifier} 及其所有相關資料嗎？")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)

        # 獲取使用者的選擇
        reply = msg_box.exec_()

        if reply == QMessageBox.Yes:
            try:
                # 刪除 database 中的 user_info 資料
                query_delete = "DELETE FROM user_info WHERE username = ?"
                self.cursorObj.execute(query_delete, (user_identifier,))
                self.con.commit()
                print(f"已從 database 刪除使用者：{user_identifier} 的所有資料")

                # 刪除與該使用者相關的 posttest 表
                related_table_name = f"{user_identifier}_posttest"
                self.cursorObj.execute(
                    f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (related_table_name,))
                table_exists = self.cursorObj.fetchone()

                if table_exists:
                    self.cursorObj.execute(f"DROP TABLE IF EXISTS {related_table_name}")
                    self.con.commit()
                    print(f"已刪除與使用者 {user_identifier} 相關的 posttest 表: {related_table_name}")
                else:
                    print(f"沒有找到與使用者 {user_identifier} 相關的 posttest 表: {related_table_name}")

                # 刪除 database 中的 threshold 資料和使用者相關表格
                self.cursorObj = self.con.cursor()

                # 刪除 threshold 表中的使用者資料
                query_delete = "DELETE FROM threshold WHERE user = ?"
                self.cursorObj.execute(query_delete, (user_identifier,))
                self.con.commit()
                print(f"已從 database 的 threshold 表中刪除使用者：{user_identifier}")

                # 刪除與該使用者相關的表（假設表名與使用者名稱一致）
                related_table_name_db = user_identifier  # 假設數據表的名稱與使用者名稱一致
                self.cursorObj.execute(
                    f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (related_table_name_db,))
                table_exists_db = self.cursorObj.fetchone()

                if table_exists_db:
                    self.cursorObj.execute(f"DROP TABLE IF EXISTS {related_table_name_db}")
                    self.con.commit()
                    print(f"數據表 {related_table_name_db} 已從 database 中刪除。")
                else:
                    print(f"數據表 {related_table_name_db} 不存在，無需刪除。")

            except sqlite3.Error as e:
                print(f"刪除 database 或 database 中使用者或相關表時發生錯誤: {e}")

            # 從 nameBox 中移除使用者名稱
            for box in [self.nameBox, self.nameBox_2, self.nameBox_3, self.nameBox_4]:
                index = box.findText(user_identifier)
                if index >= 0:
                    box.removeItem(index)

            # 返回首頁
            self.stackedWidget.setCurrentIndex(0)
            print("刪除操作已完成，返回首頁。")

        else:
            print("刪除操作已取消")

    def add_user_onchange(self):
        pass

    def camera_onchange(self):
        self.create_user_data()
        self.start_time = time.time()
        self.status = 'run'
        self.camera = cv.VideoCapture(0)
        self.timer_camera.start(5)
        self.timer_warm.start(30)
        self.camera_active = True
        self.start.setEnabled(True)
        self.suggestion.setEnabled(True)
        self.login1_homebutton.setEnabled(False)
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
                SET distance_ratio = ?, brightness = ?, blink = ? ,blink_num_th=?
                WHERE user = ?
            ''', (distance_ratio, brightness, blink, current_user))

            # Commit the changes to the database
            self.con.commit()
            print(f"Threshold values updated for user {current_user}")

        except sqlite3.Error as e:
            print(f"Error updating threshold: {e}")
        
    def start_push_onchange(self): 
        self.start_time_for_database = time.strftime("%Y-%m-%d %H:%M", time.localtime())
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
        current_time_str = time.strftime("%Y-%m-%d %H:%M", time.localtime())  # 獲取當前時間，精確到分鐘
        
        # 檢查是否在同一分鐘內重複按下
        if hasattr(self, 'last_exhausted_time_str') and self.last_exhausted_time_str == current_time_str:
            self.showMainWindow("You cannot press the button again within the same minute.", line=False)
            return

        # 更新上次按下的時間
        self.last_exhausted_time_str = current_time_str

        if self.status in ['start', 'rest']:  
            if not self.is_exhausted:  # 第一次按下，進入疲勞狀態
                self.Exhausted_state = 0  # 設置疲勞狀態為 1
                self.Exhausted_count = 1
                self.is_exhausted = True
                self.pushButton_Exhausted.setStyleSheet("background-color: yellow")  # 標記按鈕狀態
                # 顯示 "開始" 在小白板
                if self.last_time_recorded != current_time_str:
                    item = QtGui.QStandardItem(f"  {current_time_str} 開始")
                    self.listView_model.appendRow(item)
                    self.last_time_recorded = current_time_str
                message = "You entered exhausted state. Do you want to rest?"
                self.showConfirmationDialog(message, self.handle_rest_decision)
            else:  # 第二次按下按鈕，恢復正常狀態
                self.Exhausted_state = 0  # 重置疲勞狀態為0
                self.Exhausted_count = 0
                self.is_exhausted = False
                self.pushButton_Exhausted.setStyleSheet("")  # 移除按鈕狀態
                # 顯示 "結束" 在小白板
                if self.last_time_recorded != current_time_str:
                    item = QtGui.QStandardItem(f"  {current_time_str} 結束")
                    self.listView_model.appendRow(item)
                    self.last_time_recorded = current_time_str
                self.showMainWindow("Exhausted state ended", line=False)
        else:
            self.showMainWindow("Cannot change to exhausted state during shutting down")


    def showConfirmationDialog(self, message, callback):
        # 創建訊息對話框
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Confirmation')
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        
        # 設置窗口保持在最前方
        msg_box.setWindowFlags(msg_box.windowFlags() | Qt.WindowStaysOnTopHint)
        
        reply = msg_box.exec_()
        
        # 根據回應呼叫對應的回調
        if reply == QMessageBox.Yes:
            callback('yes')
        else:
            callback('no')

    def handle_rest_decision(self, choice):
        if choice == 'yes':
            # 使用者選擇休息，進入休息狀態
            self.status = 'rest'
            self.record_state = 0  # 設置為休息狀態
            self.pass_time = 0  # 重置計時
            self.previous_time_step = time.time()  # 更新時間基準
            self.showMainWindow("結束工作狀態，進入休息狀態", line=False)
        else:
            # 使用者選擇繼續工作，保持疲勞狀態
            self.is_exhausted = True           
            # 顯示仍處於疲勞狀態的消息
            self.showMainWindow("Continuing to work in exhausted state", line=False)

    def next_rest_decision(self, choice):
        if choice == 'yes':
            # 使用者選擇休息，進入休息狀態
            self.status = 'rest'
            self.record_state = 0  # 設置為休息狀態
            self.pass_time = 0  # 重置計時
            self.previous_time_step = time.time()  # 更新時間基準
            self.showMainWindow("結束工作狀態，進入休息狀態", line=False)
            self.next_threshold = 10  # 重置詢問閾值回到10分鐘
        else:
            # 使用者選擇繼續工作，保持疲勞狀態
            self.is_exhausted = True
            
            # 根據規則減少下一次彈窗的間隔
            # 第一次間隔 8 分鐘，之後每次間隔減少 2 分鐘
            if self.next_threshold == 15:
                self.next_threshold += 10
            else:
                self.next_threshold += 5
            
            # 顯示仍處於疲勞狀態的消息
            self.showMainWindow("Continuing to work in exhausted state", line=False)


    def finish_push_onchange(self): 
        self.last_exhausted_time_str = 0
        self.time_status = 'finished'
        self.status = 'shutting_down'
        self.is_running = False  # 停止推理運行
        self.release_resources()  # 釋放與推理相關的資源
        logging.getLogger('tensorflow').setLevel(logging.ERROR)  # 停止時只顯示錯誤級別的日誌

        # 關閉相機和停止推理
        if self.camera is not None:
            self.camera.release()

        # 清空 camera_site 和 camera_site_2 的畫面
        empty_frame = QPixmap(800, 600)  # 創建一個空白的畫面
        empty_frame.fill(Qt.white)  # 設置背景為黑色或其他顏色
        self.camera_site.setPixmap(empty_frame)  # 清空顯示區域
        self.camera_site_2.setPixmap(empty_frame)  # 清空副顯示區域

        # 重置疲勞按鈕狀態
        self.is_exhausted = False  # 將疲勞狀態設置為初始狀態
        self.start.setEnabled(False) 
        self.suggestion.setEnabled(False)
        self.Exhausted_state = 0  # 重置疲勞狀態變量
        self.pushButton_Exhausted.setStyleSheet("")  # 移除反黃顯示

        # 清空小白板（ListView）的內容
        self.listView_model.clear()  # 清除小白板中所有條目
        self.last_time_recorded = None  # 重置最後記錄的時間
        self.switch_page(6)  #page2 按下Finish 跳轉至page6填寫後測


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
        month = selectDay.toString("M")
        day = selectDay.toString("d")
        selected_date = selectDay.toString('yyyy-MM-dd')
        print(year, month, day)

        self.cursorObj = self.con.cursor()

        cursor = self.cursorObj.execute(
            f"SELECT year, month, day, hour, minute, distance, brightness, blink, state, Exhausted_state "
            f"FROM {self.current_user}_data WHERE year=? AND month=? AND day=? ORDER BY hour, minute",
            (year, month, day)
        )        
        self.con.commit()
        date = []
        dis = []
        bri = []
        blink = []
        use = []
        for i in cursor:
            date.append(datetime(i[0], i[1], i[2], i[3], i[4]))
            use.append(i[8])
            dis.append(float(i[5]))
            bri.append(int(i[6]))
            blink.append(int(i[7]))
        
        xfmt = matplotlib.dates.DateFormatter('%H:%M')
        datestime = matplotlib.dates.date2num(date)

        # 1. 使用時間圖表
        plt.gca().xaxis.set_major_formatter(xfmt)
        plt.plot_date(datestime, use, linestyle='solid')
        plt.yticks([0, 1, 2])
        plt.ylim(-0.1, 2.1)
        plt.title('Using Time')
        plt.text(1.0, 1.05, selected_date, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right')
        plt.savefig('use.png')
        plt.close()

        # 顯示圖片
        self.display_image(cv.imread('use.png'), (400, 270), self.use_time_graph)

        # 2. 距離圖表
        plt.gca().xaxis.set_major_formatter(xfmt)
        plt.plot_date(datestime, dis, linestyle='solid')
        plt.ylim(0, 2)
        plt.title('Distance')
        plt.text(1.0, 1.05, selected_date, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right')
        plt.savefig('dis.png')
        plt.close()

        # 顯示圖片
        self.display_image(cv.imread('dis.png'), (400, 270), self.distance_graph)

        # 3. 環境亮度圖表
        plt.gca().xaxis.set_major_formatter(xfmt)
        plt.plot_date(datestime, bri, linestyle='solid')
        plt.ylim(0, 255)
        plt.title('Brightness')
        plt.text(1.0, 1.05, selected_date, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right')
        plt.savefig('bri.png')
        plt.close()

        # 顯示圖片
        self.display_image(cv.imread('bri.png'), (400, 270), self.brightness_graph)

        # 4. 每分鐘眨眼次數圖表
        plt.gca().xaxis.set_major_formatter(xfmt)
        plt.plot_date(datestime, blink, linestyle='solid')
        plt.ylim(0, 60)
        plt.title('Blinking')
        plt.text(1.0, 1.05, selected_date, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right')
        plt.savefig('blink.png')
        plt.close()

        # 顯示圖片
        self.display_image(cv.imread('blink.png'), (400, 270), self.blink_graph)

    def send_images_to_line(self):
        """
        發送日期文字訊息和四張圖片到 LINE Notify，每張圖片附帶不同訊息
        """

        # 1. 取得當日日期並發送文字訊息
        selectDay = self.calendarWidget.selectedDate()
        selected_date = selectDay.toString('yyyy-MM-dd')  # 將選擇的日期格式化為 'yyyy-MM-dd'
        message = f"以下為 {selected_date} 的用眼分析報表"

        try:
            # 發送文字訊息到 LINE Notify
            headers = {
                "Authorization": "Bearer " + self.token,  # 使用存儲的 token
                "Content-Type": "application/x-www-form-urlencoded"
            }
            data = {'message': message}
            
            # 發送 POST 請求傳送訊息
            r = requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data)

            if r.status_code == 200:
                print("Text message sent successfully.")
            else:
                print(f"Failed to send text message. Status code: {r.status_code}")
        except Exception as e:
            print(f"Error sending text message: {e}")
            return  # 如果發送訊息失敗，就不進行後續的圖片傳送

        # 2. 發送四張圖片，每張圖片有不同的訊息
        image_files = ['use.png', 'dis.png', 'bri.png', 'blink.png']
        image_messages = [
            '當日使用時間',  # 對應 use.png
            '當日距離',      # 對應 dis.png
            '當日環境亮度',  # 對應 bri.png
            '當日平均每分鐘的眨眼次數'  # 對應 blink.png
        ]

        for image_file, image_message in zip(image_files, image_messages):
            try:
                # 開啟圖片檔案並以二進位方式讀取
                with open(image_file, 'rb') as image:
                    image_headers = {
                        "Authorization": "Bearer " + self.token,  # 使用存儲的 token
                    }

                    # 傳送每張圖片時附帶對應的訊息
                    image_data = {'message': image_message}

                    # 發送 POST 請求到 LINE Notify 並附上圖片和訊息
                    files = {'imageFile': image}
                    r = requests.post("https://notify-api.line.me/api/notify", headers=image_headers, data=image_data, files=files)

                    if r.status_code == 200:
                        print(f"Image {image_file} sent successfully with message: {image_message}")
                    else:
                        print(f"Failed to send {image_file}. Status code: {r.status_code}")
            except Exception as e:
                print(f"Error sending {image_file}: {e}")
    
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
        self.nameBox_4.addItem(text)
        self.current_user  = str(self.nameBox_2.currentText())
        if (text != ''):
            self.con = sqlite3.connect('database.db')
            self.cursorObj = self.con.cursor()

            try:
                self.cursorObj.execute(f'''CREATE TABLE IF NOT EXISTS {self.current_user}_data (year, month, day, hour, minute, distance, brightness, blink, state, Exhausted_state,start_time_for_database)''' )
                self.cursorObj.execute(f'''
                    CREATE TABLE IF NOT EXISTS {self.current_user}_posttest (
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
                        submission_time TEXT,
                        start_time_for_database TEXT
                    );
                ''')
                self.cursorObj.execute("insert or ignore into threshold(user,line_token,  distance_area, distance_ratio, brightness, blink,blink_num_th) VALUES (?,?,?,?,?,?,?)" ,(text,self.line_token_input.text(),self.eye_area_record,self.eye_area_ratio,60,4,15))
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
        query = "UPDATE threshold SET distance_area = ?, distance_ratio = ?, brightness = ?, blink = ?,blink_num_th=? WHERE user = ?"
        
        # 更新第一組閾值
        self.cursorObj.execute(query, (self.eye_area, self.distance_th.value(), self.bright_th.value(), self.blink_th.value(), self.blink_num_th_2.value(), self.current_user))
        
        # 更新第二組閾值
        self.cursorObj.execute(query, (self.eye_area, self.distance_th_2.value(), self.bright_th_2.value(), self.blink_th_2.value(), self.blink_num_th_2.value(), self.current_user))
        
        self.con.commit()


    def check_status(self):     #太近/太暗警示
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
                    if self.Exhausted_count == 1:
                        self.Exhausted_state += 1  # 累加疲勞狀態的分鐘數
                    print(f"Minute: {int(pass_minute)}, Exhausted_state: {self.Exhausted_state}")
              
                    self.previous_minute = pass_minute
                    print(f"Minute updated: previous_minute = {self.previous_minute}")

                    # 在計算是否要彈出詢問視窗的地方
                    if self.Exhausted_state >= self.next_threshold and self.status != 'rest':
                        message = "You have been in exhausted state for over {} minutes. Do you want to rest?".format(self.next_threshold)
                        self.showConfirmationDialog(message, self.next_rest_decision)

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
                    self.current_user  = str(self.nameBox_2.currentText())
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
                            f"INSERT INTO {self.current_user}_data (year, month, day, hour, minute, distance, brightness, blink, state, Exhausted_state, start_time_for_database) "
                            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (int(result.tm_year), int(result.tm_mon), int(result.tm_mday), current_hour, current_minute - 1, distance_avg, bright_avg, blink_avg, self.record_state, self.Exhausted_state, self.start_time_for_database)
                        )
                    elif self.status == 'rest':
                        print(f"Inserting into database: {self.status}, {current_hour}:{current_minute - 1}")
                        self.cursorObj.execute(
                            f"INSERT INTO {self.current_user}_data (year, month, day, hour, minute, distance, brightness, blink, state, Exhausted_state, start_time_for_database) "
                            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (int(result.tm_year), int(result.tm_mon), int(result.tm_mday), current_hour, current_minute - 1, 1, 10, 0, self.record_state, self.Exhausted_state, self.start_time_for_database)
                        )

                    self.con.commit()
                    # 插入數據後立即重置`Exhausted_state`
                    #self.Exhausted_state = 0
                    
                    if self.status == 'start':  # 確保只有在工作狀態下才檢查眨眼次數
                   # **檢查每分鐘的眨眼次數是否達標**
                        print(f"Current blink_per_minute: {blink_avg}, Threshold: {self.blink_num_th_2.value()}")
                        if blink_avg < self.blink_num_th_2.value():
                            message = f'Low blink rate: {blink_avg} blinks/minute'
                            self.lineNotifyMessage(message)  # 確保只傳送一次
                           
                            self.showMainWindow(message,line=False)
                    print(f"Before reset - blink_per_minute: {blink_avg}, Threshold: {self.blink_num_th_2.value()}")
                    # **重置每分鐘的計數器**
                    self.blink_per_minute = 0                
            
                if (remain_time< 0 and self.status=='start'):
                    print('rest')
                    self.status = 'rest'
                    self.pass_time = 0.01
                    self.previous_time_step = time.time()
                    self.blink_counter = 0
                    message = 'rest now'
                    self.showMainWindow(message,line=False)
                    # 發送LINE提醒，不依賴視窗點擊                        
                    self.lineNotifyMessage(message)                      
                elif((remain_time< 0  or self.count >= self.excerise_count.value()) and self.status=='rest'):
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
    
    def sendout(self):
        try:
            # 獲取當下的時間
            current_time = datetime.now()

            # 確保該使用者的 posttest 表存在
            self.cursorObj.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.current_user}_posttest (
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
                    submission_time TEXT,  -- 填表的時間
                    start_time_for_database TEXT             
                );
            ''')
            self.con.commit()

            # 查詢最近一次的提交時間
            self.cursorObj.execute(f'SELECT submission_time FROM {self.current_user}_posttest ORDER BY id DESC LIMIT 1')
            last_submission = self.cursorObj.fetchone()

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

            # 繼續執行資料插入
            question_1_choice = self.question_1_comboBox.currentText()
            question_2_choice = self.question_2_comboBox.currentText()
            question_3_choice = self.question_3_comboBox.currentText()
            question_4_choice = self.question_4_comboBox.currentText()
            question_5_choice = '是' if self.question_5yes_Button.isChecked() else '否'
            question_6_choice = '是' if self.question_6yes_Button.isChecked() else '否'
            question_7_value = self.question_button_group7.id(self.question_button_group7.checkedButton()) if self.question_button_group7.checkedButton() else None
            question_8_value = self.question_button_group8.id(self.question_button_group8.checkedButton()) if self.question_button_group8.checkedButton() else None
            question_9_value = self.question_button_group9.id(self.question_button_group9.checkedButton()) if self.question_button_group9.checkedButton() else None
            question_10_value = self.question_button_group10.id(self.question_button_group10.checkedButton()) if self.question_button_group10.checkedButton() else None
            question_11_value = self.question_button_group11.id(self.question_button_group11.checkedButton()) if self.question_button_group11.checkedButton() else None
            question_12_text = self.question_12_input.text()
            submission_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

            self.cursorObj.execute(f'''
                INSERT INTO user_id(
                    user_name,test_id
                )VALUES(?,?)
            ''',(
                self.current_user,self.start_time_for_database
                ))
            # 插入新資料到資料庫
            self.cursorObj.execute(f'''
                INSERT INTO {self.current_user}_posttest (
                    question_1, question_2, question_3, question_4, 
                    question_5, question_6, question_7, question_8, 
                    question_9, question_10, question_11, question_12, submission_time,start_time_for_database
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
            ''', (
                question_1_choice, question_2_choice, question_3_choice, question_4_choice,
                question_5_choice, question_6_choice, question_7_value, question_8_value,
                question_9_value, question_10_value, question_11_value, question_12_text, submission_time,self.start_time_for_database
            ))
            self.con.commit()

            print(f"資料已存入 {self.current_user}_posttest，提交時間為 {submission_time}，start_time_for_database為{self.start_time_for_database}")

            # 顯示成功訊息
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setIcon(QtWidgets.QMessageBox.Information)
            msg_box.setText("已送出")
            msg_box.setWindowTitle("確認")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg_box.buttonClicked.connect(lambda: self.switch_page(0))
            msg_box.exec_()

        except sqlite3.Error as e:
            print(f"資料庫操作失敗: {e}")
        except Exception as e:
            print(f"發生錯誤: {e}")


        self.blink_th_2.setValue(self.blink_th.value())
   
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
        target_directory = "Users/chiahsin/Eye_Myself/1022"  # 指定目標目錄
        new_file_name = os.path.join(target_directory, f"{user_name}_database.db")  # 生成新文件的完整路徑
        
        # 使用 shutil 複製檔案並重新命名
        shutil.copyfile(original_file_name, new_file_name)
        print(f"Database file copied and renamed to {new_file_name}")
        

        return [new_file_name] # 回傳兩個新檔案的路徑
    except Exception as e:
        print(f"Failed to copy and rename database files: {e}")
        return []

def upload_to_google_drive(file_paths):
    try:
        # 使用服務帳戶的 JSON 憑證檔案進行認證
        SERVICE_ACCOUNT_FILE = "/Users/chiahsin/Eye_Myself/1022/eye-myself-357cdddd6407.json"
        SCOPES = ['https://www.googleapis.com/auth/drive.file']
        
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # 建立 Google Drive API 服務
        service = build('drive', 'v3', credentials=credentials)

        # 指定目標資料夾的 ID
        folder_id = '1rowZJjh184Ogz5STLAGwms5utm2z8lsn'
        
        for file_path in file_paths:
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

            # 確認上傳成功後打印訊息
            print(f"'{file_name}' 已成功上傳到 Google Drive 中的「畢業專題」資料夾。")
        
        # 當兩個檔案都上傳成功後，打印最終確認
        if len(file_paths) == 2:
            print("兩個檔案皆已成功上傳。")

    except Exception as e:
        print(f"Failed to upload files to Google Drive: {e}")


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
