import numpy as np
import pandas as pd
import streamlit as st
import joblib
import warnings
warnings.filterwarnings('ignore')



df = pd.read_csv('train.csv')


def main():
	st.title("Hackathon")
	
	html_tmp = """
	<div style='background-color:red;'>
	<h2 style = 'color:white;text-align:centre;'> Subscriber Prediction App </h2>
	</div>
	"""
	
	st.markdown(html_tmp,unsafe_allow_html=True)

	age = st.number_input("Age",min_value=1,max_value=100)
	job = st.selectbox('Type of job:',pd.unique(df['job']))
	marital = st.selectbox('Marital Status:',pd.unique(df['marital']))
	education = st.selectbox('Education:',pd.unique(df['education']))
	default = st.selectbox('Default:',pd.unique(df['default']))
	balance = st.number_input("Balance Amount",min_value=0)
	housing = st.selectbox('Has Housing Loan:',pd.unique(df['housing']))
	loan = st.selectbox('Has Personal Loan:',pd.unique(df['loan']))
	contact = st.selectbox('Type of Contact:',pd.unique(df['contact']))
	day = st.number_input("Day",min_value=1,max_value=31)
	month = st.selectbox('Month:',pd.unique(df['month']))
	duration = st.number_input('Duration:',min_value=0)
	campaign = st.number_input('Campaign:',min_value=1,max_value=31)
	pdays = st.number_input('Prev Days:',min_value=0)
	previous = st.number_input('Previous:',min_value=0)
	poutcome = st.selectbox('Prev Campaign Outcome:',pd.unique(df['poutcome']))	

	


if __name__=='__main__':
	main()
