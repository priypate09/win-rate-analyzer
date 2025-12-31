"""
Main script to run win rate analysis
"""
from src.data_loader import load_sales_data, get_data_summary
from src.win_rate_analyzer import (
    calculate_overall_win_rate,
    calculate_win_rate_by_segment,
    calculate_win_rate_by_time,
    find_top_performers,
    find_opportunities
)


def main():
    print("="*70)
    print("WIN RATE ANALYSIS")
    print("="*70)
    
    # Load data
    print("\nLoading data...")
    df = load_sales_data()
    
    # Overall summary
    get_data_summary(df)
    
    # Overall win rate
    print("\n" + "-"*70)
    print("OVERALL WIN RATE")
    print("-"*70)
    overall = calculate_overall_win_rate(df)
    print(f"Total: {overall['total_deals']} | Won: {overall['won']} | Lost: {overall['lost']} | Win Rate: {overall['win_rate_pct']}%")
    
    # By deal size
    print("\n" + "-"*70)
    print("BY DEAL SIZE")
    print("-"*70)
    size_analysis = calculate_win_rate_by_segment(df, 'deal_size_segment')
    print(size_analysis.to_string(index=False))
    
    # By product line
    print("\n" + "-"*70)
    print("BY PRODUCT LINE")
    print("-"*70)
    product_analysis = calculate_win_rate_by_segment(df, 'product_line')
    print(product_analysis.to_string(index=False))
    
    # By territory
    print("\n" + "-"*70)
    print("BY TERRITORY")
    print("-"*70)
    territory_analysis = calculate_win_rate_by_segment(df, 'territory')
    print(territory_analysis[territory_analysis['segment'] != 'Unknown'].to_string(index=False))
    
    # Time trends
    print("\n" + "-"*70)
    print("TRENDS OVER TIME")
    print("-"*70)
    time_analysis = calculate_win_rate_by_time(df)
    print(time_analysis.to_string(index=False))
    
    # Top performers
    print("\n" + "-"*70)
    print("TOP PERFORMERS (Min 10 Deals)")
    print("-"*70)
    top_products = find_top_performers(df, 'product_line', min_deals=10)
    print(top_products[['segment', 'total_deals', 'win_rate_pct']].to_string(index=False))
    
    # Opportunities
    print("\n" + "-"*70)
    print("IMPROVEMENT OPPORTUNITIES")
    print("-"*70)
    opportunities = find_opportunities(df, 'product_line', min_deals=10)
    print(opportunities[['segment', 'total_deals', 'win_rate_pct']].to_string(index=False))
    
    print("\n" + "="*70)


if __name__ == "__main__":
    main()