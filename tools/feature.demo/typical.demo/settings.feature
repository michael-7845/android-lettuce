language:zh-CN

特性: 3设置-1修改设置
    将屏幕安全保护设置为"无"、
    启用定时开关机以及
    打开自动旋转屏幕

    @F1
    场景: 1设置屏幕安全保护为无
        1、打开设置:启动活动【"com.android.settings/.Settings"】
        2、在列表中找到"安全"选项:手指纵向滚动框架【className=android.widget.ListView】至文本【"安全"】
        3、进入"安全":点击文本【"安全"】
        4、打开"屏幕锁定方式":点击文本【"屏幕锁定"】
        5、选择锁定方式:点击文本【"无"】
        6、查看修改后的状态:应该可看到文本【"无"】

    @F2
    场景: 2启用定时开关机
        1、打开设置:启动活动【"com.android.settings/.Settings"】
        2、在列表中找到"定时开关机"选项:手指纵向滚动框架【className=android.widget.ListView】至文本【"定时开关机"】
        3、进入定时开关机:点击文本【"定时开关机"】
        4、打开时间为"7:00"的定时开机:点击【text=07:00】右边的【className=android.widget.CheckBox】页面元素
        5、检查定时开机状态:应该可看到页面元素父【className=android.widget.LinearLayout,index=0】自【className=android.widget.CheckBox,checked=true】
        
    @F3
    场景: 3打开自动旋转屏幕
        1、打开设置:启动活动【"com.android.settings/.Settings"】
        2、在列表中找到"显示"选项:手指纵向滚动框架【className=android.widget.ListView】至文本【"显示"】
        3、进入显示设置:点击文本【"显示"】
        4、打开自动旋转屏幕设置:点击【text=自动旋转屏幕】右边的【className=android.widget.CheckBox】页面元素
        5、检查自动旋转屏幕是否被勾选:应该可看到页面元素父【className=android.widget.LinearLayout,index=7】自【className=android.widget.CheckBox,checked=true】