import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd
import csv
from data import *

app = dash.Dash()
# tab标签的css
tabs_styles = {'height': '44px'}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',# 选项卡底部的边框样式为1像素宽的实线边框
    'padding': '6px',#设置选项卡的内边距
    'fontWeight': 'bold'
    }
tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
    }

# pd方式读取csv文件
df = pd.read_csv('googleplaystore.csv')
# 获取软件分类列表
available_indicators = df['Category'].unique()
indicator_list=available_indicators.tolist();
indicator_list.insert(0,'ALL')
print(indicator_list)
#每次都要新读
def getfile():
    return csv.reader(open('googleplaystore.csv',
                           encoding='UTF-8'))


app.layout = html.Div(
    [
    html.Div(
        [
        html.Div(
            [
            #category下拉框
            dcc.Dropdown(
                id='category',
                options=[{'label': i, 'value': i} for i in indicator_list],
                value='ALL'
            ),
            #是否要付费选择
            dcc.RadioItems(
                id='price',
                options=[{'label': i, 'value': i} for i in ['Free', 'Paid', 'All']],
                value='All',
                labelStyle={'display': 'inline-block'}
                #使元素可以像内联元素一样水平流动，与周围内容在同一行显示，同时保留块级特性，如能够设置宽度和高度
            )
            ],

        style={'width': '49%', 'display': 'inline-block'}
        ),
        html.Div(
            [
            dcc.Tabs(
                id="tabs",
                children=[
                    #tab1文件大小和数量折线图
                    dcc.Tab(label='Size',
                        style=tab_style,
                        selected_style=tab_selected_style,
                        children=[
                            html.Div(
                                [
                                 # 软件大小折线图
                                dcc.Graph(id='size-graph',animate=True),
                                ],
                                style={'display': 'inline-block','width': '97%','margin-top': '100px'}
                            ),
                        ],
                    ),
                    #tab2收费和数量条状图
                    dcc.Tab(label='Price',
                        style=tab_style,
                        selected_style=tab_selected_style,
                        children=[
                            html.Div(
                                [
                                # 价格条状图
                                dcc.Graph(id='price-graph',animate=False),
                                ],
                                style={'display': 'inline-block','width': '97%','margin-top': '100px'}
                            ),
                        ]
                    ),
                    #tab3人群扇形图
                    dcc.Tab(label='Content Rating',
                        style=tab_style,
                        selected_style=tab_selected_style,
                        children=[
                            html.Div(
                                [
                                  dcc.Graph(id="ratingpeople-graph",animate=False),

                                ],
                                style={'display': 'inline-block','width': '97%','height':'100%','margin-top': '100px'}
                            ),

                        ],
                    ),
                    # tab4评分条状图
                    dcc.Tab(label='Rating Count',
                            style=tab_style,
                            selected_style=tab_selected_style,
                            children=[
                                html.Div(
                                    [
                                        dcc.Graph(id="ratingcount-graph", animate=False),

                                    ],
                                    style={'display': 'inline-block', 'width': '97%', 'height': '100%',
                                           'margin-top': '100px'}
                                ),

                            ],
                            ),
                ]
            ),
            ],
            style={'width': '49%', 'float': 'right','display': 'inline-block'},
            #必须放后面……？
        ),
        ]
    ),
    html.Div(
        [
        dcc.Graph(id="dot-graph",animate=True)
        ],
        style={'width':'49%','display': 'inline-block','margin-left': '20px','margin-top': '100px'}
    )
    ]
)



#下载、评分散点图
@app.callback(
    dash.dependencies.Output('dot-graph', 'figure'),  # 输出 -> main点状图
    [
        dash.dependencies.Input('category', 'value'),  # 输入1 -> 软件分类
        dash.dependencies.Input('price', 'value'),  # 输入2 -> 软件是否收费

    ]
)
def udpate_dotGraph(category_name, price_choice):
    file = getfile()
    newfile = category_price_filter(file, category_name, price_choice)
    [Rating, Installs, App] = get_dot(newfile)

    return {
        'data': [
            go.Scatter(
                x=Rating,      # x轴为评分
                y=Installs,     # y轴为安装数
                text=App,       # 点信息为App的名字
                mode='markers',
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'line': {
                        'width': 0.5,
                        'color': 'white'
                        }
                })],
        'layout':
            go.Layout(
                xaxis={
                    'title': 'Rating',
                    },
                yaxis={
                    'title': 'Installs',
                    },
                margin={
                    'l': 40,
                    'b': 30,
                    't': 10,
                    'r': 0
                    },
                height=450,
                hovermode='closest')
        #图表将根据鼠标的位置自动选择最近的数据点进行悬停效果的展示
        }

