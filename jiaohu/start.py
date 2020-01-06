# @Authon:jinlin
from flask import Flask, render_template, request
import pandas as pd
import plotly as py
import plotly.graph_objs as go

app = Flask(__name__)

df = pd.read_csv('The divorce rate.csv',encoding = 'ANSI',index_col=['Name'])
df1 = pd.read_csv('The fertility rate.csv',encoding = 'ANSI',index_col=['Name'])
df2 = pd.read_csv("The proportion of women in the national parliament.csv",encoding='ANSI')
df3 = pd.read_csv("country_female_ployment rate.csv",encoding='ANSI')
df4 = pd.read_csv('country_female_ployment rate1.csv',encoding='ANSI')
py.offline.init_notebook_mode()
regions_available_loaded = ['冰岛国家会议中妇女参与的比例','全球各国女性就业率','全球女性就业比率']
dict1 = {"冰岛国家会议中妇女参与的比例":df2,"全球各国女性就业率":df3,"全球女性就业比率":df4}
texts={"冰岛国家会议中妇女参与的比例":'数据来源-世界银行一是冰岛国家会议中妇女参与的比例数据，二是冰岛女性就业情况数据',"全球各国女性就业率":'全球各国女性就业率---数据来源世界银行中的世界发展指标数据库',"全球女性就业比率":' '}
endings={"冰岛国家会议中妇女参与的比例":'从2001年开始，冰岛女性参与国会人数占比逐渐增加，到2018年时，可以看到将近有超过半数的女士可以参与到国家会议中',"全球各国女性就业率":'从这图中可以看到全球女性就业比率大体呈上升趋势发展',"全球女性就业比率":' 从这图可以看到其中冰岛女性就业率遥遥领先于其他国家，说明在将近半年的时间里，在冰岛有超过70%的女性能够拥有自己的工作。超过半数的冰岛女性能够参与会议，能够在经济发展与政治中起到作用，可见冰岛女性社会地位之高。'}

@app.route('/',methods=['GET'])
def run_one():

    with open("example.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all1 = "".join(f.readlines())

    return render_template('result.html',
                           the_plot_all=plot_all,
                           the_plot_all1=plot_all1,
                           the_title='分析“乌托邦式”下冰岛女性婚姻观的形成'
                           )

@app.route('/second',methods=['GET'])
def run_two():
    冰岛 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['Iceland', :].values, name='Iceland')
    瑞士 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['Switzerland', :].values, name='Switzerland')
    韩国 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['SouthKorea', :].values, name='SouthKorea')
    北欧国家 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['The Nordic countries', :].values, name='The Nordic countries')
    G1 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['Australia', :].values, name='Australia')
    G2 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['Brazil', :].values, name='Brazil')
    G3 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['China', :].values, name='China')
    G4 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['India', :].values, name='India')
    G5 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['France', :].values, name='France')
    G6 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['Germany', :].values, name='Germany')
    G7 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['Italy', :].values, name='Italy')
    G8 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['Japan', :].values, name='Japan')
    G9 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['United States', :].values, name='United States')

    layout = dict(xaxis=dict(rangeselector=dict(buttons=list([
        dict(count=3,
             label="3年",
             step="year",
             stepmode="backward"),
        dict(count=5,
             label="5年",
             step="year",
             stepmode="backward"),
        dict(count=10,
             label="10年",
             step="year",
             stepmode="backward"),
        dict(count=20,
             label="20年",
             step="year",
             stepmode="backward"),
        dict(step="all")
    ])),
        rangeslider=dict(bgcolor="grey"),
        title='年份'
    ),
        yaxis=dict(title='不同地区总离婚率'),
        title="不同地区离婚情况"
    )
    fig = dict(data=[冰岛, 瑞士, 韩国, 北欧国家, G1, G2, G3, G4, G5, G6, G7, G8, G9], layout=layout)
    py.offline.plot(fig, filename="example3.html", auto_open=False)
    with open("example3.html", encoding="utf8", mode="r") as f:
        plot2 = "".join(f.readlines())

    trace_1 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['Iceland', :].values, name='Iceland')

    trace_2 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['United Kingdom', :].values, name='United Kingdom')

    trace_3 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['United States', :].values, name='United States')

    t4 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['Switzerland', :].values, name='Switzerland')
    t5 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['Australia', :].values, name='Australia')
    t6 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['Brazil', :].values, name='Brazil')
    t7 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['China', :].values, name='China')
    t8 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['France', :].values, name='France')
    t9 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['Germany', :].values, name='Germany')
    t10 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['India', :].values, name='India')
    t11 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['Indonesia', :].values, name='Indonesia')
    t12 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['Italy', :].values, name='Italy')
    t13 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['Japan', :].values, name='Japan')
    t14 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['Mexico', :].values, name='Mexico')
    t15 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['Netherlands', :].values, name='Netherlands')
    t16 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['Spain', :].values, name='Spain')

    trace = [trace_1, trace_2, trace_3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16]

    layout = go.Layout(title="冰岛与欧盟国家、世界国家总生育率对比情况")

    figure = go.Figure(data=trace, layout=layout)
    py.offline.plot(figure, filename="example2.html", auto_open=False)
    with open("example2.html", encoding="utf8", mode="r") as f:
        plot1 = "".join(f.readlines())
    data_str2 = df1.to_html()
    data_str1 = df.to_html()
    return render_template('page1.html',
                           the_plot1=plot1,
                           the_plot2=plot2,
                           the_res=data_str1,
                           the_res1=data_str2
                           )
@app.route('/third',methods=['GET'])
def run_three():
    regions_available = regions_available_loaded

    data_str = df2.to_html()
    with open("example4.html", encoding="utf8", mode="r") as f:
        plot = "".join(f.readlines())

    return render_template('page2.html',
                           the_select_region=regions_available,
                           the_res=data_str,
                           the_plot=plot,
                           text='数据来源-世界银行一是冰岛国家会议中妇女参与的比例数据，二是冰岛女性就业情况数据',
                           ending='从2001年开始，冰岛女性参与国会人数占比逐渐增加，到2018年时，可以看到将近有超过半数的女士可以参与到国家会议中'
                           )
@app.route('/thirdone',methods=['POST'])
def run_select() -> 'html':
    the_region = request.form["the_region_selected"]  ## 取得用户交互输入
    print(the_region)

    data_str = dict1[the_region].to_html()
    text = texts[the_region]
    ending = endings[the_region]
    if the_region == "冰岛国家会议中妇女参与的比例":
        with open("example4.html", encoding="utf8", mode="r") as f:
            plot = "".join(f.readlines())
    elif the_region=="全球各国女性就业率":
        with open("example5.html", encoding="utf8", mode="r") as f:
            plot = "".join(f.readlines())
    elif the_region=="全球女性就业比率":
        with open("example6.html", encoding="utf8", mode="r") as f:
            plot = "".join(f.readlines())


    regions_available = regions_available_loaded  # 下拉选单有内容
    return render_template('page2.html',
                           the_plot=plot,
                           the_res=data_str,
                           the_select_region=regions_available,
                           text=text,
                           ending=ending)