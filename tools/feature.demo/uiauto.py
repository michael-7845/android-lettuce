#!/usr/bin/python
# -*- coding: utf-8 -*- 
from uiautomator import Device

d = Device('CKT Z')
#d(text='7').click()

# Retrieve the device info
def use_info():
    print d(text='7').info

#Turn on/off screen
def use_screen():
    # Turn on screen
    d.screen.on()
    # Turn off screen
    d.screen.off()
    #Alternative method is:
    # wakeup the device
    d.wakeup()
    # sleep the device, same as turning off the screen.
    d.sleep()

# press key
# debug in caculator app
def use_key():
    ## press home key
    #d.press.home()
    ## press back key
    #d.press.back()
    ## the normal way to press back key
    #d.press("back")
    ## press keycode 0x07('0') with META ALT(0x02) on
    d.press(0x07, 0x02)
    #d.press(0x07, 0x08) # what it means?
    #d.press("recent") #调用最近使用app列表
    #d.press(0x07)

# (x,y)
def use_position():
    #Click the screen
    # click (x, y) on screen
    d.click(10, 10)
    
    #Long click the screen
    # long click (x, y) on screen
    d.long_click(20, 20)
    
    #Swipe
    # swipe from (sx, sy) to (ex, ey)
    d.swipe(10, 10, 20, 20)
    # swipe from (sx, sy) to (ex, ey) with 10 steps
    d.swipe(10, 10, 20, 20, steps=10)
    
    #Drag
    # drag from (sx, sy) to (ex, ey)
    d.drag(sx, sy, ex, ey)
    # drag from (sx, sy) to (ex, ey) with 10 steps
    d.drag(sx, sy, ex, ey, steps=10)

#Screen Actions of the device
def use_device():
    #Retrieve/Set Orientation
    #The possible orientation is:
    #natural or n
    #left or l
    #right or r
    #upsidedown or u (can not be set)
    # retrieve orientation, it may be "natural" or "left" or "right" or "upsidedown"
    orientation = d.orientation
    print orientation
    # set orientation and freeze rotation.
    # notes: "upsidedown" can not be set until Android 4.3.
    d.orientation = "l" # or "left"
    d.orientation = "r" # or "right"
    d.orientation = "n" # or "natural"
    
    #Freeze/Un-Freeze rotation
    # freeze rotation
    d.freeze_rotation()
    # un-freeze rotation
    d.freeze_rotation(False)
    
    #Take screenshot
    # take screenshot and save to local file "home.png", can not work until Android 4.2.
    d.screenshot("home.png")
    
    #Dump Window Hierarchy
    # dump the widown hierarchy and save to local file "hierarchy.xml"
    d.dump("hierarchy.xml")
    # or get the dumped content(unicode) from return.
    xml = d.dump()
    
    #Open notification or quick settings
    # open notification, can not work until Android 4.3.
    #d.open.notification()
    # open quick settings, can not work until Android 4.3.
    #d.open.quick_settings()
    
    #Wait for idle or window update
    # wait for current window to idle
    d.wait.idle()
    # wait until window update event occurs
    d.wait.update()
    #d.wait.idle(timeout=1000)
    #d.wait.update(timeout=1000, package_name="com.android.settings")
    #d(text="Clock").click()  # click on the center of the ui object
    #d(text="OK").click.wait(timeout=3000) # click and wait for the new window update
    #d(text="John").click.topleft() # click on the topleft of the ui object
    #d(text="John").click.bottomright() # click on the bottomright of the ui object
    #d(text="Clock").wait.gone()  # wait until it's gone.
    #d(text="Settings").wait.exists() # wait until it appears.

