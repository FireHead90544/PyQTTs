from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
import pyttsx3
import os
import resources
try:
    from PyQt5 import QtWinExtras
except ImportError:
    pass

engine = pyttsx3.init()
voices = engine.getProperty("voices")
batchSavePath = None
count = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon(":/logo/assets/pyqtts-logo.png"))
        MainWindow.setFixedSize(1108, 851)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLineBottom = QtWidgets.QFrame(self.centralwidget)
        self.horizontalLineBottom.setGeometry(QtCore.QRect(10, 790, 1091, 20))
        self.horizontalLineBottom.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontalLineBottom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLineBottom.setObjectName("horizontalLineBottom")
        self.verticalLineLeft = QtWidgets.QFrame(self.centralwidget)
        self.verticalLineLeft.setGeometry(QtCore.QRect(0, 10, 20, 791))
        self.verticalLineLeft.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalLineLeft.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLineLeft.setObjectName("verticalLineLeft")
        self.verticalLineRight = QtWidgets.QFrame(self.centralwidget)
        self.verticalLineRight.setGeometry(QtCore.QRect(1090, 10, 20, 791))
        self.verticalLineRight.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalLineRight.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLineRight.setObjectName("verticalLineRight")
        self.horizontalLineTop = QtWidgets.QFrame(self.centralwidget)
        self.horizontalLineTop.setGeometry(QtCore.QRect(10, 0, 1091, 20))
        self.horizontalLineTop.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontalLineTop.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLineTop.setObjectName("horizontalLineTop")
        self.horizontalLineSeparator = QtWidgets.QFrame(self.centralwidget)
        self.horizontalLineSeparator.setGeometry(QtCore.QRect(10, 310, 1091, 20))
        self.horizontalLineSeparator.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontalLineSeparator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLineSeparator.setObjectName("horizontalLineSeparator")
        self.verticalLineTextSeparator = QtWidgets.QFrame(self.centralwidget)
        self.verticalLineTextSeparator.setGeometry(QtCore.QRect(580, 320, 20, 481))
        self.verticalLineTextSeparator.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalLineTextSeparator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLineTextSeparator.setObjectName("verticalLineTextSeparator")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, -10, 671, 91))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setToolTip("")
        self.label.setObjectName("label")
        self.horizontalLineTitleSeparator = QtWidgets.QFrame(self.centralwidget)
        self.horizontalLineTitleSeparator.setGeometry(QtCore.QRect(10, 50, 1091, 20))
        self.horizontalLineTitleSeparator.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontalLineTitleSeparator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLineTitleSeparator.setObjectName("horizontalLineTitleSeparator")
        self.labelSpeechRate = QtWidgets.QLabel(self.centralwidget)
        self.labelSpeechRate.setGeometry(QtCore.QRect(60, 110, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelSpeechRate.setFont(font)
        self.labelSpeechRate.setObjectName("labelSpeechRate")
        self.labelSpeechVolume = QtWidgets.QLabel(self.centralwidget)
        self.labelSpeechVolume.setGeometry(QtCore.QRect(60, 210, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelSpeechVolume.setFont(font)
        self.labelSpeechVolume.setObjectName("labelSpeechVolume")
        self.volumeSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.volumeSpinBox.setGeometry(QtCore.QRect(210, 210, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.volumeSpinBox.setFont(font)
        self.volumeSpinBox.setToolTipDuration(5)
        self.volumeSpinBox.setMaximum(1.0)
        self.volumeSpinBox.setSingleStep(0.1)
        self.volumeSpinBox.setProperty("value", 1.0)
        self.volumeSpinBox.setObjectName("volumeSpinBox")
        self.speedSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.speedSpinBox.setGeometry(QtCore.QRect(210, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.speedSpinBox.setFont(font)
        self.speedSpinBox.setToolTipDuration(5)
        self.speedSpinBox.setMinimum(10)
        self.speedSpinBox.setMaximum(1000)
        self.speedSpinBox.setSingleStep(10)
        self.speedSpinBox.setProperty("value", 200)
        self.speedSpinBox.setObjectName("speedSpinBox")
        self.labelSpeechRate_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelSpeechRate_2.setGeometry(QtCore.QRect(510, 110, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelSpeechRate_2.setFont(font)
        self.labelSpeechRate_2.setObjectName("labelSpeechRate_2")
        self.voiceComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.voiceComboBox.setGeometry(QtCore.QRect(640, 110, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.voiceComboBox.setFont(font)
        self.voiceComboBox.setToolTipDuration(5)
        self.voiceComboBox.setEditable(False)
        self.voiceComboBox.setMaxVisibleItems(25)
        self.voiceComboBox.setObjectName("voiceComboBox")
        self.voiceComboBox.addItem("")
        self.ttsTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.ttsTextEdit.setGeometry(QtCore.QRect(30, 366, 541, 411))
        self.ttsTextEdit.setToolTipDuration(5)
        self.ttsTextEdit.setTabStopDistance(79.0)
        self.ttsTextEdit.setObjectName("ttsTextEdit")
        self.labelTtsText = QtWidgets.QLabel(self.centralwidget)
        self.labelTtsText.setGeometry(QtCore.QRect(260, 320, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelTtsText.setFont(font)
        self.labelTtsText.setObjectName("labelTtsText")
        self.playPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.playPushButton.setGeometry(QtCore.QRect(620, 390, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.playPushButton.setFont(font)
        self.playPushButton.setObjectName("playPushButton")
        self.labelTtsControls = QtWidgets.QLabel(self.centralwidget)
        self.labelTtsControls.setGeometry(QtCore.QRect(770, 320, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelTtsControls.setFont(font)
        self.labelTtsControls.setObjectName("labelTtsControls")
        self.batchSavePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.batchSavePushButton.setGeometry(QtCore.QRect(940, 390, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.batchSavePushButton.setFont(font)
        self.batchSavePushButton.setObjectName("batchSavePushButton")
        self.directorySelectPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.directorySelectPushButton.setGeometry(QtCore.QRect(870, 390, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.directorySelectPushButton.setFont(font)
        self.directorySelectPushButton.setObjectName("directorySelectPushButton")
        self.savePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.savePushButton.setGeometry(QtCore.QRect(620, 490, 451, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.savePushButton.setFont(font)
        self.savePushButton.setObjectName("savePushButton")
        self.quitPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitPushButton.setGeometry(QtCore.QRect(850, 670, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quitPushButton.setFont(font)
        self.quitPushButton.setObjectName("quitPushButton")
        self.aboutPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.aboutPushButton.setGeometry(QtCore.QRect(620, 670, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aboutPushButton.setFont(font)
        self.aboutPushButton.setObjectName("aboutPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQTTs - Open Source Text To Speech GUI Application"))
        self.label.setStatusTip(_translate("MainWindow", "Designed & Developed By </Rudransh Joshi> | GitHub: FireHead90544"))
        self.label.setText(_translate("MainWindow", "PyQTTs - Open Source Text To Speech GUI Application"))
        self.labelSpeechRate.setText(_translate("MainWindow", "Speed"))
        self.labelSpeechVolume.setText(_translate("MainWindow", "Volume"))
        self.volumeSpinBox.setToolTip(_translate("MainWindow", "Volume of the Speech. It determines the loudness of the sound."))
        self.volumeSpinBox.setStatusTip(_translate("MainWindow", "Volume of the Speech. It determines the loudness of the sound."))
        self.speedSpinBox.setToolTip(_translate("MainWindow", "Speed of the speech in WPM. How fast or slow will the words be spoken."))
        self.speedSpinBox.setStatusTip(_translate("MainWindow", "Speed of the speech in WPM. How fast or slow will the words be spoken."))
        self.labelSpeechRate_2.setText(_translate("MainWindow", "Voice"))
        self.voiceComboBox.setToolTip(_translate("MainWindow", "Voice of the spokesperson. Select one voice from available voices installed on your system."))
        self.voiceComboBox.setStatusTip(_translate("MainWindow", "Voice of the spokesperson. Select one voice from available voices installed on your system."))
        self.ttsTextEdit.setToolTip(_translate("MainWindow", "The text which you want to convert into speech."))
        self.ttsTextEdit.setStatusTip(_translate("MainWindow", "The text which you want to convert into speech."))
        self.ttsTextEdit.setPlaceholderText(_translate("MainWindow", "Enter your text here which you want to convert into speech."))
        self.labelTtsText.setText(_translate("MainWindow", "Text"))
        self.playPushButton.setStatusTip(_translate("MainWindow", "Plays the speech with the selected settings and given text."))
        self.playPushButton.setText(_translate("MainWindow", "Play"))
        self.labelTtsControls.setText(_translate("MainWindow", "Controls"))
        self.batchSavePushButton.setStatusTip(_translate("MainWindow", "Saves the file instantly in the directory selected with names 1.wav, 2.wav, and so on. Click (...) button on left to select directory."))
        self.batchSavePushButton.setText(_translate("MainWindow", "Save"))
        self.directorySelectPushButton.setStatusTip(_translate("MainWindow", "Select the directory to save Batch save output in."))
        self.directorySelectPushButton.setText(_translate("MainWindow", "..."))
        self.savePushButton.setStatusTip(_translate("MainWindow", "Saves the speech output in .wav format."))
        self.savePushButton.setText(_translate("MainWindow", "Save As"))
        self.quitPushButton.setStatusTip(_translate("MainWindow", "Quits the application."))
        self.quitPushButton.setText(_translate("MainWindow", "Quit"))
        self.aboutPushButton.setStatusTip(_translate("MainWindow", "Shows the info about the application and developer."))
        self.aboutPushButton.setText(_translate("MainWindow", "About"))

        # Logic Handling
        self.quitPushButton.clicked.connect(self.quitApplication)  # Quit Button Quits The Application
        self.aboutPushButton.clicked.connect(self.aboutApplication)  # Shows About Application & Developer Box
        self.playPushButton.clicked.connect(self.playTTSThread)  # Plays Speech Using Separate Thread
        self.savePushButton.clicked.connect(self.saveOutput)  # Saves The Speech Output In A .wav File
        self.directorySelectPushButton.clicked.connect(self.selectDirectory)  # Selects The Batch Save Directory
        self.batchSavePushButton.clicked.connect(self.batchSave)  # Saves The Speech Instantly On Clicking Save In Save Directory

        # Adding Available Voices In Combo Boxes
        allVoices = voices
        self.voiceComboBox.removeItem(0)  # Removing The Blank Choice
        # self.voiceComboBox.setItemText(0, _translate("MainWindow", allVoices[0].name))
        # allVoices.pop(0)
        for voice in allVoices:
            self.voiceComboBox.addItem(voice.name)

    # Quit Button
    def quitApplication(self):
        app.quit()

    # About Button
    def aboutApplication(self):
        self.aboutMessageBox = QtWidgets.QMessageBox(self.centralwidget)
        self.pixmap = QtGui.QPixmap(":/logo/assets/pyqtts-logo.png")
        self.pixmap = self.pixmap.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
        self.aboutMessageBox.setIconPixmap(self.pixmap)
        self.aboutMessageBox.setWindowTitle("About PyQTTs")
        self.aboutMessageBox.setTextFormat(QtCore.Qt.RichText)
        self.aboutMessageBox.setText("PyQTTs is an open-source text-to-speech GUI Program written in Python. This program allows you to convert text to speech even with custom voices installed on your system with speech controls. You can save the output of speech in .wav format. You can know more about PyQTTs, get support, download new builds, report bugs at our GitHub Repository Here:<br><a href=\"https://github.com/FireHead90544/PyQTTs\">©Rudransh Joshi | PyQTTs</a>")
        self.aboutMessageBox.exec_()

    # Directory Selection Button
    def selectDirectory(self):
        self.saveDirectoryDialog = QtWidgets.QFileDialog(self.centralwidget)
        global batchSavePath
        batchSaveCheckPath = self.saveDirectoryDialog.getExistingDirectory(self.centralwidget, "Batch Save Path")
        try:
            pathToDirectory = os.listdir(batchSaveCheckPath)
        except FileNotFoundError:
            return
        if not len(pathToDirectory) == 0:
            self.directoryNotEmptyErrorMessageBox = QtWidgets.QMessageBox(self.centralwidget)
            self.directoryNotEmptyErrorMessageBox.setIcon(QtWidgets.QMessageBox.Critical)
            self.directoryNotEmptyErrorMessageBox.setWindowTitle("Directory Not Empty")
            self.directoryNotEmptyErrorMessageBox.setText("Batch save requires an empty directory, else you might face problems, so please select an empty directory. You need to select an empty directory each time you rerun the program.")
            self.directoryNotEmptyErrorMessageBox.exec_()
        else:
            batchSavePath = batchSaveCheckPath


    # Play Button
    def playTTSThread(self):
        text = self.ttsTextEdit.toPlainText().lstrip().rstrip()
        if text == "" or text.isspace():
            return
        rate = self.speedSpinBox.value()
        volume = round(self.volumeSpinBox.value(), 2)
        selectedVoiceName = self.voiceComboBox.currentText()
        for voice in voices:
            if voice.name == selectedVoiceName:
                voiceSelected = voice.id

        self.playThread = PlayThread(rate, volume, voiceSelected, text)
        self.playPushButton.setEnabled(False)
        self.savePushButton.setEnabled(False)
        self.directorySelectPushButton.setEnabled(False)
        self.batchSavePushButton.setEnabled(False)
        self.playThread.start()
        self.playThread.finished.connect(self.controlPlayStopButtons)

    # Enabling/Disabling Buttons After Thread Has Finished Working
    def controlPlayStopButtons(self):
        self.playPushButton.setEnabled(True)
        self.savePushButton.setEnabled(True)
        self.directorySelectPushButton.setEnabled(True)
        self.batchSavePushButton.setEnabled(True)


    # Save Button
    def saveOutput(self):
        text = self.ttsTextEdit.toPlainText().lstrip().rstrip()
        if text == "" or text.isspace():
            return
        rate = self.speedSpinBox.value()
        volume = round(self.volumeSpinBox.value(), 2)
        selectedVoiceName = self.voiceComboBox.currentText()
        for voice in voices:
            if voice.name == selectedVoiceName:
                voiceSelected = voice.id

        self.saveFileDialog = QtWidgets.QFileDialog(self.centralwidget)
        savePath = self.saveFileDialog.getSaveFileName(self.centralwidget, "Save As", "", "Wave Audio File (*.wav)")
        savePath = savePath[0]
        self.saveThread = SaveThread(rate, volume, voiceSelected, text, savePath)
        self.savePushButton.setEnabled(False)
        self.saveThread.start()
        self.saveThread.finished.connect(lambda: self.savePushButton.setEnabled(True))

    # Batch Save Button
    def batchSave(self):
        global batchSavePath
        global count
        if batchSavePath == None:
            self.batchSaveDirectoryErrorMessageBox = QtWidgets.QMessageBox(self.centralwidget)
            self.batchSaveDirectoryErrorMessageBox.setIcon(QtWidgets.QMessageBox.Warning)
            self.batchSaveDirectoryErrorMessageBox.setWindowTitle("Select Directory")
            self.batchSaveDirectoryErrorMessageBox.setText("For batch save, you need to first select a directory where all speech outputs will be saved with names 1.wav, 2.wav, and so on, Kindly don\'t mess the directory and keep it clean else you might face problems. Better select an empty directory. Click the (...) button on the left of the Save button to select the batch save directory.")
            self.batchSaveDirectoryErrorMessageBox.exec_()
            return
        text = self.ttsTextEdit.toPlainText().lstrip().rstrip()
        if text == "" or text.isspace():
            return
        rate = self.speedSpinBox.value()
        volume = round(self.volumeSpinBox.value(), 2)
        selectedVoiceName = self.voiceComboBox.currentText()
        for voice in voices:
            if voice.name == selectedVoiceName:
                voiceSelected = voice.id
        count += 1
        batchSaveFilePath = f"{batchSavePath}/{count}.wav"
        self.batchSaveThread = BatchSaveThread(rate, volume, voiceSelected, text, batchSaveFilePath)
        self.directorySelectPushButton.setEnabled(False)
        self.batchSavePushButton.setEnabled(False)
        self.batchSaveThread.start()
        self.batchSaveThread.finished.connect(self.controlPlayStopButtons)


class PlayThread(QThread):
    def __init__(self, rate, volume, voice, text):
        super(PlayThread, self).__init__()
        self.rate = rate
        self.volume = volume
        self.voice = voice
        self.text = text

    def run(self):
        engine.setProperty("voice", self.voice)
        engine.setProperty("volume", self.volume)
        engine.setProperty("rate", self.rate)

        engine.say(self.text)
        engine.runAndWait()


class SaveThread(QThread):
    def __init__(self, rate, volume, voice, text, batchSaveFilePath):
        super(SaveThread, self).__init__()
        self.rate = rate
        self.volume = volume
        self.voice = voice
        self.text = text
        self.batchSaveFilePath = batchSaveFilePath

    def run(self):
        engine.setProperty("voice", self.voice)
        engine.setProperty("volume", self.volume)
        engine.setProperty("rate", self.rate)

        engine.save_to_file(self.text, self.batchSaveFilePath)
        engine.runAndWait()


class BatchSaveThread(QThread):
    def __init__(self, rate, volume, voice, text, savePath):
        super(BatchSaveThread, self).__init__()
        self.rate = rate
        self.volume = volume
        self.voice = voice
        self.text = text
        self.savePath = savePath

    def run(self):
        engine.setProperty("voice", self.voice)
        engine.setProperty("volume", self.volume)
        engine.setProperty("rate", self.rate)

        engine.save_to_file(self.text, self.savePath)
        engine.runAndWait()


if __name__ == "__main__":
    import sys

    QtWinExtras.QtWin.setCurrentProcessExplicitAppUserModelID("rudranshjoshi.python.pyqt5.v1")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
