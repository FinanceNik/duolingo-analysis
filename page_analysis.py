from dash import html
import Styles
import data_handler as dh
from dash import dcc


def render_page_content():
    averages_instance = dh.Averages()
    totals_instance = dh.Totals()

    return html.Div(children=[
        html.H1(children='Analysis'),
        html.Hr(),
        html.Div([
            Styles.kpiboxes('Avg. League Score', averages_instance.league(), Styles.colorPalette[0]),
            Styles.kpiboxes('Avg. Monthly Score', averages_instance.monthly(), Styles.colorPalette[0]),
            Styles.kpiboxes('Avg. Yearly Score', averages_instance.yearly(), Styles.colorPalette[0]),
            Styles.kpiboxes('Total Score', totals_instance.total(), Styles.colorPalette[0]),
        ]),
        html.Hr(),
        html.Div([
            dcc.Graph(
                id='Monthly Score',
                figure={'data': [{'x': dh.monthly_score(dh.current_year - 2)[0],
                                  'y': dh.monthly_score(dh.current_year - 2)[1],
                                  'type': 'bar', 'name': f"{dh.current_year - 2}",
                                  'marker': {'color': Styles.colorPalette[2]},
                                  },
                                 {'x': dh.monthly_score(dh.current_year - 1)[0],
                                  'y': dh.monthly_score(dh.current_year - 1)[1],
                                  'type': 'bar', 'name': f"{dh.current_year - 1}",
                                  'marker': {'color': Styles.colorPalette[1]},
                                  },
                                 {'x': dh.monthly_score(dh.current_year - 0)[0],
                                  'y': dh.monthly_score(dh.current_year - 0)[1],
                                  'type': 'bar', 'name': f"{dh.current_year - 0}",
                                  'marker': {'color': Styles.colorPalette[0]},
                                  }
                                 ],
                        'layout': {
                            'title': f'Number of Activities per Month in the past 3 years',
                            'xaxis': {'title': 'Months'},
                            'yaxis': {'title': 'Monthly Duo Score'}}}
            ),
        ], style=Styles.STYLE(100)),
        html.Hr(),
        html.Div([
            dcc.Graph(
                id='Cumulative Score',
                figure={'data': [{'x': dh.cumulative_score_cumsum()[0],
                                  'y': dh.cumulative_score_cumsum()[1],
                                  'type': 'bar', 'name': f"",
                                  'marker': {'color': Styles.colorPalette[2]},
                                  },
                                 ],
                        'layout': {
                            'title': f'Cumulative Monthly Duo Score',
                            'xaxis': {'title': 'Months'},
                            'yaxis': {'title': 'Monthly Duo Score'}}}
            ),
        ], style=Styles.STYLE(100)),
        # html.Div([
        #     Styles.kpiboxes('',
        #                     '',
        #                     Styles.colorPalette[0]),
        # ]),
    ])

