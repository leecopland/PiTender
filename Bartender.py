## Define constants ##
# Pump flowrate
# flowrate = 100 mL per min
flowrate_minute = 100
flowrate_second = flowrate_minute / 60
 
# Volumes for drinks
# standard_drink = 30mL
# glass = 250mL
# mixer = glass - standard_drink = 220mL
 
# Imports
import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import font
from time import sleep
 
## Initialise parts ##
 
#Raspberry Pi pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinList = [6, 13, 19, 26, 12, 16]
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)
 
    #################
    # pump   = pin  #
    #  1     =  6   #
    #  2     =  13  #
    #  3     =  19  #
    #  4     =  26  #
    #  5     =  12  #
    #  6     =  16  #
    #################

coke = 6
lemonade = 13
orange_juice = 19
vodka = 26
scotch = 12
rum = 16
 
# Fluids in pump numbers
pump_1 = coke
pump_2 = lemonade
pump_3 = orange_juice
pump_4 = vodka
pump_5 = scotch
pump_6 = rum 
 
# Drinks list
scotch_coke = (scotch, coke)
screwdriver = (vodka, orange_juice)
vodka_lemonade = (vodka, lemonade)
rum_coke = (rum, coke)
gin_juice = (gin, orange_juice)
vodka_coke = (vodka, coke)

# Pour drink
def pour_drink(drink):
    booze = 30 / flowrate_second
    mixer = 220 / flowrate_second
    GPIO.output(drink[0], GPIO.HIGH)
    GPIO.output(drink[1], GPIO.HIGH)
    sleep(booze)
    GPIO.output(drink[0], GPIO.LOW)
    sleep(mixer - booze)
    GPIO.output(drink[1], GPIO.LOW)

def cleaning_cycle():
    pumps = [6, 13, 19, 26, 12, 16]
    cleaning_time = 4000 / flowrate_second
    for i in pumps:
        GPIO.output(pumps[i], GPIO.HIGH)
        sleep(cleaning_time)
        GPIO.output(pumps[i], GPIO.LOW)
 
# Cleanup and poweroff
def close():
    GPIO.cleanup()
    win.destroy() 
 
# Menu GUI
win = tk.Tk()
win.configure(background='black')
win.attributes('-fullscreen', True)
win.title('Bartender')
btnFont = font.Font(family='Helvetica', size=18, weight='bold')
button1 = tk.Button(win, width=14, height=5, bg='black', fg='white', command= lambda: pour_drink(scotch_coke), text='Scotch & Coke', font=btnFont)
button1.grid(row=0,column=1)
 
button2 = tk.Button(win, width=14, height=5, bg='black', fg='white', command= lambda: pour_drink(screwdriver), text='Screwdriver', font=btnFont)
button2.grid(row=0,column=2)
 
button3 = tk.Button(win, width=14, height=5, bg='black', fg='white', command= lambda: pour_drink(vodka_lemonade), text='Vodka Lemonade', font=btnFont)
button3.grid(row=0,column=3)
 
button4 = tk.Button(win, width=14, height=5, bg='black', fg='white', command= lambda: pour_drink(rum_coke), text='Rum & Coke', font=btnFont)
button4.grid(row=1,column=1)
 
button5 = tk.Button(win, width=14, height=5, bg='black', fg='white', command= lambda: pour_drink(gin_juice), text='Gin & Juice', font=btnFont)
button5.grid(row=1,column=2)
 
button6 = tk.Button(win, width=14, height=5, bg='black', fg='white', command= lambda: pour_drink(vodka_coke), text='Vodka & Coke', font=btnFont)
button6.grid(row=1,column=3)
 
button7 = tk.Button(win, width=14, height=5, bg='black', fg='white', command= cleaning_cycle, text='Cleaning cycle', font=btnFont)
button7.grid(row=2,column=1)
 
button8 = tk.Button(win, width=14, height=5, bg='black', fg='white', command= close, text='Power off', font=btnFont)
button8.grid(row=2,column=3)
 
win.protocol("WM_DELETE_WINDOW", close) # exit cleanly
win.mainloop()