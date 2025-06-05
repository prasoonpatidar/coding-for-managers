"""
PRODUCT PUZZLE #8: THE LAUNCH READINESS EVALUATOR

Your team is preparing to launch a new feature for your mobile app. You need a 
systematic way to evaluate readiness across multiple dimensions to ensure a 
successful launch.

Each criterion has:
- Completion status (True/False)
- Importance weight (1-5, where 5 is critical)
- Category (Technical, Marketing, Legal, UX, Business)

Your challenge:
1. Calculate an overall readiness score (0-100%)
2. Identify blocking issues (incomplete critical items)
3. Calculate readiness by category to see which areas need attention
4. Puzzle element: Determine the minimum viable launch score - what's the lowest 
   overall score you could launch with while ensuring all critical items are complete?

EXAMPLE CALCULATION:
If you have 2 items:
- "API Performance Testing" (Complete: True, Weight: 4, Category: Technical)
- "Legal Review" (Complete: False, Weight: 5, Category: Legal)

Category scores:
- Technical: 4/4 = 100% (all items complete)
- Legal: 0/5 = 0% (critical item incomplete)

Overall score: (4 + 0) / (4 + 5) = 44%
This would be a NO-GO for launch due to incomplete critical legal item.

WEIGHT GUIDE:
1 = Nice to have
2 = Recommended  
3 = Important
4 = High priority
5 = Critical (must be complete to launch)
"""

# Launch readiness checklist
readiness_criteria = [
    # Technical Criteria
    {"name": "Core Feature Development", "complete": True, "weight": 5, "category": "Technical"},
    {"name": "API Performance Testing", "complete": True, "weight": 4, "category": "Technical"},
    {"name": "Security Penetration Testing", "complete": False, "weight": 5, "category": "Technical"},
    {"name": "Mobile App Store Optimization", "complete": True, "weight": 3, "category": "Technical"},
    {"name": "Database Migration Scripts", "complete": True, "weight": 4, "category": "Technical"},
    {"name": "Error Monitoring Setup", "complete": False, "weight": 3, "category": "Technical"},
    
    # UX Criteria  
    {"name": "User Interface Design", "complete": True, "weight": 5, "category": "UX"},
    {"name": "Accessibility Compliance", "complete": False, "weight": 4, "category": "UX"},
    {"name": "User Testing Sessions", "complete": True, "weight": 4, "category": "UX"},
    {"name": "Onboarding Flow", "complete": True, "weight": 3, "category": "UX"},
    {"name": "Help Documentation", "complete": False, "weight": 2, "category": "UX"},
    
    # Marketing Criteria
    {"name": "Launch Campaign Materials", "complete": True, "weight": 3, "category": "Marketing"},
    {"name": "Press Release Draft", "complete": False, "weight": 2, "category": "Marketing"},
    {"name": "Social Media Content", "complete": True, "weight": 2, "category": "Marketing"},
    {"name": "Customer Communication Plan", "complete": False, "weight": 4, "category": "Marketing"},
    {"name": "Pricing Strategy Finalized", "complete": True, "weight": 5, "category": "Marketing"},
    
    # Legal Criteria
    {"name": "Terms of Service Update", "complete": False, "weight": 5, "category": "Legal"},
    {"name": "Privacy Policy Review", "complete": True, "weight": 5, "category": "Legal"},
    {"name": "Data Protection Compliance", "complete": True, "weight": 5, "category": "Legal"},
    {"name": "Trademark Clearance", "complete": True, "weight": 3, "category": "Legal"},
    
    # Business Criteria
    {"name": "Revenue Model Validation", "complete": True, "weight": 4, "category": "Business"},
    {"name": "Support Team Training", "complete": False, "weight": 4, "category": "Business"},
    {"name": "Success Metrics Defined", "complete": True, "weight": 3, "category": "Business"},
    {"name": "Rollback Plan", "complete": False, "weight": 3, "category": "Business"},
    {"name": "Launch Timeline Approved", "complete": True, "weight": 2, "category": "Business"}
]

# Your code here to evaluate launch readiness

def calculate_overall_readiness_score(criteria_list):
    """
    Calculate overall readiness score as a percentage
    """
    # TODO: Calculate weighted score
    # Hint: Sum of (complete items * their weights) / Sum of all weights * 100
    pass

def find_blocking_issues(criteria_list):
    """
    Find all incomplete items that are critical (weight 5)
    """
    # TODO: Find incomplete critical items
    pass

def calculate_category_readiness(criteria_list):
    """
    Calculate readiness score for each category
    """
    # TODO: Group criteria by category and calculate scores for each
    pass

def find_minimum_viable_launch_score(criteria_list):
    """
    Calculate the minimum score possible while completing all critical items
    """
    # TODO: Simulate completing all critical items and calculate the resulting score
    pass

# TODO: Calculate overall readiness score

# TODO: Identify blocking issues (incomplete critical items)

# TODO: Calculate readiness by category

# TODO: Determine minimum viable launch score

# TODO: Provide launch recommendation based on analysis


# Expected output format:
# LAUNCH READINESS ASSESSMENT
# ===========================
# Overall Readiness Score: X%
# 
# Blocking Issues (Critical items incomplete):
# - Issue name (Category)
# ...
# 
# Readiness by Category:
# Technical: X% (Y/Z items complete)
# UX: X% (Y/Z items complete)
# ...
# 
# Minimum Viable Launch Score: X% (if all critical items completed)
# 
# LAUNCH RECOMMENDATION: GO / NO-GO
# Reasoning: [Your analysis]
# 
# Priority Actions:
# 1. Complete critical item X
# 2. Complete critical item Y
# ...
