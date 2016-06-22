#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import time
import subprocess
import optparse
from uiautomator.myConfig import config

base_path = config.project.basepath
current_path = os.getcwd()

uiautomator_dir=r"/usr/local/lib/python2.7/dist-packages/uiautomator-0.1.30-py2.7.egg/uiautomator"
lettuce_dir=r"/usr/local/lib/python2.7/dist-packages/lettuce"
lettuce_plugins_dir=r"/usr/local/lib/python2.7/dist-packages/lettuce/plugins"
jenkins_dir=r"/var/lib/jenkins/jobs/My_Android_Lettuce/workspace"
modify_files = {
"__init__.py": [uiautomator_dir, "root", "staff", "644"],
"myDevice.py": [uiautomator_dir, "root", "staff", "755"],
"myConfig.py": [uiautomator_dir, "root", "staff", "755"],
"uiautomatorEx.py": [uiautomator_dir, "root", "staff", "755"],
"__init__.py": [lettuce_dir, "root", "staff", "644"],
"terrain.py":[lettuce_dir, "root", "staff", "644"],
"fs.py":[lettuce_dir, "root", "staff", "644"],
"regex.py":[lettuce_dir, "root", "staff", "644"],
"xunit_output.py":[lettuce_plugins_dir, "root", "staff", "644"],
"mylettuce.sh":[jenkins_dir, "jenkins", "jenkins", "755"]
}

def backup_file(files):
    now = time.strftime("%Y%m%d%H%M%S")
    # backup uiautomator files
    new_uiauto_dir=os.path.join(r"/root/copies", now, "uiautomator")
    new_lettuce_dir=os.path.join(r"/root/copies", now, "lettuce")
    new_lettuce_plugins_dir=os.path.join(r"/root/copies", now, "lettuce", "plugins")
    new_jenkins_dir=os.path.join(r"/root/copies", now, "lettuce")
    if not os.path.exists(new_uiauto_dir):
        os.makedirs(new_uiauto_dir)
    if not os.path.exists(new_lettuce_dir):
        os.makedirs(new_lettuce_dir)
    if not os.path.exists(new_lettuce_plugins_dir):
        os.makedirs(new_lettuce_plugins_dir)
    if not os.path.exists(new_jenkins_dir):
        os.makedirs(new_jenkins_dir)
    
    for (filename, values) in files.items():
        destdir=values[0]
        destfile = os.path.join(destdir, filename)
        if destdir == uiautomator_dir:
            run(r"cp -r %s %s" % (destfile, new_uiauto_dir), isshow=False)
        elif destdir == lettuce_dir:
            run(r"cp -r %s %s" % (destfile, new_lettuce_dir), isshow=False)
        elif destdir == lettuce_plugins_dir:
            run(r"cp -r %s %s" % (destfile, new_lettuce_plugins_dir), isshow=False)
        elif destdir == jenkins_dir:
            run(r"cp -r %s %s" % (destfile, new_jenkins_dir), isshow=False)
        
def modify_file(files):
    for (filename, values) in files.items():
        # copy file
        destdir=values[0]
        svnfile=""
        if destdir == uiautomator_dir:
            svnfile = os.path.join(base_path, "tools", "uiautomator", filename)
        elif destdir == lettuce_dir:
            svnfile = os.path.join(base_path, "tools", "lettuce", filename)
        elif destdir == lettuce_plugins_dir:
            svnfile = os.path.join(base_path, "tools", "lettuce", "plugins", filename)
        elif destdir == jenkins_dir:
            svnfile = os.path.join(base_path, "tools", "jenkins", filename)
        destfile = os.path.join(destdir, filename)
        run(r"cp %s %s" % (svnfile, destfile), isshow=False)
        # modify file property
        run(r"chown %s %s" % (values[1], destfile), isshow=False)
        run(r"chgrp %s %s" % (values[2], destfile), isshow=False)
        run(r"chmod %s %s" % (values[3], destfile), isshow=False)

