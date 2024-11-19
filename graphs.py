import numpy as np
from plotly import graph_objects as go

from data import get_data

from constants import FLAT_COLUMN_LABELS

def construct_scatter(data, group_column, x_axis, y_axes, mode='markers'):
    fig = go.Figure()

    customdata = data[[group_column, 'hash']].values
    x_axis_static = np.full((len(data), 1), x_axis)
    customdata = np.concatenate([customdata, x_axis_static], axis=1)

    for y_axis in y_axes:
        fig.add_trace(go.Scatter(
            x=data[x_axis],
            y=data[y_axis],
            mode=mode,
            name=f'{FLAT_COLUMN_LABELS[y_axis]}',
            hovertemplate=(
                '%{customdata[0]}<br>' +
                f'{FLAT_COLUMN_LABELS[x_axis]}: '  + '%{x}<br>' +
                'Count: %{y}'
            ),
            customdata=customdata
        ))

    fig.update_layout(
        title=", ".join([FLAT_COLUMN_LABELS[y_axis] for y_axis in y_axes]),
        xaxis_title=FLAT_COLUMN_LABELS[x_axis],
        yaxis_title='Count',
        height=600
    )

    return fig

def construct_time_series(data, group_column, x_axis, y_axes):
    return construct_scatter(data, group_column, x_axis, y_axes, mode='lines+markers')

def construct_bar(data, group_column, x_axis, y_axes):
    fig = go.Figure()

    customdata = data[[group_column, 'hash']].values
    x_axis_static = np.full((len(data), 1), x_axis)
    customdata = np.concatenate([customdata, x_axis_static], axis=1)

    for y_axis in y_axes:
        fig.add_trace(go.Bar(
            x=data[x_axis],
            y=data[y_axis],
            text=data[y_axis],
            textposition='auto',
            name=f'{FLAT_COLUMN_LABELS[y_axis]}',
            hovertemplate=(
                '%{customdata[0]}<br>' +
                'Count: %{y}'
            ),
            customdata=customdata
        ))

    fig.update_layout(
        title=", ".join([FLAT_COLUMN_LABELS[y_axis] for y_axis in y_axes]),
        xaxis_title=f'{FLAT_COLUMN_LABELS[x_axis]}',
        yaxis_title='Count'
    )

    return fig

def construct_bar_means(grouped_data, x_axis, y_axes):
    mean_data = grouped_data.groupby([x_axis], observed=False)[y_axes].mean().reset_index()

    fig = go.Figure()

    for y_axis in y_axes:
        fig.add_trace(go.Bar(
            x=mean_data[x_axis],
            y=mean_data[y_axis],
            text=mean_data[y_axis],
            textposition='auto',
            name=f'Mean of {FLAT_COLUMN_LABELS[y_axis]}',
            hovertemplate=(
                f'{FLAT_COLUMN_LABELS[x_axis]}: ' + '%{x}<br>' +
                'Mean: %{y}'
            ),
        ))

    fig.update_layout(
        title=", ".join([f'Mean of {FLAT_COLUMN_LABELS[y_axis]}' for y_axis in y_axes]),
        xaxis_title=f'{FLAT_COLUMN_LABELS[x_axis]}',
        yaxis_title='Mean'
    )

    return fig

def get_graph(data, group_by, graph_type, x_axis, y_axes):
    fig = None
    if graph_type == 'time_series':
        fig = construct_time_series(data, group_by, x_axis, y_axes)
    elif graph_type == 'scatter':
        fig = construct_scatter(data, group_by, x_axis, y_axes)
    elif graph_type == 'bar':
        fig = construct_bar(data, group_by, x_axis, y_axes)
    elif graph_type == 'bar_means':
        fig = construct_bar_means(data, x_axis, y_axes)

    if fig is None:
        fig = go.Figure()

    fig['layout']['uirevision'] = True
    fig['layout']['autosize'] = True

    return fig

def get_graphs(group_by, graph_type, x_axis, y_axes):
    data = get_data()

    figs = []
    
    for group in data[group_by].unique():
        grouped_data = data[data[group_by] == group]
        figs.append(get_graph(grouped_data, group_by, graph_type, x_axis, y_axes))
    
    return figs