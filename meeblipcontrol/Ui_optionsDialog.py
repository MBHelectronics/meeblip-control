# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_options_dialog.ui'
#
# Created: Mon Jun 18 16:45:07 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MIDIOptions(object):
    def setupUi(self, MIDIOptions):
        MIDIOptions.setObjectName(_fromUtf8("MIDIOptions"))
        MIDIOptions.resize(197, 103)
        MIDIOptions.setMinimumSize(QtCore.QSize(197, 103))
        MIDIOptions.setMaximumSize(QtCore.QSize(197, 103))
        MIDIOptions.setToolTip(_fromUtf8(""))
        MIDIOptions.setWhatsThis(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(MIDIOptions)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.midiInputChannelComboBox = QtGui.QComboBox(MIDIOptions)
        self.midiInputChannelComboBox.setMinimumSize(QtCore.QSize(69, 20))
        self.midiInputChannelComboBox.setMaximumSize(QtCore.QSize(69, 20))
        self.midiInputChannelComboBox.setObjectName(_fromUtf8("midiInputChannelComboBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.midiInputChannelComboBox)
        self.label_2 = QtGui.QLabel(MIDIOptions)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.midiOutputChannelComboBox = QtGui.QComboBox(MIDIOptions)
        self.midiOutputChannelComboBox.setMinimumSize(QtCore.QSize(69, 20))
        self.midiOutputChannelComboBox.setMaximumSize(QtCore.QSize(69, 20))
        self.midiOutputChannelComboBox.setObjectName(_fromUtf8("midiOutputChannelComboBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.midiOutputChannelComboBox)
        self.label = QtGui.QLabel(MIDIOptions)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(MIDIOptions)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_2.setBuddy(self.midiOutputChannelComboBox)
        self.label.setBuddy(self.midiInputChannelComboBox)

        self.retranslateUi(MIDIOptions)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MIDIOptions.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MIDIOptions.reject)
        QtCore.QMetaObject.connectSlotsByName(MIDIOptions)

    def retranslateUi(self, MIDIOptions):
        MIDIOptions.setWindowTitle(QtGui.QApplication.translate("MIDIOptions", "MIDI Options", None, QtGui.QApplication.UnicodeUTF8))
        self.midiInputChannelComboBox.setToolTip(QtGui.QApplication.translate("MIDIOptions", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select MIDI Input channel.  All MIDI events from selected MIDI Inputs will be routed to device; CC messages can be used to control the patch editor via MIDI Learn.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.midiInputChannelComboBox.setWhatsThis(QtGui.QApplication.translate("MIDIOptions", "Select MIDI Input channel.  All MIDI events from selected MIDI Inputs will be routed to device; CC messages can be used to control the patch editor via MIDI Learn.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("MIDIOptions", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">MIDI Output Channel.  Should be set to same channel as device.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setWhatsThis(QtGui.QApplication.translate("MIDIOptions", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">MIDI Output Channel.  Should be set to same channel as device.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MIDIOptions", "MIDI Output Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.midiOutputChannelComboBox.setToolTip(QtGui.QApplication.translate("MIDIOptions", "MIDI Output Channel.  Should be set to same channel as device.", None, QtGui.QApplication.UnicodeUTF8))
        self.midiOutputChannelComboBox.setWhatsThis(QtGui.QApplication.translate("MIDIOptions", "MIDI Output Channel.  Should be set to same channel as device.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("MIDIOptions", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select MIDI Input channel.  All MIDI events from selected MIDI Inputs will be routed to device; CC messages can be used to control the patch editor via MIDI Learn.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setWhatsThis(QtGui.QApplication.translate("MIDIOptions", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select MIDI Input channel.  All MIDI events from selected MIDI Inputs will be routed to device; CC messages can be used to control the patch editor via MIDI Learn.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MIDIOptions", "MIDI Input Channel", None, QtGui.QApplication.UnicodeUTF8))

