"""
PRODUCT PUZZLE #7: THE FEATURE GAP DISCOVERY

As a product manager for a project management tool, you're conducting competitive 
research to identify market opportunities. You've analyzed 5 major competitors 
and documented which features they offer.

You also have data on how frequently users request certain features in support 
tickets and feedback surveys.

Your challenge:
1. Calculate feature coverage across all competitors (what % of competitors offer each feature)
2. Identify "white space" opportunities - features with high user demand but low competitor coverage
3. Find your unique differentiators - features you offer that most competitors don't
4. Puzzle element: Discover the "golden opportunity" - the feature with the highest 
   opportunity score (high demand + low competition + feasible to implement)

EXAMPLE CALCULATION:
Feature: "Time Tracking"
- Offered by 3 out of 5 competitors = 60% market coverage
- Requested by users 45 times = High demand
- Implementation difficulty: Medium
- Opportunity Score = (User Requests * 2) - (Market Coverage * 100) + Feasibility Bonus
- Opportunity Score = (45 * 2) - (60) + 20 = 50

MARKET COVERAGE CATEGORIES:
- Saturated: 80%+ of competitors offer it
- Competitive: 40-79% of competitors offer it  
- Opportunity: 0-39% of competitors offer it
"""

# Competitor feature matrix (True = they offer this feature)
competitors = {
    "Asana": {
        "Kanban Boards": True,
        "Gantt Charts": True,
        "Time Tracking": False,
        "Custom Fields": True,
        "Automation Rules": True,
        "Advanced Reporting": True,
        "White Labeling": False,
        "API Integration": True,
        "Mobile Offline": False,
        "Video Calls": False,
        "Invoice Generation": False,
        "Resource Planning": True
    },
    "Trello": {
        "Kanban Boards": True,
        "Gantt Charts": False,
        "Time Tracking": False,
        "Custom Fields": True,
        "Automation Rules": True,
        "Advanced Reporting": False,
        "White Labeling": False,
        "API Integration": True,
        "Mobile Offline": True,
        "Video Calls": False,
        "Invoice Generation": False,
        "Resource Planning": False
    },
    "Monday.com": {
        "Kanban Boards": True,
        "Gantt Charts": True,
        "Time Tracking": True,
        "Custom Fields": True,
        "Automation Rules": True,
        "Advanced Reporting": True,
        "White Labeling": True,
        "API Integration": True,
        "Mobile Offline": False,
        "Video Calls": False,
        "Invoice Generation": True,
        "Resource Planning": True
    },
    "Notion": {
        "Kanban Boards": True,
        "Gantt Charts": False,
        "Time Tracking": False,
        "Custom Fields": True,
        "Automation Rules": False,
        "Advanced Reporting": False,
        "White Labeling": False,
        "API Integration": True,
        "Mobile Offline": True,
        "Video Calls": False,
        "Invoice Generation": False,
        "Resource Planning": False
    },
    "ClickUp": {
        "Kanban Boards": True,
        "Gantt Charts": True,
        "Time Tracking": True,
        "Custom Fields": True,
        "Automation Rules": True,
        "Advanced Reporting": True,
        "White Labeling": False,
        "API Integration": True,
        "Mobile Offline": True,
        "Video Calls": True,
        "Invoice Generation": False,
        "Resource Planning": True
    }
}

# User feature requests from support tickets and surveys (last 6 months)
user_requests = {
    "Kanban Boards": 12,
    "Gantt Charts": 34,
    "Time Tracking": 67,
    "Custom Fields": 23,
    "Automation Rules": 45,
    "Advanced Reporting": 56,
    "White Labeling": 8,
    "API Integration": 29,
    "Mobile Offline": 78,
    "Video Calls": 41,
    "Invoice Generation": 52,
    "Resource Planning": 38
}

# Implementation difficulty scores (lower = easier to implement)
implementation_difficulty = {
    "Kanban Boards": 2,  # Easy
    "Gantt Charts": 4,   # Hard
    "Time Tracking": 3,  # Medium
    "Custom Fields": 3,  # Medium
    "Automation Rules": 4,  # Hard
    "Advanced Reporting": 4,  # Hard
    "White Labeling": 5,  # Very Hard
    "API Integration": 3,  # Medium
    "Mobile Offline": 4,  # Hard
    "Video Calls": 5,   # Very Hard
    "Invoice Generation": 3,  # Medium
    "Resource Planning": 4   # Hard
}

# Your current product's features (what you already offer)
our_features = {
    "Kanban Boards": True,
    "Gantt Charts": False,
    "Time Tracking": True,
    "Custom Fields": True,
    "Automation Rules": False,
    "Advanced Reporting": False,
    "White Labeling": False,
    "API Integration": True,
    "Mobile Offline": False,
    "Video Calls": False,
    "Invoice Generation": False,
    "Resource Planning": False
}

# Your code here to analyze the competitive landscape

# TODO: Calculate market coverage for each feature (% of competitors that offer it)

# TODO: Identify white space opportunities (low coverage + high demand)

# TODO: Find your unique differentiators (features you have that most competitors don't)

# TODO: Calculate opportunity scores for features you don't currently offer
# Suggested formula: (User Requests * demand_weight) - (Market Coverage * competition_penalty) - (Implementation Difficulty * difficulty_penalty)
# You can experiment with different weights to see how it affects prioritization

# TODO: Find the "golden opportunity" feature with the highest opportunity score


# Expected output format:
# Feature Coverage Analysis:
# Kanban Boards: 100% coverage (Saturated)
# Gantt Charts: X% coverage (Competitive/Opportunity)
# ...
#
# White Space Opportunities (High demand + Low coverage):
# 1. Feature Name: X% coverage, Y user requests
# ...
#
# Your Unique Differentiators:
# 1. Feature Name (you offer, X% of competitors offer)
# ...
#
# Golden Opportunity Analysis:
# Top 3 features to consider building:
# 1. Feature Name: Opportunity Score X (Y requests, Z% coverage, difficulty: N)
# 2. ...
# 3. ...
