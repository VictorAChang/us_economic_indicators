import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

# Streamlit App
st.set_page_config(page_title="Economic Indicators Dashboard", layout="wide")
st.title("Economic Indicators Dashboard")
st.markdown("This dashboard provides insights into various economic indicators including exchange rates, GDP, mortgage rates, and wealth distribution. " \
"The Total Public Debt as a percentage of GDP is also calculated to provide a clearer picture of the economic landscape. This indicator is crucial for understanding the fiscal health of a country, as it shows how much of the country's debt is relative to its economic output. The smaller this percentage, the more manageable the debt is in relation to the country's GDP. ")

# Load data from CSV files
exchus = pd.read_csv("data/EXCHUS.csv")
exuseu = pd.read_csv("data/EXUSEU.csv")
gdp = pd.read_csv("data/GDP.csv")
gfdebtn = pd.read_csv("data/GFDEBTN.csv")
mortgage30 = pd.read_csv("data/MORTGAGE30US.csv")
wfrb = pd.read_csv("data/WFRBST01134.csv")

# Merging dataframes into a single dataframe
df = exchus
for other_df in [exuseu, gdp, gfdebtn, mortgage30, wfrb]:
    df = pd.merge(df, other_df, on="observation_date")

# Renaming columns for clarity
# Renaming all columns for clarity
df.rename(columns={
    "EXCHUS": "Exchange Rate (CHN/USD)",
    "EXUSEU": "Exchange Rate (USD/EUR)",
    "GDP": "GDP Billions (USD)",
    "GFDEBTN": "Federal Debt Millions (USD)",
    "MORTGAGE30US": "30-Year Mortgage Rate (%)",
    "WFRBST01134": "Share of Net Worth Held by Top 1%",
    "observation_date": "Date"
}, inplace=True)

# Setting the Date column as the index
df.set_index("Date", inplace=True)

# Changing CHN/USD to USD/CHN for clarity
df["Exchange Rate (USD/CHN)"] = 1/df["Exchange Rate (CHN/USD)"]
df.drop(columns=["Exchange Rate (CHN/USD)"], inplace=True)

# Changing the Federal Debt from Millions to Billions for clarity
# and calculating Total Public Debt as a percentage of GDP
df["Federal Debt Billions (USD)"] = df["Federal Debt Millions (USD)"] / 1000
df.drop(columns=["Federal Debt Millions (USD)"], inplace=True)
df["Total Public Debt as Percentage of GDP (%)"] = (df["Federal Debt Billions (USD)"] / df["GDP Billions (USD)"])*100

# Displaying the dataframe in Streamlit
st.subheader("Economic Indicators Data")
st.dataframe(df)

# Min-Max normalization of Exchange Rates
df["USD/CHN (Normalized)"] = (df["Exchange Rate (USD/CHN)"] - df["Exchange Rate (USD/CHN)"].min()) / (df["Exchange Rate (USD/CHN)"].max() - df["Exchange Rate (USD/CHN)"].min())
df["USD/EUR (Normalized)"] = (df["Exchange Rate (USD/EUR)"] - df["Exchange Rate (USD/EUR)"].min()) / (df["Exchange Rate (USD/EUR)"].max() - df["Exchange Rate (USD/EUR)"].min())

# Min-Max normalization of Debt GDP and Share of Net Worth Held by Top 1%
df["Normalized Total Public Debt as Percentage of GDP (%)"] = (df["Total Public Debt as Percentage of GDP (%)"] - df["Total Public Debt as Percentage of GDP (%)"].min()) / (df["Total Public Debt as Percentage of GDP (%)"].max() - df["Total Public Debt as Percentage of GDP (%)"].min())
df["Normalized Share of Net Worth Held by Top 1%"] = (df["Share of Net Worth Held by Top 1%"] - df["Share of Net Worth Held by Top 1%"].min()) / (df["Share of Net Worth Held by Top 1%"].max() - df["Share of Net Worth Held by Top 1%"].min())


df_normalized = df[["Normalized Total Public Debt as Percentage of GDP (%)", 
          "Normalized Share of Net Worth Held by Top 1%", 
          "USD/CHN (Normalized)", 
          "USD/EUR (Normalized)"]]

# Displaying the normalized dataframe
st.subheader("Normalized Economic Indicators Using Min-Max Normalization")
st.dataframe(df_normalized)

st.markdown("The normalized values are scaled between 0 and 1, allowing for easier comparison across different indicators. This normalization helps in visualizing trends and patterns in the data without the influence of differing scales.")


# Plotting the data
st.markdown("## The following plots visualize the trends in exchange rates for USD/CHN and USD/EUR, as well as the total public debt as a percentage of GDP compared to the share of net worth held by the top 1%.")

fig1 = px.line(df, x=df.index, y=["USD/CHN (Normalized)", "USD/EUR (Normalized)"],
               labels={"value": "Normalized Exchange Rate", "variable": "Exchange Rate"},
               title="Normalized Exchange Rates of USD/CHN and USD/EUR")
st.plotly_chart(fig1)

fig2 = px.line(df, x=df.index, y=["Normalized Total Public Debt as Percentage of GDP (%)", "Normalized Share of Net Worth Held by Top 1%"],
               labels={"value": "Normalized Value", "variable": "Indicator"},
               title="Normalized Total Public Debt as Percentage of GDP and Share of Net Worth Held by Top 1%")
st.plotly_chart(fig2)



