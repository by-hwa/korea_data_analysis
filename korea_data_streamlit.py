import streamlit as st
import data_analysis
import pandas as pd
import numpy as np
import time


def main():
    st.header('Pose Data Analysis')

    col = st.columns(2)

    with col[0]:
        video = st.empty()

    with col[1]:
        st.write("예측값 !")
        st.write(data_analysis.get_predict())

    line_chart1 = st.empty()
    line_chart2 = st.empty()
    line_chart3 = st.empty()

    for i in range(40):
        video.image(f'./test_img/a_{i}.jpg')
        line_chart1.line_chart(pd.DataFrame(np.random.randn(i), columns=['ax']), height=100)
        line_chart2.line_chart(pd.DataFrame(np.random.randn(i), columns=['ay']), height=100)
        line_chart3.line_chart(pd.DataFrame(np.random.randn(i), columns=['az']), height=100)
        time.sleep(1)


if __name__ == '__main__':
    st.set_page_config(layout='wide')
    main()
