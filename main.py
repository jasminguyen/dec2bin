#!/usr/bin/env python3

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer
from gpiozero import LED, LEDBoard
from signal import pause


# Klasse für das Hauptfenster
class MyWindow(QMainWindow):
    def __init__(self):

        # Konstruktor von QMainWindow aufrufen
        super().__init__()
        self.leds=LEDBoard(18,23,24,25)
        self.setMinimumSize(QSize(700, 500))    
        self.setWindowTitle('Bit Konverter') 

        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        
        vbox = QtWidgets.QVBoxLayout()
        wid.setLayout(vbox)

        
        # Slider + Label Anzeige Dezimalwert
        
        self.slider = QSlider(Qt.Horizontal,wid)
        self.slider.setMinimum(0)
        self.slider.setMaximum(15)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.valueChanged[int].connect(self.slidercount)
        self.label = QLabel('0')
        
             
        sliderbox = QHBoxLayout()
            
        sliderbox.addWidget(self.slider)
        sliderbox.addWidget(self.label)
        vbox.addLayout(sliderbox)

        # Labels fuer 4 Bits
        self.bitlabels = [QLabel('8'),QLabel('4'),QLabel('2'),QLabel('1')] # Liste 
        
        # hier bitlabels erstellen      
        bitbox = QHBoxLayout()
        
        
        # Layout zusammenbauen
        vboxBit= QVBoxLayout()
        vboxBit.addLayout(bitbox)
        vbox.addLayout(vboxBit)
        
        for index,bitlabel in enumerate(self.bitlabels):
            bitbox.addWidget(bitlabel)
            bitlabel.setStyleSheet("background-color:rgb(140,140,140)")
            bitlabel.setFixedWidth(20)
            bitlabel.setFixedHeight(20)
            bitlabel.setAlignment(Qt.AlignCenter)

    def my_on(self):
        for index in self.bitlabels:
            self.bitlabels=leds[index].on()
            
            
    def slidercount(self,value):
        showValue=str(value)
        self.label.setText(showValue)
        onColor= "background-color: rgb(255,0,0)"
        offColor= "background-color: rgb(140,140,140)"
        for i in range(4):
            div= 2**(3-i)
            checkValue= int(value/div)
            if checkValue %2 ==1:
                self.bitlabels[i].setStyleSheet(onColor)
                self.leds[i].on()
            else:
                self.bitlabels[i].setStyleSheet(offColor)
                self.leds[i].off()
                
        
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
