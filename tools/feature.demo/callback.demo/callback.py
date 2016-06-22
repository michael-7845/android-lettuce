# -*- coding: utf-8 -*- 
from lettuce import *

@before.each_scenario
@belong_to_feature(u"计算器一")
def setup(scenario):
    print "before", scenario.name  

@after.each_scenario
@belong_to_feature(u"计算器一")
def teardown(scenario):
    print "after", scenario.name 
    
@before.each_feature
@at_feature(u"计算器二")
def before_feature(feature):
    print "before", feature.name  

@after.each_feature
@at_feature(u"计算器二")
def after_feature(feature):
    print "after", feature.name 
    