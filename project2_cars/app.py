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
companies = st.sidebar.multiselect(
    "Select Company",
    options=data["Company Names"].unique(),
    default=data["Company Names"].unique()
)
fuel_types = st.sidebar.multiselect(
    "Select Fuel Type",
    options=data["Fuel Types"].unique(),
    default=data["Fuel Types"].unique()
)

# Apply filters
filtered_data = data[(data["Company Names"].isin(companies)) &
                     (data["Fuel Types"].isin(fuel_types))].copy()

# Check if filtered_data is empty
if filtered_data.empty:
    st.warning("⚠️ No data available for the selected filters.")
    st.stop()

# -------------------
# CLEANING COLUMNS
# -------------------

# Clean HorsePower (number at start, followed by space and 'hp')
filtered_data["HorsePower"] = (
    filtered_data["HorsePower"]
    .astype(str)
    .str.extract(r'^(\d+)')    # prende solo il numero all'inizio
)
filtered_data["HorsePower"] = pd.to_numeric(filtered_data["HorsePower"], errors="coerce")

# Clean Total Speed (number at start, ignore letters like 'km/h')
filtered_data["Total Speed"] = (
    filtered_data["Total Speed"]
    .astype(str)
    .str.extract(r'^(\d+)')
)
filtered_data["Total Speed"] = pd.to_numeric(filtered_data["Total Speed"], errors="coerce")

# Drop rows without numeric HorsePower or Total Speed
filtered_data = filtered_data.dropna(subset=["HorsePower", "Total Speed"])

# -------------------
# SHOW FILTERED DATA
# -------------------
st.subheader("Filtered Data")
st.dataframe(filtered_data.head(10))


# -------------------
# VISUALIZATION 1: Price Distribution
# -------------------
st.subheader("Car Price Distribution")
fig, ax = plt.subplots(figsize=(10, 5), dpi=100)
sns.histplot(filtered_data["Cars Prices"], bins=15, kde=True, ax=ax, color="skyblue")
ax.set_xlabel("Price (€)")
ax.set_ylabel("Number of Cars")
ax.xaxis.set_major_locator(plt.MaxNLocator(10))
ax.xaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
ax.yaxis.set_major_locator(plt.MaxNLocator(8))
ax.yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
st.pyplot(fig)

# -------------------
# VISUALIZATION 2: HorsePower vs Price
# -------------------
st.subheader("HorsePower vs Price")
fig, ax = plt.subplots(figsize=(10, 5), dpi=100)
sns.scatterplot(
    data=filtered_data,
    x="HorsePower",
    y="Cars Prices",
    hue="Fuel Types",
    palette="Set2",
    ax=ax
)
ax.set_xlabel("HorsePower")
ax.set_ylabel("Car Price (€)")
ax.set_title("HorsePower vs Price")
st.pyplot(fig)

# -------------------
# VISUALIZATION 3: Average Top Speed per Company
# -------------------
st.subheader("Average Top Speed per Company")
avg_speed = filtered_data.groupby("Company Names")["Total Speed"].mean().sort_values(ascending=False)

if not avg_speed.empty:
    fig, ax = plt.subplots(figsize=(10, 5), dpi=100)
    avg_speed.plot(kind="bar", ax=ax, color="lightcoral")
    ax.set_ylabel("Average Speed (km/h)")
    ax.set_xlabel("Company")
    ax.set_title("Average Top Speed by Company")
    st.pyplot(fig)
else:
    st.warning("No valid 'Total Speed' data available for the selected filters.")