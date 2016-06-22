language:zh-CN
特性: 演示莴苣交互
为了和莴苣交互
作为初学者
我们实现此函数

场景: 点击
# in calculator app
点击页面坐标【540,960】
我想要：点击页面元素右下角【text=8,index=1,enabled=true】
点击页面元素右下角，父【className=android.widget.LinearLayout,index=2】自【index=0,text=1】
点击页面元素右下角，兄【text=1】自【index=2】
点击【text=5】上边的【className=android.widget.Button】页面元素右下角
点击【text=5】下边的【className=android.widget.Button】页面元素右下角
点击【text=5】左边的【className=android.widget.Button】页面元素右下角
点击【text=5】右边的【className=android.widget.Button】页面元素右下角
点击页面元素【text=8,index=1,enabled=true】
点击页面元素，父【className=android.widget.LinearLayout,index=2】自【index=0,text=1】
点击页面元素，兄【text=1】自【index=2】
点击【text=5】上边的【className=android.widget.Button】页面元素
点击【text=5】下边的【className=android.widget.Button】页面元素
点击【text=5】左边的【className=android.widget.Button】页面元素
点击【text=5】右边的【className=android.widget.Button】页面元素
点击页面元素左上角【text=8,index=1,enabled=true】
点击页面元素左上角，父【className=android.widget.LinearLayout,index=2】自【index=0,text=1】
点击页面元素左上角，兄【text=1】自【index=2】
点击【text=5】上边的【className=android.widget.Button】页面元素左上角
点击【text=5】下边的【className=android.widget.Button】页面元素左上角
点击【text=5】左边的【className=android.widget.Button】页面元素左上角
点击【text=5】右边的【className=android.widget.Button】页面元素左上角
# in calllog app
#在可滚动框架【className=android.widget.FrameLayout,index=1】内，点击页面元素【className=android.view.View】且子孙结点含description值【u'\u202d\u202d457\u202c\u202c'】
#在框架【className=android.widget.FrameLayout,index=1】内，点击页面元素【className=android.view.View】且子孙结点含instance序号【15】
#点击可滚动框架【scrollable=true】内的页面元素【text=Accessibility】且其子孙结点含text值【Accessibility】
点击可滚动框架【scrollable=true】内的特征文字【"Date & time"】页面元素

场景: 长按
# in calculator app
#我想要：长按页面元素【text=8,index=1,enabled=true】
#长按页面元素【className=android.widget.EditText】
# in calllog app
#在可滚动框架【className=android.widget.FrameLayout,index=1】内，长按页面元素【className=android.view.View】且子孙结点含text值【u'\u202d\u202d232\u202c\u202c'】
#长按页面元素【className=android.widget.QuickContactBadge,instance=2】
长按页面坐标【540,960】

场景: 快速双击
# in calculator app
#我想要：快速双击页面元素【text=8,index=1,enabled=true】
快速双击页面坐标【540,960】

场景: 物理键和键码
# in calculator app
#我想要，点按物理键【home】
#点按物理键【recent】
#快速双按物理键【home】
点按键码【0x07】

场景: 滑动
#手指向左滑动屏幕
#手指向右滑动屏幕
手指从坐标【0,960】滑动至坐标【1079,960】
#以页面元素【%s】为范围，步长为【%s】手指从右向左滑动

场景: 拖动
#拖动页面元素【text=ZAKER】至坐标【540,960】

场景: 滚动
#手指向上滚动屏幕
以步长【20】手指向下滚动框架【className=android.widget.ListView,instance=0】

场景: 设置
#下载界面结构文件保存为【./tools/layout.xml】
获取界面结构内容

场景: 快速滑动
手指快速向上滑动屏幕
#手指快速向下滑动屏幕
