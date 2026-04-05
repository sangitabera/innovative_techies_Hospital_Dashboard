import plotly.express as px

def bed_heatmap(df):
    fig = px.density_heatmap(
        df,
        x="room_id",
        y="ward",
        z="risk_score",
        color_continuous_scale="Reds",
        title="ICU Bed Heatmap"
    )
    return fig


def resource_graph(df):
    fig = px.line(
        df,
        x=df.index,
        y="risk_score",
        title="Resource Consumption Trend"
    )
    return fig


def patient_timeline(df):
    fig = px.scatter(
        df,
        x=df.index,
        y="risk_score",
        color="ward",
        title="Patient Flow Timeline"
    )
    return fig