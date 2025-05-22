"""
PRODUCT PUZZLE #1: THE CONVERSION FUNNEL MYSTERY

As a product manager for an e-commerce app, you've noticed a drop in 
conversion rates. You have data on how many users reach each step of your 
purchase funnel, but you need to identify where the biggest drop-offs occur.

Your challenge:
1. Calculate the conversion rate between each consecutive step
2. Identify the step with the largest drop-off percentage
3. Calculate the overall funnel conversion rate (from first to last step)
4. Bonus: If we improved the worst-performing step by 20%, what would the 
   new overall conversion rate be?

Step data [step_name, number_of_users]:
- Homepage visits: 45,000 users
- Product page views: 36,750 users
- Add to cart: 12,500 users
- Begin checkout: 5,400 users
- Complete purchase: 3,200 users

EXAMPLE:
For steps with values [100, 50]:
- Conversion rate would be (50/100) * 100 = 50%
- Drop-off rate would be 100% - 50% = 50%
"""

# Step data
funnel_steps = [
    {"name": "Homepage visits", "users": 45000},
    {"name": "Product page views", "users": 36750},
    {"name": "Add to cart", "users": 12500},
    {"name": "Begin checkout", "users": 5400},
    {"name": "Complete purchase", "users": 3200}
]

# Your code here to analyze the funnel data
# HINT: To calculate conversion rate between steps: (current_step_users / previous_step_users) * 100

# Setup to store conversion rates and drop-offs
conversion_rates = []
drop_offs = []

# Setup to find largest drop-off
largest_drop_off_percentage = 0
largest_drop_off_step = 0

# TODO: Loop through the steps to calculate conversion rates between consecutive steps

# TODO: Calculate the overall funnel conversion rate (from first to last step)

# TODO: Find the step with the largest drop-off

# TODO: Calculate new overall conversion rate if worst step improved by 20%


# Expected output format:
# Step 1 to 2: X% conversion (Homepage visits → Product page views)
# ...
# Largest drop-off: X% between Step X and Step Y (Step X → Step Y)
# Overall funnel conversion rate: X%
# If worst step improved by 20%: New overall conversion rate would be X%
