"""
PRODUCT PUZZLE #10: THE FEEDBACK INSIGHTS DETECTOR

Your product team conducted an NPS survey with open-ended feedback questions.
You received 20 responses with both numerical scores (0-10) and text comments.

You need to process these responses to extract actionable insights for product 
improvements and understand what drives user satisfaction.

Your challenge:
1. Categorize sentiment of each response (Positive, Neutral, Negative)
2. Identify the most frequently mentioned topics/themes
3. Correlate sentiment with NPS scores to validate the scoring
4. Puzzle element: Find the "hidden insight" - a recurring theme that appears 
   across multiple responses but uses different words (e.g., "slow", "laggy", 
   "takes forever" all referring to performance issues)

SENTIMENT SCORING:
- Positive sentiment: Contains more positive words than negative
- Negative sentiment: Contains more negative words than positive  
- Neutral sentiment: Balanced or no strong sentiment indicators

NPS SCORE CATEGORIES:
- Promoters: 9-10 (should correlate with positive sentiment)
- Passives: 7-8 (should correlate with neutral sentiment)
- Detractors: 0-6 (should correlate with negative sentiment)

EXAMPLE ANALYSIS:
Response: "Love the new features but the app is really slow on my phone"
- Positive words: ["love", "new features"] 
- Negative words: ["slow"]
- Mixed sentiment, but performance issue noted
- Hidden insight: Performance complaints (also expressed as "laggy", "takes forever", etc.)
"""

# Survey responses with NPS scores and feedback
survey_responses = [
    {
        "response_id": 1,
        "nps_score": 9,
        "feedback": "Absolutely love this app! The interface is so intuitive and clean. Makes my work so much easier."
    },
    {
        "response_id": 2, 
        "nps_score": 3,
        "feedback": "App crashes constantly on my Android device. Very frustrating and unreliable."
    },
    {
        "response_id": 3,
        "nps_score": 8,
        "feedback": "Great features overall, but I wish there was a dark mode option for night use."
    },
    {
        "response_id": 4,
        "nps_score": 2,
        "feedback": "Takes forever to load anything. So slow and laggy, can't get anything done efficiently."
    },
    {
        "response_id": 5,
        "nps_score": 10,
        "feedback": "Perfect app! Does exactly what I need. The automation features save me hours every week."
    },
    {
        "response_id": 6,
        "nps_score": 7,
        "feedback": "Decent app with good functionality. Could use better search capabilities though."
    },
    {
        "response_id": 7,
        "nps_score": 1,
        "feedback": "Terrible user experience. Navigation is confusing and the app freezes all the time."
    },
    {
        "response_id": 8,
        "nps_score": 9,
        "feedback": "Amazing product! Love the collaboration features and how fast everything loads."
    },
    {
        "response_id": 9,
        "nps_score": 6,
        "feedback": "The app is okay but missing some key features I need. Also runs pretty slow on older devices."
    },
    {
        "response_id": 10,
        "nps_score": 8,
        "feedback": "Really like the design and most features work well. Just needs dark theme support."
    },
    {
        "response_id": 11,
        "nps_score": 4,
        "feedback": "Buggy and unreliable. Lost my work twice due to unexpected crashes."
    },
    {
        "response_id": 12,
        "nps_score": 10,
        "feedback": "Excellent app! Intuitive design and lightning fast performance. Highly recommend!"
    },
    {
        "response_id": 13,
        "nps_score": 5,
        "feedback": "App is too slow and the interface feels outdated compared to competitors."
    },
    {
        "response_id": 14,
        "nps_score": 9,
        "feedback": "Love how easy it is to use! Clean interface and great automation tools."
    },
    {
        "response_id": 15,
        "nps_score": 7,
        "feedback": "Good app with useful features. Would be perfect if it had dark mode."
    },
    {
        "response_id": 16,
        "nps_score": 2,
        "feedback": "Constantly freezing and crashing. Very unreliable for important work."
    },
    {
        "response_id": 17,
        "nps_score": 8,
        "feedback": "Great functionality and I love the clean design. Just wish it was faster."
    },
    {
        "response_id": 18,
        "nps_score": 6,
        "feedback": "Average app. Works fine but nothing special. Could use more advanced features."
    },
    {
        "response_id": 19,
        "nps_score": 10,
        "feedback": "Perfect! Fast, reliable, and has all the features I need. Best app in this category."
    },
    {
        "response_id": 20,
        "nps_score": 3,
        "feedback": "Disappointing experience. App is laggy and the user interface is confusing."
    }
]

