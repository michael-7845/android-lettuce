#!/usr/bin/python
# -*- coding: utf-8 -*- 
from lettuce import *
import os,sys
import time
from uiautomator.myConfig import config
import mtklog

#to save cmd & logpath from android_lettuce.conf
_all = None

def _is_option(option):
    # not ends with options, it is an option
    options = ("_get", "_file", "_kill", "_clear")
    result = []
    for o in options:
        if not option.endswith(o):
            result.append(True)
        else:
            result.append(False)
    return all(result)

def _parse_config():
    _logtype = config.logtype.__dict__
    logtypes = []
    for option in _logtype:
        if _is_option(option):
            logtypes.append(option)
    _all = {}
    for type in logtypes:
        _all[type] = {
        "type":_logtype[type].strip(), 
        "get":_logtype[type+"_get"].strip(), 
        "file":_logtype[type+"_file"].strip(), 
        "kill":_logtype[type+"_kill"].strip(),
        "clear":_logtype[type+"_clear"].strip()
        }
    return _all

try:
    # {'log type1':{'get': log1 command, 'file': log2 file, ...}, 
    #  'log type2':{'get': log2 command, 'file': log2 file, ...}, 
    #  ... }
    _all = _parse_config()
except:
    None    
    
recordpath = []

# ======= before all
# 1. clear old logs
# 2. start logging process
@before.all
def before_all():
    #*-* qi.zhao added begin *-*
    if not config.allog.is_logged:
        return None
    #*-* qi.zhao added end *-*
    clear_log()
    start_log()
    
# rm -rf [allogdir]/*
def clear_log():
    log_dir = os.path.join(os.getcwd(), config.allog.dir)
    if not os.path.exists(log_dir):
        return
    delete_path = os.path.join(log_dir, "*")
    os.popen(r"rm -rf %s" % delete_path)
    
def start_log():
    command = []
    try:
        #for [logtype] section
        for type in _all.keys():
            if _all[type]['type'] != 'user':
                continue
            command.append("%s >> %s &" % (_all[type]['get'], _all[type]['file']))  
    except:
        None
    
    #start to run log capture command
    for c in command:
        os.popen(c)
        
# ======= after all
# 1. kill logging process
@after.all
def after_all(scenario):
    if config.allog.is_logged:
        stop_log()
        
def stop_log():
    try:
        for log_type in _all.keys():
            if _all[log_type]['type'] != 'user':
                continue
            kill_command = _all[log_type]['kill']
            try:
                os.popen(kill_command)
            except:
                None
    except Exception as e:
        print "Exception:", e
        
# ======= before each scenario
# 1. clear log public log
# 2. create new log file
# 3. record new log file in recordpath
# 4. output new log info to logpath.rec
@before.each_scenario
def before_scenario(scenario):
    #*-* qi.zhao added begin *-*
    if not config.allog.is_logged:
        return None
    #*-* qi.zhao added end *-*
    
    feature = scenario.feature
    #reset public logfile
    for log_type in _all.keys():
        os.popen(_all[log_type]['clear'])
        
    try:
        # create log dir, if not exists
        log_dir = os.path.join(os.getcwd(), config.allog.dir)
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
    except Exception as e:
        print e
        None
        
    try:    
        for log_type in _all.keys():
            topath = os.path.join(log_dir, "%s_%s_%s_%s.log" % (feature.name.encode('utf-8'), scenario.name.encode('utf-8'), log_type, _timeformat()))
            try:
                # create log file
                f = open(topath, "w")
                #record all logfile path
                recordpath.append(topath)
            finally:
                f.close()
        output_conf_rec(recordpath,scenario)
    except Exception as e:
        # print e
        None
        
#generate logpath.rec
def output_conf_rec(recordpath,scenario):
    feature = scenario.feature
    # create log dir, if not exists
    log_dir = os.path.join(os.getcwd(), config.allog.dir)
    # output logpath.rec
    logpath_rec = os.path.join(log_dir, config.allog.logpath_record_file)
    try:
        for p in recordpath:
            recfile = open(logpath_rec,'a')
            recfile.write("%s:%s@%s\n" % (feature.name.encode('utf-8'), scenario.name.encode('utf-8'), "[[ATTACHMENT|%s]]" % p))
            recfile.close()
    except Exception as e:
        print e
    
# ======= after each scenario
# 1. save log file
@after.each_scenario
def after_scenario(scenario):
    if config.allog.is_logged:
        save_scenario_log(scenario)
    
def save_scenario_log(scenario):
    log_dir = os.path.join(os.getcwd(), config.allog.dir)
    logpath_rec = os.path.join(log_dir, config.allog.logpath_record_file)
    file_object = open(logpath_rec)
    
    try:
        #for log in public_log:
        for log_type in _all.keys():
            if _all[log_type]['type'] == 'system':
                command = "%s > %s" % (_all[log_type]['get'], _all[log_type]['file'])
                os.popen(command)
            for logpath in recordpath:
                if not log_type in logpath:
                    continue
                #for line in file_object:
                #    if logpath in line:
                #        break
                file_r = open(_all[log_type]['file'], 'rb')
                file_w = open(logpath, 'wb')
                try:            
                    file_w.write(file_r.read())
                finally:
                    file_r.close()
                    file_w.close()
                if not len(recordpath)==0:
                    recordpath.remove(logpath) 
                break
    finally:
        file_object.close()
    
def _timeformat():
    return time.strftime("%Y-%m-%d_%X", time.localtime())
        
def debug2():
    _all = _parse_config()
    print _all

def debug():
    class _feature:
        def __init__(self, nm):
            self.name = nm
    
    f = _feature("myfeature")

if __name__ == '__main__':
    debug2()

