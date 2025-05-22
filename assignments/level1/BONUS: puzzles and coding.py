###############################################################################
# Problem 1: The User Segmentation Mystery
###############################################################################
"""
As a product manager, you've noticed some unusual patterns in user behavior.
You have data on users' session duration, feature usage, and conversion status.

THE PUZZLE: There appear to be distinct user segments hidden in this data, 
but the traditional segmentation rules aren't working. Your task is to uncover
the "secret formula" that correctly segments these users into exactly three 
groups: "Power Users", "Casual Users", and "Potential Churners".

HINT: The segmentation is based on a combination of the metrics, but not in 
the way you might initially think. Look for patterns!
"""

# User behavior data: [user_id, session_duration_mins, features_used, conversion]
user_data = [
    [101, 45, 7, True],
    [102, 5, 1, False],
    [103, 25, 2, True],
    [104, 60, 8, True],
    [105, 10, 1, False],
    [106, 30, 4, True],
    [107, 15, 2, False],
    [108, 50, 6, True],
    [109, 3, 1, False],
    [110, 20, 3, True],
    [111, 35, 5, False],
    [112, 7, 1, False],
    [113, 55, 6, True],
    [114, 40, 5, True],
    [115, 8, 2, False]
]

# Your task: Create a function that segments users correctly
def segment_users(users):
    power_users = []
    casual_users = []
    potential_churners = []
    
    # Your segmentation logic here
    # The correct segmentation will place 5 users in each segment
    
    # Return the three segments
    return power_users, casual_users, potential_churners

# Test your function
power, casual, churners = segment_users(user_data)
print(f"Power Users: {power}")
print(f"Casual Users: {casual}")
print(f"Potential Churners: {churners}")

# To verify your solution, each list should contain exactly 5 user IDs
# Hint: There's a mathematical relationship between the metrics that determines the segments


###############################################################################
# Problem 2: The Feature Launch Decoder
###############################################################################
"""
Your product team has been tracking usage data for a new feature launch.
Unfortunately, the data came through in an encoded format, and you need to
decode it to understand the feature's performance.

THE PUZZLE: The encoded data contains daily usage counts for your new feature.
However, the encoding has shifted each number by a varying amount based on
its position. Your task is to decode the numbers and calculate key metrics.

HINT: The encoding pattern follows a simple rule that you must discover.
"""

# Encoded data: List of daily feature usage counts (but they're encoded!)
encoded_feature_data = [12, 15, 19, 24, 29, 36, 41, 48, 55, 64, 71, 80, 89]

# Your task: Decode the usage data and calculate metrics
def decode_feature_data(encoded_data):
    decoded_data = []
    
    # Your decoding logic here
    # Hint: Each number has been shifted, but by how much?
    
    return decoded_data

def calculate_feature_metrics(usage_data):
    # Calculate these metrics:
    total_usage = 0
    average_usage = 0
    growth_rate = 0  # Percentage growth from first to last day
    
    # Your calculation logic here
    
    return total_usage, average_usage, growth_rate

# Decode and analyze the data
decoded_data = decode_feature_data(encoded_feature_data)
total, average, growth = calculate_feature_metrics(decoded_data)

print(f"Decoded daily usage: {decoded_data}")
print(f"Total feature usage: {total}")
print(f"Average daily usage: {average:.2f}")
print(f"Growth rate: {growth:.2f}%")

# To verify your solution: 
# The sum of the actual usage numbers should be 126
# The final growth rate should be 75.00%


###############################################################################
# Problem 3: The Priority Matrix Optimizer
###############################################################################
"""
As a product manager, you're responsible for prioritizing the product roadmap.
You have a list of features with different impact, effort, and risk scores.

THE PUZZLE: Create an optimal prioritization of features based on a custom
scoring system that maximizes impact while balancing effort and risk.

HINT: The optimal priority order should achieve the highest cumulative impact
by the time all features are implemented, considering that features with lower
effort should generally be done first.
"""

# Feature data: [feature_name, impact_score, effort_score, risk_score]
feature_data = [
    ["User Authentication", 8, 5, 4],
    ["Dashboard Redesign", 7, 7, 2],
    ["Search Functionality", 9, 6, 3],
    ["Notification System", 6, 4, 3],
    ["Payment Integration", 9, 8, 5],
    ["Social Sharing", 5, 3, 2],
    ["Data Export", 4, 4, 1],
    ["Mobile Responsive", 8, 6, 3],
    ["User Onboarding", 7, 5, 2],
    ["Analytics Panel", 6, 5, 4]
]

# Your task: Create a prioritization algorithm
def calculate_priority_score(feature):
    # Create a custom scoring formula that balances impact, effort, and risk
    # Your scoring formula here
    
    return priority_score

def prioritize_features(features):
    # Create a prioritized list of features using your scoring formula
    prioritized_features = []
    
    # Your prioritization logic here
    
    return prioritized_features

# Prioritize the features
prioritized_roadmap = prioritize_features(feature_data)

