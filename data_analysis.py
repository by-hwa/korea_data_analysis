import streamlit as st
from joblib import load
import numpy as np

RandomForest = load('./RandomForestClassifier.joblib')
AdaBoost = load('./AdaBoostClassifier.joblib')
# Xboost = load('./XBoostingClassifier.joblib')
DecisionTree = load('./DecisionTreeClassifier.joblib')


def get_predict():
    pass