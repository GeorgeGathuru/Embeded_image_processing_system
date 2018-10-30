# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Scanning.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
import pickle
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from welcome import  Ui_MainWindow

class Ui_Dialog(QWidget):
    def guiCheck(self):
        print('Back button pressed ')
        self.welcome = QMainWindow
        # self.ui = Ui_MainWindow
        # self.ui.show()
        self.ui.setupUi(self.welcome)
        self.welcome.show()





    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 90, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.guiCheck)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 170, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(QApplication.instance().quit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Scanninig"))
        self.pushButton.setText(_translate("Dialog", "CAMERA"))
        self.pushButton_2.setText(_translate("Dialog", "BACK"))
        self.pushButton_3.setText(_translate("Dialog", "QUIT"))


    @pyqtSlot()
    def on_click(pushButton):

        face_cascade = cv2.CascadeClassifier(
            "/home/george/PycharmProjects/Embeded image processing system/haarcascade_frontalface_alt2.xml")
        eye_cascade = cv2.CascadeClassifier("frontalEyes35x16.xml")

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('recognizer/trainingData.xml')

        labels = {"person_name": 1}
        # with open("/home/george/PycharmProjects/Embeded image processing system/venv/labels.pickle", 'rb') as f:
        #     og_labels = pickle.load(f)
        #     labels = {v: k for k, v in og_labels.items()}
        print(labels)

        cap = cv2.VideoCapture(0)

        while (True):
            # Capture frame-by-frame
            ret, img = cap.read()

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=4)

            for (x, y, w, h) in faces:
                print(x, y, w, h)
                roi_gray = gray[y:y + h, x:x + w]  # (ycord_start,ycord2_end)
                roi_color = img[y:y + h, x:x + w]

                # recognizer# deep learned model predict keras tensorflow pytorch
                id, conf = recognizer.predict(roi_gray)
                if conf >= 45 and conf <= 85:

                 print(id)
                 print(labels[id])
                 font = cv2.FONT_HERSHEY_SIMPLEX
                 name = labels[id]
                 name1='George'
                 color = (255, 255, 0)
                 stroke = 2
                 cv2.putText(img, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)


                # color = (255, 0, 0)  # bgr 0-255
                # stroke = 2
                width = x + w
                height = y + h
                cv2.rectangle(img, (x, y), (width, height), color, stroke)

                # eyes = eye_cascade.detectMultiScale(roi_gray)
                #
                # for (ex, ey, ew, eh) in eyes:
                #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Scanning', img)
            if cv2.waitKey(20) & 0xFF == ord("q"):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    # sys.exit(app.exec_())

    ex = Ui_Dialog()
    sys.exit(app.exec_())
