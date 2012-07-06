'''
Created on Mar 20, 2012

@author: Matt
'''
import sys
import hashlib
from PyQt4 import QtGui, QtCore
from Ui_mainWindow import Ui_MainWindow
from windowHandler import MainWindowHandler
from functools import partial
from pygame import midi

class MainWindow(QtGui.QMainWindow):    
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.midiOutputDevicesDict = {}
        self.midiInputDevicesDict = {}
        self.onValue = 64
        self.offValue = 0
        #control change values
        self.dialDict = {'resonanceDial': 48, 'cutoffDial': 49, 'lfoRateDial': 50, 'lfoDepthDial': 51,
        'envAmountDial': 52, 'glideAmountDial' : 53, 'oscPWMDial': 54, 'oscDetuneDial' :55,
        'filterDecaySlider': 58, 'filterAttackSlider' :59, 'ampDecaySlider' :60, 'ampAttackSlider': 61}
        
        self.buttonDict = {'oscFMOn':[65, self.onValue], 'oscFMOff':[65, self.offValue], 'lfoRandomOn':[66, self.onValue],
                      'lfoRandomOff':[66, self.offValue], 'lfoSquareOn':[67, self.onValue], 
                      'lfoTriangleOn':[67, self.offValue], 'lpOn':[68, self.offValue],'hpOn':[68, self.onValue],
                      'distortionOn':[69, self.onValue], 'distortionOff':[69, self.offValue], 
                      'lfoOn':[70, self.onValue], 'lfoOff':[70, self.offValue], 'lfoOscOn':[71, self.onValue],
                      'lfoFilterOn':[71, self.offValue], 'antiAliasOn':[72, self.onValue], 'antiAliasOff':[72, self.offValue],
                      'oscBOctaveOn':[73, self.onValue], 'oscBOctaveOff':[73, self.offValue],'oscBOn':[74, self.onValue], 
                      'oscBOff':[74, self.offValue], 'oscBWaveSquare':[75, self.onValue], 'oscBWaveTri':[75, self.offValue], 
                      'envSustainOn':[76, self.onValue], 'envSustainOff':[76, self.offValue], 'oscANoiseOn':[77, self.onValue], 
                      'oscANoiseOff':[77, self.offValue],'pwmSweepOn':[78, self.onValue], 'pwmSweepOff':[78, self.offValue], 
                      'oscAPWMOn':[79, self.onValue], 'oscASawOn':[79, self.offValue]}        
        
        self.buttonBoxDict = {'oscAWaveBox':'oscAWaveGroup', 'oscANoiseBox':'oscANoiseGroup', 'oscBEnableBox':'oscBEnableGroup', 
                                'oscBWaveBox':'oscBWaveGroup', 'oscBOctaveBox':'oscBOctaveGroup', 'oscFMBox':'oscFMGroup',
                                'lfoEnableBox':'lfoEnableGroup', 'lfoDestBox':'lfoDestGroup', 'lfoWaveBox':'lfoWaveGroup', 
                                'lfoRandomBox':'lfoRandomGroup', 'filterModeBox':'filterModeGroup', 'distortionBox':'distortionGroup',
                                'antiAliasBox':'antiAliasGroup', 'envSustainBox':'envSustainGroup', 'pwmSweepBox':'pwmSweepGroup', 
                                'oscAWaveBox':'oscAWaveGroup'}
        
        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)
        self.windowHandler = MainWindowHandler(self.dialDict, self.buttonDict) 
        self.settings = QtCore.QSettings('MeeblipControl', 'MeeblipControl')        
        #connect signals and slots
        for dial, cc, in self.dialDict.iteritems():
            currentDial = getattr(self.ui, dial)
            currentDial.setRange(0,127)
            dialChanged = partial(self.windowHandler.dialChanged, mainWindowInstance=self, cc=cc)
            currentDial.valueChanged.connect(dialChanged)
            currentDial.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            currentDial.customContextMenuRequested.connect(partial(self.windowHandler.contextMenu, mainWindowInstance=self, widgetName=dial))
        for button, buttonList in self.buttonDict.iteritems():
            currentButton = getattr(self.ui, button)
            buttonFunc = partial(self.windowHandler.buttonChanged, mainWindowInstance=self, value=buttonList[1], cc=buttonList[0], button=currentButton)
            currentButton.toggled.connect(buttonFunc)
        for buttonGroupBox in self.buttonBoxDict.keys():
            currentGroup = getattr(self.ui, buttonGroupBox)
            currentGroup.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            currentGroup.customContextMenuRequested.connect(partial(self.windowHandler.contextMenu, mainWindowInstance=self, 
                                                                    widgetName=buttonGroupBox))
        
        class _MidiInput(QtCore.QThread):
            dataReceivedSignal = QtCore.pyqtSignal(int, int)
            midiExceptionSignal = QtCore.pyqtSignal(str)
            
            def __init__(self, mainWindow, mainWindowHandler, parent=None):
                super(_MidiInput, self).__init__(parent)
                self.mainWindow = mainWindow
                self.mainWindowHandler = mainWindowHandler
                
            def run(self):
                while True:
                    if self.mainWindowHandler.midiSelectedInputDevicesDict:
                        try:
                            self.mainWindowHandler.midiInputMutex.lock()
                            for inputDevice in self.mainWindowHandler.midiSelectedInputDevicesDict.values():
                                        if inputDevice.poll():
                                            data = inputDevice.read(1)
                                            channel = (data[0][0][0] & 0xF) + 1
                                            if channel == self.mainWindowHandler.midiInputChannel:
                                                status = data[0][0][0] & 0xF0
                                                cc = data[0][0][1]
                                                #if a CC message arrives and is mapped
                                                if status == 0xB0 and cc in self.mainWindowHandler.currentPatch.patchMIDIMapDict:  
                                                    value = data[0][0][2]
                                                    self.dataReceivedSignal.emit(cc, value)
                                                else:
                                                    if self.mainWindowHandler.midiSelectedOutputDevice:
                                                        self.mainWindowHandler.midiSelectedOutputDevice.write(data)                    
                        except midi.MidiException as e:
                            self.midiExceptionSignal.emit(unicode(e))
                        finally:
                            self.mainWindowHandler.midiInputMutex.unlock()
                    self.usleep(200) #don't hog the processor in the polling loop!
        #initialize MIDI, start listening for incoming MIDI data       
        midi.init()
        self.getMIDIDevices()
        self.midiInputThread = _MidiInput(self, self.windowHandler)
        self.midiInputThread.dataReceivedSignal.connect(self.midiInputCallback)         
        self.midiInputThread.midiExceptionSignal.connect(lambda e: QtGui.QMessageBox.warning(self, "MIDI Error", unicode(e)))
        self.midiInputThread.start()
        self.ui.action_Save.setEnabled(False)
        self.restoreSettings(self.windowHandler)
        self.windowHandler.new(self)
        
    def midiInputCallback(self, cc, value):        
        widgetName = self.windowHandler.currentPatch.patchMIDIMapDict[cc]
        if widgetName in self.dialDict:
            getattr(self.ui, widgetName).setValue(value)
            self.windowHandler.dialChanged(value, self, self.dialDict[widgetName])
        elif widgetName in self.buttonBoxDict:
            buttonGroup = getattr(self.ui, self.buttonBoxDict[widgetName])
            checkedButton = buttonGroup.checkedButton()
            checkedButtonName = str(checkedButton.objectName())
            if value >= self.onValue and self.buttonDict[checkedButtonName][1] == self.offValue:
                for button in buttonGroup.buttons():
                    if button != checkedButton:
                        button.toggle()
            elif value < self.onValue and self.buttonDict[checkedButtonName][1] == self.onValue:
                for button in buttonGroup.buttons():
                    if button != checkedButton:
                        button.toggle()

    def getMIDIDevices(self):
        midiOutputDevices = []
        midiInputDevices = []
        for index in xrange(0, midi.get_count()):
            device = midi.get_device_info(index)
            deviceName = device[1]
            if device[3] == 1 and device[4] == 0: #if the device is an output and not opened
                setattr(self, deviceName, QtGui.QAction(QtGui.QIcon(''), deviceName, self))
                deviceWidget = getattr(self, deviceName)
                deviceWidget.setCheckable(True)
                midiOutputDevices.append(deviceWidget)
                self.midiOutputDevicesDict[deviceWidget] = index
            elif device[2] == 1 and device[4] == 0: #if devices is an input and not opened
                deviceName = device[1]
                setattr(self, deviceName, QtGui.QAction(QtGui.QIcon(''), deviceName, self))
                deviceWidget = getattr(self, deviceName)
                deviceWidget.setCheckable(True)
                midiInputDevices.append(deviceWidget)
                self.midiInputDevicesDict[deviceWidget] = index
                
        if midiOutputDevices:
            self.ui.midiOutputDevicesMenu = self.ui.menubar.addMenu("&Midi Output Device")
            self.ui.midiOutputDevicesMenu.addActions(midiOutputDevices)
        if midiInputDevices:
            self.ui.midiInputDevicesMenu = self.ui.menubar.addMenu("&Midi Input Devices")
            self.ui.midiInputDevicesMenu.addActions(midiInputDevices)
        
        for device in midiOutputDevices:
            outputFunction = partial(self.windowHandler.midiOutputSelect, mainWindowInstance=self, device=device)
            device.triggered.connect(outputFunction)

        for device in midiInputDevices:
            inputFunction = partial(self.windowHandler.midiInputSelect, mainWindowInstance=self, device=device)
            device.triggered.connect(inputFunction)
    
    def restoreSettings(self, mainWindowHandler):
        mainWindowHandler.midiInputChannel = self.settings.value('midiInputChannel').toInt()[0]
        if not mainWindowHandler.midiInputChannel:
            self.midiInputChannel = 1
        self.midiOutputChannel = self.settings.value('midiOutputChannel').toInt()[0]
        if not mainWindowHandler.midiOutputChannel:
            mainWindowHandler.midiOutputChannel = 1
        
        registryInputDeviceList = []    
        for inputDeviceHash in self.settings.value('midiInputDevices', []).toList():
            inputDeviceHash = str(inputDeviceHash.toString())
            for deviceWidget, index in self.midiInputDevicesDict.iteritems():
                deviceName = midi.get_device_info(index)[1]
                deviceHash = hashlib.md5(deviceName).hexdigest()
                if deviceHash == inputDeviceHash:
                    deviceWidget.setChecked(True)
                    self.windowHandler.midiInputSelect(self, deviceWidget)
                    registryInputDeviceList.append(deviceHash)            
        self.settings.setValue('midiInputDevices', registryInputDeviceList) 
        #update the registry so unplugged devices aren't 
        #reselected when plugged back in at some later time
        outputDeviceHash = str(self.settings.value('midiOutputDevice').toString())
        registryOutputDevice = None
        for deviceWidget, index in self.midiOutputDevicesDict.iteritems():
                deviceName = midi.get_device_info(index)[1]
                deviceHash = hashlib.md5(deviceName).hexdigest()
                if deviceHash == outputDeviceHash:
                    deviceWidget.setChecked(True)
                    self.windowHandler.midiOutputSelect(self, deviceWidget)
                    registryOutputDevice = deviceHash
        self.settings.setValue('midiOutputDevice', registryOutputDevice)
            
    @QtCore.pyqtSignature("")
    def on_action_MIDI_Channel_triggered(self):
        self.windowHandler.menuOptions(self)
        
    @QtCore.pyqtSignature("")
    def on_action_Save_as_triggered(self):
        self.windowHandler.saveAs(self)
    
    @QtCore.pyqtSignature("")
    def on_action_Load_triggered(self):
        self.windowHandler.load(self)
        
    @QtCore.pyqtSignature("")
    def on_action_Save_triggered(self):
        self.windowHandler.save(self)
            
    @QtCore.pyqtSignature("")
    def on_action_New_triggered(self):
        self.windowHandler.new(self)
    
    @QtCore.pyqtSignature("")
    def on_action_Export_patch_as_MIDI_triggered(self):
        self.windowHandler.midiExport(self)
    
    @QtCore.pyqtSignature("")
    def on_action_Import_MIDI_patch_triggered(self):
        self.windowHandler.midiImport(self)

    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())