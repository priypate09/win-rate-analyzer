"""
Calculate win rates by different segments
"""
import pandas as pd
import numpy as np


def calculate_win_rate_by_segment(df, segment_column):
    """
    Calculate win rate for each value in a segment
    
    Args:
        df: DataFrame with sales data
        segment_column: Column name to group by
        
    Returns:
        DataFrame with win rate analysis by segment
    """
    results = []
    
    for segment in df[segment_column].unique():
        segment_df = df[df[segment_column] == segment]
        
        total_deals = len(segment_df)
        won_deals = (segment_df['status_clean'] == 'won').sum()
        lost_deals = (segment_df['status_clean'] == 'lost').sum()
        
        win_rate = (won_deals / total_deals * 100) if total_deals > 0 else 0
        
        total_revenue = segment_df[segment_df['status_clean']=='won']['sales_amount'].sum()
        avg_deal_size = segment_df[segment_df['status_clean']=='won']['sales_amount'].mean()
        
        results.append({
            'segment': segment,
            'total_deals': total_deals,
            'won': won_deals,
            'lost': lost_deals,
            'win_rate_pct': round(win_rate, 1),
            'total_revenue': round(total_revenue, 2),
            'avg_deal_size': round(avg_deal_size, 2) if not pd.isna(avg_deal_size) else 0
        })
    
    result_df = pd.DataFrame(results)
    return result_df.sort_values('win_rate_pct', ascending=False)


def calculate_overall_win_rate(df):
    """Calculate overall win rate"""
    total = len(df)
    won = (df['status_clean'] == 'won').sum()
    lost = (df['status_clean'] == 'lost').sum()
    
    return {
        'total_deals': total,
        'won': won,
        'lost': lost,
        'win_rate_pct': round((won / total * 100), 1) if total > 0 else 0
    }


def calculate_win_rate_by_time(df):
    """Calculate win rate trends over time"""
    results = []
    
    for year in sorted(df['year'].unique()):
        year_df = df[df['year'] == year]
        
        for quarter in sorted(year_df['quarter'].unique()):
            quarter_df = year_df[year_df['quarter'] == quarter]
            
            total = len(quarter_df)
            won = (quarter_df['status_clean'] == 'won').sum()
            win_rate = (won / total * 100) if total > 0 else 0
            
            results.append({
                'year': year,
                'quarter': quarter,
                'period': f"Q{quarter} {year}",
                'total_deals': total,
                'won': won,
                'win_rate_pct': round(win_rate, 1)
            })
    
    return pd.DataFrame(results)


def find_top_performers(df, by_column='product_line', min_deals=10):
    """
    Identify top performing segments
    
    """
    win_rates = calculate_win_rate_by_segment(df, by_column)
    
    # Filter for statistical significance
    win_rates_filtered = win_rates[win_rates['total_deals'] >= min_deals]
    
    return win_rates_filtered.nlargest(5, 'win_rate_pct')


def find_opportunities(df, by_column='product_line', min_deals=10):
    """
    Identify segments with improvement opportunities (low win rates)
    """
    win_rates = calculate_win_rate_by_segment(df, by_column)
    
    # Filter for statistical significance
    win_rates_filtered = win_rates[win_rates['total_deals'] >= min_deals]
    
    return win_rates_filtered.nsmallest(5, 'win_rate_pct')


if __name__ == "__main__":
    from data_loader import load_sales_data
    
    print("Testing win rate analyzer...")
    df = load_sales_data()
    
    print("\nOverall:")
    print(calculate_overall_win_rate(df))
    
    print("\nBy Deal Size:")
    print(calculate_win_rate_by_segment(df, 'deal_size_segment'))
    
    print("\nBy Product Line:")
    print(calculate_win_rate_by_segment(df, 'product_line'))