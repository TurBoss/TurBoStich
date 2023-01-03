# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

from qtpyvcp.widgets.button_widgets.action_button import ActionButton
from qtpyvcp.widgets.button_widgets.dialog_button import DialogButton
from qtpyvcp.widgets.display_widgets.dro_label import DROLabel
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
from qtpyvcp.widgets.display_widgets.vtk_backplot.vtk_backplot import VTKBackPlot
from qtpyvcp.widgets.input_widgets.action_combobox import ActionComboBox
from qtpyvcp.widgets.input_widgets.gcode_text_edit import GcodeTextEdit
from qtpyvcp.widgets.input_widgets.mdientry_widget import MDIEntry
from qtpyvcp.widgets.input_widgets.recent_file_combobox import RecentFileComboBox
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1043)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionOPEN = QAction(MainWindow)
        self.actionOPEN.setObjectName(u"actionOPEN")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionFullscreen = QAction(MainWindow)
        self.actionFullscreen.setObjectName(u"actionFullscreen")
        self.actionFullscreen.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.statuslabel_13 = StatusLabel(self.centralwidget)
        self.statuslabel_13.setObjectName(u"statuslabel_13")
        self.statuslabel_13.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Sans"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.statuslabel_13.setFont(font)

        self.horizontalLayout_5.addWidget(self.statuslabel_13)

        self.statuslabel_14 = StatusLabel(self.centralwidget)
        self.statuslabel_14.setObjectName(u"statuslabel_14")
        self.statuslabel_14.setFont(font)

        self.horizontalLayout_5.addWidget(self.statuslabel_14)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalWidget = QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(0, 0))
        self.horizontalWidget.setSizeIncrement(QSize(0, 0))
        self.horizontalWidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_6 = QVBoxLayout(self.horizontalWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.plotClear = QPushButton(self.horizontalWidget)
        self.plotClear.setObjectName(u"plotClear")
        self.plotClear.setMinimumSize(QSize(32, 48))
        font1 = QFont()
        font1.setFamilies([u"Sans"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.plotClear.setFont(font1)

        self.verticalLayout_6.addWidget(self.plotClear)

        self.plotClear_2 = QPushButton(self.horizontalWidget)
        self.plotClear_2.setObjectName(u"plotClear_2")
        self.plotClear_2.setMinimumSize(QSize(32, 48))
        self.plotClear_2.setFont(font1)
        self.plotClear_2.setCheckable(True)
        self.plotClear_2.setChecked(False)

        self.verticalLayout_6.addWidget(self.plotClear_2)

        self.plotClear_3 = QPushButton(self.horizontalWidget)
        self.plotClear_3.setObjectName(u"plotClear_3")
        self.plotClear_3.setMinimumSize(QSize(32, 48))
        self.plotClear_3.setFont(font1)

        self.verticalLayout_6.addWidget(self.plotClear_3)

        self.plotClear_5 = QPushButton(self.horizontalWidget)
        self.plotClear_5.setObjectName(u"plotClear_5")
        self.plotClear_5.setMinimumSize(QSize(32, 48))
        self.plotClear_5.setFont(font1)

        self.verticalLayout_6.addWidget(self.plotClear_5)

        self.plotMinus = QPushButton(self.horizontalWidget)
        self.plotMinus.setObjectName(u"plotMinus")
        self.plotMinus.setMinimumSize(QSize(32, 48))
        self.plotMinus.setFont(font1)

        self.verticalLayout_6.addWidget(self.plotMinus)

        self.plotPlus = QPushButton(self.horizontalWidget)
        self.plotPlus.setObjectName(u"plotPlus")
        self.plotPlus.setMinimumSize(QSize(32, 48))
        self.plotPlus.setFont(font1)

        self.verticalLayout_6.addWidget(self.plotPlus)

        self.plotZ2 = QPushButton(self.horizontalWidget)
        self.plotZ2.setObjectName(u"plotZ2")
        self.plotZ2.setMinimumSize(QSize(32, 48))
        self.plotZ2.setFont(font1)
        self.plotZ2.setCheckable(False)
        self.plotZ2.setAutoExclusive(False)

        self.verticalLayout_6.addWidget(self.plotZ2)

        self.plotZ = QPushButton(self.horizontalWidget)
        self.plotZ.setObjectName(u"plotZ")
        self.plotZ.setMinimumSize(QSize(32, 48))
        self.plotZ.setFont(font1)
        self.plotZ.setCheckable(False)
        self.plotZ.setChecked(False)
        self.plotZ.setAutoExclusive(False)

        self.verticalLayout_6.addWidget(self.plotZ)

        self.plotY = QPushButton(self.horizontalWidget)
        self.plotY.setObjectName(u"plotY")
        self.plotY.setMinimumSize(QSize(32, 48))
        self.plotY.setFont(font1)
        self.plotY.setCheckable(False)
        self.plotY.setAutoExclusive(False)

        self.verticalLayout_6.addWidget(self.plotY)

        self.plotX = QPushButton(self.horizontalWidget)
        self.plotX.setObjectName(u"plotX")
        self.plotX.setMinimumSize(QSize(32, 48))
        self.plotX.setFont(font1)
        self.plotX.setCheckable(False)
        self.plotX.setAutoExclusive(False)

        self.verticalLayout_6.addWidget(self.plotX)

        self.plotP = QPushButton(self.horizontalWidget)
        self.plotP.setObjectName(u"plotP")
        self.plotP.setMinimumSize(QSize(32, 48))
        self.plotP.setFont(font1)
        self.plotP.setCheckable(False)
        self.plotP.setAutoExclusive(False)

        self.verticalLayout_6.addWidget(self.plotP)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.actioncombobox = ActionComboBox(self.horizontalWidget)
        self.actioncombobox.addItem("")
        self.actioncombobox.addItem("")
        self.actioncombobox.addItem("")
        self.actioncombobox.addItem("")
        self.actioncombobox.addItem("")
        self.actioncombobox.addItem("")
        self.actioncombobox.addItem("")
        self.actioncombobox.addItem("")
        self.actioncombobox.addItem("")
        self.actioncombobox.setObjectName(u"actioncombobox")
        font2 = QFont()
        font2.setFamilies([u"Sans"])
        font2.setBold(False)
        font2.setItalic(False)
        self.actioncombobox.setFont(font2)

        self.verticalLayout_6.addWidget(self.actioncombobox)


        self.horizontalLayout.addWidget(self.horizontalWidget)

        self.vtkbackplot = VTKBackPlot(self.centralwidget)
        self.vtkbackplot.setObjectName(u"vtkbackplot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vtkbackplot.sizePolicy().hasHeightForWidth())
        self.vtkbackplot.setSizePolicy(sizePolicy)
        self.vtkbackplot.setMinimumSize(QSize(0, 0))
        self.vtkbackplot.setProperty("backgroundColor", QColor(36, 31, 49))
        self.vtkbackplot.setProperty("backgroundColor2", QColor(119, 118, 123))
        self.vtkbackplot.setProperty("enableProgramTicks", True)

        self.horizontalLayout.addWidget(self.vtkbackplot)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.actionbutton_2 = ActionButton(self.centralwidget)
        self.actionbutton_2.setObjectName(u"actionbutton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.actionbutton_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_2.setSizePolicy(sizePolicy1)
        self.actionbutton_2.setMinimumSize(QSize(0, 48))
        self.actionbutton_2.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.actionbutton_2)

        self.actionbutton = ActionButton(self.centralwidget)
        self.actionbutton.setObjectName(u"actionbutton")
        sizePolicy1.setHeightForWidth(self.actionbutton.sizePolicy().hasHeightForWidth())
        self.actionbutton.setSizePolicy(sizePolicy1)
        self.actionbutton.setMinimumSize(QSize(0, 48))
        self.actionbutton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.actionbutton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.mode_mdi_button = ActionButton(self.centralwidget)
        self.mode_mdi_button.setObjectName(u"mode_mdi_button")
        self.mode_mdi_button.setMinimumSize(QSize(0, 48))
        font3 = QFont()
        font3.setFamilies([u"Sans"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.mode_mdi_button.setFont(font3)
        self.mode_mdi_button.setCheckable(True)
        self.mode_mdi_button.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.mode_mdi_button)

        self.mod_auto_button = ActionButton(self.centralwidget)
        self.mod_auto_button.setObjectName(u"mod_auto_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mod_auto_button.sizePolicy().hasHeightForWidth())
        self.mod_auto_button.setSizePolicy(sizePolicy2)
        self.mod_auto_button.setMinimumSize(QSize(0, 48))
        self.mod_auto_button.setFont(font3)
        self.mod_auto_button.setCheckable(True)
        self.mod_auto_button.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.mod_auto_button)

        self.mode_man_button = ActionButton(self.centralwidget)
        self.mode_man_button.setObjectName(u"mode_man_button")
        sizePolicy2.setHeightForWidth(self.mode_man_button.sizePolicy().hasHeightForWidth())
        self.mode_man_button.setSizePolicy(sizePolicy2)
        self.mode_man_button.setMinimumSize(QSize(0, 48))
        self.mode_man_button.setFont(font3)
        self.mode_man_button.setCheckable(True)
        self.mode_man_button.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.mode_man_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.zero_dbutton = DialogButton(self.centralwidget)
        self.zero_dbutton.setObjectName(u"zero_dbutton")
        self.zero_dbutton.setMinimumSize(QSize(0, 48))
        self.zero_dbutton.setFont(font3)

        self.horizontalLayout_6.addWidget(self.zero_dbutton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.homeall_abutton = ActionButton(self.centralwidget)
        self.homeall_abutton.setObjectName(u"homeall_abutton")
        self.homeall_abutton.setEnabled(False)
        self.homeall_abutton.setMinimumSize(QSize(0, 48))

        self.verticalLayout_2.addWidget(self.homeall_abutton)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font4 = QFont()
        font4.setFamilies([u"Sans"])
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setItalic(False)
        self.tabWidget.setFont(font4)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setTabsClosable(False)
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_13 = QVBoxLayout(self.tab_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_3 = QLabel(self.tab_8)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMaximumSize(QSize(16777215, 36))
        font5 = QFont()
        font5.setFamilies([u"Sans"])
        font5.setPointSize(24)
        font5.setBold(True)
        font5.setItalic(False)
        self.label_3.setFont(font5)
        self.label_3.setFrameShape(QFrame.StyledPanel)
        self.label_3.setFrameShadow(QFrame.Sunken)
        self.label_3.setLineWidth(3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_3)

        self.drolabel_10 = DROLabel(self.tab_8)
        self.drolabel_10.setObjectName(u"drolabel_10")
        self.drolabel_10.setMaximumSize(QSize(16777215, 36))
        self.drolabel_10.setFont(font5)
        self.drolabel_10.setFrameShape(QFrame.StyledPanel)
        self.drolabel_10.setFrameShadow(QFrame.Sunken)
        self.drolabel_10.setLineWidth(3)
        self.drolabel_10.setMidLineWidth(0)
        self.drolabel_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.drolabel_10.setProperty("referenceType", 1)
        self.drolabel_10.setProperty("axisNumber", 0)
        self.drolabel_10.setProperty("latheMode", 0)

        self.horizontalLayout_23.addWidget(self.drolabel_10)


        self.verticalLayout_22.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_5 = QLabel(self.tab_8)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMaximumSize(QSize(16777215, 36))
        self.label_5.setFont(font5)
        self.label_5.setFrameShape(QFrame.StyledPanel)
        self.label_5.setFrameShadow(QFrame.Sunken)
        self.label_5.setLineWidth(3)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_5)

        self.drolabel_15 = DROLabel(self.tab_8)
        self.drolabel_15.setObjectName(u"drolabel_15")
        self.drolabel_15.setMaximumSize(QSize(16777215, 36))
        self.drolabel_15.setFont(font5)
        self.drolabel_15.setFrameShape(QFrame.StyledPanel)
        self.drolabel_15.setFrameShadow(QFrame.Sunken)
        self.drolabel_15.setLineWidth(3)
        self.drolabel_15.setMidLineWidth(0)
        self.drolabel_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.drolabel_15.setProperty("referenceType", 1)
        self.drolabel_15.setProperty("axisNumber", 1)
        self.drolabel_15.setProperty("latheMode", 0)

        self.horizontalLayout_24.addWidget(self.drolabel_15)


        self.verticalLayout_22.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_6 = QLabel(self.tab_8)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMaximumSize(QSize(16777215, 36))
        self.label_6.setFont(font5)
        self.label_6.setFrameShape(QFrame.StyledPanel)
        self.label_6.setFrameShadow(QFrame.Sunken)
        self.label_6.setLineWidth(3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_6)

        self.drolabel_16 = DROLabel(self.tab_8)
        self.drolabel_16.setObjectName(u"drolabel_16")
        self.drolabel_16.setMaximumSize(QSize(16777215, 36))
        self.drolabel_16.setFont(font5)
        self.drolabel_16.setFrameShape(QFrame.StyledPanel)
        self.drolabel_16.setFrameShadow(QFrame.Sunken)
        self.drolabel_16.setLineWidth(3)
        self.drolabel_16.setMidLineWidth(0)
        self.drolabel_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.drolabel_16.setProperty("referenceType", 1)
        self.drolabel_16.setProperty("axisNumber", 2)
        self.drolabel_16.setProperty("latheMode", 0)

        self.horizontalLayout_25.addWidget(self.drolabel_16)


        self.verticalLayout_22.addLayout(self.horizontalLayout_25)


        self.verticalLayout_13.addLayout(self.verticalLayout_22)

        self.tabWidget.addTab(self.tab_8, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_20 = QVBoxLayout(self.tab_7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_7 = QLabel(self.tab_7)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMaximumSize(QSize(16777215, 36))
        self.label_7.setFont(font5)
        self.label_7.setFrameShape(QFrame.StyledPanel)
        self.label_7.setFrameShadow(QFrame.Sunken)
        self.label_7.setLineWidth(3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_7)

        self.drolabel_7 = DROLabel(self.tab_7)
        self.drolabel_7.setObjectName(u"drolabel_7")
        self.drolabel_7.setMaximumSize(QSize(16777215, 36))
        font6 = QFont()
        font6.setFamilies([u"Sans"])
        font6.setPointSize(24)
        font6.setBold(True)
        font6.setItalic(False)
        font6.setUnderline(False)
        self.drolabel_7.setFont(font6)
        self.drolabel_7.setFrameShape(QFrame.StyledPanel)
        self.drolabel_7.setFrameShadow(QFrame.Sunken)
        self.drolabel_7.setLineWidth(3)
        self.drolabel_7.setMidLineWidth(0)
        self.drolabel_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.drolabel_7.setProperty("referenceType", 0)
        self.drolabel_7.setProperty("axisNumber", 0)
        self.drolabel_7.setProperty("latheMode", 0)

        self.horizontalLayout_26.addWidget(self.drolabel_7)


        self.verticalLayout_18.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_8 = QLabel(self.tab_7)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setMaximumSize(QSize(16777215, 36))
        self.label_8.setFont(font5)
        self.label_8.setFrameShape(QFrame.StyledPanel)
        self.label_8.setFrameShadow(QFrame.Sunken)
        self.label_8.setLineWidth(3)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_8)

        self.drolabel_8 = DROLabel(self.tab_7)
        self.drolabel_8.setObjectName(u"drolabel_8")
        self.drolabel_8.setMaximumSize(QSize(16777215, 36))
        self.drolabel_8.setFont(font6)
        self.drolabel_8.setFrameShape(QFrame.StyledPanel)
        self.drolabel_8.setFrameShadow(QFrame.Sunken)
        self.drolabel_8.setLineWidth(3)
        self.drolabel_8.setMidLineWidth(0)
        self.drolabel_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.drolabel_8.setProperty("referenceType", 0)
        self.drolabel_8.setProperty("axisNumber", 1)
        self.drolabel_8.setProperty("latheMode", 0)

        self.horizontalLayout_27.addWidget(self.drolabel_8)


        self.verticalLayout_18.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_9 = QLabel(self.tab_7)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMaximumSize(QSize(16777215, 36))
        self.label_9.setFont(font5)
        self.label_9.setFrameShape(QFrame.StyledPanel)
        self.label_9.setFrameShadow(QFrame.Sunken)
        self.label_9.setLineWidth(3)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_9)

        self.drolabel_9 = DROLabel(self.tab_7)
        self.drolabel_9.setObjectName(u"drolabel_9")
        self.drolabel_9.setMaximumSize(QSize(16777215, 36))
        self.drolabel_9.setFont(font6)
        self.drolabel_9.setFrameShape(QFrame.StyledPanel)
        self.drolabel_9.setFrameShadow(QFrame.Sunken)
        self.drolabel_9.setLineWidth(3)
        self.drolabel_9.setMidLineWidth(0)
        self.drolabel_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.drolabel_9.setProperty("referenceType", 0)
        self.drolabel_9.setProperty("axisNumber", 2)
        self.drolabel_9.setProperty("latheMode", 0)

        self.horizontalLayout_29.addWidget(self.drolabel_9)


        self.verticalLayout_18.addLayout(self.horizontalLayout_29)


        self.verticalLayout_20.addLayout(self.verticalLayout_18)

        self.tabWidget.addTab(self.tab_7, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(8)
        self.jogxplus_abutton = ActionButton(self.centralwidget)
        self.jogxplus_abutton.setObjectName(u"jogxplus_abutton")
        self.jogxplus_abutton.setMinimumSize(QSize(0, 48))
        self.jogxplus_abutton.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/images/x_plus_jog_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.jogxplus_abutton.setIcon(icon)
        self.jogxplus_abutton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.jogxplus_abutton, 1, 5, 1, 1)

        self.jogxmin_abutton = ActionButton(self.centralwidget)
        self.jogxmin_abutton.setObjectName(u"jogxmin_abutton")
        self.jogxmin_abutton.setMinimumSize(QSize(0, 48))
        self.jogxmin_abutton.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/images/x_minus_jog_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.jogxmin_abutton.setIcon(icon1)
        self.jogxmin_abutton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.jogxmin_abutton, 1, 3, 1, 1)

        self.jogyplus_abutton = ActionButton(self.centralwidget)
        self.jogyplus_abutton.setObjectName(u"jogyplus_abutton")
        self.jogyplus_abutton.setMinimumSize(QSize(0, 48))
        self.jogyplus_abutton.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/images/y_plus_jog_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.jogyplus_abutton.setIcon(icon2)
        self.jogyplus_abutton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.jogyplus_abutton, 0, 4, 1, 1)

        self.jogzplus_abutton = ActionButton(self.centralwidget)
        self.jogzplus_abutton.setObjectName(u"jogzplus_abutton")
        self.jogzplus_abutton.setMinimumSize(QSize(0, 48))
        self.jogzplus_abutton.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/images/z_plus_jog_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.jogzplus_abutton.setIcon(icon3)
        self.jogzplus_abutton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.jogzplus_abutton, 0, 7, 1, 1)

        self.jogzmin_abutton = ActionButton(self.centralwidget)
        self.jogzmin_abutton.setObjectName(u"jogzmin_abutton")
        self.jogzmin_abutton.setMinimumSize(QSize(0, 48))
        self.jogzmin_abutton.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/images/z_minus_jog_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.jogzmin_abutton.setIcon(icon4)
        self.jogzmin_abutton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.jogzmin_abutton, 1, 7, 1, 1)

        self.jogymin_abutton = ActionButton(self.centralwidget)
        self.jogymin_abutton.setObjectName(u"jogymin_abutton")
        self.jogymin_abutton.setMinimumSize(QSize(0, 48))
        self.jogymin_abutton.setFont(font2)
        icon5 = QIcon()
        icon5.addFile(u":/images/y_minus_jog_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.jogymin_abutton.setIcon(icon5)
        self.jogymin_abutton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.jogymin_abutton, 1, 4, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.recentfilecombobox = RecentFileComboBox(self.centralwidget)
        self.recentfilecombobox.setObjectName(u"recentfilecombobox")

        self.verticalLayout_2.addWidget(self.recentfilecombobox)

        self.gcodetextedit = GcodeTextEdit(self.centralwidget)
        self.gcodetextedit.setObjectName(u"gcodetextedit")
        self.gcodetextedit.setProperty("syntaxHighlighting", True)
        self.gcodetextedit.setProperty("currentLineBackground", QColor(119, 118, 123))
        self.gcodetextedit.setProperty("marginBackground", QColor(154, 153, 150))
        self.gcodetextedit.setProperty("marginCurrentLineBackground", QColor(61, 56, 70))
        self.gcodetextedit.setProperty("marginColor", QColor(94, 92, 100))
        self.gcodetextedit.setProperty("marginCurrentLineColor", QColor(119, 118, 123))

        self.verticalLayout_2.addWidget(self.gcodetextedit)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font7 = QFont()
        font7.setFamilies([u"Sans"])
        font7.setBold(True)
        font7.setItalic(False)
        self.label.setFont(font7)

        self.horizontalLayout_7.addWidget(self.label)

        self.mdientry = MDIEntry(self.centralwidget)
        self.mdientry.setObjectName(u"mdientry")

        self.horizontalLayout_7.addWidget(self.mdientry)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.actionbutton_3 = ActionButton(self.centralwidget)
        self.actionbutton_3.setObjectName(u"actionbutton_3")

        self.horizontalLayout_3.addWidget(self.actionbutton_3)

        self.actionbutton_7 = ActionButton(self.centralwidget)
        self.actionbutton_7.setObjectName(u"actionbutton_7")

        self.horizontalLayout_3.addWidget(self.actionbutton_7)

        self.actionbutton_4 = ActionButton(self.centralwidget)
        self.actionbutton_4.setObjectName(u"actionbutton_4")

        self.horizontalLayout_3.addWidget(self.actionbutton_4)

        self.actionbutton_6 = ActionButton(self.centralwidget)
        self.actionbutton_6.setObjectName(u"actionbutton_6")

        self.horizontalLayout_3.addWidget(self.actionbutton_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.plotClear.released.connect(self.vtkbackplot.clearLivePlot)
        self.plotClear_3.released.connect(self.vtkbackplot.setViewMachine)
        self.plotClear_5.released.connect(self.vtkbackplot.setViewProgram)
        self.plotMinus.released.connect(self.vtkbackplot.zoomOut)
        self.plotPlus.released.connect(self.vtkbackplot.zoomIn)
        self.plotZ2.released.connect(self.vtkbackplot.setViewZ2)
        self.plotZ.released.connect(self.vtkbackplot.setViewZ)
        self.plotY.released.connect(self.vtkbackplot.setViewY)
        self.plotX.released.connect(self.vtkbackplot.setViewX)
        self.plotClear_2.toggled.connect(self.vtkbackplot.enable_panning)
        self.plotP.clicked.connect(self.vtkbackplot.setViewP)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionOPEN.setText(QCoreApplication.translate("MainWindow", u"oPEN", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionFullscreen.setText(QCoreApplication.translate("MainWindow", u"Fullscreen", None))
#if QT_CONFIG(shortcut)
        self.actionFullscreen.setShortcut(QCoreApplication.translate("MainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.statuslabel_13.setText(QCoreApplication.translate("MainWindow", u"G0 G0 G0 G0 G0 G0 G0 G0 G0 G0 G0 G0 G0 G0 G0 G0", None))
        self.statuslabel_13.setProperty("rules", QCoreApplication.translate("MainWindow", u"[{\"channels\": [{\"trigger\": true, \"type\": \"str\", \"url\": \"status:gcodes?text\"}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Active Codes\"}]", None))
        self.statuslabel_13.setProperty("statusItem", "")
        self.statuslabel_14.setText(QCoreApplication.translate("MainWindow", u"M0 M0 M0 M0 M0 M0 M0 M0 M0", None))
        self.statuslabel_14.setProperty("rules", QCoreApplication.translate("MainWindow", u"[{\"channels\": [{\"trigger\": true, \"type\": \"str\", \"url\": \"status:mcodes?text\"}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Active Mcodes\"}]", None))
        self.statuslabel_14.setProperty("statusItem", "")
        self.plotClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.plotClear_2.setText(QCoreApplication.translate("MainWindow", u"Pan", None))
        self.plotClear_3.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.plotClear_5.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.plotMinus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.plotPlus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.plotZ2.setText(QCoreApplication.translate("MainWindow", u"Z2", None))
        self.plotZ.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.plotY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.plotX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.plotP.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.actioncombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"G54", None))
        self.actioncombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"G55", None))
        self.actioncombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"G56", None))
        self.actioncombobox.setItemText(3, QCoreApplication.translate("MainWindow", u"G57", None))
        self.actioncombobox.setItemText(4, QCoreApplication.translate("MainWindow", u"G58", None))
        self.actioncombobox.setItemText(5, QCoreApplication.translate("MainWindow", u"G59", None))
        self.actioncombobox.setItemText(6, QCoreApplication.translate("MainWindow", u"G59.1", None))
        self.actioncombobox.setItemText(7, QCoreApplication.translate("MainWindow", u"G59.2", None))
        self.actioncombobox.setItemText(8, QCoreApplication.translate("MainWindow", u"G59.3", None))

        self.actioncombobox.setProperty("actionName", QCoreApplication.translate("MainWindow", u"machine.set-work-coord", None))
        self.actionbutton_2.setText(QCoreApplication.translate("MainWindow", u"E-Stop", None))
        self.actionbutton_2.setProperty("actionName", QCoreApplication.translate("MainWindow", u"machine.estop.toggle", None))
        self.actionbutton.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.actionbutton.setProperty("actionName", QCoreApplication.translate("MainWindow", u"machine.power.toggle", None))
        self.mode_mdi_button.setText(QCoreApplication.translate("MainWindow", u"MDI", None))
        self.mode_mdi_button.setProperty("actionName", QCoreApplication.translate("MainWindow", u"machine.mode.mdi", None))
        self.mode_mdi_button.setProperty("position", QCoreApplication.translate("MainWindow", u"last", None))
        self.mode_mdi_button.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"option", None))
        self.mod_auto_button.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.mod_auto_button.setProperty("actionName", QCoreApplication.translate("MainWindow", u"machine.mode.auto", None))
        self.mod_auto_button.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"option", None))
        self.mode_man_button.setText(QCoreApplication.translate("MainWindow", u"MAN", None))
        self.mode_man_button.setProperty("actionName", QCoreApplication.translate("MainWindow", u"machine.mode.manual", None))
        self.mode_man_button.setProperty("position", QCoreApplication.translate("MainWindow", u"first", None))
        self.mode_man_button.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"option", None))
        self.zero_dbutton.setText(QCoreApplication.translate("MainWindow", u"ZERO", None))
        self.zero_dbutton.setProperty("dialogName", QCoreApplication.translate("MainWindow", u"set_work_offsets", None))
        self.homeall_abutton.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.homeall_abutton.setProperty("rules", QCoreApplication.translate("MainWindow", u"[]", None))
        self.homeall_abutton.setProperty("actionName", QCoreApplication.translate("MainWindow", u"machine.home.all", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.drolabel_10.setText(QCoreApplication.translate("MainWindow", u"     0.000", None))
        self.drolabel_10.setProperty("inchFormat", QCoreApplication.translate("MainWindow", u"%9.4f", None))
        self.drolabel_10.setProperty("millimeterFormat", QCoreApplication.translate("MainWindow", u"%10.3f", None))
        self.drolabel_10.setProperty("degreeFormat", QCoreApplication.translate("MainWindow", u"%10.2f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.drolabel_15.setText(QCoreApplication.translate("MainWindow", u"     0.000", None))
        self.drolabel_15.setProperty("inchFormat", QCoreApplication.translate("MainWindow", u"%9.4f", None))
        self.drolabel_15.setProperty("millimeterFormat", QCoreApplication.translate("MainWindow", u"%10.3f", None))
        self.drolabel_15.setProperty("degreeFormat", QCoreApplication.translate("MainWindow", u"%10.2f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.drolabel_16.setText(QCoreApplication.translate("MainWindow", u"     0.000", None))
        self.drolabel_16.setProperty("inchFormat", QCoreApplication.translate("MainWindow", u"%9.4f", None))
        self.drolabel_16.setProperty("millimeterFormat", QCoreApplication.translate("MainWindow", u"%10.3f", None))
        self.drolabel_16.setProperty("degreeFormat", QCoreApplication.translate("MainWindow", u"%10.2f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Relative", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.drolabel_7.setText(QCoreApplication.translate("MainWindow", u"     0.000", None))
        self.drolabel_7.setProperty("inchFormat", QCoreApplication.translate("MainWindow", u"%9.4f", None))
        self.drolabel_7.setProperty("millimeterFormat", QCoreApplication.translate("MainWindow", u"%10.3f", None))
        self.drolabel_7.setProperty("degreeFormat", QCoreApplication.translate("MainWindow", u"%10.2f", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.drolabel_8.setText(QCoreApplication.translate("MainWindow", u"     0.000", None))
        self.drolabel_8.setProperty("inchFormat", QCoreApplication.translate("MainWindow", u"%9.4f", None))
        self.drolabel_8.setProperty("millimeterFormat", QCoreApplication.translate("MainWindow", u"%10.3f", None))
        self.drolabel_8.setProperty("degreeFormat", QCoreApplication.translate("MainWindow", u"%10.2f", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.drolabel_9.setText(QCoreApplication.translate("MainWindow", u"     0.000", None))
        self.drolabel_9.setProperty("inchFormat", QCoreApplication.translate("MainWindow", u"%9.4f", None))
        self.drolabel_9.setProperty("millimeterFormat", QCoreApplication.translate("MainWindow", u"%10.3f", None))
        self.drolabel_9.setProperty("degreeFormat", QCoreApplication.translate("MainWindow", u"%10.2f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Absolute", None))
        self.jogxplus_abutton.setText("")
        self.jogxplus_abutton.setProperty("actionName", QCoreApplication.translate("MainWindow", u"machine.jog.axis:x,pos", None))
        self.jogxmin_abutton.setText("")
        self.jogxmin_abutton.setProperty("actionName", QCoreApplication.translate("MainWindow", u"machine.jog.axis:x,neg", None))
        self.jogyplus_abutton.setText("")
        self.jogyplus_abutton.setProperty("actionName", QCoreApplication.translate("MainWindow", u"machine.jog.axis:y,pos", None))
        self.jogzplus_abutton.setText("")
        self.jogzplus_abutton.setProperty("actionName", QCoreApplication.translate("MainWindow", u"machine.jog.axis:z,pos", None))
        self.jogzmin_abutton.setText("")
        self.jogzmin_abutton.setProperty("actionName", QCoreApplication.translate("MainWindow", u"machine.jog.axis:z,neg", None))
        self.jogymin_abutton.setText("")
        self.jogymin_abutton.setProperty("actionName", QCoreApplication.translate("MainWindow", u"machine.jog.axis:y,neg", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MDI", None))
        self.actionbutton_3.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.actionbutton_3.setProperty("actionName", QCoreApplication.translate("MainWindow", u"program.run", None))
        self.actionbutton_7.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.actionbutton_7.setProperty("actionName", QCoreApplication.translate("MainWindow", u"program.step", None))
        self.actionbutton_4.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.actionbutton_4.setProperty("actionName", QCoreApplication.translate("MainWindow", u"program.pause", None))
        self.actionbutton_6.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
        self.actionbutton_6.setProperty("actionName", QCoreApplication.translate("MainWindow", u"program.abort", None))
    # retranslateUi

