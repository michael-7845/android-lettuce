# -*- coding: utf-8 -*-
from uiautomator import Device
from uiautomator.myConfig import config

device = None
device2 = None
device3 = None

if config.phone.is_only_one_device:
    device = Device()
else:
    device = Device(config.phone.device1)
    device2 = Device(config.phone.device2)
    device3 = Device(config.phone.device3)
    
