'''
==============================================================================================
Project:      Micropython
Program:      Threading
Programmer:   Mike C. Trethowan
Date:         April 14, 2025
 MIT License
Copyright (c) 2025 Mike Trethowan

Description:
    XIAO RP2040
    This is a simple program demonstrating interrupts with a twist. Instead of
    an interrupt for button presses, I needed an interrupt for UART data received.
    On previous Micropython UF2 versions, I wasn't able to implement a data
    received interrupt for the UART. With a recent update, I found that a UART
    interrupt is possible. The company I work for manufactures Tower Clocks,
    many utilizing the now obsolete M12 GPS module. I am working on a replacement
    module using a UBlox 6M module along with an Xiao module for those starting
    to fail with age.
    
    Out of the box, the 6M sends several NMEA messages automatically. I wanted to
    eliminate the constant stream of messages and only receive the desired data
    on demand. The final project uses this data to update the RP2040s onboard RTC.
    In this manner, the replacement module sends time information to the tower
    clocks even if there is an interruption in GPS data
    
Note:
    This snippet can run on the PICO by deleting ports for LEDR and LEDG.
    Infinate loop warning: while not TxR.any(): can be employed, but one would need
    an escape or time out to exit the loop.

==============================================================================================
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
                      
==============================================================================================
'''
from machine import Pin, UART
from utime import sleep, sleep_us

#=============================================================================================
TxR = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Xiao has onboard RGB Leds.
LEDR = Pin(17, Pin.OUT, Pin.PULL_UP, value=1) # Turns off red LED
LEDG = Pin(16, Pin.OUT, Pin.PULL_UP, value=1) # Turns off green LED
LEDB = Pin(25, Pin.OUT, Pin.PULL_UP, value=1) # Turns off blue LED

# UART Interupt Request Handling =============================================================
def RxCallback(x): # X is unused but needed or TypeError: function takes 0 positional arguments but 1 were given
    if TxR.any(): # As this is a callback, this is not actually needed, but is here for demonstration.
        dat = str(TxR.readline()).split(",")
        if dat[1] == "03":
            print("Sats: " + dat[2])
        elif dat[1] == "04":
            t = dat[2]
            d = dat[3]
            print("Time: " + t[0:2] + ":" + t[2:4] + ":" + t[4:6])
            print("Date: " + d[0:2] + "/" + d[2:4] + "/"  + d[4:6])
        else: # Expose NMEA code not shut-down with CFG()
            print("Other Data: " + dat[0])
            
TxR.irq(handler = RxCallback, trigger = TxR.IRQ_RXIDLE) 

#=============================================================================================
def CFG(): # Turn off automatic NMEA sentenses.
    print("Configuring 5M, Please Wait")
    TxR.write("$PUBX,40,GGA,0,0,0,0,0,0*5A\n")
    sleep_us(300)
    TxR.write("$PUBX,40,GLL,0,0,0,0,0,0*5C\n")
    sleep_us(300)
    TxR.write("$PUBX,40,GSA,0,0,0,0,0,0*4E\n")
    sleep_us(300)
    TxR.write("$PUBX,40,GSV,0,0,0,0,0,0*59\n")
    sleep_us(300)
    TxR.write("$PUBX,40,RMC,0,0,0,0,0,0*47\n")
    sleep_us(300)
    TxR.write("$PUBX,40,VTG,0,0,0,0,0,0*5E\n")
    sleep_us(300)     
    print("CFG Done")

def GetTimeDate(): # Poll Date Time
    TxR.write("$PUBX,04,0,0,0,0,0,0*37\n")
    

def GetSats(): # Poll satalites in view 
    TxR.write("$PUBX,03,0,0,0,0,0,0*30\n")
 
#=============================================================================================
print("Hello World")
CFG()
while True:
    GetTimeDate()
    LEDG.toggle()
    sleep(1)
    GetSats()
    LEDG.toggle()
    sleep(6)

 #=============================================================================================


