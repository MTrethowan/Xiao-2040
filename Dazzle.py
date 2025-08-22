'''
==============================================================================================
 Project:      Micropython
 Program:      Dazzle
 Programmer:   Mike C. Trethowan
 Date:         April 14, 2025
 MIT License
 Copyright (c) 2025 Mike Trethowan

Description:
    XIAO RP2040
    This is a simple program to control the onboard RGB LEDs.    

==============================================================================================
Pin Assignments:

                      -------- XIAO RP2040 --------
            GP26   1-|                             |-14   5V
            GP27   2-|                             |-13   GND
            GP28   3-|                             |-12   3V3
            GP29   4-|                             |-11   GP3 
            GP6    5-|                             |-10   GP4
            GP7    6-|                             |- 9   GP2 
            GP0    7-| UART0 TX           UART0 RX |- 8   GP1 
                      -----------------------------

==============================================================================================
'''
from machine import Pin
from utime import sleep

#==============================================================================================
LEDR = Pin(17, Pin.OUT, Pin.PULL_UP, value=1)
LEDG = Pin(16, Pin.OUT, Pin.PULL_UP, value=1)
LEDB = Pin(25, Pin.OUT, Pin.PULL_UP, value=1)

#==============================================================================================
def Dazzle1():
    LEDG.low()
    sleep(0.5)
    LEDG.high()
    LEDR.low()
    sleep(0.5)
    LEDR.high()
    LEDB.low()
    sleep(0.5)
    LEDB.high()

def Dazzle2():
    LEDG.toggle()
    sleep(0.5)
    LEDG.toggle()
    LEDR.toggle()
    sleep(0.5)
    LEDR.toggle()
    LEDB.toggle()
    sleep(0.5)
    LEDB.toggle()

#==============================================================================================
print("Hello World")
while True:
    Dazzle2()
#==============================================================================================
    


