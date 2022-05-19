from dash import dcc, html, Input, Output, callback
from http import server
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, callback

lazım = pd.read_csv("datasets/tahminlenen.csv")
lazım2 = lazım[lazım["Tahmin"] == 1]

def charts8():
    labels = ['Sistemden Ayrılan', 'Sistemde Kalan']
    values = [lazım[lazım["Tahmin"] == 1].value_counts().count(), lazım[lazım["Tahmin"] == 0].value_counts().count()]

    fig8 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig8.update_layout(
        autosize=True,
        title="Tahminlenen Ayrılma Yüzdesi",
        title_font_color= 'black',
        margin=dict(
            l=50,
            r=50,
            b=50,
            t=50,
            pad=4
        ))
    return fig8

def charts9():
    labels = ['Fransa', 'Almanya','İspanya']
    values = [lazım[(lazım["Germany"] == 0) & (lazım["Spain"] == 0) & (lazım["Tahmin"]==1)].value_counts().count(), 
              lazım[(lazım["Germany"] == 1) & (lazım["Tahmin"] == 1)].value_counts().count(),
              lazım[(lazım["Spain"] == 1) & (lazım["Tahmin"] == 1)].value_counts().count()]

    fig9 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig9.update_layout(
        autosize=True,
        title="Tahminlenen Ayrılanların Ülke Dağılımı",
        title_font_color= 'black',
        margin=dict(
            l=50,
            r=50,
            b=50,
            t=50,
            pad=4
        ))
    fig9.update_traces(marker=dict(colors=['rgb(150, 195, 255)','rgb(202, 52, 51)','rgb(249, 215, 61)']))
    return fig9

def charts0():
    labels = ['Kadın', 'Erkek']
    values = [lazım[(lazım["Gender"] == 0) & (lazım["Tahmin"] == 1)].value_counts().count(), 
              lazım[(lazım["Gender"] == 1) & (lazım["Tahmin"] == 1)].value_counts().count(),]

    fig0 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig0.update_layout(
        autosize=True,
        title="Tahminlenen Ayrılanların Cinsiyet Dağılımı",
        title_font_color= 'black',
        margin=dict(
            l=50,
            r=50,
            b=50,
            t=50,
            pad=4
        ))
    return fig0

def charts12():
    df = lazım
    fig12 = px.histogram(df, x="Year1", color = "Tahmin")
    fig12.update_layout(
            autosize=True,
            bargap=0.2,
            xaxis=dict(tickvals=[2022,2023]),
            title="Tahminlenen Yıllar Bazında Ayrılma",
            title_font_color= 'black',
            xaxis_title_text='Yıllar', 
            yaxis_title_text='Tahmin', 
            margin=dict(
                l=50,
                r=50,
                b=50,
                t=50,
                pad=2
            ))
    return fig12

def charts13():
    fig13 = px.line(lazım2, x='date', y='CreditScore',color ="Tahmin",color_discrete_sequence = ['rgb(236, 0, 0)'])
    fig13.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    fig13.update_layout(
            autosize=True,
            title="Kredi Skoruna Göre Yıllar Bazında Ayrılma",
            xaxis_title_text='Yıllar', 
            yaxis_title_text='Tahmin', 
            title_font_color= 'black',
            margin=dict(
                l=60,
                r=60,
                b=60,
                t=60,
                pad=2,

            ))
    return fig13


def charts14():
    fig14 = px.histogram(lazım, x='date', y='Tahmin',color_discrete_sequence = ['rgb(236, 0, 0)'])

    fig14.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    fig14.update_layout(
            autosize=True,
            title="Tahminlenen Aylık Bazda Ayrılma",
            xaxis_title_text='Yıllar',
            bargap=0.2,
            yaxis_title_text='Tahmin', 
            margin=dict(
                l=60,
                r=60,
                b=60,
                t=60,
                pad=4,

        ))
    return fig14

layout = html.Div(className="container", children=[
        
        html.Div(className="app-header", children=[
            html.Span('BANKA MÜŞTERİ KAYBI TAHMİNLEMESİ',className="info"),
            html.Span('Tahminler Sayfası',className="info1"),
            html.Div(
                (html.Img(src=("./assets/img/santander-logo-1.png"), className="logo"))
                ),
            html.Div(dcc.Link('ANALİZLER', href='/page1',className="hrefa")),
        ]),
        
        html.Div(className="content", children=[
            html.Div(className="depo1", children=[
                    html.Br(),
                    html.P('78.75%',className="egitim-dogruluk2"),
                    html.Br(),
                    html.P('Model Eğitim Doğruluğu',className="egitim-dogruluk"),
            ]),
            html.Div(className="depo2", children=[
                    html.Br(),
                    html.P('79.95%',className="test-dogruluk2"),
                    html.Br(),
                    html.P('Model Test Doğruluğu',className="test-dogruluk"),
            ]),
            html.Div(className="depo3", children=[
                html.Br(),
                    html.P('8000 / 2000',className="dagilim2"),
                    html.Br(),
                    html.P('Eğitim / Test Dağılımı',className="dagilim"),
            ]),
            #*******************************************************************************************
            html.Div(className="tahmin1", children=[dcc.Graph(
                style={"height":"35vh", "width":"30vw"},
                id='figure8',
                figure=charts8()
            )]
            ),
            html.Div(className="tahmin2", children=[dcc.Graph(
                style={"height":"35vh", "width":"30vw"},
                id='figure9',
                figure=charts9()
            )]
            ),
            html.Div(className="tahmin3", children=[dcc.Graph(
                style={"height":"35vh", "width":"30vw"},
                id='figure0',
                figure=charts0()
            )]
            ),
            html.Div(className="tahmin4", children=[dcc.Graph(
                style={"height":"45vh", "width":"45vw"},
                id='figure12',
                figure=charts12()
            )]
            ),
            html.Div(className="tahmin5", children=[dcc.Graph(
                style={"height":"38vh", "width":"91.9vw"},
                id='figure13',
                figure=charts13()
            )]
            ),
            html.Div(className="tahmin6", children=[dcc.Graph(
                style={"height":"45vh", "width":"45.9vw"},
                id='figure14',
                figure=charts14()
            )]
            ),
        ]),
            
])

        
     


@callback(
    Output('page-2-display-value', 'children'),
    Input('page-2-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'