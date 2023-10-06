import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('/content/DataAnalyst.csv',index_col=0)
job_title=pd.DataFrame(df.groupby('Job Title')['Job Title'].count().sort_values(ascending=False).head(30))
job_industry=pd.DataFrame(df.groupby('Industry')['Industry'].count().sort_values(ascending=False).head(30))
fig_1 = go.Bar(x=job_title.index , y=job_title['Job Title'],name = 'job title')
fig_2 = go.Bar(x=job_industry.index , y=job_industry['Industry'],name="Number of Job Openings by Industry")
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Data Analyst jobs'),
    html.Div(children='''Data Analyst jobs'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [fig_1,fig_2],
            'layout':
            go.Layout(title='Data Analyst')
        })
])
if __name__ == '__main__':
    app.run_server(debug=True)
