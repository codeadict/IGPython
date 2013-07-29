# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
import serial


class BaseDevice(object):
    """
    Core class for device drivers
    """
    baud = None
    parity = None #Odd or Even
    stopBits = None
    byteSize = None

    def __init__(self, device_name='Dummy Device', port_id=None):
        """
        Initialize with a name for device and port that is connected
        """
        self.device_name = device_name
        self.port_id = port_id
        self.connection = None

    def connect(self):
        """
        Connect to the device
        """
        if self.connection is None:
            try:
                self.connection = serial.Serial(port= self.port_id, baudrate=self.baud,
                    parity=self.parity, stopbits=self.stopBits,bytesize=self.byteSize)
                return True
            except:
                print "Error connecting with serial Port"
                return False

    def get_weight(self):
        """
        Get the Weight from device
        """
        raise NotImplementedError

    def get_live_weight(self):
        """
        Get live weightin for graph
        """
        raise NotImplementedError


