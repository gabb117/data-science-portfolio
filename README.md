# Data-Science-Portfolio

## Project 1 - Mall Customers Analysis

### 🏬 Objective
This project aims to analyze customer data from a shopping mall to understand patterns in **age, income, and spending habits**. Optionally, **clustering** is performed to segment customers into similar groups.

### 📂 Contents
- `mall_customers_eda.ipynb`: Jupyter Notebook with the full analysis.  
- `data/`: contains the customer dataset (`mall_customers.csv`).  
- `images/`: main visualizations generated during analysis.  

### 🛠 Tools Used
- Python (Pandas, NumPy, Matplotlib, Seaborn)  
- scikit-learn (optional, for KMeans clustering)  
- Jupyter Notebook  

### 📊 Analysis Steps
1. **Data Loading & Cleaning**  
   - Check for missing values.  
   - Inspect data types and descriptive statistics.  

2. **Exploratory Data Analysis (EDA)**  
   - Visualize distributions of Age, Annual Income, and Spending Score.  
   - Scatterplots to explore relationships between income and spending.  
   - Group analysis by gender or age brackets.  

3. **Optional: Clustering (KMeans)**  
   - Segment customers based on Annual Income and Spending Score.  
   - Visualize clusters and centroids to identify customer groups.  

4. **Insights & Conclusions**  
   - Identify trends and patterns in spending behavior.  
   - Highlight customer segments that may be targeted for marketing strategies.  

### 📈 Key Insights 
- Customers with higher annual income tend to spend more, but some moderate-income customers also have high spending scores.  
- Younger customers may have a different spending pattern compared to older ones.  
- Optional clustering can reveal distinct customer segments for targeted marketing.


# Project3_Bank-Transaction-Analysis

This project performs **bank transaction analysis** using Python and Pandas.  
It processes account and transaction data to extract meaningful insights.

## Features

- **Calculate account balance per account**  
  Aggregates all transactions to compute the total balance for each account.

- **Calculate balance per transaction type per account**  
  Groups transactions by `Account` and `Causal` (transaction type) to get subtotals per type.

- **Retrieve operations for a specific branch**  
  Filters transactions for a given branch and returns columns: `Date`, `Amount`, `Causal`, and `Account`.

- **Calculate balance per transaction type per branch**  
  Groups transactions by `Branch` and `Causal` to summarize totals per type for each branch.

- **Identify inactive accounts**  
  Finds accounts with no recorded transactions.

## Data

The project uses two CSV files:

- `accounts.csv` – Bank account details (Account ID, Branch, Account Holder, etc.)  
- `transactions.csv` – Transaction details (Account, Amount, Date, Causal)  

### 🛠 Tools Used
- Python
- Pandas 
- Matplotlib (optional)
