from dash import Dash, dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc

#Local files
from d00_utils import layouts as layout
from d00_utils import callbacks

#create and instantiate the app
app = Dash(
    __name__,
    suppress_callback_exceptions=True, 
    external_stylesheets=[dbc.themes.ZEPHYR], 
    meta_tags=[{
        'name':'viewport',
        'content':'width=device-width, initial-scale=1'}
    ]
)

#The dynamic part of the website.
content = html.Div(id="page-content")
#Set the application layout
app.layout = dbc.Container([dcc.Location(id="url", refresh=True), content], fluid=False)

#>>>>>>>>>>>>>>>>>>
@callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")]
)
def display_page_content(pathname):     
    
    ##############################
    if pathname == "/":
        return layout.home 
    
    ##############################
    if pathname == "/about":
        return layout.about 
    
    #<<<<<<<<<<404>>>>>>>>>>>>
    return layout.page_not_found


#run the server
if __name__ == '__main__':
    app.run_server(port=8052, use_reloader=True)