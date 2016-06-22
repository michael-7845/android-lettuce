#!/usr/bin/python
# -*- coding: utf-8 -*- 
import re
import os
import sys
from glob import glob
import optparse
from uiautomator.myConfig import config

project_root_path = config.project.basepath
tips = '''
Usage: duplicateSteps.py [options] project
       duplicateSteps.py -h|--help for more help
'''
not_duplicated = ["compimg.py","allog.py","mtklog.py"]

device_string = r"(from uiautomator.myDevice import )(device)( as d)"
device_regex = re.compile(device_string)
step_string = ur"(@step.*'\S+)(\$'.*)$"
step_regex = re.compile(step_string)

def _newFile(filename, nth):
    f = filename.split('.')
    return "%s%d.%s" % (f[0], nth, f[1])
    
def _duplicate(filename, nth):
    fr = open(filename, 'r')
    fw = open(_newFile(filename, nth), 'w')
    for line in fr:
        line = line.decode("utf-8")
        line = device_regex.sub(r'\g<1>\g<2>%d\g<3>' % nth , line)
        line = step_regex.sub(ur'\g<1>@手机%d\g<2>' % nth, line)
        fw.write(line.encode("utf-8"))
    fr.close()
    fw.close()
    
def changeAll(stepsDir, devCount=3):
    number = devCount+1
    pys = glob(os.path.join(stepsDir, "*.py"))
    origin_pys = []
    for py in pys:
        isOrigin = True
        for nd in not_duplicated:
            if py.endswith(nd):
                isOrigin = False
        if isOrigin:
            for nth in range(2, number):
                if py.endswith("%d.py" % nth):
                    isOrigin = False
        if isOrigin:
            origin_pys.append(py)
        
    for py in origin_pys:
        for nth in range(2, number):
            newpy = _newFile(py, nth)
            if not os.path.exists(newpy):
                print "Generating %s ..." % newpy
                _duplicate(py, nth)
    
def main(steps_path):
    changeAll(steps_path)
    
def commandui(args=sys.argv[1:]):
    parser = optparse.OptionParser(usage="%prog [options] project", version="%prog 1.0")
    parser.add_option("-d", 
                  dest="default",
                  action="store_true",
                  default=False,
                  help='specify project as default current project, which is specified in android_lettuce.conf/project/current, if project not specified')
    (options, args) = parser.parse_args(args)
    if len(args) == 1:
        steps_path = os.path.join(project_root_path, args[0], "steps")
    elif options.default:
        steps_path = os.path.join(project_root_path, config.project.current, "steps")
    else:
        print tips
        exit(1)
    
    if not config.phone.is_only_one_device:
        main(steps_path)
    
if __name__ == '__main__':
    commandui()
    
