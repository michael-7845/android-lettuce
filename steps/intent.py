#!/usr/bin/python
# -*- coding: utf-8 -*-
from lettuce import *

from lettuce.regex import *
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d

@step(u'启动活动【%s】$' % (mode_activity))
def run_command(step, act):
    ex.start_activity(act.strip())
