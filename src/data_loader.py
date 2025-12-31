"""
Load and prepare sales data from Kaggle dataset
"""
import pandas as pd


def load_sales_data(filepath='data/sales_data_sample.csv'):
    """
    Returns:
        DataFrame with standardized columns
    """
    # Loading the data
    df = pd.read_csv(filepath, encoding='latin-1')
    
    print(f"Loaded {len(df)} records from dataset")
    
    # Creating clean dataset with renamed columns
    df_clean = pd.DataFrame({
        'opportunity_id': df['ORDERNUMBER'].astype(str),
        'customer_name': df['CUSTOMERNAME'],
        'product_line': df['PRODUCTLINE'],
        'deal_size_segment': df['DEALSIZE'],
        'country': df['COUNTRY'],
        'territory': df['TERRITORY'].fillna('Unknown'),
        'order_date': pd.to_datetime(df['ORDERDATE']),
        'sales_amount': df['SALES'],
        'quantity': df['QUANTITYORDERED'],
        'status': df['STATUS']
    })
    
    # Maping status to won/lost
    # Shipped = Won, everything else = Lost
    df_clean['status_clean'] = df_clean['status'].apply(
        lambda x: 'won' if x == 'Shipped' else 'lost'
    )
    
    # Adding time-based fields
    df_clean['year'] = df_clean['order_date'].dt.year
    df_clean['quarter'] = df_clean['order_date'].dt.quarter
    df_clean['month'] = df_clean['order_date'].dt.month
    
    print(f"\nData prepared for analysis:")
    print(f"  Won: {(df_clean['status_clean']=='won').sum()} deals")
    print(f"  Lost: {(df_clean['status_clean']=='lost').sum()} deals")
    print(f"  Overall win rate: {(df_clean['status_clean']=='won').sum() / len(df_clean) * 100:.1f}%")
    
    return df_clean


def get_data_summary(df):
    """Print summary statistics"""
    print("\n" + "="*70)
    print("DATA SUMMARY")
    print("="*70)
    
    total = len(df)
    won = (df['status_clean']=='won').sum()
    
    print(f"\nTotal: {total} orders")
    print(f"Won: {won} ({won/total*100:.1f}%)")
    print(f"Lost: {total-won} ({(total-won)/total*100:.1f}%)")
    
    print(f"\nBy Deal Size:")
    print(df.groupby('deal_size_segment')['status_clean'].value_counts())
    
    print(f"\nBy Product Line:")
    print(df.groupby('product_line')['status_clean'].value_counts().head(10))


if __name__ == "__main__":
    # Test the loader
    df = load_sales_data()
    get_data_summary(df)