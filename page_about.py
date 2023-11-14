from dash import html


def render_page_content():
    return html.Div(children=[
        html.Div([html.H1('About the Duolingo Analysis Tool...')], style={"textAlign": "left"}),
        html.Hr(),
        html.H2('Empowering Your Language Learning Journey'),
        html.P('This tool was created to help you understand your language learning journey on Duolingo. '),
        html.P('Duolingo is a language learning app that has over 300 million users. It is a free app that allows users to learn over 30 languages.'),
        html.H2('Get Started'),
        html.P('1. Import your Duolingo data by going to the import data section and upload your .csv file.'),
        html.P('2. Explore your language learning insights by going to the dashboard section.'),
        html.P('3. Enjoy!'),
        html.Hr(),

    ], style={"width": "40%", "textAlign": "left"})

