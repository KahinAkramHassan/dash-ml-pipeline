from dash import Input, Output, State, callback
import pandas as pd
import plotly.express as px

from d01_data import load_data as data
from d07_visualization import graphs as draw

# add callback for toggling the collapse on small screens
@callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

#Update the bubble chart
@callback(
    Output('bubble_chart','figure'),
    Input('bubble_chart_select_year','value'),
    Input('bubble_chart_select_commodity','value'),
    Input('bubble_chart_select_commodity_infl','value')
)
def update_bubble_chart(selected_year, selected_commodity, selected_commodity_infl):
    
    if selected_year[0] == 'All':
        df = data.df_02_intermediate
    else:
        df = pd.concat([
            data.df_02_intermediate_grouped.get_group(year) for year in selected_year
        ])

    fig = draw.bubble_chart(df,'Year','Month',selected_commodity,selected_commodity_infl)

    return fig
     
