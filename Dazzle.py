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
from utime import sleep, sleep_ms, sleep_us
#==============================================================================================
LEDR = Pin(17, Pin.OUT, Pin.PULL_UP, value=1)
LEDG = Pin(16, Pin.OUT, Pin.PULL_UP, value=1)
LEDB = Pin(25, Pin.OUT, Pin.PULL_UP, value=1)
#==============================================================================================
def Dazzle1():
    for i in range(4):
        LEDG.low()
        sleep(0.5)
        LEDG.high()
        sleep(0.5)
    for i in range(4):
        LEDR.low()
        sleep(0.5)
        LEDR.high()
        sleep(0.5)
    for i in range(4):
        LEDB.low()
        sleep(0.5)
        LEDB.high()
        sleep(0.5)
        
def Dazzle2():
    for i in range(4):
        LEDG.toggle()
    for i in range(4):
        sleep(0.5)
        LEDR.toggle()
        sleep_ms(500)
    for i in range(4):
        LEDB.toggle()
        sleep_us(5000)

#==============================================================================================
print("Hello World")
while True:
    Dazzle2()
#==============================================================================================
