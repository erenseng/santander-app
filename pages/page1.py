from chart_studio import plotly as py
from click import style
from plotly.graph_objs import Scatter, Layout, Figure, Data, Stream, YAxis, Marker
from http import server
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, callback


df = pd.read_csv("datasets/Churn_Modelling.csv")


def charts():
    labels = ['Erkek', 'Kadın']
    values = [df[df["Gender"] == "Male"].value_counts().count(
    ), df[df["Gender"] == "Female"].value_counts().count()]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    fig.update_layout(
        autosize=True,
        title="Cinsiyet Dağılımı",
        title_font_color= 'black',
        margin=dict(
            l=0,
            r=0,
            b=20,
            t=50,
        
        ))
    return fig


def charts2():
    counts, bins = np.histogram(df.Age, bins=range(0, 100, 1))
    bins = 0.5 * (bins[:-1] + bins[1:])

    fig2 = px.bar(x=bins, y=counts, labels={
                  'x': 'Age', 'y': 'count'}, title="Yaş",color_discrete_sequence = ['rgb(236, 0, 0)'])
    fig2.update_layout(
        autosize=True,
        title="Yaş Dağılımı",
        title_font_color= 'black',
        xaxis_color= 'black',
        yaxis_color= 'black',
        xaxis_title_text='Yaş',
        yaxis_title_text='Değer',
        margin=dict(
            l=50,
            r=50,
            b=50,
            t=50,
            pad=4
        ))
    return fig2


def charts3():
    labels = ['Sahip', 'Sahip Değil']
    values = [df[df["HasCrCard"] == 1].value_counts().count(
    ), df[df["HasCrCard"] == 0].value_counts().count()]

    fig3 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig3.update_layout(
        autosize=True,
        title="Kart Kullanımı",
        title_font_color= 'black',
        margin=dict(
            l=0,
            r=0,
            b=20,
            t=50,
            pad=4
        ))
    return fig3

def charts4():
    a = df[df["Geography"]=='France'].value_counts().count()
    b = df[df["Geography"]=='Germany'].value_counts().count()
    c = df[df["Geography"]=='Spain'].value_counts().count()
    py.sign_in('erenseng', '9kUD4aJFmYY0vth2M2SB')
    trace1 = {
      "geo": "geo", 
      "type": "choropleth", 
      "z": [int(a),int(b),int(c)], 
      "showscale": True, 
      "locationmode": "country names", 
      "locations": ["France", "Germany", "Spain"], 
      "autocolorscale": True
    }
    
    data = [trace1]
    layout = {
      "geo": {
        "scope": "europe", 
        "domain": {
          "x": [0, 1], 
          "y": [0, 1]
        }, 
        "lataxis": {"range": [35.0, 70.0]}, 
        "lonaxis": {"range": [-9.0, 38.0]}, 
        "showland": True, 
        "landcolor": "rgb(229, 229, 229)", 
        "showframe": True, 
        "resolution": 50, 
        "countrycolor": "rgb(0, 0, 0)", 
        "coastlinecolor": "rgb(47, 47, 47)", 
        "showcoastlines": True
      }, 
      "title": "Müşterilerin Bulunduğu Ülkeler", 
      "legend": {"traceorder": "reversed"}
    }

    fig4 = Figure(data=data, layout=layout)
    fig4.update_layout(
            autosize=True,
            title="Müşteri Ülke Dağılımı",
            title_font_color= 'black',
            margin=dict(
                l=30,
                r=30,
                b=50,
                t=50,
                pad=4
            ))
    return fig4


layout = html.Div(className="container", children=[
        html.Div(className="app-header", children=[
            html.Span('BANKA MÜŞTERİ KAYBI TAHMİNLEMESİ',className="info"),
            html.Span('Analizler Sayfası',className="info1"),
            html.Div(
                (html.Img(src=("./assets/img/santander-logo-1.png"), className="logo"))
                ),
            html.Div(dcc.Link('TAHMİNLER', href='/page2',className="hrefa")),
        ]),
        
        html.Div(className="content", children=[
            html.Div(className="bar1", children=[
                html.P(round((df.Age.mean())),className="yas-ortalama2"),
                html.Br(),
                html.P('Yaş Ortalaması',className="yas-ortalama"),
            ]
            ),
            html.Div(className="bar2", children=[
                html.P(round((df.Balance.mean())),className="bakiye-ortalama2"),
                html.Br(),
                html.P('Bakiye Ortalaması',className="bakiye-ortalama"),
            ]
            ),
            html.Div(className="bar3", children=[
                html.P(round((df.EstimatedSalary.mean())),className="maas-ortalama2"),
                html.Br(),
                html.P('Maaş Ortalaması',className="maas-ortalama"),
            ]
            ),
            html.Div(className="bar4", children=[
                html.P(round((df.Tenure.mean())),className="yıl-ortalama2"),
                html.Br(),
                html.P('Çalışma Yılı Ortalaması',className="yıl-ortalama"),
            ]
            ),
            html.Div(className="bar5", children=[
                html.P(round((df.CreditScore.mean())),className="kredi-ortalama2"),
                html.Br(),
                html.P('Kredi Skoru Ortalaması',className="kredi-ortalama"),
            ]
            ),


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------



            html.Div(className="div1", children=[dcc.Graph(
                style={"height":"39vh", "width":"33vw"},
                id='figure1',
                figure=charts()
            )]
            ),
            html.Div(className="div2", children=[dcc.Graph(
                style={"height":"56.5vh", "width":"66.7vw"},
                id='figure2',
                figure=charts2()
            )]
            ),
            html.Div(className="div3", children=[dcc.Graph(
                style={"height":"39vh", "width":"32.5vw"},
                id='figure3',
                figure=charts3()
            )]
            ),
            html.Div(className="div4", children=[dcc.Graph(
                style = {'width': '26.1vw','height': '56.5vh'},
                id='figure4',
                figure=charts4()
            )]
            ),
            html.Div([
            dcc.Graph(id="graph",style={'width': '26vw','height': '25vh'}),
            ],className="div5"),
        

           html.Div([
             html.Div(className='name',children=[
                html.P("Değişkenler:",className="degiskenler"),
                dcc.Dropdown(id='names',
                options=['Gender', 'Geography'],
                value='Gender', clearable=False
            )]),
            html.Div(className='value',children=[
                html.P("Değerler:",className="degerler"),
                dcc.Dropdown(id='values',
                options=['HasCrCard', 'IsActiveMember', 'Exited','NumOfProducts'],
                value='HasCrCard', clearable=False
            )]),
            ],className='div6')

            
        ])
        
    ])
    
            



@callback(
    Output("graph", "figure"), 
    Input("names", "value"), 
    Input("values", "value"))
def generate_chart(names, values):
    global df
    df = df
    fig4 = px.pie(df, values=values, names=names, hole=.3)
    fig4.update_layout(
            autosize=True,
            title="Çaprazlamalar",
            title_font_color= 'black',
            margin=dict(
                l=0,
                r=0,
                b=20,
                t=50,
            ))
    return fig4


@callback(
    Output('page-1-display-value', 'children'),
    Input('page-1-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'
