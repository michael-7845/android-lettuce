#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
from uiautomator.myConfig import config

is_going = True

def _parse_config():
    _logtype = config.logtype.__dict__
    
    logtypes = []
    for option in _logtype:
        if not option.endswith("_file") and not option.endswith("_kill"):
            logtypes.append(option)
    
    all = {}
    for type in logtypes:
        all[type] = {"cmd":_logtype[type], "file":_logtype[type+"_file"]}
    print all
    return all

all_log = _parse_config()
    
def make_log():
    while is_going:
        #os.system("")
        time.sleep(1)
        
def main():
    _parse_config()
    
if __name__ == '__main__':
    main()
    