# Sentiment word lists (you can expand these)
positive_words = [
    "love", "amazing", "perfect", "excellent", "great", "awesome", "fantastic", 
    "wonderful", "brilliant", "outstanding", "superb", "terrific", "good", 
    "nice", "useful", "helpful", "easy", "simple", "clean", "intuitive",
    "fast", "quick", "efficient", "reliable", "smooth", "lightning", "recommend"
]

negative_words = [
    "hate", "terrible", "awful", "horrible", "bad", "poor", "disappointing",
    "frustrating", "annoying", "confusing", "difficult", "hard", "slow", 
    "laggy", "buggy", "unreliable", "crashes", "freezing", "broken", "issues",
    "problems", "fails", "worst", "useless", "outdated", "missing"
]

# Common themes/topics to look for
themes = {
    "performance": ["slow", "fast", "laggy", "quick", "speed", "performance", "efficient", "lightning", "forever", "takes"],
    "reliability": ["crashes", "crash", "freezing", "freeze", "buggy", "reliable", "unreliable", "stable", "broken"],
    "interface": ["interface", "design", "clean", "intuitive", "confusing", "navigation", "layout", "ui", "ux"],
    "features": ["features", "functionality", "automation", "tools", "capabilities", "missing", "needs"],
    "dark_mode": ["dark", "night", "theme", "mode"],
    "search": ["search", "find", "lookup"],
    "collaboration": ["collaboration", "sharing", "team", "together"]
}

# Your code here to analyze survey sentiment and extract insights

def analyze_sentiment(feedback_text, positive_words, negative_words):
    """
    Analyze sentiment of feedback text
    Returns: "Positive", "Negative", or "Neutral"
    """
    # TODO: Count positive and negative words in the feedback
    # TODO: Determine overall sentiment based on word counts
    pass

def extract_themes(feedback_text, themes):
    """
    Identify which themes are mentioned in the feedback
    Returns: List of theme names found
    """
    # TODO: Check which theme keywords appear in the feedback
    pass

def validate_nps_sentiment_correlation(responses):
    """
    Check if sentiment analysis aligns with NPS score categories
    """
    # TODO: Compare predicted sentiment with NPS score categories
    # Promoters (9-10) should mostly be positive
    # Detractors (0-6) should mostly be negative
    # Passives (7-8) should be mixed or neutral
    pass

def find_hidden_insights(responses, themes):
    """
    Identify the most frequently mentioned themes across all responses
    """
    # TODO: Count theme mentions across all responses
    # TODO: Identify patterns and recurring issues
    pass

# TODO: Analyze sentiment for each response

# TODO: Extract themes from each response  

# TODO: Validate correlation between sentiment and NPS scores

# TODO: Find the most frequently mentioned themes (hidden insights)

# TODO: Calculate summary statistics


# Expected output format:
# SURVEY SENTIMENT ANALYSIS
# =========================
# 
# Individual Response Analysis:
# Response 1 (NPS: 9): Positive sentiment - Themes: [interface, features]
# Response 2 (NPS: 3): Negative sentiment - Themes: [reliability]
# ...
# 
# Sentiment Distribution:
# Positive: X responses (Y%)
# Negative: X responses (Y%) 
# Neutral: X responses (Y%)
# 
# NPS vs Sentiment Correlation:
# Promoters (9-10): X% positive sentiment, Y% negative sentiment
# Passives (7-8): X% positive sentiment, Y% negative sentiment  
# Detractors (0-6): X% positive sentiment, Y% negative sentiment
# Correlation strength: [Strong/Moderate/Weak]
# 
# Most Mentioned Themes:
# 1. performance: X mentions (Y% of responses)
# 2. interface: X mentions (Y% of responses)
# ...
# 
# Hidden Insights:
# - Performance is the biggest concern (mentioned in X different ways)
# - Dark mode is highly requested (mentioned in Y responses)
# - [Other patterns you discover]
# 
# Actionable Recommendations:
# 1. Priority 1: Address performance issues (affects X% of detractors)
# 2. Priority 2: Add dark mode feature (requested by Y% of users)
# ...
