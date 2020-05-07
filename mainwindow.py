# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_qencoder(object):
    def setupUi(self, qencoder):
        qencoder.setObjectName("qencoder")
        qencoder.resize(780, 595)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(qencoder.sizePolicy().hasHeightForWidth())
        qencoder.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(qencoder)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_status.sizePolicy().hasHeightForWidth())
        self.label_status.setSizePolicy(sizePolicy)
        self.label_status.setMinimumSize(QtCore.QSize(180, 0))
        self.label_status.setStatusTip("")
        self.label_status.setText("")
        self.label_status.setObjectName("label_status")
        self.gridLayout_3.addWidget(self.label_status, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_simple = QtWidgets.QWidget()
        self.tab_simple.setObjectName("tab_simple")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_simple)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_preset = QtWidgets.QLabel(self.tab_simple)
        self.label_preset.setToolTip("")
        self.label_preset.setObjectName("label_preset")
        self.gridLayout_2.addWidget(self.label_preset, 1, 2, 1, 1)
        self.audioqualitybox = QtWidgets.QComboBox(self.tab_simple)
        self.audioqualitybox.setToolTip("")
        self.audioqualitybox.setObjectName("audioqualitybox")
        self.gridLayout_2.addWidget(self.audioqualitybox, 2, 3, 1, 1)
        self.label_quality = QtWidgets.QLabel(self.tab_simple)
        self.label_quality.setToolTip("")
        self.label_quality.setObjectName("label_quality")
        self.gridLayout_2.addWidget(self.label_quality, 0, 2, 1, 1)
        self.checkBox_audio = QtWidgets.QCheckBox(self.tab_simple)
        self.checkBox_audio.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox_audio.setToolTip("")
        self.checkBox_audio.setChecked(False)
        self.checkBox_audio.setObjectName("checkBox_audio")
        self.gridLayout_2.addWidget(self.checkBox_audio, 2, 0, 1, 1)
        self.label_audioquality = QtWidgets.QLabel(self.tab_simple)
        self.label_audioquality.setToolTip("")
        self.label_audioquality.setObjectName("label_audioquality")
        self.gridLayout_2.addWidget(self.label_audioquality, 2, 2, 1, 1)
        self.comboBox_quality = QtWidgets.QComboBox(self.tab_simple)
        self.comboBox_quality.setToolTip("")
        self.comboBox_quality.setObjectName("comboBox_quality")
        self.gridLayout_2.addWidget(self.comboBox_quality, 0, 3, 1, 1)
        self.presetbox = QtWidgets.QComboBox(self.tab_simple)
        self.presetbox.setToolTip("")
        self.presetbox.setObjectName("presetbox")
        self.gridLayout_2.addWidget(self.presetbox, 1, 3, 1, 1)
        self.checkBox_twopass = QtWidgets.QCheckBox(self.tab_simple)
        self.checkBox_twopass.setToolTip("")
        self.checkBox_twopass.setChecked(True)
        self.checkBox_twopass.setObjectName("checkBox_twopass")
        self.gridLayout_2.addWidget(self.checkBox_twopass, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.comboBox_encoder = QtWidgets.QComboBox(self.tab_simple)
        self.comboBox_encoder.setObjectName("comboBox_encoder")
        self.gridLayout_2.addWidget(self.comboBox_encoder, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_simple)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 242, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_simple, "")
        self.tab_advanced = QtWidgets.QWidget()
        self.tab_advanced.setObjectName("tab_advanced")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_advanced)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_hdr = QtWidgets.QCheckBox(self.tab_advanced)
        self.checkBox_hdr.setObjectName("checkBox_hdr")
        self.gridLayout.addWidget(self.checkBox_hdr, 2, 4, 1, 1)
        self.label_audio = QtWidgets.QLabel(self.tab_advanced)
        self.label_audio.setObjectName("label_audio")
        self.gridLayout.addWidget(self.label_audio, 0, 3, 1, 1)
        self.checkBox_minsplit = QtWidgets.QCheckBox(self.tab_advanced)
        self.checkBox_minsplit.setObjectName("checkBox_minsplit")
        self.gridLayout.addWidget(self.checkBox_minsplit, 4, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_advanced)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_jobs = QtWidgets.QLabel(self.tab_advanced)
        self.label_jobs.setObjectName("label_jobs")
        self.gridLayout.addWidget(self.label_jobs, 3, 0, 1, 1)
        self.label_boost = QtWidgets.QLabel(self.tab_advanced)
        self.label_boost.setObjectName("label_boost")
        self.gridLayout.addWidget(self.label_boost, 1, 3, 1, 1)
        self.label_split = QtWidgets.QLabel(self.tab_advanced)
        self.label_split.setObjectName("label_split")
        self.gridLayout.addWidget(self.label_split, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 2, 1, 1)
        self.spinBox_speed = QtWidgets.QSpinBox(self.tab_advanced)
        self.spinBox_speed.setMaximum(8)
        self.spinBox_speed.setProperty("value", 4)
        self.spinBox_speed.setObjectName("spinBox_speed")
        self.gridLayout.addWidget(self.spinBox_speed, 2, 1, 1, 1)
        self.comboBox_colorspace = QtWidgets.QComboBox(self.tab_advanced)
        self.comboBox_colorspace.setObjectName("comboBox_colorspace")
        self.gridLayout.addWidget(self.comboBox_colorspace, 5, 1, 1, 1)
        self.spinBox_jobs = QtWidgets.QSpinBox(self.tab_advanced)
        self.spinBox_jobs.setMinimum(0)
        self.spinBox_jobs.setMaximum(128)
        self.spinBox_jobs.setSingleStep(1)
        self.spinBox_jobs.setProperty("value", 0)
        self.spinBox_jobs.setObjectName("spinBox_jobs")
        self.gridLayout.addWidget(self.spinBox_jobs, 3, 1, 1, 1)
        self.comboBox_inputFormat = QtWidgets.QComboBox(self.tab_advanced)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_inputFormat.sizePolicy().hasHeightForWidth())
        self.comboBox_inputFormat.setSizePolicy(sizePolicy)
        self.comboBox_inputFormat.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_inputFormat.setObjectName("comboBox_inputFormat")
        self.gridLayout.addWidget(self.comboBox_inputFormat, 4, 1, 1, 1)
        self.label_inputformat = QtWidgets.QLabel(self.tab_advanced)
        self.label_inputformat.setObjectName("label_inputformat")
        self.gridLayout.addWidget(self.label_inputformat, 4, 0, 1, 1)
        self.label_q = QtWidgets.QLabel(self.tab_advanced)
        self.label_q.setObjectName("label_q")
        self.gridLayout.addWidget(self.label_q, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_advanced)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.spinBox_boost = QtWidgets.QSpinBox(self.tab_advanced)
        self.spinBox_boost.setMaximum(50)
        self.spinBox_boost.setProperty("value", 0)
        self.spinBox_boost.setObjectName("spinBox_boost")
        self.gridLayout.addWidget(self.spinBox_boost, 1, 4, 1, 1)
        self.checkBox_tempfolder = QtWidgets.QCheckBox(self.tab_advanced)
        self.checkBox_tempfolder.setObjectName("checkBox_tempfolder")
        self.gridLayout.addWidget(self.checkBox_tempfolder, 3, 4, 1, 1)
        self.checkBox_rtenc = QtWidgets.QCheckBox(self.tab_advanced)
        self.checkBox_rtenc.setObjectName("checkBox_rtenc")
        self.gridLayout.addWidget(self.checkBox_rtenc, 4, 3, 1, 1)
        self.spinBox_audio = QtWidgets.QSpinBox(self.tab_advanced)
        self.spinBox_audio.setReadOnly(True)
        self.spinBox_audio.setMinimum(8)
        self.spinBox_audio.setMaximum(480)
        self.spinBox_audio.setSingleStep(8)
        self.spinBox_audio.setProperty("value", 96)
        self.spinBox_audio.setObjectName("spinBox_audio")
        self.gridLayout.addWidget(self.spinBox_audio, 0, 4, 1, 1)
        self.spinBox_split = QtWidgets.QSpinBox(self.tab_advanced)
        self.spinBox_split.setMinimum(1)
        self.spinBox_split.setMaximum(99)
        self.spinBox_split.setProperty("value", 30)
        self.spinBox_split.setObjectName("spinBox_split")
        self.gridLayout.addWidget(self.spinBox_split, 1, 1, 1, 1)
        self.spinBox_quality = QtWidgets.QSpinBox(self.tab_advanced)
        self.spinBox_quality.setMinimum(0)
        self.spinBox_quality.setMaximum(63)
        self.spinBox_quality.setObjectName("spinBox_quality")
        self.gridLayout.addWidget(self.spinBox_quality, 0, 1, 1, 1)
        self.checkBox_resume = QtWidgets.QCheckBox(self.tab_advanced)
        self.checkBox_resume.setObjectName("checkBox_resume")
        self.gridLayout.addWidget(self.checkBox_resume, 3, 3, 1, 1)
        self.checkBox_bitrate = QtWidgets.QCheckBox(self.tab_advanced)
        self.checkBox_bitrate.setObjectName("checkBox_bitrate")
        self.gridLayout.addWidget(self.checkBox_bitrate, 2, 3, 1, 1)
        self.lineEdit_colordata = QtWidgets.QLineEdit(self.tab_advanced)
        self.lineEdit_colordata.setEnabled(False)
        self.lineEdit_colordata.setText("")
        self.lineEdit_colordata.setObjectName("lineEdit_colordata")
        self.gridLayout.addWidget(self.lineEdit_colordata, 6, 0, 1, 5)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_advanced, "")
        self.tab_custom = QtWidgets.QWidget()
        self.tab_custom.setObjectName("tab_custom")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_custom)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_3 = QtWidgets.QLabel(self.tab_custom)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 2)
        self.checkBox_videocmd = QtWidgets.QCheckBox(self.tab_custom)
        self.checkBox_videocmd.setObjectName("checkBox_videocmd")
        self.gridLayout_7.addWidget(self.checkBox_videocmd, 1, 0, 1, 1)
        self.textEdit_videocmd = QtWidgets.QTextEdit(self.tab_custom)
        self.textEdit_videocmd.setEnabled(False)
        self.textEdit_videocmd.setAcceptRichText(False)
        self.textEdit_videocmd.setObjectName("textEdit_videocmd")
        self.gridLayout_7.addWidget(self.textEdit_videocmd, 1, 1, 1, 1)
        self.checkBox_audiocmd = QtWidgets.QCheckBox(self.tab_custom)
        self.checkBox_audiocmd.setObjectName("checkBox_audiocmd")
        self.gridLayout_7.addWidget(self.checkBox_audiocmd, 2, 0, 1, 1)
        self.textEdit_audiocmd = QtWidgets.QTextEdit(self.tab_custom)
        self.textEdit_audiocmd.setEnabled(False)
        self.textEdit_audiocmd.setAcceptRichText(False)
        self.textEdit_audiocmd.setObjectName("textEdit_audiocmd")
        self.gridLayout_7.addWidget(self.textEdit_audiocmd, 2, 1, 1, 1)
        self.checkBox_ffmpegcmd = QtWidgets.QCheckBox(self.tab_custom)
        self.checkBox_ffmpegcmd.setObjectName("checkBox_ffmpegcmd")
        self.gridLayout_7.addWidget(self.checkBox_ffmpegcmd, 3, 0, 1, 1)
        self.textEdit_ffmpegcmd = QtWidgets.QTextEdit(self.tab_custom)
        self.textEdit_ffmpegcmd.setEnabled(False)
        self.textEdit_ffmpegcmd.setAcceptRichText(False)
        self.textEdit_ffmpegcmd.setObjectName("textEdit_ffmpegcmd")
        self.gridLayout_7.addWidget(self.textEdit_ffmpegcmd, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_custom, "")
        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setMinimumSize(QtCore.QSize(120, 0))
        self.pushButton.setStatusTip("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 2, 3, 1, 1)
        self.progressBar_total = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_total.setEnabled(False)
        self.progressBar_total.setProperty("value", 0)
        self.progressBar_total.setObjectName("progressBar_total")
        self.gridLayout_3.addWidget(self.progressBar_total, 2, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.inputPath = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPath.sizePolicy().hasHeightForWidth())
        self.inputPath.setSizePolicy(sizePolicy)
        self.inputPath.setText("")
        self.inputPath.setTextFormat(QtCore.Qt.PlainText)
        self.inputPath.setWordWrap(True)
        self.inputPath.setObjectName("inputPath")
        self.gridLayout_4.addWidget(self.inputPath, 0, 1, 1, 1)
        self.inputFileChoose = QtWidgets.QPushButton(self.centralwidget)
        self.inputFileChoose.setMinimumSize(QtCore.QSize(140, 0))
        self.inputFileChoose.setMaximumSize(QtCore.QSize(140, 16777215))
        self.inputFileChoose.setObjectName("inputFileChoose")
        self.gridLayout_4.addWidget(self.inputFileChoose, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)
        self.outputPath = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputPath.sizePolicy().hasHeightForWidth())
        self.outputPath.setSizePolicy(sizePolicy)
        self.outputPath.setText("")
        self.outputPath.setTextFormat(QtCore.Qt.PlainText)
        self.outputPath.setWordWrap(True)
        self.outputPath.setObjectName("outputPath")
        self.gridLayout_4.addWidget(self.outputPath, 1, 1, 1, 1)
        self.outputFileChoose = QtWidgets.QPushButton(self.centralwidget)
        self.outputFileChoose.setObjectName("outputFileChoose")
        self.gridLayout_4.addWidget(self.outputFileChoose, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 4)
        qencoder.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(qencoder)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 34))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        qencoder.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(qencoder)
        self.statusbar.setObjectName("statusbar")
        qencoder.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(qencoder)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(qencoder)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(qencoder)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(qencoder)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(qencoder)

    def retranslateUi(self, qencoder):
        _translate = QtCore.QCoreApplication.translate
        qencoder.setWindowTitle(_translate("qencoder", "qencoder"))
        self.label_preset.setStatusTip(_translate("qencoder", "Faster presets take more space at a given quality. \'medium\' is usually best."))
        self.label_preset.setText(_translate("qencoder", "Speed Preset"))
        self.audioqualitybox.setStatusTip(_translate("qencoder", "What bitrate should the audio be? If unsure use 96kbps."))
        self.label_quality.setStatusTip(_translate("qencoder", "The final quality of your output video. If unsure, use 26."))
        self.label_quality.setText(_translate("qencoder", "Quality Preset"))
        self.checkBox_audio.setStatusTip(_translate("qencoder", "Reencode source audio as opus (otherwise will copy existing audio if any is present)"))
        self.checkBox_audio.setText(_translate("qencoder", "Reencode Audio"))
        self.label_audioquality.setStatusTip(_translate("qencoder", "What bitrate should the audio be? If unsure use 96kbps."))
        self.label_audioquality.setText(_translate("qencoder", "Audio Quality"))
        self.comboBox_quality.setStatusTip(_translate("qencoder", "The final quality of your output video. If unsure, use 26."))
        self.presetbox.setStatusTip(_translate("qencoder", "Faster presets take more space at a given quality. \'medium\' is usually best."))
        self.checkBox_twopass.setStatusTip(_translate("qencoder", "Use twopass encoding. Highly recommended when possible."))
        self.checkBox_twopass.setText(_translate("qencoder", "Two Pass"))
        self.comboBox_encoder.setStatusTip(_translate("qencoder", "av1 is the most modern/efficient. vp9/8 have good compatibility/speed."))
        self.label_4.setStatusTip(_translate("qencoder", "av1 is the most modern/efficient. vp9/8 have good compatibility/speed."))
        self.label_4.setText(_translate("qencoder", "Encoder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_simple), _translate("qencoder", "Simple Settings"))
        self.checkBox_hdr.setStatusTip(_translate("qencoder", "Use 10 bit colorspace for output video. Greatly reduces banding and improves efficiency."))
        self.checkBox_hdr.setText(_translate("qencoder", "10 bit output"))
        self.label_audio.setStatusTip(_translate("qencoder", "With 2 channel stereo, 96kbps is usually transparent."))
        self.label_audio.setText(_translate("qencoder", "Audio Bitrate"))
        self.checkBox_minsplit.setStatusTip(_translate("qencoder", "Only split as many times as you have workers. Recommended with bitrate mode."))
        self.checkBox_minsplit.setText(_translate("qencoder", "Minimal splitting"))
        self.label_6.setStatusTip(_translate("qencoder", "Encoder speed preset. Lower means a slower speed. Does not affect actual cpu usage."))
        self.label_6.setText(_translate("qencoder", "cpu-used (speed)"))
        self.label_jobs.setStatusTip(_translate("qencoder", "Encode jobs to run. 0=as many as cpu cores. Lower if ram usage too high."))
        self.label_jobs.setText(_translate("qencoder", "Jobs"))
        self.label_boost.setStatusTip(_translate("qencoder", "Lowers q factor of video in low luma scenes by up to amount. To disable set to 0."))
        self.label_boost.setText(_translate("qencoder", "Dark Boost"))
        self.label_split.setStatusTip(_translate("qencoder", "Luma change threshold to split at. If video has too many splits, raise this."))
        self.label_split.setText(_translate("qencoder", "Split threshold"))
        self.spinBox_speed.setStatusTip(_translate("qencoder", "Encoder speed preset. Lower means a slower speed. Does not affect actual cpu usage."))
        self.comboBox_colorspace.setStatusTip(_translate("qencoder", "The input colordata for your video. Leave default if unsure."))
        self.spinBox_jobs.setStatusTip(_translate("qencoder", "Encode jobs to run. 0=as many as cpu cores. Lower if ram usage too high."))
        self.comboBox_inputFormat.setStatusTip(_translate("qencoder", "Pixel format of input. Usually yuv420p (8b) or yuv420p10le (10b). If unsure leave default."))
        self.label_inputformat.setStatusTip(_translate("qencoder", "Pixel format of input. Usually yuv420p (8b) or yuv420p10le (10b). If unsure leave default."))
        self.label_inputformat.setText(_translate("qencoder", "Input Format"))
        self.label_q.setStatusTip(_translate("qencoder", "Q factor: quality of video (lower numbers = more quality). Bitrate: target video kbps to use."))
        self.label_q.setText(_translate("qencoder", "Q factor"))
        self.label_2.setStatusTip(_translate("qencoder", "The input colordata for your video. Leave default if unsure."))
        self.label_2.setText(_translate("qencoder", "Input Colordata"))
        self.spinBox_boost.setStatusTip(_translate("qencoder", "Lowers q factor of video in low luma scenes by up to amount. To disable set to 0."))
        self.checkBox_tempfolder.setStatusTip(_translate("qencoder", "Do not delete temp after running an encode."))
        self.checkBox_tempfolder.setText(_translate("qencoder", "Keep temp folder"))
        self.checkBox_rtenc.setStatusTip(_translate("qencoder", "Encode with RT preset. Not recommended for cpu-used <=6."))
        self.checkBox_rtenc.setText(_translate("qencoder", "Realtime Encoding"))
        self.spinBox_audio.setStatusTip(_translate("qencoder", "With 2 channel stereo, 96kbps is usually transparent."))
        self.spinBox_split.setStatusTip(_translate("qencoder", "Luma change threshold to split at. If video has too many splits, raise this."))
        self.spinBox_quality.setStatusTip(_translate("qencoder", "Q factor: quality of video (lower numbers = more quality). Bitrate: target video kbps to use."))
        self.checkBox_resume.setStatusTip(_translate("qencoder", "If qencoder closed prematurely, resume previous encode."))
        self.checkBox_resume.setText(_translate("qencoder", "Resume Encode"))
        self.checkBox_bitrate.setStatusTip(_translate("qencoder", "Use bitrate instead of q factor. Ideal if aiming for specific filesize. Identical to q in efficiency."))
        self.checkBox_bitrate.setText(_translate("qencoder", "Use Bitrate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_advanced), _translate("qencoder", "Advanced"))
        self.label_3.setText(_translate("qencoder", "Warning! Checking these custom boxes can override some simple/advanced settings"))
        self.checkBox_videocmd.setText(_translate("qencoder", "Custom Video Cmd"))
        self.checkBox_audiocmd.setText(_translate("qencoder", "Custom Audio Cmd"))
        self.checkBox_ffmpegcmd.setText(_translate("qencoder", "Custom FFMPEG Cmd"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_custom), _translate("qencoder", "Custom"))
        self.pushButton.setText(_translate("qencoder", "Encode"))
        self.progressBar_total.setStatusTip(_translate("qencoder", "Progress is only updated when chunks complete."))
        self.label.setText(_translate("qencoder", "Source"))
        self.inputFileChoose.setText(_translate("qencoder", "Open..."))
        self.label_5.setText(_translate("qencoder", "Output"))
        self.outputFileChoose.setText(_translate("qencoder", "Save to..."))
        self.menuFile.setTitle(_translate("qencoder", "File"))
        self.actionOpen.setText(_translate("qencoder", "Open Video"))
        self.actionOpen.setShortcut(_translate("qencoder", "Ctrl+O"))
        self.actionSave.setText(_translate("qencoder", "Save Video"))
        self.actionSave.setShortcut(_translate("qencoder", "Ctrl+S"))
        self.actionExit.setText(_translate("qencoder", "Quit"))
        self.actionExit.setShortcut(_translate("qencoder", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qencoder = QtWidgets.QMainWindow()
    ui = Ui_qencoder()
    ui.setupUi(qencoder)
    qencoder.show()
    sys.exit(app.exec_())
