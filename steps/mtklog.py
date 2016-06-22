#!/usr/bin/python
# -*- coding: utf-8 -*- 
from lettuce import *
import os
import zipfile
import time
from uiautomator.myConfig import config


no_file = r"No such file or directory"
#define mtklog path
mdlog_dir = r"/sdcard/mtklog/mdlog/"
mobilelog_dir = r"/sdcard/mtklog/mobilelog/"
netlog_dir = r"/sdcard/mtklog/netlog/"

cmd_ls = r"adb shell ls"

mtkzip_path = []

@before.all
def before_all():
    if not config.allog.is_mtklog:
        return None
    clear_log()
        
def _timeformat():
    return time.strftime("%Y-%m-%d_%X", time.localtime())
    
@before.each_scenario
def before_scenario(scenario):
    if not config.allog.is_mtklog:
        return None
    try:
        #*-* mtklog zip name *-*
        mtklog_name = None
        feature = scenario.feature     
        log_dir = os.path.join(os.getcwd(), config.allog.dir)    
        
        clear_mtklog(save_mtklog_info()) 
        mtklog_name = "%s_%s_mtklog_%s.zip" % (feature.name.encode('utf-8'), scenario.name.encode('utf-8'), _timeformat())
        topath = os.path.join(log_dir, mtklog_name)
        f = open(topath, "w")
        #*-* qi.zhao added*-*  
        mtkzip_path.append(topath)
        f.close()
        output_conf_rec(mtkzip_path,scenario)
    except:
        None

@after.each_scenario
def after_scenario(scenario):          
    if not config.allog.is_mtklog:
        return None
    pull_mtklog(mtkzip_path)
    #reset mktzip_path
    mtkzip_path.remove(mtkzip_path[0])
    clear_tmp_mtk()

#obtain the newest log folder
def get_newest_log_dir(file):
    #save all dirs which were belong to specific logtype
    all_dir = []
    for line in file:
        all_dir.append(line.replace("\r\n","")+r"/")
    newest = None
    f = 0
    while f < len(all_dir)-1 or len(all_dir) == 1:
        for file in all_dir:
            if '.' in file:
                all_dir.remove(file)
            else:
                continue
        if len(all_dir) == 1:
            newest = all_dir[0]
            return newest
        else:
            if '.' not in all_dir[f] and '.' not in all_dir[f+1]:
                if cmp(all_dir[f],all_dir[f+1]) < 0:
                    newest = all_dir[f+1]
                elif cmp(all_dir[f],all_dir[f+1]) > 0:
                    newest = all_dir[f]
                else:
                    newest = all_dir[f]
        f += 1
    return newest

#return all md_folder, mobile_folder, net_folder
def all_folders():
    all = []
    #log folder: take output from console  
    md_folder = os.popen("%s %s" % (cmd_ls, mdlog_dir))
    mobile_folder = os.popen("%s %s" % (cmd_ls, mobilelog_dir))
    net_folder = os.popen("%s %s" % (cmd_ls, netlog_dir))
    all.append(md_folder)
    all.append(mobile_folder)
    all.append(net_folder)
    return all
    
#*-* qi.zhao added *-*    
def save_mtklog_info():    
    #check if mtklog dir is exist
    try:
        cmd_print = os.popen(r"adb shell ls /sdcard/mtklog/")
    except:
        None
    if no_file in str(cmd_print):
        return None

    md_newest= get_newest_log_dir(all_folders()[0])
    mobile_newest= get_newest_log_dir(all_folders()[1])
    net_newest= get_newest_log_dir(all_folders()[2])
    
    # print md_newest
    # print mobile_newest
    # print net_newest
    
    #log files: take output from console
    md_logs = os.popen("%s %s%s" % (cmd_ls, mdlog_dir, md_newest))
    mobile_logs = os.popen("%s %s%s" % (cmd_ls, mobilelog_dir, mobile_newest))
    net_logs = os.popen("%s %s%s" % (cmd_ls, netlog_dir, net_newest))        
    
    #dict: {logtype:[log1.txt,log2.txt],logtype:[log1.dmp,log2.dmp]}
    alltype_logs = {"md_logs":md_logs.readlines(),"mobile_logs":mobile_logs.readlines(),"net_logs":net_logs.readlines()}
    
    for key in alltype_logs:
        i = 0
        while i < len(alltype_logs[key]):
            if key == "md_logs":
                alltype_logs[key][i] = mdlog_dir + md_newest + alltype_logs[key][i].replace("\r\n","")
            elif key == "mobile_logs":
                alltype_logs[key][i] = mobilelog_dir + mobile_newest + alltype_logs[key][i].replace("\r\n","")
            elif key == "net_logs":
                alltype_logs[key][i] = netlog_dir + net_newest + alltype_logs[key][i].replace("\r\n","")
            else:
                continue
            if len(alltype_logs[key]) == 1:
                break
            else:
                i += 1
    return alltype_logs
    # print alltype_logs    