#Register Watcher
#When a selector can not find a match, uiautomator will run all registered watchers.
def use_watcher():
    ##Click target when conditions match
    #d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") \
    #                             .click(text="Force Close")
    ## d.watcher(name) ## creates a new named watcher.
    ##  .when(condition)  ## the UiSelector condition of the watcher.
    ##  .click(target)  ## perform click action on the target UiSelector.
    #
    ##Press key when conditions match
    #d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") \
    #                             .press.back.home()
    ## Alternative way to define it as below
    #d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") \
    #                             .press("back", "home")
    ## d.watcher(name) ## creates a new named watcher.
    ##  .when(condition)  ## the UiSelector condition of the watcher.
    ##  .press.<keyname>.....<keyname>.()  ## press keys one by one in sequence.
    ##  Alternavie way defining key sequence is press(<keybname>, ..., <keyname>)
    #
    ##Check if the named watcher triggered
    ##A watcher is triggered, which means the watcher was run and all its conditions matched.
    #d.watcher("watcher_name").triggered
    ## true in case of the specified watcher triggered, else false
    #
    ##Remove named watcher
    ## remove the watcher
    #d.watcher("watcher_name").remove()
    #
    ##List all watchers
    #d.watchers
    ## a list of all registered wachers' names
    #
    ##Check if there is any watcher triggered
    #d.watchers.triggered
    ##  true in case of any watcher triggered
    #
    ##Reset all triggered watchers
    ## reset all triggered watchers, after that, d.watchers.triggered will be false.
    #d.watchers.reset()
    #
    ##Remvoe watchers
    ## remove all registered watchers
    #d.watchers.remove()
    ## remove the named watcher, same as d.watcher("watcher_name").remove()
    #d.watchers.remove("watcher_name")
    #
    ##Force to run all watchers
    ## force to run all registered watchers
    #d.watchers.run()
    d.watcher("Click_Zero").when(index='2').click(text='7')
    print d.watchers
    print d.watcher("Click_Zero").triggered
    #d.watchers.run()
    print d(text='5').info
    print d.watcher("Click_Zero").triggered
    
#Handler
#The functionality of handler is same as Watcher, except it is implemented ourside of Android uiautomator. The most different usage between handler and watcher is, handler can use customized callback function.
def fc_close(device):
    #if device(text='Force Close').exists:
    #    device(text='Force Close').click()
    print 'fc_close()'
    return True  # return True means to break the loop of handler callback functions.

def use_handler():
    # turn on the handler callback function
    d.handlers.on(fc_close)
    d(text='b').info
    # turn off the handler callback function
    d.handlers.off(fc_close)
    
#Selector
#Selector is to identify specific ui object in current window.
#
#Selector supports below parameters. Refer to UiSelector java doc for detailed information.
#text, textContains, textMatches, textStartsWith
#className, classNameMatches
#description, descriptionContains, descriptionMatches, descriptionStartsWith
#checkable, checked, clickable, longClickable
#scrollable, enabled,focusable, focused, selected
#packageName, packageNameMatches
#resourceId, resourceIdMatches
#index, instance
#
#debug in caculator
def use_selector():
    # To seleted the object ,text is 'Clock' and its className is 'android.widget.TextView'
    d(text='7', index='0').click()
    
