import streamlit as st
import seaborn as sns

# Load the "tips" dataset from Seaborn
df = sns.load_dataset("tips")

# Display the dataframe
st.dataframe(df)
