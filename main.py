#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer
from gpiozero import LEDBoard

LED0= 18
LED1= 23
LED2= 24
LED3= 25

leds = LEDBoard(LED0, LED1, LED2, LED3)

# Klasse für das Hauptfenster
class MyWindow(QMainWindow):
    def __init__(self):

        # Konstruktor von QMainWindow aufrufen
        super().__init__()
        self.setMinimumSize(QSize(300, 120))    
        self.setWindowTitle('Bit Konverter') 

        wid = QWidget(self)
        self.setCentralWidget(wid)
        
        vlayout = QVBoxLayout()
        wid.setLayout(vlayout)

        
        # Slider + Label Anzeige Dezimalwert
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(15)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setSingleStep(1)
        
        self.slider.connect(self.slidercount,self.my_on)
            
        self.label = QLabel()
        self.slider.valueChanged.connect(self.label.setNum)
             
        sliderbox = QHBoxLayout()
            
        sliderbox.addWidget(self.slider)
        sliderbox.addWidget(self.label)

        # Labels fuer 4 Bits
        self.bitlabels = [QLabel('8'),QLabel('4'),QLabel('2'),QLabel('1')] # Liste 
        self.bitlabels.setStyleSheet("background-color:rgb(170,170,170")
        
        # hier bitlabels erstellen      
        bitbox = QHBoxLayout()
        for bitlabel in self.bitlabels:
            bitbox.addWidget(bitlabels)

        # Layout zusammenbauen
        vbox = QVBoxLayout()
        vbox.addLayout(sliderbox)
        vbox.addLayout(bitbox)

        # vbox anzeigen in QWidget
        self.setLayout(vbox)

    
    def my_on(self):
        for index in self.bitlabels:
            self.bitlabels=led[index].on()
            
            
    def slidercount(self):
        if self.slider.sliderPressed():
            for lb in self.bitlabels:
                while lb != self.slider.value():
                    lb+=lb
                    QLabel.setStyleSheet("background-color:rgb(255,0,0)")
                
        
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
