# python--interactive-program
python期末项目

## python期末项目总结

项目题目：**分析“乌托邦式”下冰岛女性婚姻观的形成**

### URL
1. [放置python flask项目代码url](https://github.com/AylinWasson/python--interactive-program/tree/master/jiaohu)

2. [pythonenwhere web 展示URL](http://aylinwasson.pythonanywhere.com/)

### 文档描述

* HTML文档：

一类是包含合作项目可视化HTML文件，另一类则是放置flask对应页面的HTML。

其中result.html属于第一个页面对应“/”主页面，其中我通过设置了可以链接跳转的按钮（通过button和a实现）将两个按钮分别对应第二页面和第三页面，并使用了div对按钮内容进行包裹，使其在同一行呈现；在区别内容程度，我分别用了p,h1,h3进行包裹。
  
鉴于第二页面和第三页面呈现模式相同，因此使用base.html作为基础模板，body部分由page1.html和page2.html两者进行数据传递。

在page2.html中，通过form标签包裹select在第三个页面使用for循环设置**下拉菜单**以此选择内容的呈现；然后使用<input>作为数据的提交按钮，完成页面数据的转换。
  
在所有HTML中都使用了{{ the_title }}此类（jinjia2语法的动态数据绑定，在py文件中有对应的可视化函数传输数据）分别对标题，内容，HTML表格和可视化图表进行数据传递。

* python文档

我总共设置了4个url:"/","/second","/third","/thirdone"

主要导入使用flask，pandas，plotly三个模块

通过pd.pd.read_csv()来读取csv当中的内容，并通过x.to_html()的形式将csv中的内容以HTML表格的形式呈现。

"/"为主页面，通过按钮可以跳转至第二页面"/second"和第三页面"/third"，其中HTML和可视图的数据传递和交互完成；前三个url皆是使用"get"的方式接收数据。

在第四页面"/thirdone"中我使用“post”的接收方式，接收到从“/third”所提交的表单数据，在这个页面中完成了下拉菜单，利用了字典的读取还有列表，，通过菜单里面选择的内容完成数据的传递，然后由第四个页面"/thirdone"进行数据的接收和呈现。

其中the_region = request.form["the_region_selected"]这里的"the_region_selected"对应的是page2.html文档中的select下拉框中的选项；利用with语句打开生成可视化图文件（example1.html），通过数据绑定传输到page2.html当中显示。

data_str = dict[the_region].to_html()，text = texts[the_region]，ending = endings[the_region]，链接通过接收到下拉框中的选项，以字典的方式获得对应的HTML表格（data_str）及小标题文字（text）和看图总结（ending).

* webapp 动作

第一页为首页面介绍**分析“乌托邦式”下冰岛女性婚姻观的形成**下数据故事的背景，引入接下来的分析内容，内容接近结尾处将通过两种情况对内容深入分析，因此设置了两个分页面的按钮（冰岛高生育率和高离婚率）和（冰岛女性社会地位），点击可分别进入第二页面和第三页面。

其中冰岛高生育率和高离婚率和冰岛女性社会地位顶部设置了**返回**的按钮,点击即可回到首页面。

在“冰岛女性社会地位”这个页面下还设有下拉菜单，分别就“冰岛国家会议中妇女参与的比例”，“全球各国女性就业率”和“全球女性的就业比率”可以看到三种分析的选择呈现。
