# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from weighin.devices import BaseDevice
from decimal import Decimal as D

class Alibi(BaseDevice):
    """
    Driver for Alibi Devices
    """
    baud = 2400
    parity = "E" #Odd or Even
    stopBits = 1
    byteSize = 7


    def get_weight(self):
        """
        Get the Weight from device
        """
        if not self.connection:
            if self.connect():
                self.connection.timeout = 1
                self.connection.write("A")
                raw = self.connection.readline()
                self.connection.close()
                alibi = raw[0:5]
                weight = raw[6:12]
                return [int(alibi), D(weight)]
        return [D(0), D(0)]