"""
PRODUCT PUZZLE #3: THE RETENTION RIDDLE

As a product manager, you're analyzing user retention for different user cohorts.
Each cohort represents users who signed up in a specific month.

The retention_data dictionary shows how many users from each cohort were still
active in subsequent months:
- The dictionary key is the cohort's signup month
- Each value is a list where:
  * The first number is the original cohort size
  * Subsequent numbers show how many users were active in following months

Your challenge:
1. Calculate the retention rate for each cohort over time (as percentages)
2. Find which cohort has the best 3-month retention rate
3. Calculate the average retention rate across all cohorts for each month
4. Puzzle element: Identify any "hidden pattern" in retention behavior
   (Hint: Look for trends based on when users signed up)

EXAMPLE:
For the January cohort: [1200, 840, 650, 540, 445, 380]
- Original cohort size: 1200 users
- Month 1 retention: (840/1200) * 100 = 70.0%
- Month 2 retention: (650/1200) * 100 = 54.2% 
- And so on...

The 3-month retention rate would be the Month 3 percentage (Month 3 users / original users).
"""

# Retention data format: {cohort_month: [initial_users, month_1_users, month_2_users, ...]}
retention_data = {
    "January": [1200, 840, 650, 540, 445, 380],
    "February": [1350, 970, 760, 580, 510],
    "March": [1420, 1065, 820, 640],
    "April": [1520, 1170, 890],
    "May": [1650, 1270],
    "June": [1820]
}

# Your code here to analyze cohort retention

# TODO: Calculate retention rates for each cohort (as percentages)

# TODO: Find the cohort with the best 3-month retention

# TODO: Calculate average retention rates across cohorts for each month

# TODO: Look for any patterns in the data (seasonal effects, improvements over time, etc.)


# Expected output format:
# Cohort: Month 1, Month 2, Month 3...
# January: X%, X%, X%...
# ...
# Best 3-month retention: X cohort with X%
# Average retention rates: Month 1: X%, Month 2: X%...
# Hidden pattern: [Your analysis of any patterns]