#Selector2
def use_selector2():
    #child
    # get the child or grandchild
    #d(className="android.widget.ListView").child(text="Bluetooth")
    #d(className="android.widget.LinearLayout",index='2').child(index='0').click()
    
    #sibling
    # get sibling or child of sibling
    #d(text="Google").sibling(className="android.widget.ImageView")
    #d(text="1").sibling(index='2').click()
    #d(className="android.widget.LinearLayout",index='2').sibling(index='3').click()
    
    #child by text or description or instance
    # get the child match className="android.widget.LinearLayout"
    # and also it or its child or grandchild contains text "Bluetooth"
    #d(className="android.widget.ListView", resourceId="android:id/list") \
    #.child_by_text("Bluetooth", className="android.widget.LinearLayout")
    #print d(className='android.widget.FrameLayout').child_by_text('1', index='2').info
    #print d(className='android.widget.FrameLayout').child_by_text('1', index='2').count
    # child_by_text(), support only 1 property definition.
    
    # allow scroll search to get the child
    #d(className="android.widget.ListView", resourceId="android:id/list") \
    #.child_by_text("Bluetooth",allow_scroll_search=True,className="android.widget.LinearLayout")
    # in calllog app
    #print d(className="android.widget.FrameLayout",index="1").info
    #print d(className="android.widget.FrameLayout",index="1").child(className="android.widget.ListView",index="0").info #className="android.view.View",index="2"
    #print d(className="android.widget.FrameLayout",index="1").child(className="android.widget.ListView",index="0").child(className="android.view.View",index="2",instance="1").child(text=u'\u202d\u202d457\u202c\u202c').info
    #print d(className="android.widget.FrameLayout",index="1").child(textContains="1001011").info
    #d(className="android.widget.FrameLayout",index="1").child_by_text(u'\u202d\u202d232\u202c\u202c',allow_scroll_search=True,className="android.view.View").click.wait()
    d(className="android.widget.FrameLayout",index="1").child_by_instance("15",className="android.view.View").click.wait()
    #d(className="android.widget.FrameLayout",index="1").child_by_text("u'\u202d\u202d478\u202c\u202c'",className="android.widget.TextView").click.wait()
    #
    #child_by_text()!
    #Searches for child UI element within the constraints of this UiSelector selector. 
    #It looks for any child matching the childPattern argument that has a child UI element anywhere within its sub hierarchy that has a text attribute equal to text.
    #The returned UiObject will point at the childPattern instance that matched the search and not at the identifying child element that matched the text attribute.
    #
    #child_by_description is to find child which or which's grandchild contains the specified description, others are the same as child_by_text.
    #child_by_instance is to find child which has a child UI element anywhere within its sub hierarchy that is at the instance specified. It is performed on visible views without scrolling.
    #See below links for detailed information:
    #UiScrollable, getChildByDescription, getChildByText, getChildByInstance
    #UiCollection, getChildByDescription, getChildByText, getChildByInstance

#relative position
#Also we can use the relative position methods to get the view: left, right, top, bottom.
def use_relative():
    #d(A).left(B), means selecting B on the left side of A.
    #d(A).right(B), means selecting B on the right side of A.
    #d(A).up(B), means selecting B above A.
    #d(A).down(B), means selecting B under A.
    #So for above case, we can write code alternatively:
    ## select "switch" on the right side of "Wi‑Fi"
    #d(text="WiFi").right(className="android.widget.Switch").click()
    #debug in caculator
    d(text='7').right(index='1').click()
    
#Multiple instances
#Sometimes the screen may contain multiple views with the same e.g. text, then you will have to use "instance" properties in selector like below:
#debug in calculator app
def use_instance():
    d(text="8", instance="1").click()  # which means the first instance with text "Add new"
    
    ##However, uiautomator provides list like methods to use it.
    ## get the count of views with text "Add new" on current screen
    #print d(text="8").count
    #
    ## same as count property
    #print len(d(text="8"))
    #
    ## get the instance via index
    ##d(text="8")[0].click()
    ##d(text="8")[1].click()
    
    # iterator
    for view in d(text="8"):
        print view.info  # ...
    #Notes: when you are using selector like a list, you must make sure the screen keep unchanged, else you may get ui not found error.

#Get the selected ui object status and its information
#Check if the specific ui object exists
#debug in calculator app
def use_status():
    print d(text="8").exists # True if exists, else False
    print d.exists(text="8") # alias of above property.
    
    #Retrieve the info of the specific ui object
    print d(text="8").info
    #Below is a possible result:
    #{ u'contentDescription': u'',
    #  u'checked': False,
    #  u'scrollable': False,
    #  u'text': u'Settings',
    #  u'packageName': u'com.android.launcher',
    #  u'selected': False,
    #  u'enabled': True,
    #  u'bounds': {u'top': 385,
    #              u'right': 360,
    #              u'bottom': 585,
    #              u'left': 200},
    #  u'className': u'android.widget.TextView',
    #  u'focused': False,
    #  u'focusable': True,
    #  u'clickable': True,
    #  u'chileCount': 0,
    #  u'longClickable': True,
    #  u'visibleBounds': {u'top': 385,
    #                     u'right': 360,
    #                     u'bottom': 585,
    #                     u'left': 200},
    #  u'checkable': False
    #}
    
    #Set/Clear text of editable field
    #d(text="Settings").clear_text()  # clear the text
    #d(text="Settings").set_text("My text...")  # set the text
    
