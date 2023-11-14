from dash import html
from dash import dash_table

greys = ['#2b2b2b', '#ce82ff', '#cfcfcf', '#f0f0f0']

colorPalette = {
    0: ['#58cc02', '#ffc200', '#ce82ff', '#ffffff'],  # Duolingo's official colors
 }


colorPalette = colorPalette[0]

strongGreen = '#37D151'
strongRed = '#FF5B5B'

graph_padding = '5px'

HEIGHT = 250

boxshadow = '5px 4px 5px 5px lightgrey'

TAB_STYLE = {'boxShadow': boxshadow,
                      'borderStyle': '',
                      'borderColor': greys[2],
                      'fontSize': '20px',
                      'color': greys[2],
                      "backgroundColor": greys[0],
                      'borderRadius': '15px'}

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "12em",
    "padding": "2rem 1rem",
    "backgroundColor": greys[0],
    'color': greys[2],
    'fontSize': '23px',
    'boxShadow': '5px 5px 5px 5px lightgrey'}

CONTENT_STYLE = {"marginLeft": "18rem", "marginRight": "2rem", "padding": "2rem 1rem"}


def STYLE(width):
    return{'width': f'{width}%', 'display': 'inline-block', 'align': 'center', 'padding': '10px',
             'boxShadow': boxshadow,
             'borderRadius': '10px',
             'overflow': 'hidden'}


def STYLE_PIE(width):
    return{'width': f'{width}%', 'display': 'inline-block', 'align': 'center', 'padding': '10px',
           'boxShadow': boxshadow,
           'height': '30vh',
           'borderRadius': '10px',
           'overflow': 'hidden'}


def STYLE_MINI():
    return{'width': '15%', 'display': 'inline-block', 'align': 'right', 'padding': '1px',
           'boxShadow': boxshadow,
           'borderRadius': '10px',
           'overflow': 'hidden',
           'height': 250}


def FILLER():
    return{'width': '2%', 'display': 'inline-block', 'align': 'right', 'padding': '5px'}


def kpiboxes(id, formula, color):
    return html.Div([
        dash_table.DataTable(
            id='kpi_table_TV',
            columns=[{'name': id, 'id': id}],
            style_cell_conditional=[],
            style_as_list_view=False,
            style_cell={'padding': '10px', 'textAlign': 'left'},
            style_header={'fontSize': '18px',
                          'border': '1px solid white',
                          'backgroundColor': color,
                          'fontWeight': 'bold',
                          'color': 'white'},
            style_data={'border': '1px solid white',
                        'backgroundColor': color,
                        'color': 'white',
                        'fontSize': '22px'},
            style_table={'border': '1px solid lightgrey',
                         'borderRadius': '10px',
                         'overflow': 'hidden',
                         'boxShadow': '5px 4px 5px 5px lightgrey'},
            data=[{id: formula}]
        )], style={'width': '25%', 'display': 'inline-block', 'align': 'left', 'padding': "20px"})


def conditional_box(id, formula):
    return html.Div([
        dash_table.DataTable(
            id='kpi_table_TV',
            columns=[{'name': id, 'id': id}],
            style_cell_conditional=[],
            style_as_list_view=False,
            style_cell={'padding': '10px', 'textAlign': 'left'},
            data=[{id: formula}],
            editable=False,
            style_header={'fontSize': '18px',
                          'border': '1px solid white',
                          'backgroundColor': colorPalette[0],
                          'fontWeight': 'bold',
                          'color': 'white'},
            style_data={'border': '1px solid white',
                        'backgroundColor': colorPalette[0],
                        'color': 'white',
                        'fontSize': '22px'},
            style_table={'border': '1px solid lightgrey',
                         'borderRadius': '10px',
                         'overflow': 'hidden',
                         'boxShadow': '5px 4px 5px 5px lightgrey'},
            style_data_conditional=[{'if': {'filter_query': f'{{{id}}} <= 0',
                                            'column_id': f'{id}'},
                                     'backgroundColor': strongRed, 'color': 'black'},
                                    {'if': {'filter_query': f'{{{id}}} > 0',
                                            'column_id': f'{id}'},
                                     'backgroundColor': strongGreen, 'color': 'black'},
                                    ]

        )], style={'width': '25%', 'display': 'inline-block', 'align': 'left', 'padding': "20px"})


white_button_style = {'background-color': colorPalette[0],
                      'color': 'black',
                      'height': '50px',
                      'width': '100px',
                      'margin-top': '50px',
                      'margin-left': '50px'}
