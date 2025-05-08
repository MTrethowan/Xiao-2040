'''
******************************************************************************
Project:      Micropython
Program:      Threading
Programmer:   Mike C. Trethowan
Date:         April 14, 2025
Copyright     2025

Description:
    XIAO RP2040
    This is a simple program to demenstarate threading.
    This snippet can run on the PICO by deleting ports for LEDR and LEDG

******************************************************************************
Xiao RP2040 Pin Assignment:

                      -------- XIAO RP2040 --------
            GP26   1-|                             |-14   5V
            GP27   2-|                             |-13   GND
            GP28   3-|                             |-12   3V3
            GP29   4-|                             |-11   GP3 
            GP6    5-|                             |-10   GP4
            GP7    6-|                             |- 9   GP2 
            GP0    7-| UART0 TX           UART0 RX |- 8   GP1 
                      -----------------------------
                      
******************************************************************************
'''
from machine import Pin
from utime import sleep
import _thread

# Set ports for onboard RGB LEDs and turn them off
LEDR = Pin(17, Pin.OUT, Pin.PULL_UP, value=1)
LEDG = Pin(16, Pin.OUT, Pin.PULL_UP, value=1)
LEDB = Pin(25, Pin.OUT, Pin.PULL_UP, value=1)

#*****************************************************************************

def Core1():
    while True:
        print("This Is Core 1")
        LEDB.toggle()
        sleep(1)

def main():
    _thread.start_new_thread(Core1, ()) # Start core 1 
    while True: # Loop on core 0
        print("This Is Core 0")
        sleep(4)

if __name__ == "__main__":
    main()
    
#*****************************************************************************
