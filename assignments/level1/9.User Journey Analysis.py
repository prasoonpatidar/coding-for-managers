"""
PRODUCT PUZZLE #9: THE USER JOURNEY MAPPER

As a product manager for an e-learning platform, you want to understand how 
users navigate through your app to identify optimization opportunities.

Each user session is recorded as a sequence of pages they visited. You need to
analyze these paths to understand user behavior patterns.

Your challenge:
1. Find the most common user journey paths (top 5)
2. Identify pages with the highest drop-off rates
3. Calculate the average session length (number of pages visited)
4. Puzzle element: Discover the "ghost path" - a theoretically optimal route 
   that very few users actually take, suggesting a UX problem

PAGE CODES:
- HOME: Homepage/Dashboard
- CATALOG: Course catalog
- COURSE: Individual course page  
- LESSON: Lesson content page
- QUIZ: Quiz/assessment page
- PROFILE: User profile page
- SETTINGS: Account settings
- SEARCH: Search results page
- CHECKOUT: Purchase/enrollment page
- COMPLETE: Course completion page

EXAMPLE ANALYSIS:
User journey: ["HOME", "CATALOG", "COURSE", "LESSON", "QUIZ"]
- Path length: 5 pages
- Drop-off after QUIZ (session ended without completion)

Ghost path example: HOME → SEARCH → COURSE → CHECKOUT
This seems like an efficient path for users who know what they want, but if very 
few users take it, it might indicate the search functionality is hard to find.
"""

# User session data (each list represents one user's journey through the app)
user_sessions = [
    ["HOME", "CATALOG", "COURSE", "LESSON", "LESSON", "QUIZ", "LESSON"],
    ["HOME", "PROFILE", "SETTINGS"],
    ["HOME", "CATALOG", "SEARCH", "COURSE", "CHECKOUT"],
    ["HOME", "CATALOG", "COURSE", "LESSON", "LESSON", "LESSON", "QUIZ", "COMPLETE"],
    ["HOME", "CATALOG", "CATALOG", "COURSE"],
    ["HOME", "SEARCH", "COURSE", "LESSON"],
    ["HOME", "CATALOG", "COURSE", "LESSON", "QUIZ", "LESSON", "QUIZ", "COMPLETE"],
    ["HOME", "PROFILE"],
    ["HOME", "CATALOG", "COURSE", "CHECKOUT"],
    ["HOME", "CATALOG", "SEARCH", "SEARCH", "COURSE", "LESSON"],
    ["HOME", "CATALOG", "COURSE", "LESSON", "LESSON", "QUIZ"],
    ["HOME", "SEARCH", "COURSE", "LESSON", "LESSON", "LESSON", "COMPLETE"],
    ["HOME", "CATALOG", "COURSE"],
    ["HOME", "PROFILE", "SETTINGS", "PROFILE"],
    ["HOME", "CATALOG", "COURSE", "LESSON", "QUIZ", "QUIZ", "COMPLETE"],
    ["HOME", "SEARCH", "SEARCH", "COURSE", "CHECKOUT"],
    ["HOME", "CATALOG", "CATALOG", "COURSE", "LESSON"],
    ["HOME", "CATALOG", "COURSE", "LESSON", "LESSON", "QUIZ", "LESSON", "QUIZ"],
    ["HOME", "SEARCH", "COURSE", "LESSON", "LESSON"],
    ["HOME", "CATALOG", "COURSE", "CHECKOUT"],
    ["HOME", "PROFILE", "SETTINGS", "CATALOG", "COURSE"],
    ["HOME", "CATALOG", "SEARCH", "COURSE", "LESSON", "QUIZ", "COMPLETE"],
    ["HOME", "SEARCH", "COURSE"],
    ["HOME", "CATALOG", "COURSE", "LESSON", "LESSON", "LESSON"],
    ["HOME", "CATALOG", "COURSE", "LESSON", "QUIZ", "COMPLETE"]
]

# Theoretically optimal paths for different user goals
optimal_paths = {
    "quick_purchase": ["HOME", "SEARCH", "COURSE", "CHECKOUT"],
    "thorough_learning": ["HOME", "CATALOG", "COURSE", "LESSON", "QUIZ", "COMPLETE"],
    "browse_and_buy": ["HOME", "CATALOG", "COURSE", "CHECKOUT"],
    "account_management": ["HOME", "PROFILE", "SETTINGS"]
}

# Your code here to analyze user journey patterns

def find_most_common_paths(sessions, top_n=5):
    """
    Find the most frequently taken user journey paths
    """
    # TODO: Convert sessions to strings for comparison, count occurrences
    # Hint: You can join the page lists with a separator like " -> "
    pass

def calculate_drop_off_rates(sessions):
    """
    Calculate what percentage of sessions end at each page
    (indicating potential friction points)
    """
    # TODO: Count how many sessions end at each page type
    # Higher numbers might indicate friction or natural completion points
    pass

def calculate_session_statistics(sessions):
    """
    Calculate average session length and other basic stats
    """
    # TODO: Calculate average, minimum, maximum session lengths
    pass

def find_ghost_paths(sessions, optimal_paths):
    """
    Identify optimal paths that few users actually take
    """
    # TODO: Check how many users follow each optimal path
    # Look for paths that seem logical but have very low usage
    pass

def analyze_page_transitions(sessions):
    """
    Analyze which pages users typically visit after each page
    """
    # TODO: Create a transition matrix showing common page-to-page movements
    pass

# TODO: Find the 5 most common user journey paths

# TODO: Calculate drop-off rates for each page

# TODO: Calculate session length statistics

# TODO: Identify ghost paths (optimal routes with low usage)

# TODO: Analyze common page transitions


# Expected output format:
# USER JOURNEY ANALYSIS
# =====================
# 
# Most Common User Paths:
# 1. HOME -> CATALOG -> COURSE -> LESSON (X users)
# 2. HOME -> CATALOG -> COURSE (X users)
# ...
# 
# Drop-off Analysis (% of sessions ending at each page):
# HOME: X%
# CATALOG: X%
# COURSE: X%
# ...
# 
# Session Statistics:
# Average session length: X pages
# Shortest session: X pages
# Longest session: X pages
# 
# Ghost Path Analysis:
# Theoretically optimal but underused paths:
# - quick_purchase path: Only X users (X% usage rate)
# - [Analysis of why users might not be taking this path]
# 
# Common Page Transitions:
# From HOME: X% go to CATALOG, Y% go to SEARCH, Z% go to PROFILE
# From CATALOG: X% go to COURSE, Y% stay on CATALOG, Z% go to SEARCH
# ...
