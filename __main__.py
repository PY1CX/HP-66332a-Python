import PS_66332a as ps
import time

#Init the DMM with the Serial port
ps0 = ps.PS_init("/dev/ttyUSB0")
time.sleep(1)
ps.PS_power_switch(ps0, '1')
for x in range(1, 15):
    ps.PS_set_voltage(ps0, x)
    print(float(ps.PS_read_voltage_set(ps0)))
    time.sleep(2)
ps.PS_close(ps0)
    