def run_command(cmd):
    cmd_line = cmd.split("\t")
    return subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def get_std_err_pipe(process):
    (stdoutput,erroutput) = process.communicate()
    return (stdoutput,erroutput)

def run(cmd, isshow=True):
    p = run_command(cmd)
    (std, err) = get_std_err_pipe(p)
    if isshow:
        print std

def commandui(args=sys.argv[1:]):
    parser = optparse.OptionParser(usage="%prog [options] arg1", version="%prog 1.0")

    parser.add_option("-t", 
                      dest="tools",
                      action="store_true",
                      default=False,
                      help='update tools')
    parser.add_option("-u", "--update",
                      dest="update",
                      action="store",
                      default=None,
                      help='update the project xxxxx')
    parser.add_option("-a", "--account",
                      dest="account",
                      action="store",
                      default=None,
                      help='svn account')
    parser.add_option("-p", "--password",
                      dest="password",
                      action="store",
                      default=None,
                      help='svn password')
    parser.add_option("-n", "--new",
                      dest="new",
                      action="store",
                      default=None,
                      help='create new lettuce project')
    parser.add_option("-m", "--modify",
                      dest="modify",
                      action="store_true",
                      default=False,
                      help=r'modify lettuce/uiautomator/jenkins')
    parser.add_option("--feature",
                      dest="feature",
                      action="store",
                      default=None,
                      help=r'create feature sample in project xxxxx')

    def update_vnc():
        if options.account:
            if options.password:
                run(r"svn update --username %s --password %s" % (options.account, options.password))
            else:
                run(r"svn update --username %s" % (options.account))
        elif options.password:
            print "exit: no account with the password"
        else:
            run(r"svn update")
            
    def checkout_vnc(url):
        if options.account:
            if options.password:
                run(r"svn co %s --username %s --password %s" % (url, options.account, options.password))
            else:
                run(r"svn co %s --username %s" % (url, options.account))
        elif options.password:
            print "exit: no account with the password"
        else:
            run(r"svn co %s" % (url))
        
    (options, args) = parser.parse_args(args)
    
    if options.tools: # update tools
        os.chdir(current_path)
        update_vnc()
        run(r"chmod 755 *", isshow=False)
        run(r"chmod 755 *.sh", isshow=False)
        
    if options.update: # update project
        os.chdir(os.path.join(base_path, options.update, "steps"))
        update_vnc()
        run(r"chmod 644 *", isshow=False)
        run(r"rm -f *2.py", isshow=False)
        run(r"rm -f *3.py", isshow=False)
        run(r"%s %s" %(os.path.join(base_path, "tools", "steps", "duplicateSteps.py"), options.update), isshow=False)
        os.chdir(os.path.join(base_path, options.update, "features"))
        update_vnc() # for future
        run(r"chmod 644 *", isshow=False)
        os.chdir(current_path)

    if options.new: # new project
        os.mkdir(os.path.join(base_path, options.new))
        os.mkdir(os.path.join(base_path, options.new, "features"))
        os.chdir(os.path.join(base_path, options.new))
        checkout_vnc(r"http://10.120.10.57/svn/hiota/android_lettuce/steps")
        run(r"chmod -R 755 %s" % (os.path.join(base_path, options.new)), isshow=False)
        run(r"chmod 644 %s" % (os.path.join(base_path, options.new, r"steps/*")), isshow=False)
        run(r"chmod 644 %s" % (os.path.join(base_path, options.new, r"features/*")), isshow=False)
        run(r"%s %s" %(os.path.join(base_path, "tools", "steps", "duplicateSteps.py"), options.new), isshow=False)
        os.chdir(current_path)
        
    if options.modify: # update environment
        backup_file(modify_files)
        modify_file(modify_files)
    
    if options.feature:
        run(r"cp %s %s" % (os.path.join(current_path, "feature.demo", "simple.demo", "*"), os.path.join(base_path, options.feature, "features")), isshow=False)
        run(r"chmod 644 %s" % (os.path.join(base_path, options.feature, "features", "*")), isshow=False)
        
if __name__ == '__main__':
    commandui()
    
