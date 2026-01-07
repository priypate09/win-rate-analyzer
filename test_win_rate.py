"""
Simple validation tests
"""
import pandas as pd
from src.win_rate_analyzer import calculate_overall_win_rate, calculate_win_rate_by_segment


def test_win_rate_calculation():
    print("Testing win rate calculation...")
    
    # Creating test data: 3 won out of 5 = 60%
    df = pd.DataFrame({
        'status_clean': ['won', 'won', 'won', 'lost', 'lost']
    })
    
    result = calculate_overall_win_rate(df)
    
    assert result['total_deals'] == 5, "Should have 5 deals"
    assert result['won'] == 3, "Should have 3 won"
    assert result['win_rate_pct'] == 60.0, "Should be 60%"
    
    print("Calculation works correctly")


def test_segment_analysis():
    print("Testing segment analysis...")
    
    df = pd.DataFrame({
        'product': ['A', 'A', 'B', 'B'],
        'status_clean': ['won', 'won', 'won', 'lost'],
        'sales_amount': [100, 200, 150, 150]
    })
    
    result = calculate_win_rate_by_segment(df, 'product')
    
    # Product A should be 100%
    product_a = result[result['segment'] == 'A'].iloc[0]
    assert product_a['win_rate_pct'] == 100.0, "Product A should be 100%"
    
    # Product B should be 50%
    product_b = result[result['segment'] == 'B'].iloc[0]
    assert product_b['win_rate_pct'] == 50.0, "Product B should be 50%"
    
    print("Segment analysis works correctly")


if __name__ == "__main__":
    print("="*60)
    print("Validation Tests - Win Rate Analyzer")
    print("="*60)
    print()
    
    try:
        test_win_rate_calculation()
        test_segment_analysis()
        
        print()
        print("="*60)
        print("✓ All tests passed!")
        print("="*60)
        
    except AssertionError as e:
        print(f"\nTest failed: {e}")
    except Exception as e:
        print(f"\nError: {e}")