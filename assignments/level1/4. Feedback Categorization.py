"""
PRODUCT PUZZLE #4: THE FEEDBACK CLASSIFICATION CHALLENGE

Your product team has received 15 pieces of user feedback that need to be
categorized to help prioritize product improvements.

Each feedback item should be classified into one or more of these categories:
- Bug: Reports of something not working as expected
- Feature Request: Asking for new functionality
- UX Issue: Problems with usability or user experience
- Performance: Comments about speed or responsiveness
- Positive: Compliments or positive comments

Your challenge:
1. Categorize each feedback item based on keywords
2. Count how many items fall into each category
3. Identify which category has the most items
4. Puzzle element: Identify the "hidden priority" feature request that appears
   most frequently across multiple feedback items
   (Hint: Look for a specific enhancement mentioned in different ways)

EXAMPLE:
Feedback: "The app crashes whenever I try to upload photos"
Keywords detected: "crashes" matches the "Bug" category
Categorization: ["Bug"]

Feedback: "I love the app but it's too slow when loading images"
Keywords detected: "love" matches "Positive", "slow" matches "Performance"
Categorization: ["Positive", "Performance"]
"""

# User feedback data
feedback_items = [
    "The app crashes whenever I try to upload multiple photos at once",
    "I love the new dashboard design, it's so much cleaner!",
    "Would be great if you could add dark mode support",
    "Takes forever to load my profile page, please make it faster",
    "I can't figure out how to change my notification settings",
    "The search function doesn't return relevant results",
    "Please add the ability to schedule posts for later",
    "Great app overall but it's too slow on older devices",
    "The button to save changes is hard to find",
    "Dark theme would be amazing for night time use",
    "Love the simplicity of the interface, very intuitive",
    "App freezes when switching between tabs too quickly",
    "Would it be possible to add a night mode to reduce eye strain?",
    "Can't seem to sort my items by date, is this a bug?",
    "The app performs much better after the recent update"
]

# Keywords for categories (you can add more)
category_keywords = {
    "Bug": ["crash", "freeze", "bug", "doesn't work", "can't", "error", "problem"],
    "Feature Request": ["add", "would be", "could you", "please add", "ability to", "would it be possible"],
    "UX Issue": ["hard to find", "can't figure out", "confusing", "difficult to", "unclear"],
    "Performance": ["slow", "fast", "freeze", "speed", "performs", "forever", "responsive"],
    "Positive": ["love", "great", "amazing", "good", "nice", "awesome", "intuitive"]
}

# Your code here to categorize feedback

# TODO: Categorize each feedback item based on keywords
# Hint: Check if any keywords from the category are in the feedback text

# TODO: Count items in each category

# TODO: Find the category with the most items

# TODO: Look for patterns to identify the "hidden priority" feature
# Hint: Look for similar feature requests mentioned in different ways


# Expected output format:
# Feedback: "Feedback text"
# Categories: [Category1, Category2, ...]
# 
# Category counts:
# Bug: X items
# Feature Request: X items
# ...
# Most common category: X with Y items
# Hidden priority feature: [Your analysis]