#*-* qi.zhao added *-*    
def clear_mtklog(alltype_logs):
    try:
        for key in alltype_logs:
            if key == "md_logs":
                for file in alltype_logs[key]:
                    if ".txt" not in file:
                        os.popen("adb shell '>%s'" % file)
            elif key == "mobile_logs":
                for file in alltype_logs[key]:
                    if "_log" in file:
                        os.popen("adb shell '>%s'" % file)
                        if "_log." in file:
                            os.popen("adb shell 'rm %s'" % file)
            elif key == "net_logs":
                for file in alltype_logs[key]:
                    if ".cap" in file:
                        os.popen("adb shell '>%s'" % file)
    except:
        None
def clear_tmp_mtk():
    try:
        #clear mtklog tmp file
        os.popen(r"rm -rf /tmp/mtklog")
        # for log_type in all.keys():
            # #print "rm %s" % all[log_type]['file']
            # os.popen("rm %s >/dev/null 2>&1" % all[log_type]['file'])
    except:
        None
    
def pull_mtklog(mtkzip_path):
    md_newest= get_newest_log_dir(all_folders()[0])
    mobile_newest= get_newest_log_dir(all_folders()[1])
    net_newest= get_newest_log_dir(all_folders()[2])
    
    #add >/dev/null 2>&1 to avoid print a large number pull logs
    os.popen("adb pull /sdcard/mtklog/mdlog/%s /tmp/mtklog/mdlog >/dev/null 2>&1" % md_newest)
    os.popen("adb pull /sdcard/mtklog/mobilelog/%s /tmp/mtklog/mobilelog >/dev/null 2>&1" % mobile_newest)
    os.popen("adb pull /sdcard/mtklog/netlog/%s /tmp/mtklog/netlog >/dev/null 2>&1" % net_newest)
    zip_folder('/tmp/mtklog', mtkzip_path[0])
    
def zip_folder( foldername, filename):
    try:
        f = zipfile.ZipFile(filename,'w',zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(foldername):
            for file in filenames:
                f.write(os.path.join(dirpath,file).encode("utf-8"))
                # print os.path.join(dirpath,filename).encode("utf-8")
        f.close()
    except Exception as e:
        print e

#generate logpath.rec
def output_conf_rec(mtkzip_path, scenario):
    feature = scenario.feature
    # create log dir, if not exists
    log_dir = os.path.join(os.getcwd(), config.allog.dir)
    # output logpath.rec
    logpath_rec = os.path.join(log_dir, config.allog.logpath_record_file)
    try:
        recfile = open(logpath_rec,'a')
        recfile.write("%s:%s@%s\n" % (feature.name.encode('utf-8'), scenario.name.encode('utf-8'), "[[ATTACHMENT|%s]]" % mtkzip_path[0]))
    except Exception as e:
        print e
        
#*-* qi.zhao added *-*    
# def zipfile(zipName):
    # os.system("adb pull /sdcard/mtklog /tmp/mtklog")
    # os.system("zip -r zipName.zip /tmp/mtklog ")
    
def clear_log():
    '''
    clear logs
    '''
    log_dir = os.path.join(os.getcwd(), config.allog.dir)
    if not os.path.exists(log_dir):
        return
    delete_path = os.path.join(log_dir, "*")
    os.popen(r"rm -rf %s" % delete_path)
    
    
def debug2():
    clear_mtklog(save_mtklog())
    # zipfile("hellozip.zip")

def debug():
    class _feature:
        def __init__(self, nm):
            self.name = nm
    
    f = _feature("myfeature")

if __name__ == '__main__':
    #debug2()
    folder = 'mtklog'
    filename = 'test.zip'
    # zip_folder( folder, filename )
    zip_folder( '/tmp/mtklog', 'test.zip' )