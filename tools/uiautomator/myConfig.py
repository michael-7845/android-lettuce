#!/usr/bin/python
# *-* coding=utf-8 *-*
import ConfigParser

my_config = r"/home/ckt/lettuce/android_lettuce.conf"

def _read_config(config_file):
    cf = ConfigParser.ConfigParser()
    cf.read(config_file)
    secs = cf.sections()
    res = {}
    for sec in secs:
        res[sec] = {}
        opts = cf.options(sec)
        for opt in opts:
            if opt.startswith(r"is_"):
                res[sec][opt] = cf.getboolean(sec, opt)
            elif opt.startswith(r"i_"):
                res[sec][opt] = cf.getint(sec, opt)
            elif opt.startswith(r"f_"):
                res[sec][opt] = cf.getfloat(sec, opt)
            else:
                res[sec][opt] = cf.get(sec, opt)
    return res
    
class Section:
    def __init__(self, options):
        for (k, v) in options.items():
            setattr(self, k, v)

class Config:
    def __init__(self, sections):
        for (k, v) in sections.items():
            s = Section(v)
            setattr(self, k, s)
    
config = Config(_read_config(my_config))
   
def show_config():
    print dir(config)
    print config.phone.device1, type(config.phone.device1)
    print config.phone.device2, type(config.phone.device2)
    print config.phone.device3, type(config.phone.device3)
    print config.image.is_compared, type(config.image.is_compared)
    #print config.log.i_logcat, type(config.log.i_logcat)
    #print config.log.f_version, type(config.log.f_version)
   
if __name__ == '__main__':
    show_config()
    
    