# Display the optimized roadmap
print("Optimized Product Roadmap:")
for i, feature in enumerate(prioritized_roadmap, 1):
    print(f"{i}. {feature[0]} (Impact: {feature[1]}, Effort: {feature[2]}, Risk: {feature[3]})")

# Calculate cumulative impact over time
cumulative_impact = 0
print("\nCumulative Impact Over Time:")
for feature in prioritized_roadmap:
    cumulative_impact += feature[1]
    print(f"After {feature[0]}: {cumulative_impact}")

# There is no single "correct" answer, but your solution should maximize
# cumulative impact while balancing effort. The goal is to reach high
# impact quickly by implementing high-impact, low-effort features earlier.


###############################################################################
# Problem 4: The Churn Predictor Challenge
###############################################################################
"""
Your company is concerned about user churn. Based on historical data,
certain patterns of user behavior are strong predictors of potential churn.

THE PUZZLE: Analyze the user activity logs and identify which users are at
high risk of churning in the next month. The logs contain coded information
about user actions that you need to interpret.

HINT: Churn signals are hidden in both the frequency and types of actions,
as well as the patterns between actions.
"""

# User activity logs: [user_id, activity_code, frequency_last_month]
# Activity codes: A=Login, B=Feature Usage, C=Content Creation, D=Social Interaction, E=Settings Change
activity_logs = [
    [201, "AABBC", 24],
    [202, "AABDA", 12],
    [203, "AAABC", 30],
    [204, "ABBCA", 10],
    [205, "AACDA", 15],
    [206, "AAAAA", 5],
    [207, "ACDBA", 25],
    [208, "ABCDA", 18],
    [209, "AADCA", 7],
    [210, "AABBA", 20],
    [211, "ACBDA", 22],
    [212, "ABDCA", 9],
    [213, "ABCBA", 28],
    [214, "ACDEA", 14],
    [215, "AABCA", 6]
]

# Your task: Create a function that identifies users at risk of churning
def identify_churn_risk(logs):
    high_risk_users = []
    medium_risk_users = []
    low_risk_users = []
    
    # Your churn prediction logic here
    # Look for patterns in activity codes and frequency
    
    return high_risk_users, medium_risk_users, low_risk_users

# Analyze the logs and predict churn
high_risk, medium_risk, low_risk = identify_churn_risk(activity_logs)

print(f"High Risk Users: {high_risk}")
print(f"Medium Risk Users: {medium_risk}")
print(f"Low Risk Users: {low_risk}")

# To verify your solution:
# There should be 5 users in each risk category
# Users with frequency < 10 AND limited activity variety are highest risk
# Users with high frequency BUT very repetitive patterns are medium risk
# Users with high frequency AND diverse activity patterns are lowest risk


###############################################################################
# Problem 5: The Conversion Funnel Detective
###############################################################################
"""
There's a mystery in your product's conversion funnel. The overall conversion 
rate is lower than expected, but it's not clear where users are dropping off.

THE PUZZLE: Analyze the funnel data to find the problematic steps. However, 
there's a twist - the step names have been encoded, and the conversion numbers
seem inconsistent. You'll need to decode both to solve the mystery.

HINT: The step names are encoded with a simple cipher where each letter has been
shifted by the same amount in the alphabet. The conversion numbers have a 
mathematical pattern that, once understood, will reveal the actual drop-off rates.
"""

# Encoded funnel data: [encoded_step_name, encoded_conversion_count]
encoded_funnel = [
    ["XLY HZZPDHS", 1000],
    ["YLNPZAYHAPVU", 820],
    ["WYVMPSL ZLABW", 623],
    ["MPYZA HJAPVU", 445],
    ["ZLJVUK HJAPVU", 372],
    ["AOPYK HJAPVU", 238],
    ["JVUDLYZPVU", 152]
]

# Your task: Decode the funnel data and find the largest drop-off point
def decode_step_name(encoded_name):
    decoded_name = ""
    
    # Your decoding logic here
    # Hint: All letters have been shifted by the same amount
    
    return decoded_name

def analyze_funnel(encoded_data):
    decoded_funnel = []
    drop_offs = []
    
    # Decode the step names
    for step in encoded_data:
        # Your funnel analysis code here
        # Calculate the drop-off rate between each step
        pass
    
    # Find the step with the largest drop-off
    largest_drop_off_step = ""
    largest_drop_off_percentage = 0
    
    # Your logic to find the largest drop-off
    
    return decoded_funnel, largest_drop_off_step, largest_drop_off_percentage

# Analyze the funnel and find the problematic step
decoded_funnel, problem_step, drop_off_rate = analyze_funnel(encoded_funnel)

print("Decoded Conversion Funnel:")
for step, count in decoded_funnel:
    print(f"{step}: {count} users")

print(f"\nLargest drop-off occurs at: {problem_step}")
print(f"Drop-off rate: {drop_off_rate:.2f}%")

# To verify your solution:
# The step names should be meaningful when decoded correctly
# The problem step should have a drop-off rate of approximately 40%