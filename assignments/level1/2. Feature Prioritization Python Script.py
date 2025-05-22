"""
PRODUCT PUZZLE #2: THE FEATURE PRIORITIZATION MATRIX

Your product team has come up with 6 potential features to implement.
You need to prioritize them based on a simplified RICE score calculation.

For each feature, you have:
- Reach: Estimated number of users impacted per quarter
- Impact: Score from 1-3 (1=low, 2=medium, 3=high)
- Confidence: Percentage (0-100%)
- Effort: Engineer months (higher number = more effort)

RICE score = (Reach * Impact * Confidence) / Effort

Your challenge:
1. Calculate the RICE score for each feature
2. Sort the features by their RICE score (highest to lowest)
3. Group features into priority buckets:
   - Top priority: RICE > 100
   - Medium priority: RICE between 50-100
   - Low priority: RICE < 50
4. Bonus puzzle: If you only have 7 engineer months available this quarter,
   what combination of features would give you the maximum total RICE score?

EXAMPLE:
Feature: Dark Mode
- Reach: 5000 users
- Impact: 1 (low)
- Confidence: 90%
- Effort: 2 engineer months

RICE score = (5000 * 1 * 0.9) / 2 = 2250

This would be categorized as "Top priority" since 2250 > 100
"""

# Feature data
features = [
    {
        "name": "Dark Mode",
        "reach": 5000,
        "impact": 1,
        "confidence": 90,
        "effort": 2
    },
    {
        "name": "Search Functionality",
        "reach": 8000,
        "impact": 3,
        "confidence": 80,
        "effort": 4
    },
    {
        "name": "Notification Center",
        "reach": 6500,
        "impact": 2,
        "confidence": 70,
        "effort": 3
    },
    {
        "name": "Export to CSV",
        "reach": 2000,
        "impact": 2,
        "confidence": 90,
        "effort": 1
    },
    {
        "name": "User Onboarding Flow",
        "reach": 3000,
        "impact": 3,
        "confidence": 60,
        "effort": 3
    },
    {
        "name": "Performance Optimization",
        "reach": 10000,
        "impact": 2,
        "confidence": 80,
        "effort": 5
    }
]

# Your code here to calculate and organize RICE scores
# Remember to convert confidence to decimal (confidence / 100)

# TODO: Calculate RICE score for each feature

# TODO: Sort features by RICE score (highest to lowest)

# TODO: Group features into priority buckets

# BONUS TODO: Find optimal combination of features for 7 engineer months
# Hint: This is a variation of the "Knapsack problem" - you can try a greedy approach first
# (taking highest RICE score per engineer month) or try all possible combinations


# Expected output format:
# Feature name: RICE score (Priority bucket)
# ...
# Optimal feature combination for 7 engineer months: [Feature1, Feature2, ...] with total RICE score of X
