# Win Rate Analyzer

Analyzes sales win rates to figure out which types of deals actually close and which don't.

## What It Does

Takes sales data and breaks down win rates by:
- Deal size (small, medium, large)
- Product type
- Geography
- Time period

Helps sales teams understand what's working and what needs improvement.

## Why I Built This

Most sales ops teams track pipeline but don't analyze patterns in what closes vs what doesn't. This tool makes it easy to spot trends - like maybe large deals in Europe have lower win rates, or certain product lines consistently underperform.

## Setup

Need Python 3.10 or newer.
```bash
# Clone it
git clone https://github.com/priypate09/win-rate-analyzer.git
cd win-rate-analyzer

# Install stuff
pip install pandas numpy scipy

# Run it
python main.py
```

## Data Source

Using a Kaggle sales dataset for now. In a real scenario this would pull from Salesforce or your CRM.

Dataset: https://www.kaggle.com/datasets/kyanyoga/sample-sales-data

Put the CSV in `data/sales_data_sample.csv` and it should work.

## Example Output
```
BY DEAL SIZE
     segment  total_deals  won  lost  win_rate_pct
       Large          157  142    15          90.4
      Medium         1384 1285    99          92.8
       Small         1282 1190    92          92.8

BY PRODUCT LINE
          segment  total_deals  won  lost  win_rate_pct
     Classic Cars          967  928    39          95.9
     Vintage Cars          607  579    28          95.4
      Motorcycles          331  303    28          91.5
```

Shows you right away that Classic Cars have the best win rate while other categories need work.

## Project Structure
```
win-rate-analyzer/
├── src/
│   ├── data_loader.py        # loads the CSV and cleans it up
│   └── win_rate_analyzer.py  # does the actual calculations
├── data/
│   └── sales_data_sample.csv # your data goes here
├── main.py                   # run this to see results
└── requirements.txt
```

Pretty straightforward.

## Use Cases

I built this thinking about:
- Weekly pipeline reviews to see what's trending
- Sales coaching - which reps or product lines need help
- Forecasting - weight different categories based on historical win rates
- Territory planning - where to focus resources

## Notes

This is a learning project I built while working on sales analytics stuff. Code isn't perfect but it works and solves a real problem. Feel free to use it however you want.

## License

MIT