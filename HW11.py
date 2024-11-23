import pandas as pd






fact_internet_sales = pd.read_csv('C:/Users/maabi/OneDrive/Desktop/New folder/homeworks1/homeworks/fact_internet_sales.csv')
dim_product = pd.read_csv('C:/Users/maabi/OneDrive/Desktop/New folder/homeworks1/homeworks/dim_product.csv')
dim_date = pd.read_csv('C:/Users/maabi/OneDrive/Desktop/New folder/homeworks1/homeworks/dim_date.csv')
dim_customer = pd.read_csv('C:/Users/maabi/OneDrive/Desktop/New folder/homeworks1/homeworks/dim_customer.csv')
dim_currency = pd.read_csv('C:/Users/maabi/OneDrive/Desktop/New folder/homeworks1/homeworks/dim_currency.csv')







# Step 2: Join fact_internet_sales with dim_date to get date-related information
sales_with_date = fact_internet_sales.merge(dim_date, left_on='OrderDateKey', right_on='DateKey', how='inner')


# Step 3: Join sales_with_date with dim_product to get product-related information
sales_with_product = sales_with_date.merge(dim_product, left_on='ProductKey', right_on='ProductKey', how='inner')


# Step 4: Join sales_with_product with dim_customer to get customer-related information
full_data = sales_with_product.merge(dim_customer, left_on='CustomerKey', right_on='CustomerKey', how='inner')


# Step 5: Apply filters based on the requirements
filtered_data = full_data[
    (full_data['EnglishDayNameOfWeek'] == 'Sunday') &  # Filter sales on Sundays
    (full_data['Color'] == 'Silver') &  # Products with color "Silver"
    (full_data['Size'].notna()) &  # Products with size information
    (full_data['Weight'] > 10) &  # Products with weight > 10
    (full_data['YearlyIncome'] > 100000.0) &  # Customers with YearlyIncome > 100,000
    (full_data['TotalChildren'] > 1)  # Customers with more than 1 child
]


# Step 6: Perform aggregations: Total TaxAmt, Average SalesAmount, and Average TotalProductCost
aggregated_data = (
    filtered_data
    .groupby(['CustomerKey', 'FirstName'], as_index=False)
    .agg(
        Total_TaxAmt=('TaxAmt', 'sum'),
        Avg_SalesAmount=('SalesAmount', 'mean'),
        Avg_TotalProductCost=('TotalProductCost', 'mean')
    )
)


# Step 7: Sort by FirstName and drop CustomerKey
result = aggregated_data.sort_values(by='FirstName').drop(columns=['CustomerKey'])


# Step 8: Display the result
print("Sunday Sales Analysis for Silver Products:")
print(result)
