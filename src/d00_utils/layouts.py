from dash import html, dcc
import dash_bootstrap_components as dbc

from d01_data import load_data as data
from d07_visualization import graphs as draw

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

home = html.Div([
    
    dbc.Row([
            
        html.Div(
            dbc.Container([
                html.Span("Coffee, Rice, and Beef Prices over the past 30 Years", className="title"),
                html.P(
                    'Dataset from Kaggle.com containing three commodities over the past 30 years, from Jan 1992 to Jan 2022.'
                ),
                html.Hr(className="my-2"),

                #Index cards of basic info on the data
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardImg(src="../assets/images/coffee.jpg", top=True),
                            dbc.CardBody([
                                html.H4("Coffee", className="card-sub-title"),
                                html.Div([html.P(data.years_between)]),
                                html.Div([html.P("Avg. kilo price: " + '$'+data.price_coffee_avg)]),
                                draw.spark_line(data.df_02_intermediate,'Price_coffee_kilo')
                            ]),
                        ],
                        style={"width": "20rem"},
                        )
                    ],
                    className='gy-5 card-columns mx-auto d-flex justify-content-center',
                    md=4, 
                    ),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardImg(src="../assets/images/rice.jpg", top=True),
                            dbc.CardBody([
                                html.H4("Rice", className="card-sub-title"),
                                html.Div([html.P(data.years_between)]),
                                html.Div([html.P("Avg. kilo price: " + '$'+data.price_rice_avg)]),
                                draw.spark_line(data.df_02_intermediate,'Price_rice_kilo')
                            ]),
                        ],
                        style={"width": "20rem"},
                        )
                    ],        
                    className='gy-5 card-columns mx-auto d-flex justify-content-center',
                    md=4,
                    ),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardImg(src="../assets/images/beef.jpg", top=True),
                            dbc.CardBody([
                                html.H4("Beef", className="card-sub-title"),
                                html.Div([html.P(data.years_between)]),
                                html.Div([html.P("Avg. kilo price: " + '$'+data.price_beef_avg)]),
                                draw.spark_line(data.df_02_intermediate,'Price_beef_kilo')
                            ]),
                        ],
                        style={"width": "20rem"},
                        )
                    ],        
                    className='gy-5 card-columns mx-auto d-flex justify-content-center',
                    md=4,
                    ), 
                ],justify='center', className='g-1'),


                ],
                fluid=True,
                className="py-3",
            ),
            className="p-3 bg-light rounded-3",
        ),

    ],justify='center'),

    
    dbc.Row(dbc.Col([html.Hr()],className='gy-5')),
    
    dbc.Row([
        dbc.Col([
            
            html.Ul(id='', className='', children=[
                html.P('» Clean the table text'),
                html.P('» impl. Pc, radial, pie charts'),
                html.P('» follow the kaggle example'),
                html.P('» add dropdowns to line chart'),
                html.P('» plan for prediction on line chart'),
                html.P('» write a summary')
            ]),
            
            html.Div(id='step1', className='pb-5', children=[
                
                
                html.P('Determine the objectives',className='sub-title'),
                html.P('While this step might not be necessary for this sample project, it is a good practice to learn the process for "real-world" projects.\
                       This step would include discussions with stakeholders, customers, and other key roles that are going to use the results. \
                        Therefore, asking relevant questions is important. The questions will help us understand how to conduct the analysis and \
                        perhaps define the tasks that will be performed. What questions to ask is out of the scope of this project.\
                        But these might be relevant to ask:'
                ),

                html.Ul(id='', className='', children=[
                    html.P('» What problems are the stakeholders trying to solve?'),
                    html.P('» What are their expectations for the solutions?'),
                ]),
                
                html.P('Another important thing to look out for is the expectation(s) for the solutions from the stakeholders. \
                    Therefore, it is important to communicate effectively with the stakeholders and other key people to completely understand\
                    what the underlying challenges are. That being said, my overall goal with this sample project is two-fold:'),
                
                html.Ul(id='', className='', children=[
                    html.P('» to practice data storytelling and experiment with Dash Plotly, and'),
                    html.P('» to practice and experiment with machine learning in scikit-learn.'),
                ]),
                
                html.P('Although, the general goals with analysing this dataset are: ',className=''),
                
                html.Ul(id='', className='', children=[
                    html.P('» explore and understand price variation over the years,'),
                    html.P('» explore seasonal price variation, and'),
                    html.P('» predict future prices for each commodity.'),
                ])
  
            ]),
            
            html.Div(id='step2', children=[
                html.P('Understand the data', className='sub-title'),
                
                html.P('I have downloaded the dataset from Kaggle.com and it is fairly small. Although, it does not matter as the methods implemented\
                    in this project can easily handle larger datasets. The dataset has nine columns.'),
                
                html.P('Columns:', className='text-bold'),
                html.Ul(id='', className='', children=[
                    html.Div(id='', className='', children=[
                        html.Span('Year: ', className='text-bold'),
                        html.Span('The year of commodity price', className=''),
                    ]),
                    html.Div(id='', className='', children=[
                        html.Span('Month: ', className='text-bold'),
                        html.Span('The month of commodity price', className=''),
                    ]),
                    html.Div(id='', className='', children=[
                        html.Span('Price_coffee_kilo: ', className='text-bold'),
                        html.Span('The price of one kilo in $', className=''),
                    ]),
                    html.Div(id='', className='', children=[
                        html.Span('Price_rice_kilo: ', className='text-bold'),
                        html.Span('The price of one kilo in $', className=''),
                    ]),
                    html.Div(id='', className='', children=[
                        html.Span('Price_beef_kilo: ', className='text-bold'),
                        html.Span('The price of one kilo in $', className=''),
                    ]),
                    html.Div(id='', className='', children=[
                        html.Span('Inflation_rate: ', className='text-bold'),
                        html.Span('Rate of inflation during the year, month. This is used to adjust past prices to today\'s scale', className=''),
                    ]),
                    html.Div(id='', className='', children=[
                        html.Span('Price_coffee_infl: ', className='text-bold'),
                        html.Span('The price of one kilo in $, adjusted for inflation', className=''),
                    ]),
                    html.Div(id='', className='', children=[
                        html.Span('Price_rice_infl: ', className='text-bold'),
                        html.Span('The price of one kilo in $, adjusted for inflation', className=''),
                    ]),
                    html.Div(id='', className='', children=[
                        html.Span('Price_beef_infl: ', className='text-bold'),
                        html.Span('The price of one kilo in $, adjusted for inflation', className=''),
                    ]),
                    
                ])
                
            ]),
            
            html.Div(id='step3', children=[
                html.P('Choose the graphs', className='sub-title'),
                
                html.Div(id='', className='', children=[
                    html.Span(id='', className='', children=[
                        'This step is crucial as it will make it easier to find insight, given that the "correct" graph is chosen. \
                        For this simple project I will only focus on '
                    ]),
                    html.Span(id='', className='text-bold', children=['general overview, correlations, and comparisons'])
                ]),
                
                dbc.Row([dbc.Col([draw.choose_graph_table()],md=12, className='gy-5 pb-5')], justify='start')
                
            ]),
            
            html.Div(id='step4', children=[
                html.P('Visual exploration', className='sub-title')
            ]),
            
            html.H5(id='', className='', children='Overview:'),
            
            dbc.Card(
                dbc.CardBody([
                    draw.line_chart(data.df_02_intermediate_mean),
                ]),
                className="mb-3",
            ),
            dbc.Card(
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            dcc.Dropdown(
                                id='bubble_chart_select_year',
                                placeholder='Select a year',
                                value=['All'],
                                options=[{'label': i, 'value': i} for i in data.year_all], 
                                multi=True
                            ),
                        ],md=4),
                        dbc.Col([
                            dcc.Dropdown(
                                id='bubble_chart_select_commodity',
                                placeholder='Select a commodity',
                                value='Price_coffee_kilo',
                                options=[{'label': i, 'value': str(i)} for i in data.commodity_all], 
                                multi=False
                            ),
                        ],md=4),
                        dbc.Col([
                            dcc.Dropdown(
                                id='bubble_chart_select_commodity_infl',
                                placeholder='Select a commodity infl',
                                value='Price_coffee_infl',
                                options=[{'label': i, 'value': str(i)} for i in data.commodity_all_infl], 
                                multi=False
                            ),
                        ],md=4)
                    ]),
                    dcc.Graph(id='bubble_chart'),
                ]),
                className="mb-3",
            ),
            html.H5(id='', className='', children='Correlation:'),
            dbc.Card(
                dbc.CardBody([
                ]),
                className="mb-3",
            ),

        ], className='gy-5') # vertical gutter
    ],)
])

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
page_not_found = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    # If the user tries to reach a different page, return a 404 message
                    html.H1("404: Not found", className="text-danger"),
                    html.Hr(),
                    html.P(f"The pathname was not recognised..."),
                ])
            )

        ],className='gy-2')
    ])
])