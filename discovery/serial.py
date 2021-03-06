import serial
from serial.tools import list_ports

from devices import device



def find_device(serial_config):
    for pi in list_port_info():
        if pi.device != serial_config.device:
            continue

        dev = device.Device()
        dev.serial_config(serial_config)
        dev.port_info(pi)
        return dev

    return False

def list_port_info():
    return list_ports.comports()


