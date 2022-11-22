import streamlit as st
import os
import sys
import pandas as pd
import plotly.express as px
from streamlit_plotly_events import plotly_events
import plotly.graph_objects as go

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from korea_data_streamlit import get_data

names = {0: 'leaning', 1: 'non_use', 2: 'sitting_chair', 3: 'sitting_floor', 4: 'slow_walk', 5: 'standing',
             6: 'walking'}


def scale_5min(df):
    df_list = []
    for i in range(0, df.shape[0], 300):
        df_buffer = [0 for x in range(7)]
        counts = df['class'].iloc[i:i+300].value_counts()
        for count in counts.index:
            df_buffer[count] = int(counts.loc[count])
        df_list.append(df_buffer)

    df_list = pd.DataFrame(df_list, columns=[str(x) for x in range(7)])

    return df_list


def draw_chart(df):
    colors = {0: 'rgba(0,255,255,1.0)', 1: 'rgba(255,0,255,1.0)', 2: 'rgba(255,255,0,1.0)',
              3: 'rgba(0,128,128,1.0)', 4: 'rgba(128,0,128,1.0)', 5: 'rgba(128,128,0,1.0)', 6: 'rgba(128,128,128,1.0)'}

    global names

    fig = go.Figure()

    ticktexts = []
    tickvalues = []
    state_list = []

    for i in range(0, df.shape[0], 60):
        fig.add_trace(go.Bar(
            x=[10], orientation='h', name=df['time'].iloc[i], marker=dict(color=colors[df['class'].iloc[i]],
                                                                          line=dict(color='rgb(248, 248, 249)', width=0)),
        ))

        state_list.append(names[df['class'].iloc[i]])

        if not i//60 % 240:
            ticktexts.append(str(df['time'].iloc[i]))
            tickvalues.append(i//6)

    st.header("환자 Pose 현황")

    fig.update_xaxes(
        ticktext=ticktexts,
        tickvals=tickvalues)

    fig.update_layout(
        xaxis=dict(
            showgrid=True,
            showline=True,
            showticklabels=True,
            zeroline=True,
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=True,
        ),
        autosize=False,
        height=200,
        width=1000,
        barmode='stack',
        paper_bgcolor='rgb(255, 255, 255)',
        plot_bgcolor='rgb(255, 255, 255)',
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False,)

    return fig


def draw_bar_chart(df):
    names = {0: 'leaning', 1: 'non_use', 2: 'sitting_chair', 3: 'sitting_floor', 4: 'slow_walk', 5: 'standing',
             6: 'walking'}

    fig = px.bar(
        df,
        x=df.index,
        y=df.name
    )
    fig.update_layout(
        xaxis=dict(
            showgrid=True,
            showline=True,
            showticklabels=True,
            zeroline=True,
            title=None,
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=True,
            title=None,
        ),
        autosize=False,
        width=1000,
        height=100,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgb(255, 255, 255)',
        plot_bgcolor='rgb(255, 255, 255)',
    )

    ticktexts = []
    tickvalues = []

    for i in range(0, df.size+1, df.size//6):
        tickvalues.append(i)
        if not i:
            ticktexts.append('0:00h')
            continue
        ticktexts.append(str(i//12)+':00h')

    fig.update_xaxes(
        ticktext=ticktexts,
        tickvals=tickvalues)

    return fig


def main():
    global names

    df, personId_list = get_data()

    selected_personId = st.selectbox('조회하실 환자 ID를 선택하세요 !', personId_list)

    selected_df = df.loc[selected_personId]

    st.write(selected_df)

    scaled_df = scale_5min(selected_df)

    for key, value in names.items():
        st.markdown('-----------')
        st.subheader(value)
        st.plotly_chart(draw_bar_chart(scaled_df[f'{key}']), use_container_width=True)


if __name__ == '__main__':
    st.set_page_config(layout='wide', initial_sidebar_state='collapsed')
    main()
