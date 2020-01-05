# python--interactive-program
python期末项目

## python期末项目总结

### URL
1. [放置python flask项目代码url](https://github.com/AylinWasson/python--interactive-program/tree/master/jiaohu)

2. [pythonenwhere web 展示URL](http://aylinwasson.pythonanywhere.com/)

### 文档描述

* HTML文档：

一类是包含合作项目可视化HTML文件，另一类则是放置flask对应页面的HTML。

其中result.html属于第一个页面；鉴于第二页面和第三页面呈现模式一样，因此使用base.html作为基础模板，body部分由page1.html和page2.html两者进行数据传递。

在HTML文件中我设置了可以链接跳转的按钮（通过button和a实现），使用了div对按钮内容进行包裹，并且在第三个页面设置**下拉菜单**改变内容的呈现。

* python文档

我总共设置了4个url:

"/"为主页面，通过按钮可以跳转至第二页面"/second"和第三页面"/third"，其中HTML和可视图的数据传递和交互完成。

在第三页面"/third"中我完成了下拉菜单，利用了字典的读取还有列表，在HTML中使用for循环，通过菜单里面选择的内容完成数据的传递，然后由第四个页面"/thirdone"进行数据的接收和呈现。

* webapp 动作

第一页为首页面，内容中有两个分页面的按钮，点击可分别进入第二页面和第三页面，第二页面和第三页面顶部设置了返回首页面的按钮。

第三页面还设有下拉菜单，可以看到三种分析的选择呈现。
