"""
PRODUCT PUZZLE #6: THE CHURN PREDICTION CHALLENGE

As a product manager for a SaaS platform, you've noticed increasing churn rates.
Your customer success team needs a way to identify users at risk of churning so 
they can intervene proactively.

You have behavioral data for each user and need to create a risk scoring system
that combines multiple signals to predict churn likelihood.

Risk Factors:
- Login frequency (last 30 days): 0+ logins
- Feature usage depth (unique features used last month): 0+ features
- Support tickets (last 30 days): 0+ tickets
- Days since last billing issue: 0+ days
- Account age (days): 0+ days

Your challenge:
1. Create a churn risk score for each user (0-100 scale)
2. Categorize users into risk levels: Low (0-30), Medium (31-60), High (61-100)
3. Identify which risk factor has the strongest correlation with high-risk users
4. Puzzle element: Find the optimal intervention threshold - what score should 
   trigger customer success outreach for maximum impact?

EXAMPLE SCORING LOGIC:
User with:
- 2 logins (low activity) = +20 risk points
- 1 feature used (low engagement) = +25 risk points  
- 3 support tickets (high friction) = +30 risk points
- 5 days since billing issue (recent problem) = +15 risk points
- 400 days account age (established user) = -10 risk points
Total Risk Score: 80 (High Risk)

SCORING GUIDELINES:
- Fewer logins = higher risk
- Fewer features used = higher risk  
- More support tickets = higher risk
- Recent billing issues = higher risk
- Newer accounts = slightly higher risk (less committed)
"""

# User behavioral data
users = [
    {
        "user_id": "U001",
        "name": "Alice Chen",
        "logins_30d": 15,
        "features_used": 8,
        "support_tickets": 0,
        "days_since_billing_issue": 90,
        "account_age_days": 245
    },
    {
        "user_id": "U002", 
        "name": "Bob Wilson",
        "logins_30d": 2,
        "features_used": 2,
        "support_tickets": 4,
        "days_since_billing_issue": 3,
        "account_age_days": 12
    },
    {
        "user_id": "U003",
        "name": "Carol Martinez",
        "logins_30d": 8,
        "features_used": 5,
        "support_tickets": 1,
        "days_since_billing_issue": 45,
        "account_age_days": 180
    },
    {
        "user_id": "U004",
        "name": "David Kim",
        "logins_30d": 1,
        "features_used": 1,
        "support_tickets": 2,
        "days_since_billing_issue": 7,
        "account_age_days": 365
    },
    {
        "user_id": "U005",
        "name": "Emma Rodriguez",
        "logins_30d": 22,
        "features_used": 12,
        "support_tickets": 0,
        "days_since_billing_issue": 120,
        "account_age_days": 450
    },
    {
        "user_id": "U006",
        "name": "Frank Thompson",
        "logins_30d": 0,
        "features_used": 0,
        "support_tickets": 1,
        "days_since_billing_issue": 2,
        "account_age_days": 30
    }
]

# Your code here to create the churn risk scoring system

def calculate_churn_risk_score(user):
    """
    Calculate churn risk score for a user based on their behavior
    Returns a score from 0-100 (higher = more likely to churn)
    """
    # TODO: Implement scoring logic based on the risk factors
    # Consider how each factor contributes to churn risk
    # You may want to use different weights for different factors
    
    risk_score = 0
    
    # TODO: Score based on login frequency
    # Hint: Fewer logins = higher risk
    
    # TODO: Score based on feature usage depth  
    # Hint: Fewer features used = higher risk
    
    # TODO: Score based on support tickets
    # Hint: More tickets = higher frustration = higher risk
    
    # TODO: Score based on billing issues
    # Hint: Recent billing problems = higher risk
    
    # TODO: Score based on account age
    # Hint: Very new accounts might be higher risk (less committed)
    
    # Ensure score stays within 0-100 range
    risk_score = max(0, min(100, risk_score))
    return risk_score

def categorize_risk_level(score):
    """
    Categorize risk score into Low, Medium, High buckets
    """
    # TODO: Implement risk categorization
    # Low: 0-30, Medium: 31-60, High: 61-100
    pass

# TODO: Calculate risk scores for all users

# TODO: Categorize users by risk level

# TODO: Identify which factor correlates most with high-risk users

# TODO: Find optimal intervention threshold
# Hint: You might want to look at the distribution of scores and consider
# how many users you can realistically reach out to


# Expected output format:
# User: Alice Chen (U001) - Risk Score: X (Low/Medium/High Risk)
# User: Bob Wilson (U002) - Risk Score: X (Low/Medium/High Risk)
# ...
# 
# Risk Level Distribution:
# Low Risk: X users
# Medium Risk: X users  
# High Risk: X users
#
# Strongest risk factor correlation: [Your analysis]
# Recommended intervention threshold: Score >= X (affects Y users)
