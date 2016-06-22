language:zh-CN

特性: 2短信-1使用2G卡
针对手机短信功能
使用2G电话卡
进行发送普通短信、发送超长短信以及
删除短信

@F1
场景: 1发送普通短信
1、打开短信应用:启动活动【com.android.mms/com.android.mms.ui.ConversationList】
2、新建信息:点击文本描述【"新信息"】
3、输入收信人号码:在页面元素【resourceId=com.android.mms:id/recipients_editor】添加文本【"15528490093"】
4、输入信息内容:在页面元素【resourceId=com.android.mms:id/embedded_text_editor】添加文本【"test_send_message"】
5、发送信息:点击文本描述【"发送"】
6、返回短信列表:点按物理键【back】【2】次
7、打开短信应用:启动活动【com.android.mms/com.android.mms.ui.ConversationList】@手机2
8、在60秒内应该出现来电字样:在【60000】毫秒内，页面元素【text=test_send_message】应该出现@手机2

    @F2
    场景: 2发送超长短信
    1、打开短信应用:启动活动【com.android.mms/com.android.mms.ui.ConversationList】
    2、新建信息:点击文本描述【"新信息"】
    3、输入收信人号码:在页面元素【resourceId=com.android.mms:id/recipients_editor】添加文本【"15528490093"】
    4、输入信息内容:在页面元素【resourceId=com.android.mms:id/embedded_text_editor】添加文本【"long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging"】
    5、发送信息:点击文本描述【"发送"】
    6、返回短信列表:点按物理键【back】【2】次
    7、打开短信应用:启动活动【com.android.mms/com.android.mms.ui.ConversationList】@手机2
    8、在60秒内应该出现来电字样:在【60000】毫秒内，页面元素【resourceId=com.android.mms:id/subject】应该出现@手机2
    9、打开短信内容:点击页面元素【resourceId=com.android.mms:id/subject】
    10、查看短信显示内容:应该可看到文本【"long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging,long_messaging"】
    
    @F3
    场景: 3删除短信
    1、打开短信应用: 启动活动【com.android.mms/com.android.mms.ui.ConversationList】
    2、新建信息:点击文本描述【"新信息"】
    3、输入收信人号码:在页面元素【resourceId=com.android.mms:id/recipients_editor】添加文本【"13258356197"】
    4、输入信息内容:在页面元素【resourceId=com.android.mms:id/embedded_text_editor】添加文本【"test_delete"】
    5、发送信息:点击文本描述【"发送"】
    6、返回短信列表:点按物理键【back】【2】次
    7、消息列表不为空:等待，文本【"无会话"】应该消失
    8、打开菜单:点按物理键【menu】
    9、选择删除所有会话:点击文本【"删除所有会话"】
    10、点击页面元素【resourceId=android:id/button1】
    11、应该可看到文本【"无会话"】
   
        