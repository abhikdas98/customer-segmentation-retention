import pandas as pd

def clean_retail_data(df):
    # 1. Drop missing CustomerID
    df = df.dropna(subset=['CustomerID'])

    # 2. Remove negative quantities
    df = df[df['Quantity'] >= 0]

    # 3. Remove negative unit prices
    df = df[df['UnitPrice'] >= 0]

    # 4. Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['InvoiceDate'])


    # 5. Convert CustomerID to int
    df['CustomerID'] = df['CustomerID'].astype(int)

    #6. Create TotalAmount column
    df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

    print("Data cleaning completed.")
    print(f"Cleaned data shape: {df.shape}")

    return df