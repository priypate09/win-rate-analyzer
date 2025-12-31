"""
Configuration for win rate analysis
"""

# Data paths
DATA_PATH = "data/"
SQL_SCRIPTS_PATH = "sql_scripts/"

# Analysis settings
MIN_DEALS_FOR_ANALYSIS = 5  # Minimum deals needed for analysis

# Deal size segments (in dollars)
DEAL_SIZE_SEGMENTS = {
    'small': (0, 25000),
    'medium': (25001, 100000),
    'large': (100001, 500000),
    'enterprise': (500001, float('inf'))
}

# Industry categories
INDUSTRIES = [
    'Technology',
    'Healthcare', 
    'Financial Services',
    'Manufacturing',
    'Retail',
    'Other'
]

# Regions
REGIONS = [
    'North America',
    'Europe',
    'Asia Pacific',
    'Latin America'
]