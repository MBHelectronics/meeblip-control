'''
Created on Mar 26, 2012

@author: bitrex@earthlink.net
'''
from PyQt4 import QtGui, QtCore
from Ui_optionsDialog import Ui_MIDIOptions
MAC = hasattr(QtGui, "qt_mac_set_native_menubar")

class optionsDialog(QtGui.QDialog, Ui_MIDIOptions):
    '''
    MIDI Options Dialog
    '''
    def __init__(self, inputChannel, outputChannel, parent=None):
        super(optionsDialog, self).__init__(parent)
        '''
        Constructor
        '''
        self.setupUi(self)
        self.midiInputChannel = inputChannel
        self.midiOutputChannel = outputChannel
        self.midiChannelSetup()
        if not MAC:
            self.midiInputChannelComboBox.setFocusPolicy(QtCore.Qt.NoFocus)

    @QtCore.pyqtSignature("int")
    def on_midiInputChannelComboBox_activated(self, index):
        self.midiInputChannel = index + 1
    
    @QtCore.pyqtSignature("int")
    def on_midiOutputChannelComboBox_activated(self, index):
        self.midiOutputChannel = index + 1
        
    def midiChannelSetup(self):
        for channel in xrange(0, 16):
            channelString = QtCore.QString(str(channel + 1))
            self.midiInputChannelComboBox.addItem(channelString)
            self.midiOutputChannelComboBox.addItem(channelString)
        self.midiInputChannelComboBox.setCurrentIndex(self.midiInputChannel - 1)
        self.midiOutputChannelComboBox.setCurrentIndex(self.midiOutputChannel - 1)
    

            