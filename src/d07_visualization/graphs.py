#Dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from d01_data import text as description

#Graphics
import plotly.graph_objects as go
import plotly.express as px


def set_fig_margins(*args, **kwargs):
    """
    set_fig_margins takes

    l: left margin
    r: right margin
    b: bottom margin
    t: top margin
    pad: padding
    
    Return: layout.Margin
    """ 
    
    l = kwargs.get('l',None)
    r = kwargs.get('r',None)
    b = kwargs.get('b',None)
    t = kwargs.get('t',None)
    pad = kwargs.get('pad',None)
    
    return go.layout.Margin(l=l,r=r,b=b,t=t,pad=pad) 

def spark_line(df,var):
    """
    spark_line takes

    df: dataframe
    var: variable for x axis (str)
    
    Return: html.Div(dcc.Graph.Sparkline)
    """ 

    return html.Div([
        dcc.Graph(
            id='sparkline_'+var.lower(),
            figure=px.line(
                df[var],
                facet_row_spacing=0.01, 
                height=50, 
                #width=250,
            )
            .update_xaxes(visible=False, fixedrange=True)
            .update_yaxes(visible=False, fixedrange=True)
            .update_layout(
                annotations=[], 
                overwrite=True,
                plot_bgcolor="white",
                margin=set_fig_margins(l=1,r=1,b=1,t=1,pad=0),
                showlegend = False,
            )
            .update_traces(
                hoverinfo='none'
            )
        ), 
    ])
    
   
def line_chart(df):

    '''
    line_chart takes

    df: dataframe
    
    Return: html.Div(dcc.Graph.Line)
    '''

    x_ = df['Year']
    coffee = df['Price_coffee_kilo']
    rice = df['Price_rice_kilo']
    beef = df['Price_beef_kilo']


    return html.Div([
        dcc.Graph(
            id='line_chart',
            figure= go.Figure() 
            .add_trace(
                go.Line(x=x_, y=coffee,
                    mode='lines',
                    name='Coffee')
            )
            .add_trace(
                go.Line(x=x_, y=rice,
                    mode='lines',
                    name='Rice')
            )
            .add_trace(
                go.Line(x=x_, y=beef,
                    mode='lines', 
                    name='Beef')
            )
            .update_layout(
                hovermode='x',
                margin=set_fig_margins(l=50,r=2,b=2,t=30,pad=2),
                plot_bgcolor="white",
                title='Average prices over the years',
                xaxis_title='Years',
                #yaxis_title='Avg. Prices',
                
                xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='rgb(204, 204, 204)',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='rgb(82, 82, 82)',
                    ),
                ),
                yaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='rgb(204, 204, 204)',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='rgb(82, 82, 82)',
                    ),
                ),  
            )
            .update_traces(
                textposition="bottom right",
                marker=dict(
                    opacity=0.9,
                ),
            )
        ),
    ])

def bubble_chart(df,x_axis,y_axis,bubble_size, bubble_color):
    """
    set_fig_margins takes

    df: dataframe
    x_axis: variable for x axis (str)
    y_axis: variable for y axis (str)
    bubble_size: size for the dots (str)
    bubble_color: color for the dots (str)
    
    Return: px.Scatter figure
    """ 
    figure=px.scatter(
        df, 
        x=x_axis,
        y=y_axis,
        size=bubble_size, 
        color=bubble_color,
        color_continuous_scale=px.colors.sequential.Viridis,
    ).update_layout(
        title='',
        yaxis_title='',
        annotations=[], 
        overwrite=True,
        plot_bgcolor="white",
        
        coloraxis_colorbar=dict(
            title=bubble_color.split('_')[2],
            thicknessmode="pixels",
            thickness=20,
        ),
        
        margin=set_fig_margins(l=50,r=2,b=2,t=30,pad=2),
    ).update_traces(
        marker=dict(
            opacity=0.99,
        ),
    )
    
    return figure


def choose_graph_table():
    
    table_header = [
        html.Thead(html.Tr([html.Th("",className='first-child'), html.Th("Graph"), html.Th("Category", className='last-child')]))
    ]

    row1 = html.Tr([html.Td(dbc.CardImg(src="../assets/images/line_chart.png", top=True),style={"width": "5rem"}), html.Td("Line chart: "+description.line), html.Td("Overview")])
    row2 = html.Tr([html.Td(dbc.CardImg(src="../assets/images/bubble_chart.png", top=True),style={"width": "5rem"}), html.Td("Bubble Heatmap: " +description.bubble), html.Td("Overview")])
    row3 = html.Tr([html.Td(dbc.CardImg(src="../assets/images/radial_chart.png", top=True),style={"width": "5rem"}), html.Td("Radial chart: "+description.radial), html.Td("Comparison")])


    table_body = [html.Tbody([row1, row2, row3])]
    
    table = dbc.Table(
        table_header + table_body, 
        bordered=True,
        hover=True,
        responsive=True,
        striped=False,
    )
    
    return table
