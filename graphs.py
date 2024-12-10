import numpy as np
from plotly import graph_objects as go

from data import get_data

from columns import get_label, get_color_info

def construct_scatter(data, group_column, x_axis, y_axes, color, mode='markers'):
    fig = go.Figure()

    use_color = bool(color)

    customdata = data[[group_column, 'hash']].values
    x_axis_static = np.full((len(data), 1), x_axis)
    customdata = np.concatenate([customdata, x_axis_static], axis=1)

    if use_color:
        customdata = np.concatenate([customdata, data[[color]].values], axis=1)

    for y_axis in y_axes:
        marker = {
            'size': 8,
            'color': data[color] if use_color else None,
            'cmin': data[color].min() if use_color else None,
            'cmax': data[color].max() if use_color else None,
            'colorscale': get_color_info(color)['scale'] if use_color else None,
            'colorbar': dict(title=get_label(color)) if use_color else None,
            'showscale': use_color,
        }

        marker = {key: value for key, value in marker.items() if value is not None}

        hovertemplate=(
            '%{customdata[0]}<br>' +
            f'{get_label(x_axis)}: '  + '%{x}<br>' +
            'Count: %{y}<br>'
        )

        if use_color:
            hovertemplate += f'{get_label(color)}: ' + '%{customdata[3]}'

        fig.add_trace(go.Scatter(
            x=data[x_axis],
            y=data[y_axis],
            mode=mode,
            marker=marker,
            name=f'{get_label(y_axis)}',
            hovertemplate=hovertemplate,
            customdata=customdata
        ))

    fig.update_layout(
        title=", ".join([get_label(y_axis) for y_axis in y_axes]),
        xaxis_title=get_label(x_axis),
        yaxis_title='Count',
        height=600,
        legend_orientation='h'
    )

    return fig

def construct_time_series(data, group_column, x_axis, y_axes, color):
    return construct_scatter(data, group_column, x_axis, y_axes, color, mode='lines')

def construct_bar(data, group_column, x_axis, y_axes, color):
    fig = go.Figure()

    use_color = bool(color)

    customdata = data[[group_column, 'hash']].values
    x_axis_static = np.full((len(data), 1), x_axis)
    customdata = np.concatenate([customdata, x_axis_static], axis=1)

    if use_color:
        customdata = np.concatenate([customdata, data[[color]].values], axis=1)

    for y_axis in y_axes:
        marker = {
            'color': data[color] if use_color else None,
            'cmin': data[color].min() if use_color else None,
            'cmax': data[color].max() if use_color else None,
            'colorscale': get_color_info(color)['scale'] if use_color else None,
            'colorbar': dict(title=get_label(color)) if use_color else None,
            'showscale': use_color,
        }

        marker = {key: value for key, value in marker.items() if value is not None}

        hovertemplate=(
                '%{customdata[0]}<br>' +
                f'{get_label(x_axis)}: '  + '%{x}<br>' +
                'Count: %{y}<br>'
        )

        if use_color:
            hovertemplate += f'{get_label(color)}: ' + '%{customdata[3]}'

        fig.add_trace(go.Bar(
            x=data[x_axis],
            y=data[y_axis],
            text=data[y_axis],
            textposition='auto',
            marker=marker,
            name=f'{get_label(y_axis)}',
            hovertemplate=hovertemplate,
            customdata=customdata
        ))

    fig.update_layout(
        title=", ".join([get_label(y_axis) for y_axis in y_axes]),
        xaxis_title=f'{get_label(x_axis)}',
        yaxis_title='Count',
        height=600,
        legend_orientation='h'
    )

    return fig

def construct_bar_means(grouped_data, x_axis, y_axes, color):
    use_color = bool(color)

    if use_color:
        mean_data = grouped_data.groupby([x_axis], observed=False)[y_axes + [color]].mean().round(1).reset_index()

        customdata = mean_data[[color]].values
    else:
        mean_data = grouped_data.groupby([x_axis], observed=False)[y_axes].mean().round(1).reset_index()

    fig = go.Figure()

    for y_axis in y_axes:
        marker = {
            'color': mean_data[color] if use_color else None,
            'cmin': mean_data[color].min() if use_color else None,
            'cmax': mean_data[color].max() if use_color else None,
            'colorscale': get_color_info(color)['scale'] if use_color else None,
            'colorbar': dict(title=f'Mean of {get_label(color)}') if use_color else None,
            'showscale': use_color,
        }

        marker = {key: value for key, value in marker.items() if value is not None}

        hovertemplate = (
            f'{get_label(x_axis)}: ' + '%{x}<br>' +
            'Mean: %{y}<br>'
        )

        if use_color:
            hovertemplate += f'Mean of {get_label(color)}: ' + '%{customdata[0]}'

        fig.add_trace(go.Bar(
            x=mean_data[x_axis],
            y=mean_data[y_axis],
            text=mean_data[y_axis],
            textposition='auto',
            marker=marker,
            name=f'Mean of {get_label(y_axis)}',
            hovertemplate=hovertemplate,
            customdata=customdata if use_color else None
        ))

    fig.update_layout(
        title=", ".join([f'Mean of {get_label(y_axis)}' for y_axis in y_axes]),
        xaxis_title=f'{get_label(x_axis)}',
        yaxis_title='Mean',
        height=600,
        legend_orientation='h'
    )

    return fig

def construct_box_plot(data, x_axis, y_axes):
    fig = go.Figure()

    data_sorted = data.sort_values(by=x_axis)

    for y_axis in y_axes:
        fig.add_trace(go.Box(
            x=data_sorted[x_axis],
            y=data_sorted[y_axis],
            text=data_sorted[y_axis],
            name=f'{get_label(y_axis)}',
            boxmean=True
        ))
    
    fig.update_layout(
        title=', '.join([get_label(y_axis) for y_axis in y_axes]) + f' Grouped by {get_label(x_axis)}',
        xaxis_title=f'{get_label(x_axis)}',
        yaxis_title='Count',
        height=600,
        legend_orientation='h',
        boxmode='group'
    )

    return fig

def get_graph(data, group_by, graph_type, x_axis, y_axes, color):
    fig = None
    if graph_type == 'time_series':
        fig = construct_time_series(data, group_by, x_axis, y_axes, color)
    elif graph_type == 'scatter':
        fig = construct_scatter(data, group_by, x_axis, y_axes, color)
    elif graph_type == 'bar':
        fig = construct_bar(data, group_by, x_axis, y_axes, color)
    elif graph_type == 'bar_means':
        fig = construct_bar_means(data, x_axis, y_axes, color)
    elif graph_type == 'box':
        fig = construct_box_plot(data, x_axis, y_axes)

    if fig is None:
        fig = go.Figure()

    fig['layout']['uirevision'] = True
    fig['layout']['autosize'] = True

    return fig

def get_graphs(group_by, graph_type, x_axis, y_axes, color):
    data = get_data()

    figs = []
    
    for group in data[group_by].cat.categories:
        grouped_data = data[data[group_by] == group]
        figs.append(get_graph(grouped_data, group_by, graph_type, x_axis, y_axes, color))
    
    return figs