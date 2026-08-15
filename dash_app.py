"""
Real interactive Plotly Dash app for the SpaceX capstone.
Run this in your own environment (needs internet to pip install, and a
local browser to view/screenshot it):
    pip install dash pandas plotly
    python dash_app.py
Then open http://127.0.0.1:8050 in a browser, interact with the
dropdown/slider, and screenshot it for your slides.
"""
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv("falcon9_dataset.csv")

app = Dash(__name__)
app.layout = html.Div([
    html.H2("SpaceX Falcon 9 Launch Dashboard"),
    dcc.Dropdown(
        id="site-dropdown",
        options=[{"label": "All Sites", "value": "ALL"}] +
                [{"label": s, "value": s} for s in df.LaunchSite.unique()],
        value="ALL",
    ),
    dcc.Graph(id="success-pie"),
    dcc.RangeSlider(
        id="payload-slider",
        min=0, max=16000, step=1000,
        marks={i: str(i) for i in range(0, 16001, 4000)},
        value=[0, 10000],
    ),
    dcc.Graph(id="payload-scatter"),
])

@app.callback(Output("success-pie", "figure"), Input("site-dropdown", "value"))
def update_pie(site):
    d = df if site == "ALL" else df[df.LaunchSite == site]
    return px.pie(d, names="LaunchSite" if site == "ALL" else "Class",
                   title="Launches by Site" if site == "ALL" else f"Success vs Failure — {site}")

@app.callback(
    Output("payload-scatter", "figure"),
    Input("site-dropdown", "value"),
    Input("payload-slider", "value"),
)
def update_scatter(site, payload_range):
    d = df if site == "ALL" else df[df.LaunchSite == site]
    d = d[(d.PayloadMass >= payload_range[0]) & (d.PayloadMass <= payload_range[1])]
    return px.scatter(d, x="PayloadMass", y="FlightNumber", color="Class",
                       title="Payload vs Landing Outcome")

if __name__ == "__main__":
    app.run(debug=True)