# size 折线图 callback
@app.callback(
    dash.dependencies.Output('size-graph', 'figure'),   # 输出 -> size折线图
    [
        dash.dependencies.Input('category', 'value'),   # 输入1 -> 软件分类
        dash.dependencies.Input('price', 'value')       # 输入2 -> 软件是否收费
    ])
def update_sizeGraph(category_name, price_choice):


    # 获取软件大小分类, 软件大小列表
    file=getfile()
    newfile = category_price_filter(file,category_name, price_choice)
    [size_category, size_list] = get_size(newfile)

    return {
        'data': [{
            'x': size_category,     # x轴为软件大小分类
            'y': size_list,         # y轴为软件大小列表
            'type': 'Scatter',
            }],
        'layout':
            go.Layout(
                xaxis={
                    'title': 'Size',
                },
                yaxis={
                    'title': 'AppCount',
                },
                margin={
                    'l': 40,
                    'b': 50,
                    't': 20,
                    'r': 20
                    },
                legend={
                    'x': 0,
                    'y': 1
                    },
                height=450,
                hovermode='closest')
        }



@app.callback(
    dash.dependencies.Output('price-graph', 'figure'),   # 输出 -> 价格图
    [
        dash.dependencies.Input('category', 'value'),   # 输入1 -> 软件分类
        dash.dependencies.Input('price', 'value')       # 输入2 -> 软件是否收费
    ])
def update_priceGraph(category_name, price_choice):

    file = getfile()
    newfile = category_price_filter(file, category_name, price_choice)
    x_list,y_list =get_price(newfile)

    return {
        'data': [{
            "x": x_list,  # x轴为软件价格分类
            "y":y_list,
            'text':y_list,

            'type': 'bar',
            'marker': {
                'color': 'red'  # 设置直方图的颜色
            },
            'xbins':{'size': 0.1}
        }],
        'layout':
            go.Layout(
                xaxis={
                    'title': 'Price/$',
                },
                yaxis={
                    'title': 'AppCount',
                },
                margin={
                    'l': 40,
                    'b': 50,
                    't': 20,
                    'r': 20
                },
                height=450,
                hovermode='closest')
    }

# content rating饼状图 callback
@app.callback(
    dash.dependencies.Output('ratingpeople-graph', 'figure'),     # 输出 -> content rating饼状图
    [
        dash.dependencies.Input('category', 'value'),               # 输入1 -> 软件分类
        dash.dependencies.Input('price', 'value')                   # 输入2 -> 软件是否收费
    ])
def update_ratingpeopleGraph(category_name, price_choice):


    file = getfile()
    newfile = category_price_filter(file, category_name, price_choice)

    rating_category,ratingpeople_list = get_ratingpeople(newfile)

    trace = go.Pie(
        labels=rating_category,     # x轴为应用分级分类
        values=ratingpeople_list,         # y轴为应用分级列表
        )
    return {
        'data': [trace],
        'layout':
            go.Layout(
                margin={
                    'l': 40,
                    'b': 50,
                    't': 20,
                    'r': 0,
                    },
                height=600,
                width=600,
                hovermode='closest')
        }



@app.callback(
    dash.dependencies.Output('ratingcount-graph', 'figure'),   # 输出 -> 价格图
    [
        dash.dependencies.Input('category', 'value'),   # 输入1 -> 软件分类
        dash.dependencies.Input('price', 'value')       # 输入2 -> 软件是否收费
    ])
def update_ratingcountGraph(category_name, price_choice):

    file = getfile()
    newfile = category_price_filter(file, category_name, price_choice)
    xlist,ylist,colorlist =get_ratingcount(newfile)

    return {
        'data': [{
            # "x": list(range(len(ratingcount_list))) ,  # x轴为软件评分分类
            #  "y":ratingcount_list,
            "x": xlist,
            "y":ylist,
            'type': 'bar',
            'marker': {
                'color':colorlist,# 设置直方图的颜色
                #'colorscale': [[0, 'red'], [1, 'blue']],
                #'colorbar':dict(title='Count')#参考图
            },
            'xbins':{'size': 0.1}
        }],
        'layout':
            go.Layout(
                xaxis={
                    'title': 'Rating',
                },
                yaxis={
                    'title': 'AppCount',
                },
                margin={
                    'l': 40,
                    'b': 50,
                    't': 20,
                    'r': 20
                },
                height=450,
                hovermode='closest')
    }


if __name__ == '__main__':
    app.run_server(debug=True, host='localhost')