#Perform the click action on the seleted ui object
#Perform click on the specific ui object
#debug in calculator app
def use_click():
   # click on the center of the specific ui object
   d(text="8").click()
   # click on the bottomright corner of the specific ui object
   d(text="8").click.bottomright() #"tl", "topleft", "br", "bottomright"
   # click on the topleft corner of the specific ui object
   d(text="8").click.topleft() #"tl", "topleft", "br", "bottomright"
   # click and wait until the new window update
   d(text="8").click.wait()
   
   #Perform long click on the specific ui object
   # long click on the center of the specific ui object
   d(text="8").long_click()
   # long click on the bottomright corner of the specific ui object
   d(text="8").long_click.bottomright() #"tl", "topleft", "br", "bottomright"
   # long click on the topleft corner of the specific ui object
   d(text="8").long_click.topleft() #"tl", "topleft", "br", "bottomright"

#Gesture action for the specific ui object
def use_gesture():
    #Drag the ui object to another point or ui object
    # notes : drag can not be set until Android 4.3.
    # drag the ui object to point (x, y)
    d(text="Settings").drag.to(x, y, steps=100)
    # drag the ui object to another ui object(center)
    d(text="Settings").drag.to(text="Clock", steps=50)
    
    #Swipe from the center of the ui object to its edge
    #Swipe supports 4 directions:
    #left
    #right
    #top
    #bottom
    d(text="Settings").swipe.right()
    d(text="Settings").swipe.left(steps=10)
    d(text="Settings").swipe.up(steps=10)
    d(text="Settings").swipe.down()
    
    #Two point gesture from one point to another
    d(text="Settings").gesture((10, 10), (70, 70)) \
                      .to((20, 20), (60, 60))
    
    #Two point gesture on the specific ui object
    #Supports two gestures:
    #In, from edge to center
    #Out, from center to edge
    # notes : pinch can not be set until Android 4.3.
    # from edge to center. here is "In" not "in"
    d(text="Settings").pinch.In(percent=100, steps=10)
    # from center to edge
    d(text="Settings").pinch.Out()
    
    #Wait until the specific ui object appears or gone
    # wait until the ui object appears
    d(text="Settings").wait.exists(timeout=3000)
    # wait until the ui object gone
    d(text="Settings").wait.gone(timeout=1000)
    
    #Perform fling on the specific ui object(scrollable)
    #Possible properties:
    #horiz or vert
    #forward or backward or toBeginning or toEnd
    # fling forward(default) vertically(default) 
    d(scrollable=True).fling()
    # fling forward horizentally
    d(scrollable=True).fling.horiz.forward()
    # fling backward vertically
    d(scrollable=True).fling.vert.backward()
    # fling to beginning horizentally
    d(scrollable=True).fling.horiz.toBeginning(max_swipes=1000)
    # fling to end vertically
    d(scrollable=True).fling.toEnd()
    
    #Perform scroll on the specific ui object(scrollable)
    #Possible properties:
    #horiz or vert
    #forward or backward or toBeginning or toEnd, or to
    # scroll forward(default) vertically(default)
    d(scrollable=True).scroll(steps=10)
    # scroll forward horizentally
    d(scrollable=True).scroll.horiz.forward(steps=100)
    # scroll backward vertically
    d(scrollable=True).scroll.vert.backward()
    # scroll to beginning horizentally
    d(scrollable=True).scroll.horiz.toBeginning(steps=100, max_swipes=1000)
    # scroll to end vertically
    d(scrollable=True).scroll.toEnd()
    # scroll forward vertically until specific ui object appears
    d(scrollable=True).scroll.to(text="Security")
    
    
def use_scroll():
    #d(scrollable=True).scroll.vert.backward()
    #print d(className="android.widget.FrameLayout",instance=1).info
    d(className="android.widget.FrameLayout",index=1).scroll.vert.forward()
    
if __name__ == '__main__':
    #use_info()
    #use_screen()
    #use_key()
    #use_device()
    #use_watcher()
    #use_handler()
    #use_selector2()
    #use_relative()
    #use_instance()
    #use_click()
    #use_gesture()
    use_scroll()
    
