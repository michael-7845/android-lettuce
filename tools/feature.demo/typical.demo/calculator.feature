language: zh-CN
特性: 4计算器-1加减乘除
    使用【场景模板】的方式批量完成加减乘除
    
    背景:
        打开计算器:启动活动【"com.android.calculator2/.Calculator"】
    @F1    
    场景模板: 1将两个数相加
        1、点击文本【"<数值_1>"】
        2、点击文本【"<按钮_1>"】
        3、点击文本【"<数值_2>"】
        4、点击文本【"<按钮_2>"】
        4、应该可看到文本【"<结果>"】

    例如:
    | 数值_1 |  按钮_1 | 数值_2  |  按钮_2 |  结果 |
    |   1    |    +    |    2    |    =    |   3   |
    |   5    |    +    |    6    |    =    |   11  |
    |   7    |    +    |    8    |    =    |   15  |
    
    @F2
    场景模板: 2将两个数相减
        1、    点击文本【"<数值_1>"】
        2、点击文本描述【"<按钮_1>"】
        3、    点击文本【"<数值_2>"】
        4、点击文本描述【"<按钮_2>"】
        4、应该可看到文本【"<结果>"】

    例如:
    | 数值_1 |  按钮_1  | 数值_2  |   按钮_2   |  结果 |
    |   5    |    减    |    2    |    等于    |   3   |
    |   7    |    减    |    6    |    等于    |   1   |
    
    @F3
    场景: 3将两个数相乘
        1、点击数字5:点击页面元素【resourceId=com.android.calculator2:id/digit5】
        2、点击运算符X(乘):点击页面元素【resourceId=com.android.calculator2:id/mul】
        3、点击数字3:点击页面元素【resourceId=com.android.calculator2:id/digit3】
        4、点击运算符=(等于):点击页面元素【resourceId=com.android.calculator2:id/equal】
        4、检查结果:应该可看到文本【"15"】
    @F4
    场景: 4将两个数相除
        1、点击数字8:点击页面元素【resourceId=com.android.calculator2:id/digit8】
        2、点击运算符/(除):点击页面元素【resourceId=com.android.calculator2:id/div】
        3、点击数字3:点击页面元素【resourceId=com.android.calculator2:id/digit2】
        4、点击运算符=(等于):点击页面元素【resourceId=com.android.calculator2:id/equal】
        4、检查结果:应该可看到页面元素【className=android.widget.EditText,text=4】
