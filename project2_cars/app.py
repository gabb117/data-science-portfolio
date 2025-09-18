import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

# Page settings
st.set_page_config(page_title="Auto Dashboard 2025", layout="wide")

# Load dataset
data = pd.read_csv("data/cars_dataset.csv")

st.title("🚗 Auto Dashboard 2025")

# Show dataset preview
st.subheader("Dataset Preview")
st.dataframe(data.head())

# Sidebar filters
st.sidebar.header("Filters")
companies = st.sidebar.multiselect("Select Company", options=data["Company Names"].unique(), default=data["Company Names"].unique())
fuel_types = st.sidebar.multiselect("Select Fuel Type", options=data["Fuel Types"].unique(), default=data["Fuel Types"].unique())

# Apply filters
filtered_data = data[(data["Company Names"].isin(companies)) & (data["Fuel Types"].isin(fuel_types))]

st.subheader("Filtered Data")
st.dataframe(filtered_data)

# Visualization 1: Price distribution
st.subheader("Car Price Distribution")
fig, ax = plt.subplots(figsize=(12, 4), dpi=100)
sns.histplot(filtered_data["Cars Prices"], bins=15, kde=True, ax=ax)
ax.set_xlabel("Price (€)")
ax.set_ylabel("Number of Cars")
# only show max 10 ticks on x axis
ax.xaxis.set_major_locator(plt.MaxNLocator(10))
ax.xaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
plt.tight_layout()
st.pyplot(fig)

# Visualization 2: HorsePower vs Price
st.subheader("HorsePower vs Price")
fig, ax = plt.subplots(figsize=(12, 4), dpi=100)
sns.histplot(filtered_data["HorsePower, Cars Prices"], bins=15, kde=True, ax=ax)
ax.set_xlabel("HorsePower")
ax.set_ylabel("Cars Prices")
st.pyplot(fig)

# Visualization 3: Top speed by company
st.subheader("Average Top Speed per Company")
filtered_data["Total Speed"] = pd.to_numeric(filtered_data["Total Speed"], errors="coerce")

avg_speed = filtered_data.groupby("Company Names")["Total Speed"].mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10, 5))
avg_speed.plot(kind="bar", ax=ax)
plt.ylabel("Average Speed (km/h)")
st.pyplot(fig)