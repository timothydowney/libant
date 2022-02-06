#!/usr/bin/env python3
from time import sleep

from libAnt.drivers.serial import SerialDriver
from libAnt.node import Node
from libAnt.profiles.factory import Factory


def callback(msg):
    print(msg)


def eCallback(e):
    raise e


with Node(SerialDriver('/dev/ttyUSB0'), 'SerialNode1') as n:
    n.enableRxScanMode()
    f = Factory(callback)

    f.enableFilter()
    f.addToFilter(15211) # heart rate monitor
    #f.addToFilter(7103)  # tacx neo2t
    
    n.start(f.identifyDevices, eCallback)
    sleep(30)  # Listen for 30sec
