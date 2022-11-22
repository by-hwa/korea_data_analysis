import streamlit as st
import data_analysis
import pandas as pd
import numpy as np
import time
import datetime


def get_data():
    df = pd.read_csv('./testdata.csv')
    df.rename(columns={'persionId':'personID'}, inplace=True)
    df.drop(df.columns[0], axis=1, inplace=True)
    personId_lsit = list(set(df['personID']))

    df.set_index(keys=['personID', 'time'], inplace=True, drop=False)
    df.drop('personID', inplace=True, axis=1)

    df['timediff'] = 1

    return df, personId_lsit


def main():
    st.header('Pose Data Analysis')

    df, personId_list = get_data()

    st.write(df)
    st.write(personId_list)

    video = st.empty()


if __name__ == '__main__':
    st.set_page_config(layout='wide', initial_sidebar_state='collapsed')
    main()
