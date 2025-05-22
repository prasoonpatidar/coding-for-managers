"""
PRODUCT PUZZLE #5: THE A/B TEST ANALYZER

You've run an A/B test on your product's signup page with two variations:
- Control (A): The current signup page
- Variant (B): A new signup page with simplified form fields

You have daily results for both variants over a two-week period.
For each day, you know how many users visited each variant and how many
completed the signup process.

Your challenge:
1. Calculate the daily conversion rate for each variant
2. Calculate the overall conversion rate for each variant
3. Determine if the test reached statistical significance
   (For simplicity, assume statistical significance if the difference
    in overall conversion rates is greater than 1 percentage point)
4. Puzzle element: Detect if there are any anomalies in the data
   (Hint: Look for days with unusual conversion patterns)

Bonus: Visualize the results with print statements to create a simple
ASCII chart of daily conversion rates.

EXAMPLE:
For Day 1:
- Variant A: 68 signups out of 450 visitors = (68/450) * 100 = 15.1%
- Variant B: 75 signups out of 447 visitors = (75/447) * 100 = 16.8%
- Difference: 16.8% - 15.1% = 1.7 percentage points

For an anomaly detection example: 
If most days Variant B outperforms Variant A, but on one particular day 
Variant A suddenly has a higher conversion rate, that would be an anomaly.
"""

# A/B test results - [visitors, signups]
test_results = {
    "Day 1": {"A": [450, 68], "B": [447, 75]},
    "Day 2": {"A": [512, 79], "B": [509, 94]},
    "Day 3": {"A": [488, 73], "B": [492, 88]},
    "Day 4": {"A": [465, 69], "B": [470, 82]},
    "Day 5": {"A": [495, 75], "B": [502, 92]},
    "Day 6": {"A": [329, 49], "B": [341, 59]},
    "Day 7": {"A": [312, 47], "B": [305, 56]},
    "Day 8": {"A": [468, 72], "B": [472, 67]},  # Anomaly hint: lower conversion for B
    "Day 9": {"A": [486, 74], "B": [483, 89]},
    "Day 10": {"A": [502, 76], "B": [506, 93]},
    "Day 11": {"A": [512, 78], "B": [516, 95]},
    "Day 12": {"A": [494, 76], "B": [502, 93]},
    "Day 13": {"A": [521, 79], "B": [529, 97]},
    "Day 14": {"A": [505, 77], "B": [513, 94]}
}

# Your code here to analyze the A/B test

# TODO: Calculate daily conversion rates for each variant

# TODO: Calculate overall conversion rates

# TODO: Determine if the test reached statistical significance

# TODO: Look for anomalies in the data

# TODO (Bonus): Create a simple ASCII chart to visualize the data
# Hint: You can use characters like "|", "-", "*", etc. to create a bar chart


# Expected output format:
# Day X: Variant A: X%, Variant B: X% (Difference: +/-X%)
# ...
# Overall: Variant A: X%, Variant B: X% (Difference: +/-X%)
# Statistical significance: Yes/No
# Anomalies detected: [Your analysis]
#
# Simple ASCII visualization of daily conversion rates
