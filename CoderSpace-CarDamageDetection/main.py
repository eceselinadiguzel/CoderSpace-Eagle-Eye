########################################################################
# IMPORT LIBS
from carDamageGUI import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtCore import QTimer, QDir, Qt, QUrl
import cv2
import os
import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication,
                             QLabel, QFileDialog, QStyle, QVBoxLayout, QComboBox, QButtonGroup, QInputDialog)
########################################################################
# IMPORT DETECTION FILE
current_script_path = os.path.abspath(__file__)
project_directory = current_script_path
while os.path.basename(project_directory) != 'CoderSpace-CarDamageDetection' and project_directory != os.path.dirname(project_directory):
    project_directory = os.path.dirname(project_directory)
if os.path.basename(project_directory) != 'CoderSpace-CarDamageDetection':
    raise Exception("Proje klasörü 'CoderSpace-CarDamageDetection' bulunamadı.")
yolo_model_path = os.path.join(project_directory, 'yoloModel')
sys.path.append(yolo_model_path)
import detectDamage
########################################################################
# DECLARATION SIZE OF IMAGES
x = 640
y = 480

x2 = 640
y2 = 480
########################################################################
# GLOBAL DECLARATION
fileName = ""
########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #######################################################################
        ## # Remove window tittle bar
        ########################################################################
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #######################################################################
        ## # Set main background to transparent
        ########################################################################
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #######################################################################
        ## # Shadow effect style
        ########################################################################

        #Minimize window
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        #######################################################################
        #Close window
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        #######################################################################
        #Restore/Maximize window
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        ###################################################
        # Timer for cam and video
        ####################################################
        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.ui.selectButton.clicked.connect(self.controlTimerCam)



        # ###############################################
        # Function to Move window on mouse drag event on the tittle bar
        # ###############################################
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    #Move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        #######################################################################

        #######################################################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        #######################################################################
        self.ui.header_frame.mouseMoveEvent = moveWindow
        #######################################################################
        self.show()

    #######################################################################
    # Update restore button icon on msximizing or minimizing window
    #######################################################################
    def restore_or_maximize_window(self):
        # If window is maxmized
        if self.isMaximized():
            self.showNormal()
            # Change Icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            # Change Icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/minimize-2.svg"))
    ####################################################################

    def openFile(self):
        global fileName
        current_directory = os.getcwd()
        test_img_directory = os.path.join(current_directory, 'TestImg')
        fileName, _ = QFileDialog.getOpenFileName(
            None,
            "Open Image",
            test_img_directory,
            "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )
        if fileName:
            return fileName
        else:
            return None
    def viewCam(self):
        self.ui.info = "cam"
        self.ui.image = cv2.imread(fileName)
        img = detectDamage.main(self.ui.image)
        self.ui.image = cv2.resize(img, (x2,y2))
        height, width, channel = self.ui.image.shape
        step = channel * width
        qImg = QImage(self.ui.image.data, width, height, step, QImage.Format_BGR888)
        self.ui.screen.setPixmap(QPixmap.fromImage(qImg))
        self.timer.stop()


    def controlTimerCam(self):
        if not self.timer.isActive():
            fileName = self.openFile()
            self.timer.start(20)
        else:
            self.timer.stop()
            self.cap.release()


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

########################################################################
## END===>
########################################################################  