'''
    PROJECT  : Project 2.7. Long ISP: The Stock Market Ticker
    PURPOSE  : Creating GUI and sending stock data to Arduino using Python
    DATE     : 2021 05 29
    MCU      : 328P
    STATUS   : Working
    NOTES    : None
    REFERENCE: http://darcy.rsgc.on.ca/ACES/TEI3M/2021/ISPs.html
'''
from tkinter import *    # Imports Tkinter (for GUI)
from yahoo import search # Imports my function for finding info
import sys               # Allows me to check OS
import serial            # PySerial: send data to Arduino Serial Monitor
import glob              # Allows me to find path to USB port

ports_available = []                # List to show in GUI
if sys.platform == "darwin":        # If user is on MacOS
	ports = glob.glob('/dev/tty.*') # Set USB path to ports var
else:
	print("Platform not supported") # Not adapted for use on Linus or Windows
for port in ports:
	ports_available.append(port)    # Add port to ports_available list

# Available Serial/Baud Rates (selected must match Arduino)
serial_available = [300, 600, 1200, 2400, 4800, 9600,
                    14400, 19200, 28800, 38400, 57600, 115200]

ticker = vars() # Future ticker information

class App():
    def __init__(self):
        global e1, entry, user_baud, user_ports
        self.root = Tk()
        self.root.title("Stock Ticker GUI") # Window title
        self.root.resizable(False, False)   # Do not allow user to resize window on x or y axis
        user_baud = StringVar(self.root)
        user_baud.set(serial_available[0])
        Label(self.root, text="Serial Rate:").pack() # Label saying "Serial Rate:"
        OptionMenu(self.root, user_baud, *serial_available).pack() # Dropdown List with baud rates
        user_ports = StringVar(self.root)
        user_ports.set(ports_available[0])
        Label(self.root, text="USB Port:").pack() # Label saying "USB Port:"
        OptionMenu(self.root, user_ports, *ports_available).pack() # Dropdown List with available USB ports
        Label(self.root, text="Ticker:").pack() # Label saying "Ticker:"
        entry = Entry(self.root)    # Entry box for user to enter stock ticker
        entry.pack()

        # Various Buttons
        self.button = Button(text="Start", command=self.loop_setup).pack(side=LEFT, padx=50) # Searches for stock info on click
        self.button = Button(text="Exit", command=self.close_program).pack(side=LEFT, padx=50) # Closes program on click
        self.root.mainloop()

    def close_program(self): # Used to close program when "Exit" button is pressed
        exit()

    def loop_setup(self):
        global ser                               # Allows ser to be used throughout program
        baud_rate = user_baud.get()              # Finds user selected baud rate
        usb_port = user_ports.get()              # Finds user selected USB port
        ser = serial.Serial(usb_port, baud_rate) # Use PySerial to create "ser" object
        self.serial_output()                     # Start serial_output function

    def serial_output(self):
        global update
        tickers = str(entry.get()).split()                    # Creates list of tickers entered by user
        for item in tickers:                                  # Iterate through items in list
            print(item)                                       # This is just for easy testing
            ser.write(search(item).encode())                  # Write information given by search function (yahoo.py) to Arduino
            print(ser.readline())                             # Read Arduino Serial monitor to ensure it sent (testing)
            update = self.root.after(1000, self.loop_setup) # This allows the program to run multiple times

app=App() # Opens GUI