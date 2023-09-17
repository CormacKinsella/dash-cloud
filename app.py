import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.P("Testing cloud deploy. And this testing an app update.")
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
