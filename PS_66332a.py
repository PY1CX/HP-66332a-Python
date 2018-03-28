import serial
import time
import re

"""
 66332a Power Supply Driver Class
 Author: Felipe Navarro
"""

"""
Based on the SCPI command list on: 
http://www.manson.com.hk/getimage3/index/action/images/name/SDP_SCPI_command_list_1_2.pdf
Accessed in 27/03/2018 - 03:20 GMT
"""


def PS_init(port_number): 
    ser = serial.Serial(port = port_number,
                        baudrate = 9600,
                        parity = serial.PARITY_NONE,
                        stopbits = serial.STOPBITS_TWO,
                        bytesize = serial.EIGHTBITS)
                        #xonxoff  = True)
                        #xonxoff=True
    time.sleep(0.5)
    if ser.isOpen() == True:
        ser.write("SYSTem:REMote\n".encode())
        print("Serial open")
        return ser #Return ser as a handler
    else:
        return False   

def PS_close(self):
    self.close()
    print("Serial Closed")

"""
Voltage Set Function
"""
def PS_set_voltage(self, voltage):
    #Guard Clause
    if voltage > 20 or voltage < 0:
        return False
    #SET VOLTAGE FUNCTION: VOLT 1.00V for example
    self.write("VOLT " + str(voltage) + "\n".encode())
    return True

"""
Voltage Set Read Function
"""
def PS_read_voltage_set(self):
    self.write("VOLT?\n".encode())
    result = self.readline()
    regex = re.compile('[0-9]*[.][0-9]*[VmV]')
    if re.findall(regex, result) >= 1:
        return result
    else:
        return False

"""
Current Limit Set Function
"""
def PS_set_limit_current(self, current, unit_):
    #Guard Clause
    if unit_ != "mA" or "A":
        return False
    if current > 5 or current < 0:
        return False
    #SET VOLTAGE FUNCTION: VOLT 1.00V for example
    self.write("CURR " + current + unit_ + "\n".encode())
    return True

"""
Current actual limit Read Function
"""
def PS_read_limit_current(self):
    self.write("CURR?\n".encode())
    result = self.readline()
    regex = re.compile('[0-9]*[.][0-9]*[AmA]')
    if re.findall(regex, result) >= 1:
        return result
    else:
        return False

"""
Actual voltage read function
"""
def PS_read_voltage(self):
    self.write("MEAS:VOLT?\n".encode())
    result = self.readline()
    regex = re.compile('[0-9]*[.][0-9]*[AmA]')
    if re.findall(regex, result) >= 1:
        return result
    else:
        return False

"""
Actual current consumption read function
"""
def PS_read_current(self):
    self.write("MEAS:CURR?\n".encode())
    result = self.readline()
    regex = re.compile('[0-9]*[.][0-9]*[AmA]')
    if re.findall(regex, result) >= 1:
        return result
    else:
        return False

"""
Actual POWER consumption read functionhttps://www.edx.org/
"""
def PS_read_power(self):
    self.write("MEAS:POW?\n".encode())
    result = self.readline()
    regex = re.compile('[0-9]*[.][0-9]*[W]')
    if re.findall(regex, result) >= 1:
        return result
    else:
        return False    

"""
SET OUTPUT ON/OFF
With checking if it really powered the power supply up!
"""
def PS_power_switch(self, state):
    #Guard Clause
    #if state != "0" or state != "1":
    #    return False
    self.write("OUTP " + state  +"\n".encode())
    """
    self.write("OUTP ?".encode())
    result = self.readline()
    if result == 0:
        return True
    else:
        return result """

"""
Returns the state of the output voltage.
If ON return True if OFF return False
"""
def PS_power_switch_state(self):
    self.write("OUTP ?".encode())
    result = self.readline()
    if result == 0:
        return True
    elif result == 1:
        return False
    else:
        return result