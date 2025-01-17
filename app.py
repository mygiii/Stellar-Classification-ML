import streamlit as st
from data_app import *

st.title('Star Classification')
st.write('This app uses a dataset of stars to classify them into three classes: GALAXY, STAR, QSO')
st.write('The dataset contains 10000 rows and 18 columns')
st.code('df.head()', language='python')
st.dataframe(head)
st.write('The dataset has been cleaned and outliers have been removed')
st.write('15256 outliers have been removed')
st.write('The dataset has been split into training and testing datasets')
st.write('0.67 of the dataset has been used for training and 0.33 for testing')
st.write('The following classifiers have been used:')
st.write('Random Forest Classifier')
st.write('Support Vector Machine Classifier (SVM)')
st.write('XGBoost Classifier (XGB)')
st.write('The following metrics have been used to evaluate the classifiers:')
st.write('Confusion Matrix')
st.write('Classification Report')
st.write('ROC AUC')
st.write('Class Prediction Error')
st.write('The accuracy of the classifiers is as follows:')
st.pyplot(fig)
st.pyplot(f)